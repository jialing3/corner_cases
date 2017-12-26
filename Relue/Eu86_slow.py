#!/usr/local/bin/python3
import numpy as np


### need to de-dupe like finding out prime number style

def is_shortest_path_integer_length(a, b, c):
  # on face ab, then bc
  min_b = min(((a ** 2 + x ** 2) ** .5 + ((b - x) ** 2 + c ** 2) ** .5, x)
          for x in np.arange(0, b + 0.01, 0.01))
  # on face ac, then cb
  min_c = min(((a ** 2 + x ** 2) ** .5 + ((c - x) ** 2 + b ** 2) ** .5, x)
          for x in np.arange(0, c + 0.01, 0.01))
  # on face ba, then ac
  min_a = min(((b ** 2 + x ** 2) ** .5 + ((a - x) ** 2 + c ** 2) ** .5, x)
          for x in np.arange(0, a + 0.01, 0.01))

  min_path = min(min_b, min_c, min_a)[0]
  if np.isclose(int(min_path), min_path):
    return True


def num_distinct_cuboids(M):
  cnt = 0
  for c in range(1, M + 1):
    for b in range(1, c + 1):
      for a in range(1, b + 1):
        if is_shortest_path_integer_length(a, b, c):
          cnt += 1
          print(a, b, c) # note multiples and co-primes
  return cnt


print(num_distinct_cuboids(6))
