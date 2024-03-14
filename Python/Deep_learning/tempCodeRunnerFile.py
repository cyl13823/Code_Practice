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
from sklearn.metrics import confusion_matrix

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
def make_predictions(model: torch.nn.Module, data_loader: DataLoader, device: torch.device = device):
    pred_probs = []
    pred_classes = []
    true_labels = []
    model.eval()
    with torch.no_grad():
        for X, y in data_loader:
            X, y = X.to(device), y.to(device)
            outputs = model(X)
            pred_prob_batch = torch.softmax(outputs, dim=1)
            pred_class_batch = torch.argmax(pred_prob_batch, dim=1)
            pred_probs.extend(pred_prob_batch.cpu().numpy())
            pred_classes.extend(pred_class_batch.cpu().numpy())
            true_labels.extend(y.cpu().numpy())
            
    return pred_probs, pred_classes, true_labels

# Make predictions for the test dataset
pred_probs, pred_classes, true_labels = make_predictions(model, test_dataloader)

# Compute confusion matrix
conf_matrix = confusion_matrix(true_labels, pred_classes)

# Print confusion matrix
print("Confusion Matrix:")
print(conf_matrix)

# Plot confusion matrix
plt.figure(figsize=(8, 8))
plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.colorbar()
tick_marks = range(len(train_data.classes))
plt.xticks(tick_marks, train_data.classes, rotation=45)
plt.yticks(tick_marks, train_data.classes)
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.tight_layout()
plt.show()