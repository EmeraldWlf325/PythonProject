import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

chosenFile = 'test.txt'
chosenStock = 'currentStock.txt'

#this reads the file for the seed stock and returns it
def ReadSeedStock(toRead):
    file = open(toRead, 'rb')
    seed = file.read()
    return eval(seed)

#this is for both start new seed stock and add seed stock, status deterimines what is what
def AddSeedStock(invID, newPN, newCount, newDesc, status = "add"):
    if status == "add":
        seedStock = ReadSeedStock(chosenFile)

    inventory = {}
    inventory["Part Number"] = newPN
    inventory["Count"] = newCount
    inventory["Description"] = newDesc
    if status == "new":
        seedStock = {}
        seedStock[invID] = inventory

    if status == "add":
        newSeedStock = {}
        newSeedStock[invID] = inventory
        seedStock.update(newSeedStock)

    with open(chosenFile, 'w') as fp:
        fp.write(str(seedStock))

#uses up inventory 
def UseInventory(PN, count):
    seedStock = ReadSeedStock(chosenStock)

    seedCount = seedStock[PN]["Count"]

    if count <= seedCount:
        newCount = int(seedCount) - int(count)
        seedStock[PN]["Count"] = newCount
        with open(chosenStock, 'w') as fp:
            fp.write(str(seedStock))
        return True
    else:
        return False

#replenishes stock
def ReplenishStock(invID, count):
    currentStock = ReadSeedStock(chosenStock)
    seedStock = ReadSeedStock(chosenFile)
    
    seedCount = int(seedStock[invID]["Count"])
    currentCount = currentStock[invID]["Count"]

    updatedCount = int(count) + int(currentCount)
    if updatedCount <= seedCount:
        currentStock[invID]["Count"] = updatedCount
        with open(chosenStock, 'w') as fp:
            fp.write(str(currentStock))
        return True
    else:
        return False


def Menu():
    print("\nMenu: \n1: Start New Seed Stock \n2: Add Seed Stock \n3: Get Seed Stock")
    print("4: Use Inventory \n5: Replenish Stock \n6: Get Current Stock")
    selection = input("\nPlease select an option: ")

    if(selection == '1'):
        invID = input("Enter the new ID for the new Seed Stock: ")
        newPN = input("Please enter the Part Number: ")
        newCount = input("What is the count for this part? ")
        newDesc = input("Please enter the part description: ")

        AddSeedStock(invID, newPN, newCount, newDesc, "new")
            
    elif(selection == '2'):

        invID = input("Enter the new ID for the new Seed Stock: ")
        newPN = input("Please enter the Part Number: ")
        newCount = input("What is the count for this part? ")
        newDesc = input("Please enter the part description: ")

        AddSeedStock(invID, newPN, newCount, newDesc, "add")
        
        Menu()
    
    elif(selection == '3'):
        print(ReadSeedStock(chosenFile))    
            
        Menu()
    
    elif(selection == '4'):
            
        PN = input("Please enter the inventory ID you would like to use. 'format: 000' ")
        count = input("How many of this part would you like to use? ")

        if not UseInventory(PN, count):
            print("Not enough parts on hand. Please try again")

        Menu()

    elif(selection == '5'):
        invID = input("Please enter the inventory ID for the part you would like to replenish. 'format: 000' ")
        count = input("How many parts are you replenishing? ")
        
        if not ReplenishStock(invID, count):
            print("Too many parts for your location. Please check the destination adress and try again!")

        Menu()

    elif(selection == '6'):
        currentStock = ReadSeedStock(chosenStock)
        print(currentStock)

        Menu()

    else:
        print("\nThank you for using this program!")


