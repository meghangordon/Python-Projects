from cgitb import text
from sqlite3 import Row
import tkinter as tk
from tkinter import *
from tkinter.tix import COLUMN
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        self.btn = tk.Button(self.master, text="Default HTML Page", width=20, height=2, command=self.defaultHTML)
        self.btn.grid(row=4, column = 2, padx=(10, 10), pady=(10, 10), sticky=S+W)

        self.custbtn = tk.Button(self.master, text="Submit Custom Text", width=20, height=2, command=self.CustomHTML)
        self.custbtn.grid(row=4, column=3, padx=(10, 10), pady=(10, 10), sticky=S+E)

        self.custlabel = tk.Label(self.master, text="Enter custom text or click the 'Default HTML Page' button")
        self.custlabel.grid(row=0, column=0, rowspan= 1, columnspan=2, padx=(10,10), pady=(10, 10))

        self.custsource = StringVar()
        self.custsbt = tk.Entry(self.master, width=100, textvariable=self.custsource)
        self.custsbt.grid(row=1, column=0, rowspan = 1, columnspan = 5, padx=(10, 10), pady=(10, 10))
        

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</html>\n</body>\n</h1>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def CustomHTML(self):
        chtmlText = self.custsource.get()
        chtmlFile = open("Custom.html", "w")
        chtmlContent = "<html>\n<body>\n<h1>" + chtmlText + "</html>\n</body>\n</h1>" 
        chtmlFile.write(chtmlContent)
        chtmlFile.close()
        webbrowser.open_new_tab("Custom.html")
   

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
