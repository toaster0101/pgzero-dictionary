fruitTracker={}
for i in range(3):
    fruitChoice=input("fruit")
    if fruitChoice not in fruitTracker:
        fruitTracker[fruitChoice]=1
    else:
        fruitTracker[fruitChoice]+=1
print(fruitTracker)