def make_window():
    #Creates the main window
    root = tk.Tk()
    #Sets the window size
    root.geometry("400x300")

    def clearWindow(): #clears the whole window of stuff
        for widget in root.winfo_children():
            widget.destroy()
    
    def mainMenu():
        clearWindow()
        #This is for the main menu
        title_label = tk.Label(root, text="Welcome to the stock program!\nWhat would you like to do today?", font=("Arial", 10))
        #The options for each
        B1 = Button(root, text ="Start New Seed Stock", command = newSeedStockMenu)
        B2 = Button(root, text ="Add Seed Stock", command = addSeedStockMenu)
        B3 = Button(root, text ="Get Seed Stock", command = getSeedStockMenu)
        B4 = Button(root, text ="Use Inventory", command = useInventoryMenu)
        B5 = Button(root, text ="Replenish Stock", command = replenishStockMenu)
        #B6 = Button(root, text ="Get Current Stock", command = getCurrentStockMenu)


        #puts all of the elements on the window in order
        title_label.pack(pady=4)
        B1.pack(pady=4)
        B2.pack(pady=4)
        B3.pack(pady=4)
        B4.pack(pady=4)
        B5.pack(pady=4)
        #B6.pack(pady=4)
    
    def newSeedStockMenu():
        clearWindow() #clears the window to add more stuff

        title_label = tk.Label(root, text="Start New Seed Stock", font=("Arial", 10))
        
        #executes the command AddSeedStock with the entry values
        def doTheThing():
            AddSeedStock(e1.get(), e2.get(), e3.get(), e4.get(), "new")

        #the comments are references to the original code
        #invID = input("Enter the new ID for the new Seed Stock: ")
        invID = tk.Label(root, text="ID: ", font=("Arial", 10))
        e1 = Entry(root)
        
        #newPN = input("Please enter the Part Number: ")
        newPN = tk.Label(root, text="Part Number: ", font=("Arial", 10))
        e2 = Entry(root)
        
        #newCount = input("What is the count for this part? ")
        newCount = tk.Label(root, text="Count: ", font=("Arial", 10))
        e3 = Entry(root)
        
        #newDesc = input("Please enter the part description: ")
        newDesc = tk.Label(root, text="Description: ", font=("Arial", 10))
        e4 = Entry(root)

        cur_y = 0
        x_pos = [150, 250]
        #places stuff down
        title_label.place(anchor=N, x=200, y=cur_y)
        cur_y += 35
        
        invID.place(anchor=N, x=x_pos[0], y=cur_y)
        e1.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35

        newPN.place(anchor=N, x=x_pos[0], y=cur_y)
        e2.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35

        newCount.place(anchor=N, x=x_pos[0], y=cur_y)
        e3.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35

        newDesc.place(anchor=N, x=x_pos[0], y=cur_y)
        e4.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35
        
        #buttons for adding and canceling
        add_button = Button(root, text ="Start New Seed Stock", command = doTheThing)
        back_button = Button(root, text ="Back to menu", command = mainMenu)

        add_button.place(anchor=N, x=200, y=cur_y)
        cur_y += 35
        back_button.place(anchor=N, x=200, y=cur_y)
    
    def addSeedStockMenu():
        clearWindow() #clears the window to add more stuff

        title_label = tk.Label(root, text="Start New Seed Stock", font=("Arial", 10))
        
        #executes the command AddSeedStock with the entry values
        def doTheThing():
            AddSeedStock(e1.get(), e2.get(), e3.get(), e4.get(), "add")

        #the comments are references to the original code
        #invID = input("Enter the new ID for the new Seed Stock: ")
        invID = tk.Label(root, text="ID: ", font=("Arial", 10))
        e1 = Entry(root)
        
        #newPN = input("Please enter the Part Number: ")
        newPN = tk.Label(root, text="Part Number: ", font=("Arial", 10))
        e2 = Entry(root)
        
        #newCount = input("What is the count for this part? ")
        newCount = tk.Label(root, text="Count: ", font=("Arial", 10))
        e3 = Entry(root)
        
        #newDesc = input("Please enter the part description: ")
        newDesc = tk.Label(root, text="Description: ", font=("Arial", 10))
        e4 = Entry(root)

        cur_y = 0
        x_pos = [150, 250]
        #places stuff down
        title_label.place(anchor=N, x=200, y=cur_y)
        cur_y += 35
        
        invID.place(anchor=N, x=x_pos[0], y=cur_y)
        e1.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35

        newPN.place(anchor=N, x=x_pos[0], y=cur_y)
        e2.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35

        newCount.place(anchor=N, x=x_pos[0], y=cur_y)
        e3.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35

        newDesc.place(anchor=N, x=x_pos[0], y=cur_y)
        e4.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35
        
        #buttons for adding and canceling
        add_button = Button(root, text ="Add Seed Stock", command = doTheThing)
        back_button = Button(root, text ="Back to menu", command = mainMenu)

        add_button.place(anchor=N, x=200, y=cur_y)
        cur_y += 35
        back_button.place(anchor=N, x=200, y=cur_y)
    
    def getSeedStockMenu():
        seedStock = ReadSeedStock(chosenFile)

        clearWindow() #clears the window to add more stuff
        
        title_label = tk.Label(root, text="Currently reading " + chosenFile, font=("Arial", 10))
        back_button = Button(root, text ="Back to menu", command = mainMenu)

        
        cataNames = list(seedStock.keys())

        invID = tk.Label(root, text="ID: ", font=("Arial", 10))
        #The options menu
        option_var = tk.StringVar(value=cataNames[0]) 
        l1 = tk.OptionMenu(root, option_var, *cataNames) 
        
        #newPN = input("Please enter the Part Number: ")
        newPN = tk.Label(root, text="Part Number: ", font=("Arial", 10))
        l2 = tk.Label(root, text="", font=("Arial", 10))
        
        #newCount = input("What is the count for this part? ")
        newCount = tk.Label(root, text="Count: ", font=("Arial", 10))
        l3 = tk.Label(root, text="", font=("Arial", 10))
        
        #newDesc = input("Please enter the part description: ")
        newDesc = tk.Label(root, text="Description: ", font=("Arial", 10))
        l4 = tk.Label(root, text="", font=("Arial", 10))

        cur_y = 0
        x_pos = [150, 250]
        #places stuff down
        title_label.place(anchor=N, x=200, y=cur_y)
        cur_y += 35
        
        invID.place(anchor=N, x=x_pos[0], y=cur_y)
        l1.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35

        newPN.place(anchor=N, x=x_pos[0], y=cur_y)
        l2.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35

        newCount.place(anchor=N, x=x_pos[0], y=cur_y)
        l3.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35

        newDesc.place(anchor=N, x=x_pos[0], y=cur_y)
        l4.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35
        
        back_button.place(anchor=N, x=200, y=cur_y)

        #This is what the menu does when an option is changed
        def reset_labels(*args):
            #this gets the index of the new option, as well as getting the chosen dicitonary
            new_name = option_var.get()
            chosen_dic = seedStock[new_name]

            l2.config(text = chosen_dic["Part Number"])
            l3.config(text = chosen_dic["Count"])
            l4.config(text = chosen_dic["Description"])
        
        #This detects if the option has changed
        option_var.trace("w", reset_labels)
        reset_labels()
    
    def useInventoryMenu():
        clearWindow() #clears the window to add more stuff

        title_label = tk.Label(root, text="Currently taking from " + chosenStock, font=("Arial", 10))

        #executes the command UseInventory with the entry values
        def doTheThing():
            if UseInventory(e1.get(), int(e2.get())):
                title_label.config(text="Done!")
            else:
                title_label.config(text="Not enough parts on hand. Please try again")

        #PN = input("Please enter the inventory ID you would like to use. 'format: 000' ")
        PN = tk.Label(root, text="(Format '000') Inventory ID: ", font=("Arial", 10))
        e1 = Entry(root)
        
        #count = input("How many of this part would you like to use? ")
        count = tk.Label(root, text="How many to use: ", font=("Arial", 10))
        e2 = Entry(root)

        cur_y = 0
        x_pos = [150, 250]
        #places stuff down
        title_label.place(anchor=N, x=200, y=cur_y)
        cur_y += 35
        PN.place(anchor=N, x=x_pos[0]-50, y=cur_y)
        e1.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35
        count.place(anchor=N, x=x_pos[0]-50, y=cur_y)
        e2.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35
        
        #buttons for adding and canceling
        add_button = Button(root, text ="Use Inventory", command = doTheThing)
        back_button = Button(root, text ="Back to menu", command = mainMenu)
        add_button.place(anchor=N, x=200, y=cur_y)
        cur_y += 35
        back_button.place(anchor=N, x=200, y=cur_y)

    def replenishStockMenu():
        clearWindow() #clears the window to add more stuff

        title_label = tk.Label(root, text="Currently taking from " + chosenFile + " to replenish " + chosenStock, font=("Arial", 10))

        #executes the command UseInventory with the entry values
        def doTheThing():
            if UseInventory(e1.get(), int(e2.get())):
                title_label.config(text="Done!")
            else:
                title_label.config(text="Too many parts for your location. Please check the destination adress and try again!")

        #invID = input("Please enter the inventory ID for the part you would like to replenish. 'format: 000' ")
        invID = tk.Label(root, text="(Format '000') Inventory ID: ", font=("Arial", 10))
        e1 = Entry(root)
        
        #count = input("How many parts are you replenishing? ")
        count = tk.Label(root, text="How many to replenish: ", font=("Arial", 10))
        e2 = Entry(root)

        cur_y = 0
        x_pos = [150, 250]
        #places stuff down
        title_label.place(anchor=N, x=200, y=cur_y)
        cur_y += 35
        invID.place(anchor=N, x=x_pos[0]-50, y=cur_y)
        e1.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35
        count.place(anchor=N, x=x_pos[0]-50, y=cur_y)
        e2.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35
        
        #buttons for adding and canceling
        add_button = Button(root, text ="Use Inventory", command = doTheThing)
        back_button = Button(root, text ="Back to menu", command = mainMenu)
        add_button.place(anchor=N, x=200, y=cur_y)
        cur_y += 35
        back_button.place(anchor=N, x=200, y=cur_y)
    
    mainMenu()

    #Shows the window
    root.mainloop()


#Menu()
make_window()
