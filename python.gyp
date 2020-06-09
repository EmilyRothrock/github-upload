total = 0
score = [90, 100, 70, 60, 30]
for x in range(len(score)):
    total = total + score[x] 
print(total / len(score))

score[0] = 0
for x in range(len(score)):
    total = total + score[x]
  
print(total / len(score))

