import random
import sys

def main():
  if len(sys.argv) < 2:
    print "usage: monty.py trials"
    sys.exit(1)

  t = int(sys.argv[1])

  # Stick with door
  stick_winners = 0
  for i in xrange(t):
    car = random.randint(1, 3)
    choice = random.randint(1, 3)
    if car == choice:
      stick_winners += 1
  print "(stick) won:", stick_winners, "out of", t, float(stick_winners) / float(t)

  # Switch door
  switch_winners = 0
  for i in xrange(t):
    car = random.randint(1, 3)
    choice = random.randint(1, 3)
    # If car != choice, open a goat door and switch, win the car
    if car != choice:
      switch_winners += 1
  print "(switch) won:", switch_winners, "out of", t, float(switch_winners) / float(t)

if __name__ == "__main__":
  main()
