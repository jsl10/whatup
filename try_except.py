try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

"""
If the code in a try block works, python skips over the except block.
If the code in the try bolck causes an error,
python looks for an except block whose error matches the one that was raised
and runs the cod in that block.
"""
