from Chef import Chef #import class Chef from the file chef

class Chinese_Chef(Chef):
    def make_dessert(self):
        print("The Chinese chef makes a red bean mochi")
    # this is to override the data of (make_dessert)
    # so instead of choco mousse, the program will print red bean mochi

    def make_fried_rice(self):
        print("The Chinese chef makes a fried rice") 
    # the extra features you wanted to add to this class
    # apart from the function you inherited from Chef

# To inherit all of the class function from Chef (to Chinese Chef)
# just put the class as 'class Chinese_chef(Chef):'
# so put 'Chef' in the (), instead of 'self'
# so you wont have to copy/paste the function back and forth