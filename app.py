#AB17
#Import
from time import strftime
from tkinter import Label, Tk
#windowspecification
window = Tk()
window.title("")
window.geometry("220x100")
window.configure(bg="blue")  #clock BG
window.resizable(False, False)  
#clockspecification
clock_label = Label(
    window, bg="black", fg="red", font=("Arial", 30, "bold"), relief="flat"
)
clock_label.place(x=20, y=20)
#def and update
def update_label():

    current_time = strftime("%H: %M: %S\n %d-%m-%Y ")
    clock_label.configure(text=current_time)
    clock_label.after(80, update_label)
    clock_label.pack(anchor="center")

update_label()
window.mainloop()
