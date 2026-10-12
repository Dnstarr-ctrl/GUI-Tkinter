from tkinter import *
w=Tk()
w.title("activity 2")
w.geometry("500x600")
lbl=Label(w,text="new",bg="red",fg="white",height=1,width=300)
lbl.pack()

entry=Entry(w,width=150)
entry.pack()



w.mainloop()