from tkinter import *
import tkinter as tk
import os
import urllib.request
import sqlite3


    
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(450,200)
        self.master.maxsize(450,200)
        self.master.title("Check files")
        self.master.configure(bg="lightgray")
        
        def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
        # get user's screen width and height
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()
        # calculate x and y coordinates to paint the app centered on the user's screen
            x = int((screen_width/2) - (w/2))
            y = int((screen_height/2) - (h/2))
            centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
            return centerGeo
       
        def go():
                text.delete(1.0, END)
                with urllib.request.urlopen(entry.get()) as response:
                        received_html = response.read()
                text.insert(1.0, received_html)
                entry = Entry(txt_Browser,txt_Browser2)

        txt_Browser = Tk()
        text = Text(txt_Browser)
        self.txt_Browser = tk.Entry(self.master,width=50,text='')
        self.txt_Browser.grid(row=1,column=7,pady=(35,8))
        self.txt_Browser2 = tk.Entry(self.master,width=50,text='')
        self.txt_Browser2.grid(row=25,column=7)

                

        self.btn_Browse1 = tk.Button(self.master,width=15,height=1,text='Browse...',command=go)
        self.btn_Browse1.grid(row=1,column=2,pady=(35,8))
        self.btn_Browse2 = tk.Button(self.master,width=15,height=1,text='Browse...',command=go)
        self.btn_Browse2.grid(row=25,column=2,pady=10)
        self.btn_Check = tk.Button(self.master,width=15,height=2,text='Check for files...',command=go)
        self.btn_Check.grid(row=75,column=2,padx=10,pady=10)
        self.btn_Close = tk.Button(self.master,width=15,height=2,text='Close Program',command=None)
        self.btn_Close.grid(row=75,column=7,sticky=S+E)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
