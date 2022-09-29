import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import time
import shutil
from datetime import datetime, timedelta


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #title for GUI window
        self.master.title("File Transfer")
        
        #Button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #Positions source button in GUI with tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30, 0))
        #Positions source directory selection
        self.source_dir = Entry(width=75)
        #positions entry in GUI using tkinter grid()
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30, 0))

        #Creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #Positions destination button in GUI using tkinter grid() on the next row
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #Creates entry for destiantion directory selection
        self.destination_dir = Entry(width=75)
        #Postitions entry in GUI using tkinter grid() padx and pady
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        #creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command = self.transferFiles)
        #positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0,15))

        #creates an exit button
        self.exit_btn = Button(text= "Exit", width=20, comman=self.exit_program)
        #positions the exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))
        
    
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #The .delete will clear the content that is inserted in the entry widget
        self.source_dir.delete(0, END)
        #The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)
        

    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        #The .delete will clear the content that is inserted in the entry widget
        self.destination_dir.delete(0, END)
        #The insert method will insert the user selection to the destination_dir Entry widget
        self.destination_dir.insert(0,selectDestDir)
        

    def transferFiles(self):
        
        source = self.source_dir.get()
        destination = self.destination_dir.get()
        source_files = os.listdir(source)


####USE DATETIME AND TIMEDELTA TO GET THE CURRENT TIME
        current_time = datetime.today()
        
        mod_check = current_time - timedelta(days = 1)
        #print("mod_check is: ", mod_check)

        
        
    
####USE OS.PATH.GETMTIME() TO GET THE TIMESTAMP OF THE FILE FROM ITS FILEPATH

        
        mod_time = os.path.getmtime(source)
    
        #timestamp of file
        file_date = datetime.fromtimestamp(mod_time)
        #print("file_date is: ", file_date)
                
####DEDUCT CURRENT TIME FROM THE TIMESTAMP OF THE FILES IN FOLDER
        
        compare_date = current_time - file_date
        


        
        
####CHECK IF THE RESULT OF THAT DEDUCTION IS LESS AND 24 HOURS.
        
        for i in source_files:
            if file_date > mod_check:
                print(i + ' is a new or edited in last 24 hours file')


    
    
    def exit_program(self):
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
