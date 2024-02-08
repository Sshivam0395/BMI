from tkinter import*

root= Tk()
root.title("BMI Generator")
root.geometry("800x400")


def  calculate():
    weight = float(Entry1.get())
    height = float(Entry2.get())
    BMI = (weight / ((height)**2))
    if BMI < 18:
       T1="Underweight"
    elif BMI >= 18 and BMI < 25:
        T1="normal weight"
    else:
       T1="over weight"
    Entry3.delete(0,END)
    Entry3.insert(0,BMI)
    entry4.delete(0,END)
    entry4.insert(0,T1)


l1= Label(root,text="Enter your weight in kg:",font=('ariel',20,'bold'))
Entry1= Entry(root)
l2= Label(root,text="Enter your height in m:",font=('ariel',20, 'bold'))
Entry2 = Entry(root)
l3= Label(root, text="" , font=('ariel',25,'bold'))
Entry3 = Entry(root, text="")
entry4=Entry(root,text="")

l1.pack()
Entry1.pack(pady=20)
l2.pack()
Entry2.pack(pady=20)
Entry3.pack(pady=20)
entry4.pack(pady=20)

B1 = Button(root, text = "generate", command=calculate,bg="blue",fg="white")
B1.pack()



root.mainloop()