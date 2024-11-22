import random
import math

# evaluate probability that neg1 is majority of sample by running 200 times and then taking the vag.

def makePick(popSize, distributions, sampleSizes):
    # generate population based on the distributions
    labels = ["pos1", "neg1", "zero"]
    population = random.choices(labels, weights=distributions, k=popSize)
    # for storing probabilities for each sample size
    probabilities = []

    # Loop over each sample size
    for size in sampleSizes:
        neg1_majority_count = 0
        
        # do 200 trials for the current sample size
        for _ in range(200):
            sample = random.sample(population, size)
            counts = {"pos1": sample.count("pos1"), 
                      "neg1": sample.count("neg1"), 
                      "zero": sample.count("zero")}
            
            # check if 'neg1' is the majority
            if (counts["neg1"] > (counts["pos1"])) and (counts["neg1"] > counts["zero"]):  # Majority condition
                neg1_majority_count += 1
        
        # calc and store the probability for the current sample size
        prob = neg1_majority_count / 200
        probabilities.append(prob)
        print(f"For sampSize {size}: Prob = {prob}")
    
    return probabilities


# population size
size = 1000000

# distributions
pos1 = .35
neg1 = .40
zero = .25
distribs = [pos1, neg1, zero]

# sample sizes
a = 10
b = 120
c = 250
d = 500
e = 750
f = 1000

sampSizes = [a,b,c,d,e,f]

probs = makePick(size, distribs, sampSizes)
print(probs)
