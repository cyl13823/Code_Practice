import torch
from torch import nn
from torch.utils.data import DataLoader
import torchvision
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
import requests
from pathlib import Path 
from timeit import default_timer as timer
from tqdm.auto import tqdm
import random

# Check if CUDA is available
device = "cuda" if torch.cuda.is_available() else "cpu"

# Set random seeds for reproducibility
torch.manual_seed(42)
torch.cuda.manual_seed(42)

# Set batch size
BATCH = 32

# Download and prepare dataset
train_data = datasets.FashionMNIST(
    root="./data",
    train=True,
    transform=ToTensor(),
    target_transform=None,
    download=True
)

test_data = datasets.FashionMNIST(
    root="./data",
    train=False,
    transform=ToTensor(),
    target_transform=None,
    download=True
)

# Print the shape and label of a sample
image, label = train_data[0]
print(image.shape)
print(label)
print(len(train_data))
print(len(test_data))
print(train_data.classes)

# Create data loaders
train_dataloader = DataLoader(
    dataset=train_data,
    batch_size=BATCH,
    shuffle=True
)

test_dataloader = DataLoader(
    dataset=test_data,
    batch_size=BATCH,
    shuffle=False
)

# Define the model
class Classification(nn.Module):
    def __init__(self, input_shape: int, hidden_units: int, output_shape: int):
        super().__init__()
        self.block_1 = nn.Sequential(
            nn.Conv2d(in_channels=input_shape,
                      out_channels=hidden_units,
                      kernel_size=3,
                      stride=1,
                      padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=hidden_units,
                      out_channels=hidden_units,
                      kernel_size=3,
                      stride=1,
                      padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.block_2 = nn.Sequential(
            nn.Conv2d(hidden_units, hidden_units, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(hidden_units, hidden_units, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(in_features=hidden_units*7*7,
                      out_features=output_shape)
        )
    
    def forward(self, x):
        x = self.block_1(x)
        x = self.block_2(x)
        x = self.classifier(x)
        return x

# Initialize the model
model = Classification(input_shape=1,
                        hidden_units=10,
                        output_shape=len(train_data.classes)).to(device)

# Download the helper functions
if not Path("helper_functions.py").is_file():
    print("Downloading helper_functions.py")
    request = requests.get("https://raw.githubusercontent.com/mrdbourke/pytorch-deep-learning/main/helper_functions.py")
    with open("helper_functions.py", "wb") as f:
        f.write(request.content)

from helper_functions import accuracy_fn

# Define the loss function and optimizer
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(params=model.parameters(), lr=0.1)

# Training loop
epochs = 3
training_start_time = timer()

for epoch in tqdm(range(epochs)):
    print(f"Epoch: {epoch}\n---------")
    model.train()
    for batch, (X, y) in enumerate(train_dataloader):
        X, y = X.to(device), y.to(device)
        optimizer.zero_grad()
        outputs = model(X)
        loss = loss_fn(outputs, y)
        loss.backward()
        optimizer.step()
        if batch % 100 == 0:
            print(f"Batch {batch}, Loss {loss.item()}")

training_end_time = timer()
print(f"Training took {training_end_time - training_start_time:.2f} seconds")

# Evaluation loop
model.eval()
test_loss, test_accuracy = 0, 0

with torch.no_grad():
    for X_test, y_test in test_dataloader:
        X_test, y_test = X_test.to(device), y_test.to(device)
        test_outputs = model(X_test)
        test_loss += loss_fn(test_outputs, y_test)
        test_accuracy += accuracy_fn(y_true=y_test, y_pred=test_outputs.argmax(dim=1))

test_loss /= len(test_dataloader)
test_accuracy /= len(test_dataloader)

print(f"Test Loss: {test_loss:.5f}, Test Accuracy: {test_accuracy:.2f}%")

# Make predictions function
def make_predictions(model: torch.nn.Module, data: list, device: torch.device = device):
    pred_probs = []
    pred_classes = []
    model.eval()
    with torch.inference_mode():
        for sample in data:
            # Prepare sample
            sample = torch.unsqueeze(sample, dim=0).to(device) # Add an extra dimension and send sample to device

            # Forward pass (model outputs raw logit)
            pred_logit = model(sample)

            # Get prediction probability (logit -> prediction probability)
            pred_prob = torch.softmax(pred_logit.squeeze(), dim=0) # note: perform softmax on the "logits" dimension, not "batch" dimension (in this case we have a batch size of 1, so can perform on dim=0)

            # Get predicted class
            pred_class = torch.argmax(pred_prob).item()

            # Get pred_prob off GPU for further calculations
            pred_probs.append(pred_prob.cpu())
            pred_classes.append(pred_class)
            
    # Stack the pred_probs to turn list into a tensor
    return torch.stack(pred_probs), pred_classes

# Randomly select 9 test samples
test_samples = []
test_labels = []
for sample, label in random.sample(list(test_data), k=9):
    test_samples.append(sample)
    test_labels.append(label)

# View the first test sample shape and label
print(f"Test sample image shape: {test_samples[0].shape}\nTest sample label: {test_labels[0]}")

# Make predictions
pred_probs, pred_classes = make_predictions(model, test_samples)

# Plot predictions
plt.figure(figsize=(9, 9))
nrows = 3
ncols = 3
for i, sample in enumerate(test_samples):
    # Create a subplot
    plt.subplot(nrows, ncols, i+1)

    # Plot the target image
    plt.imshow(sample.squeeze(), cmap="gray")

    # Find the prediction label
    pred_label = train_data.classes[pred_classes[i]]

    # Get the truth label
    truth_label = train_data.classes[test_labels[i]] 

    # Create the title text of the plot
    title_text = f"Pred: {pred_label}\nTruth: {truth_label}"
  
    # Check for equality and change title colour accordingly
    if pred_label == truth_label:
        plt.title(title_text, fontsize=10, c="g") # green text if correct
    else:
        plt.title(title_text, fontsize=10, c="r") # red text if wrong
        
    plt.axis(False)
plt.tight_layout()
plt.show()