import torch
from torchsummary import summary
from torch.autograd import Variable
from torchvision import models
import cv2
import sys
import numpy as np
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import dataset
from prune import *
import argparse
from operator import itemgetter
from heapq import nsmallest
import time
from finetune import *
orig = torch.load("model")
summary(orig,input_size=(3,224,224))
modified = torch.load("model_prunned")
sums = 0
print("------MOdified Model-------")
for i in modified:
    product = 1
    for j in modified[i].shape:
        product*=j
    sums += product
    print(i,modified[i].shape,product)
print("total parameters:",sums)
print("estimated size:",741*0.3)
model.load_state_dict(modified)
summary(model,input_size=(3,224,224))
