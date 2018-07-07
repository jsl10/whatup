#slicing a list
players=['charles','martina','michael','florence','eli']

#First three players
print(players[0:3])
print("----")

#slice at index 1 and end at index 4
print(players[1:4])
print("----")


#omit the first index in a slice, python automatically starts your slice at the beginning
print(players[:4])
print("----")

print(players[2:])
print("----")

# a negative index returns an element a certain distance from the end of a list
print(players[-3:])
print("----")

#Looping through a slice
print("Here are the first three players on my team: ")
for player in players[:3]: #loops through only the first three names
    print(player.title())
