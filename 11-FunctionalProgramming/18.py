captured = [48,47,54,50,42,68,39,46]


speedo = list(filter(lambda x: x > 50, captured))

print("Recorded values:",captured)
print("Speed too high:",speedo)