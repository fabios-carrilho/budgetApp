#Libraries and imports 
from gui import BudgetApp
import tkinter as tk

#This is the main function that initialized the app
if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()
