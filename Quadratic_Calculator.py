from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import math

root = Tk()
root.title("Quadratic Calculater")


def quad():
    a1 = float(a.get())
    b1 = float(b.get())
    c1 = float(c.get())
    try:
        x = (-b1 + math.sqrt((b1**2) - (4 * a1 * c1))) / (2*a1)
        y = (-b1 - math.sqrt((b1**2) - (4 * a1 * c1))) / (2*a1)
        z = (-b1)/(2*a1)
        e = (a1*(z)**2) + (b1 * z) + c1
        formu.config(text = f"{a.get()}x\u00b2 + {b.get()}x + {c.get()}")
        ans_1.config(text = (f"x\u2081 = {round(x, 5)}, x\u2082 = {round(y, 5)}"))
        ans_2.config(text = (f"line of symmetry = {round(z, 5)}"))
        ans_3.config(text = (f"vertex = ({round(z, 2)}, {round(e, 2)})"))
        ans_1.grid(row = 4, column = 0, columnspan = 2)
        ans_2.grid(row = 5, column = 0, columnspan = 2)
        ans_3.grid(row = 6, column = 0, columnspan = 2)
        q = np.arange(-20, 20, 0.1)
        p = a1*q**2 + b1*q + c1
        plt.plot(q,p)
        plt.show()
    except ValueError:
        ans_1.config(text = "Discrimant is smaller than 0", font = ("", 22, "italic"))
        ans_1.grid(row = 4, column = 0, columnspan = 2)
        ans_2.grid_forget()
        ans_3.grid_forget()

formu = Label(root, text = "ax\u00b2 + bx + c", font = ("", 22, "bold", "italic"))
a = Entry(root, font = ("", 22))
b = Entry(root, font = ("", 22))
c = Entry(root, font = ("", 22))
a_lab = Label(root, text = "a : ", font = ("", 22, "bold", "italic"))
b_lab = Label(root, text = "b : ", font = ("", 22, "bold", "italic"))
c_lab = Label(root, text = "c : ", font = ("", 22, "bold", "italic"))
ans_1 = Label(root, text = "", font = ("", 22))
ans_2 = Label(root, text = "", font = ("", 22))
ans_3 = Label(root, text = "", font = ("",22))
enter = Button(root, text = "Enter", font = ("", 22, "bold", "italic"), command = quad)

formu.grid(row = 0, column = 0, columnspan = 2)
a_lab.grid(row = 1, column = 0)
a.grid(row = 1, column = 1)
b_lab.grid(row = 2, column = 0)
b.grid(row = 2, column = 1)
c_lab.grid(row = 3, column = 0)
c.grid(row = 3, column = 1)
enter.grid(row = 7, column = 0, columnspan = 2)

root.mainloop()