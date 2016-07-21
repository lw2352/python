import tkinter as tk:

class APP():
    def __init__(self,master):
        frame = tk.Frame(master)
        frame.pack()

        self.hi_there = tk.Button(frame,text = "你好",fg = "red")

root = tk.TK()
app = APP(root)

root.mainloop()
