# https://github.com/spro/practical-pytorch

import unidecode
import string
import random
import time
import math
import torch
from torch.autograd import Variable

# Reading and un-unicode-encoding data

all_characters = string.printable
n_characters = len(all_characters)

def read_file(filename):
    with open(filename, encoding='utf-8') as fh:
        f = fh.read()
    return f, len(f)

# Turning a string into a tensor

def char_tensor(string):
    tensor = torch.zeros(len(string)).long()
    for c in range(len(string)):
        tensor[c] = all_characters.index(string[c])
    return Variable(tensor)

# Readable time elapsed

def time_since(since):
    s = time.time() - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)

