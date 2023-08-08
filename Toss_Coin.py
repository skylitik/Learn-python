#Basic toss coin
import random

rand_cue = random.random() * 5
if rand_cue <= 2.99:
  print("Tails")
else:
  print("Heads")