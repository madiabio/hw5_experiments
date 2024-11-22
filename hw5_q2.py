import random
import math
t = 4*(10**4)  # t = num trails/steps
rt_t = math.sqrt(t) # get sqrt of t
X = 0 # start at origin

prev = X # step prev val of X to current val of X.
crosses = 0 # 0 origin crosses
for j in range(50):  # repeat for 50 trials
    X = 0  # reset X for each trial
    prev = X  # initialize previous value of X
    for i in range(t):
        step_dir = random.choice([-1, 1])  # random step direction
        X += step_dir  # take a step

        # Check for crossing the origin
        if (prev > 0 and X <= 0) or (prev < 0 and X >= 0):
            crosses += 1

        # Update the previous value
        prev = X
print("For t=4*(10**4)")
print(f"crosses (average): {crosses/50}")
print(f"X: {X}")
print(f"sqrt t = {rt_t}")

t = 9*(10**4)
rt_t = math.sqrt(t) # get sqrt of t
X = 0 # start at origin
prev = X # step prev val of X to current val of X.
crosses = 0 # 0 origin crosses
for j in range(50):  # repeat for 50 trials
    X = 0  # reset X for each trial
    prev = X  # initialize previous value of X
    for i in range(t):
        step_dir = random.choice([-1, 1])  # random step direction
        X += step_dir  # take a step

        # Check for crossing the origin
        if (prev > 0 and X <= 0) or (prev < 0 and X >= 0):
            crosses += 1

        # Update the previous value
        prev = X
print("For t=9*(10**4)")
print(f"crosses (average): {crosses/50}")
print(f"X: {X}")
print(f"sqrt t = {rt_t}")




t = 16*(10**4)
rt_t = math.sqrt(t) # get sqrt of t
X = 0 # start at origin
prev = X # step prev val of X to current val of X.
crosses = 0 # 0 origin crosses
for j in range(50):  # repeat for 50 trials
    X = 0  # reset X for each trial
    prev = X  # initialize previous value of X
    for i in range(t):
        step_dir = random.choice([-1, 1])  # random step direction
        X += step_dir  # take a step

        # Check for crossing the origin
        if (prev > 0 and X <= 0) or (prev < 0 and X >= 0):
            crosses += 1

        # Update the previous value
        prev = X
print("For t=16*(10**4)")
print(f"crosses (average): {crosses/50}")
print(f"X: {X}")
print(f"sqrt t = {rt_t}")




