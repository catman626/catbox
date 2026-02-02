import torch
import sys

fname = sys.argv[1]
data = torch.load(fname)
print(f" >>> shape of data: {list(data.shape)}")