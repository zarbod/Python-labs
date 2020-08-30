hits = int(input("Enter number of hits: "))
atBats = int(input("Enter number of at bats: "))
walks = int(input("Enter number of walks: "))
battingAvg = hits/atBats
onBasePCT = (hits + walks) / (atBats + walks)
print("The user's batting average is: " + str(battingAvg))
print("The user's on base PCT is: " + str(onBasePCT))