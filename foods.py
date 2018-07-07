my_foods=['pizza','falafel','carrot cake']
#make a new list called friend_foods
friend_foods=my_foods[:]

print("My favorite foods are: ",my_foods)
print("\nMy friend's favorite foods are:",friend_foods)
print("----")

#add a new food to each list
#add cannoli to my_foods
my_foods.append('cannoli')
#add ice cream to friends_foods
friend_foods.append('ice cream')
print("My favorite foods are: ",my_foods)
print("\nMy friend's favorite foods are:",friend_foods)
print("----")
"""
If we had simply set friend_foods equal to my_foods, we would not produce two separate lists. 
"""

# instead of stroing a copy of my_foods in friend_foods[:]
# we set friends_foods=my_foods
friend_foods=my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are: ",my_foods)
print("\nMy friend's favorite foods are:",friend_foods)

