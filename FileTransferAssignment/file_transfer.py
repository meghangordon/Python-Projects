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

        #gets source directory
        source = self.source_dir.get()

        #gets destination directory
        destination = self.destination_dir.get()

        #gets a list of files in the source directory
        source_files = os.listdir(source)

        
        
       #### Datetime & Datetime Timedelta to get the current time.

        now_time = datetime.now()
        print("Initial Date:", str(now_time))

        unknown_time = timedelta(hours = 24)

        mod_check = now_time - unknown_time

        #print("Checking for any files changed on or later than: ", str(mod_check))
              


        #### os.path.getmtime() to get the timestamp of the last modification

    
        modification_time = os.path.getmtime(source)

        local_time = time.ctime(modification_time)

        print("Last modification time(local time):", local_time)



        #### Deducting the current time from the timestamp of the files in folder
        date_time_of_file = datetime.fromtimestamp(modification_time)

        deduct_time = (now_time) - (date_time_of_file)

        print(date_time_of_file)
        print(now_time)
        print(deduct_time)


        ####Check if the result of that deduction is less than 24hrs. 

        def auto_transfer():
            if deduct_time <= modification_time:
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred automatically.')

        transferFiles()
        
    

    
    def exit_program(self):
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
