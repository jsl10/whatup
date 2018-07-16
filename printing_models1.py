#simulate printing each desing, until none are left
#move each design to completedModels are printing

#define print_models with two parameters
def print_models(unprintedDesigns,completedModels):
    """
    Simulate printing each design, until none are left.
    Move each design to completedModels after printing
    """
    while unprintedDesigns:
        currentDesign=unprintedDesigns.pop()

        #simulate creating a 3D print from the design
        print("Printing model: "+currentDesign)
        completedModels.append(currentDesign)

#showCompletedModels() displays the name of each model that was printed 
def showCompletedModels(completedModels):
    """Show all the models that were printed."""
    #desplay all completed models.
    print("\nThe following models have been printed:")
    for completedModel in completedModels:
        print(completedModel)


unprintedDesigns=['iphone case','robot pendant','dodecahedron']
#empty list
completedModels=[]
print_models(unprintedDesigns,completedModels)
showCompletedModels(completedModels)

"""
This program is easier to extend and maintain than the version without functions.
If we need to print more designs later on, we can simply call print_models() again.
If we realize the printing code needs to be modified,
we can change the code once, and our changes will take place everywhere the functionis called.
This technique is more efficient than having to update code seperately in several places in the program
"""
