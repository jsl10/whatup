#modifying a list in a function
"""
when you pass a list to a function, the function can modify the list.
any changes made to the list inside the function's body are permanent,
allowing you to work efficiently even when you're dealing with large amount of data.
"""
#start with some designs that need to be printed
unprintedDesigns=['iphone case','robot pendant','dodecahedron']
#empty list
completedModels=[]

#simulate printing each desing, until none are left
#move each design to completedModels are printing
while unprintedDesigns:
    currentDesign=unprintedDesigns.pop()
    #simulate creating a 3D print from the design
    print("Printing model: "+currentDesign)
    completedModels.append(currentDesign)

#desplay all completed models.
print("\nThe following models have been printed:")
for completedModel in completedModels:
    print(completedModel)
