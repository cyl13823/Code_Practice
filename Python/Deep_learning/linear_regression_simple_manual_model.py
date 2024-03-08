import torch
from torch import nn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('linear_data.csv')
X_data = data.iloc[:,0]  # get the zeroth column value
y_data = data.iloc[:,1]
X = torch.tensor(X_data.values, dtype=torch.float32)
y = torch.tensor(y_data.values, dtype=torch.float32)

# print("Tensor data:\n", X[:10])

# Split the data and suffle it
train_size = int(len(X) * 0.8)
test_size = int(len(X)) - train_size

torch.manual_seed(42)
train_indices, test_indices = torch.utils.data.random_split(torch.arange(len(X)), [train_size, test_size])
X_train = X[train_indices].unsqueeze(1)  # unsqueeze is to flatten the tensor
X_test = X[test_indices].reshape(-1,1)  # reshape is another approach
y_train = y[train_indices].reshape(-1,1)
y_test = y[test_indices].reshape(-1,1)

# plt.scatter(X_train, y_train, c='r', s=4)
# plt.scatter(X_test, y_test, c='b', s = 4)
# plt.show()

# Select device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Model
class LinearRegression_v1(nn.Module):
    def __init__(self):
        super().__init__()
        self.weight = nn.Parameter(data=torch.randn(1, requires_grad=True, dtype=torch.float))
        self.bias = nn.Parameter(data=torch.randn(1, requires_grad=True, dtype=torch.float))

    def forward(self, x:torch.Tensor) -> torch.Tensor:
        return self.weight * x + self.bias
    
torch.manual_seed(42)
model_1 = LinearRegression_v1()
# print(model_1.state_dict())

# Loss_fn and Optimizer
loss_fn = nn.L1Loss()
optimizer = torch.optim.SGD(params=model_1.parameters(), lr=0.01)

# Train
torch.manual_seed(42)
torch.cuda.manual_seed(42)

X_train = X_train.to(device)
X_test = X_test.to(device)
y_train = y_train.to(device)
y_test = y_test.to(device)
model_1.to(device)  # model also need to transform to device

epochs = 500

for epoch in range(epochs):
    model_1.train()

    y_training = model_1(X_train)
    loss = loss_fn(y_training, y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Understain the training loop work
    # if epoch % 20 == 0:
    #     model_1.eval()
    #     with torch.inference_mode():
    #         y_pred = model_1(X_test)
    #         loss_test = loss_fn(y_pred, y_test)
    #         print(f"Epoch: {epoch}, Train loss: {loss:.3f}, Test loss: {loss_test:.3f}")

# Get the parameter
print(model_1.state_dict())

model_1.eval()
with torch.inference_mode():
    y_pred = model_1(X_test)
    loss_test = loss_fn(y_pred, y_test)
    print(loss_test)

# Take a look
plt.scatter(X_train.cpu(), y_train.cpu(), c='r', s=4)
plt.scatter(X_test.cpu(), y_test.cpu(), c='b', s = 4)
plt.plot(X_test.cpu(), y_pred.cpu(), c='g')
plt.show()