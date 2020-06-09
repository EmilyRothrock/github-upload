#instantiates total as a tracker for total score and an array to hold test scores
total = 0
score = [90, 100, 70, 60, 30]

#adds scores up and finds the average
for x in range(len(score)):
    total = total + score[x] 
print(total / len(score))

#adds scores up and adds a random boost to each score before finding average
for x in range(len(score)):
    score[x] = score[x] + random.randrange(100)
for x in range(len(score)):
    total = total + score[x] 
print(total / len(score))

