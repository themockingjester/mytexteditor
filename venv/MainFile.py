import tkinter as tk
import time
from tkinter import filedialog
from tkinter import scrolledtext

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        ################################################create file panel#####################################################
        self.logo = tk.PhotoImage(file='createfile1.png')
        self.newbutton = tk.Button(self, text='new file', command = self.create_file, compound=tk.TOP, relief=tk.FLAT, image=self.logo,
                                      font=("garamond", "10", "bold"))  # score teller
        self.newbutton.place(x=0, y=30)
        #######################################################################################################################


        ############################################### Scrolledtext panel ####################################################
        self.txtbox = scrolledtext.ScrolledText(self, width=190, height=38)
        self.txtbox.place(x=32,y=160)
        #######################################################################################################################


        ########################################## open file panel ###########################################################
        self.logo2 = tk.PhotoImage(file='openfile.png')
        self.openfilebutton = tk.Button(self, text='open file', command=self.open_file, compound=tk.TOP, relief=tk.FLAT,image=self.logo2,font=("garamond", "10", "bold"))  # score teller
        self.openfilebutton.place(x=100, y=30)
        #######################################################################################################################

        ####################################### setting status icon ##########################################################
        self.logo3 = tk.PhotoImage(file='running.png')
        self.logo4 = tk.PhotoImage(file='loading.png')
        self.status = tk.Label(self, relief=tk.FLAT,image=self.logo3)  # score teller
        self.status.place(x=1500, y=60)
        ######################################################################################################################


        ################################################# setting save icon ##################################################

        self.logo5 = tk.PhotoImage(file='save')
        self.savebutton = tk.Button(self, text='save file', command=self.save_file, compound=tk.TOP, relief=tk.FLAT,image=self.logo5,font=("garamond", "10", "bold"))  # score teller
        self.savebutton.place(x=200, y=30)
        #######################################################################################################################


        ############################################## setting saveas icon ###################################################
        self.logo6 = tk.PhotoImage(file='saveas')
        self.saveasbutton = tk.Button(self, text='save file as', command=self.save_as_file, compound=tk.TOP, relief=tk.FLAT,image=self.logo6, font=("garamond", "10", "bold"))
        self.saveasbutton.place(x=300, y=30)
        #######################################################################################################################


        ############################################### setting time traverser ################################################
        self.logo7 = tk.PhotoImage(file='clock')
        self.timetraverserbutton = tk.Button(self, text='time traverser', command=self.open_file, compound=tk.TOP, relief=tk.FLAT,
                                    image=self.logo7, font=("garamond", "10", "bold"))
        self.timetraverserbutton.place(x=400, y=30)
        ########################################################################################################################

        ############################################### setting AI enabler ################################################
        self.logo8 = tk.PhotoImage(file='ai activated')
        self.logo9 = tk.PhotoImage(file='ai deactivated')
        self.aibutton = tk.Button(self,command=self.open_file, compound=tk.TOP,
                                             relief=tk.FLAT,
                                             image=self.logo9, font=("garamond", "10", "bold"))
        self.aibutton.place(x=1400, y=60)
        ########################################################################################################################


        ############################################# file address label ####################################################

        self.file_address_label = tk.Label(self, relief=tk.FLAT, text='untitled',font=("garamond", "15", "bold","italic"))  # score teller
        self.file_address_label.place(x=800, y=822)

        ######################################################################################################################
        
    def save_file(self):
        self.status.config(image=self.logo4)
        self.update()
        try:
            if self.file_address_label.cget("text")!='untitled':
                f = open(self.filename_pointer, "w")
                a = self.txtbox.get(1.0, tk.END)

                f.write(a)
                f.close()
            else:
                filename = tk.filedialog.asksaveasfilename(initialdir="/", title="Select file",filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
                self.filename_pointer=filename
                f = open(filename, "w")
                a=self.txtbox.get(1.0,tk.END)

                f.write(a)
                f.close()
                self.file_address_label.config(text=filename)
        except:
            pass
        self.status.config(image=self.logo3)
        self.update()
    def save_as_file(self):
        self.status.config(image=self.logo4)
        self.update()
        try:
            filename = tk.filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                       filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
            f = open(filename, "w")
            a = self.txtbox.get(1.0, tk.END)

            f.write(a)
            f.close()
        except:
            pass
        self.status.config(image=self.logo3)
        self.update()
    def create_file(self):
        self.status.config(image=self.logo4)
        self.update()
        self.filename_pointer=""
        self.file_address_label.config(text='untitled')
        self.txtbox.delete(1.0, tk.END)
        self.status.config(image=self.logo3)
        self.update()
    def open_file(self):

        self.status.config(image=self.logo4)
        self.update()

        filename = tk.filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        try:
            self.txtbox.delete(1.0, tk.END)
            self.filename_pointer = filename
            f = open(filename, "r")
            for i in f.read():
                self.txtbox.insert(tk.END, i)
            self.file_address_label.config(text=filename)

        except:
            pass

        self.status.config(image=self.logo3)
        self.update()
if __name__ == "__main__":
        app = Main()
        app.mainloop()