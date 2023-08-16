import tkinter as tk
import sys

window = tk.Tk()
window.grid_columnconfigure(0, weight=1)
window.title("Lambda")
window.geometry("300x100")
lable = tk.Label(window, text="Lambda calculus")
lable.grid(column=0, row=0)
button = tk.Button(
    window,
    text="Reverse",
    command=lambda: lable.configure(text=lable.cget("text")[::-1])
)
button.grid(column=0, row=1)

window.mainloop()