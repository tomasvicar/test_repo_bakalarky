import torch

a = torch.tensor([1, 2, 3])
device = torch.device("cuda:0") # test gpu
# device = torch.device("cpu")   # test cpu
aa = a.to(device)