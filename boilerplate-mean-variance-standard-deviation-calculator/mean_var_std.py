import numpy as np
import sys


def custom_exit(status_code):
  sys.exit(status_code)


def calculate(list):
  try:
    if len(list) != 9:
      raise ValueError("List must contain nine numbers.")
  except ValueError as e:
    print(f"Error:{e}")
    custom_exit(0)
  ls = np.array(list).reshape(3, 3)

  calculations = {
      'mean':
      [ls.mean(axis=0).tolist(),
       ls.mean(axis=1).tolist(),
       ls.mean().tolist()],
      'variance':
      [ls.var(axis=0).tolist(),
       ls.var(axis=1).tolist(),
       ls.var().tolist()],
      'standard deviation':
      [ls.std(axis=0).tolist(),
       ls.std(axis=1).tolist(),
       ls.std().tolist()],
      'max':
      [ls.max(axis=0).tolist(),
       ls.max(axis=1).tolist(),
       ls.max().tolist()],
      'min':
      [ls.min(axis=0).tolist(),
       ls.min(axis=1).tolist(),
       ls.min().tolist()],
      'sum':
      [ls.sum(axis=0).tolist(),
       ls.sum(axis=1).tolist(),
       ls.sum().tolist()]
  }

  return calculations
