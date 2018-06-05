from tkinter import *
window = Tk()
window.title("Package Calculator")

totalLabel = Label(window, text="Package Total", font=("Arial Bold", 20))
totalLabel.grid(column=0, row=0)
window.geometry('600x600')
totalEntry = Entry(window, width=20)
totalEntry.grid(column=1, row=0)
totalFinal = Label(window, font=("Arial Bold",20))
totalFinal.grid(column=2, row=0)

firstLabel = Label(window, text="Item 1", font=("Arial Bold", 20))
firstLabel.grid(column=0, row=1)
firstEntry = Entry(window, width=20)
firstEntry.grid(column=1, row=1)
firstFinal = Label(window, font=("Arial Bold",20))
firstFinal.grid(column=2, row=1)

secondLabel = Label(window, text="Item 2", font=("Arial Bold", 20))
secondLabel.grid(column=0, row=2)
secondEntry = Entry(window, width=20)
secondEntry.grid(column=1, row=2)
secondFinal = Label(window, font=("Arial Bold",20))
secondFinal.grid(column=2, row=2)

thirdLabel = Label(window, text="Item 3", font=("Arial Bold", 20))
thirdLabel.grid(column=0, row=3)
thirdEntry = Entry(window, width=20)
thirdEntry.grid(column=1, row=3)
thirdFinal = Label(window, font=("Arial Bold",20))
thirdFinal.grid(column=2, row=3)

fourthLabel = Label(window, text="Item 4", font=("Arial Bold", 20))
fourthLabel.grid(column=0, row=4)
fourthEntry = Entry(window, width=20)
fourthEntry.grid(column=1, row=4)
fourthFinal = Label(window, font=("Arial Bold",20))
fourthFinal.grid(column=2, row=4)

fifthLabel = Label(window, text="Item 5", font=("Arial Bold", 20))
fifthLabel.grid(column=0, row=5)
fifthEntry = Entry(window, width=20)
fifthEntry.grid(column=1, row=5)
fifthFinal = Label(window, font=("Arial Bold",20))
fifthFinal.grid(column=2, row=5)

sixthLabel = Label(window, text="Item 6", font=("Arial Bold", 20))
sixthLabel.grid(column=0, row=6)
sixthEntry = Entry(window, width=20)
sixthEntry.grid(column=1, row=6)
sixthFinal = Label(window, font=("Arial Bold",20))
sixthFinal.grid(column=2, row=6)

seventhLabel = Label(window, text="Item 7", font=("Arial Bold", 20))
seventhLabel.grid(column=0, row=7)
seventhEntry = Entry(window, width=20)
seventhEntry.grid(column=1, row=7)
seventhFinal = Label(window, font=("Arial Bold",20))
seventhFinal.grid(column=2, row=7)

eighthLabel = Label(window, text="Item 8", font=("Arial Bold", 20))
eighthLabel.grid(column=0, row=8)
eighthEntry = Entry(window, width=20)
eighthEntry.grid(column=1, row=8)
eighthFinal = Label(window, font=("Arial Bold",20))
eighthFinal.grid(column=2, row=8)

ninthLabel = Label(window, text="Item 9", font=("Arial Bold", 20))
ninthLabel.grid(column=0, row=9)
ninthEntry = Entry(window, width=20)
ninthEntry.grid(column=1, row=9)
ninthFinal = Label(window, font=("Arial Bold",20))
ninthFinal.grid(column=2, row=9)

tenthLabel = Label(window, text="Item 10", font=("Arial Bold", 20))
tenthLabel.grid(column=0, row=10)
tenthEntry = Entry(window, width=20)
tenthEntry.grid(column=1, row=10)
tenthFinal = Label(window, font=("Arial Bold",20))
tenthFinal.grid(column=2, row=10)

emptyLabel1 = Label(window,font=("Arial Bold",20))
emptyLabel1.grid(column=0,row=11)
emptyLabel2 = Label(window,font=("Arial Bold",20))
emptyLabel2.grid(column=0,row=12)
emptyLabel3 = Label(window,font=("Arial Bold",20))
emptyLabel3.grid(column=0,row=13)
lastLabel = Label(window, text="Package Calculator by Dan", font=("Arial", 10))
lastLabel.grid(column=0,row=14)

def calculate():
    packageTotal = float(getCost(totalEntry.get()))
    item1 = float(getCost(firstEntry.get()))
    item2 = float(getCost(secondEntry.get()))
    item3 = float(getCost(thirdEntry.get()))
    item4 = float(getCost(fourthEntry.get()))
    item5 = float(getCost(fifthEntry.get()))
    item6 = float(getCost(sixthEntry.get()))
    item7 = float(getCost(seventhEntry.get()))
    item8 = float(getCost(eighthEntry.get()))
    item9 = float(getCost(ninthEntry.get()))
    item10 = float(getCost(tenthEntry.get()))

    total = (item1+item2+item3+item4+item5+item6+item7+item8+item9+item10)

    multiplier = packageTotal / total
    
    packageItem1 = f"{round(item1*multiplier,2):.2f}"
    packageItem2 = f"{round(item2*multiplier,2):.2f}"
    packageItem3 = f"{round(item3*multiplier,2):.2f}"
    packageItem4 = f"{round(item4*multiplier,2):.2f}"
    packageItem5 = f"{round(item5*multiplier,2):.2f}"
    packageItem6 = f"{round(item6*multiplier,2):.2f}"
    packageItem7 = f"{round(item7*multiplier,2):.2f}"
    packageItem8 = f"{round(item8*multiplier,2):.2f}"
    packageItem9 = f"{round(item9*multiplier,2):.2f}"
    packageItem10 = f"{round(item10*multiplier,2):.2f}"

    packageTotal = f"{round(float(packageItem1)+float(packageItem2)+float(packageItem3)+float(packageItem4)+float(packageItem5)+float(packageItem6)+float(packageItem7)+float(packageItem8)+float(packageItem9)+float(packageItem10), 2):.2f}"

    totalFinal.configure(text=packageTotal, anchor=E, width=15)
    firstFinal.configure(text=packageItem1, anchor=E, width=15)
    secondFinal.configure(text=packageItem2, anchor=E, width=15)
    thirdFinal.configure(text=packageItem3, anchor=E, width=15)
    fourthFinal.configure(text=packageItem4, anchor=E, width=15)
    fifthFinal.configure(text=packageItem5, anchor=E, width=15)
    sixthFinal.configure(text=packageItem6, anchor=E, width=15)
    seventhFinal.configure(text=packageItem7, anchor=E, width=15)
    eighthFinal.configure(text=packageItem8, anchor=E, width=15)
    ninthFinal.configure(text=packageItem9, anchor=E, width=15)
    tenthFinal.configure(text=packageItem10, anchor=E, width=15)

def getCost(entry):
    if entry == "":
        entry = 0
    return entry

button = Button(window, text="Calculate", command=calculate)
button.grid(column=1, row=11)

window.mainloop()
