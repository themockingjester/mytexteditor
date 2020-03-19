import os
from mic_feature import mic_feature
import speech_recognition as sr
import json  # used for catching the exception thrown by google audio

import openpyxl

import tkinter as tk
from datetime import date
from filename_provider import filename_provider
from Words_Suggestor import Words_Suggestor
from Words_adder import Words_adder
import time, threading
import keyboard
from tkinter import filedialog
from tkinter import scrolledtext

from words_filter import words_filter


class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        try:
            path1 = os.getcwd()
            path = path1 + '/include/resources/_usr/logs/traverse'
            os.makedirs(path)
            os.chdir(path1)
        except:
            pass

        self.title('Volcan Text Editor')
        ################################# thread which what to do when pair of keys pressed ################################
        # thread3 = threading.Thread(target=self.keysresponser)
        # thread3.start()
        ######################################### #########################################################################

        ################################################create file panel#####################################################
        self.logo = tk.PhotoImage(file='createfile1.png')
        self.newbutton = tk.Button(self, text='new file', command=self.create_file, compound=tk.TOP, relief=tk.FLAT,
                                   image=self.logo,
                                   font=("garamond", "10", "bold"))  # score teller
        self.newbutton.place(x=0, y=30)
        #######################################################################################################################

        ############################################### Scrolledtext panel ####################################################
        self.txtbox = scrolledtext.ScrolledText(self, width=190, height=38)
        self.txtbox.place(x=32, y=160)
        #######################################################################################################################

        ########################################## open file panel ###########################################################
        self.logo2 = tk.PhotoImage(file='openfile.png')
        self.openfilebutton = tk.Button(self, text='open file', command=self.open_file, compound=tk.TOP, relief=tk.FLAT,
                                        image=self.logo2, font=("garamond", "10", "bold"))  # score teller
        self.openfilebutton.place(x=100, y=30)
        #######################################################################################################################

        ####################################### setting status icon ##########################################################
        self.logo3 = tk.PhotoImage(file='running.png')
        self.logo4 = tk.PhotoImage(file='loading.png')
        self.status = tk.Label(self, relief=tk.FLAT, image=self.logo3)  # score teller
        self.status.place(x=1500, y=60)
        ######################################################################################################################

        ################################################# setting save icon ##################################################

        self.logo5 = tk.PhotoImage(file='save')
        self.savebutton = tk.Button(self, text='save file', command=self.save_file, compound=tk.TOP, relief=tk.FLAT,
                                    image=self.logo5, font=("garamond", "10", "bold"))  # score teller
        self.savebutton.place(x=200, y=30)
        #######################################################################################################################

        ############################################## setting saveas icon ###################################################
        self.logo6 = tk.PhotoImage(file='saveas')
        self.saveasbutton = tk.Button(self, text='save file as', command=self.save_as_file, compound=tk.TOP,
                                      relief=tk.FLAT, image=self.logo6, font=("garamond", "10", "bold"))
        self.saveasbutton.place(x=300, y=30)
        #######################################################################################################################

        ############################################### setting time traverser ################################################
        self.logo7 = tk.PhotoImage(file='clock')
        self.timetraverserbutton = tk.Button(self, text='time traverser', command=self.time_traverse, compound=tk.TOP,
                                             relief=tk.FLAT,
                                             image=self.logo7, font=("garamond", "10", "bold"))
        self.timetraverserbutton.place(x=400, y=30)
        ########################################################################################################################

        ############################################### setting AI enabler ################################################
        self.logo8 = tk.PhotoImage(file='ai activated')
        self.aicounter = 0
        self.logo9 = tk.PhotoImage(file='ai deactivated')
        self.aibutton = tk.Button(self, command=self.ai_mode, compound=tk.TOP,
                                  relief=tk.FLAT,
                                  image=self.logo9, font=("garamond", "10", "bold"))
        self.aibutton.place(x=1400, y=60)
        ########################################################################################################################

        ############################################# file address label ####################################################

        self.file_address_label = tk.Label(self, relief=tk.FLAT, text='untitled',
                                           font=("garamond", "15", "bold", "italic"))  # score teller
        self.file_address_label.place(x=40, y=822)

        ######################################################################################################################

        ###########################################setting listbox ###########################################################

        root = tk.Frame(self)
        root.place(x=1200, y=35)
        scrollbar = tk.Scrollbar(root)
        # scrollbar.pack(side=RIGHT, fill=Y) # Now it's active, but not visible
        self.lstbox = tk.Listbox(root, height=6)
        self.lstbox.pack(side=tk.LEFT)

        # attach listbox to scrollbar
        self.lstbox.config(yscrollcommand=scrollbar.set)

        scrollbar.config(command=self.lstbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        #######################################################################################################################

        ##################################################### settinng copy button ##############################################
        self.logo10 = tk.PhotoImage(file='copy')

        self.copybutton = tk.Button(self, text='copy', command=self.copy_file, compound=tk.TOP,
                                    relief=tk.FLAT,
                                    image=self.logo10, font=("garamond", "10", "bold"))
        self.copybutton.place(x=530, y=30)
        ######################################################################################################################

        ############################################ setting microphone icon ##################################################
        self.botcounter = 0
        self.logo11 = tk.PhotoImage(file='offmic')
        self.logo12 = tk.PhotoImage(file='onmic')
        self.micbutton = tk.Button(self, text='mic', command=self.auto_type, compound=tk.TOP,
                                   relief=tk.FLAT,
                                   image=self.logo11, font=("garamond", "10", "bold"))
        self.micbutton.place(x=630, y=30)

    def auto_type(self):
        thread4 = threading.Thread(target=self.bot)
        thread4.start()

    def bot(self):
        self.botcounter += 1

        while self.botcounter % 2 != 0:
            self.micbutton.config(image=self.logo12)
            obj = mic_feature()

            self.txtbox.insert(tk.INSERT, obj.get())
        self.micbutton.config(image=self.logo11)
        print("bot stopped")
    def copy_file(self):
        self.clipboard_clear()
        text = self.txtbox.get(1.0, tk.END)
        self.clipboard_append(text)
        return 0

    def keysresponser(self):
        if 1 == 1:
            try:  # used try so that if user pressed other than the given key error will not be shown

                if keyboard.is_pressed('ctrl + s'):  # save file
                    print('saving the file!')
                    self.save_file()
                if keyboard.is_pressed('ctrl + shift + c'):  # COPY file
                    print('coping the file!')
                    self.copy_file()
                if keyboard.is_pressed('ctrl + o'):  # open file
                    print('opening the file!')
                    self.open_file()
                if keyboard.is_pressed('esc'):  # ai button
                    print('ai !')
                    self.ai_mode()
                if keyboard.is_pressed('ctrl + shift + r'):  # time traverser button
                    print('time traverser mode !')
                    self.time_traverse()
                if keyboard.is_pressed('ctrl + shift + n'):  # new file  button
                    print('new file!')
                    self.create_file()

                return 0

            except:
                pass

    def time_traverse(self):

        path1 = os.getcwd()
        path = path1 + '/include/resources/_usr/logs/traverse'
        filename = tk.filedialog.askopenfilename(initialdir=path, title="Select file",
                                                 filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        try:
            self.txtbox.delete(1.0, tk.END)
            self.filename_pointer = filename
            f = open(filename, "r")
            for i in f.read():
                self.txtbox.insert(tk.END, i)
            self.file_address_label.config(text=filename)

        except:
            pass

    @property
    def word_suggestion_method(self):
        while 1 == 1:
            self.keysresponser()
            if self.aicounter % 2 != 0:

                a = self.txtbox.get(1.0, tk.INSERT)

                lis = a.split(" ")
                removablewords = ['\n', '\t']
                word = ' '.join([i for i in lis if i not in removablewords])  # removining tabs and new line character
                word = word.split(" ")  # againg breaking the filtewred string to get the last word
                word = str(word[-1])
                word = word.split('\n')

                if (len(word) <= 1):
                    word = str(word[0])
                else:
                    word = str(word[-1])

                try:
                    if old == word:
                        if len(self.lstbox.curselection()) != 0 and lstboxcurrcounter == 0:

                            #########################
                            str5 = str(self.lstbox.get(self.lstbox.curselection()))
                            str5 = str5.replace(word, "", 1)
                            try:
                                for m in str5:
                                    self.txtbox.insert(tk.INSERT, m)
                                self.txtbox.focus_set()
                            except:
                                pass
                            ####################
                            lstboxcurrcounter += 1
                        continue
                    else:
                        pass
                except:
                    pass
                lstboxcurrcounter = 0
                obj = Words_Suggestor(word)

                try:
                    self.lstbox.delete(0, tk.END)
                except:
                    pass
                for i in obj.list_return():
                    self.lstbox.insert(0, i)

                old = word

            else:
                return 0

    def ai_mode(self):
        self.aicounter += 1


        thread1 = threading.Thread(target=self.ai_working)
        thread1.start()

    def ai_working(self):

        if self.aicounter % 2 != 0:
            self.aibutton.config(image=self.logo8)
            self.update()
            thread2 = threading.Thread(target=self.word_suggestion_method)
            thread2.start()


        else:
            print('stopped!!!!')
            self.aibutton.config(image=self.logo9)
            self.update()
        return 0

    def anoynymous_save(self, namecopy):
        currdate = date.today()
        currtime = time.strftime("%H:%M:%S")
        if 1 == 1:
            path1 = os.getcwd()
            filename = path1 + '/include/resources/_usr/logs/traverse/'
            filename = filename + namecopy + str(currdate) + str(currtime)
            f = open(filename, "w")
            a = self.txtbox.get(1.0, tk.END)

            f.write(a)
            f.close()
            return 0

    def save_file(self):
        self.status.config(image=self.logo4)
        self.update()
        # try:
        if 1 == 1:
            if self.file_address_label.cget("text") != 'untitled':
                f = open(self.filename_pointer, "w")
                a = self.txtbox.get(1.0, tk.END)

                f.write(a)
                f.close()
                obj2 = filename_provider(self.filename_pointer)
                namecopy = obj2.get()
                self.anoynymous_save(namecopy)

                ################# adding the files word to words library file ###################
                lis = words_filter(a)
                listofwords = lis.output()
                obj = Words_adder(listofwords)

            else:
                filename = tk.filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                           filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
                self.filename_pointer = filename
                f = open(filename, "w")
                a = self.txtbox.get(1.0, tk.END)

                f.write(a)
                f.close()
                self.file_address_label.config(text=filename)
                self.update()
                obj2 = filename_provider(filename)
                namecopy = obj2.get()
                self.anoynymous_save(namecopy)
                ################# adding the files word to words library file ###################
                lis = words_filter(a)
                listofwords = lis.output()
                obj = Words_adder(listofwords)

        # except:
        #   print('exception!!')
        self.status.config(image=self.logo3)
        self.update()

    def save_as_file(self):
        self.status.config(image=self.logo4)
        self.update()
        try:
            filename = tk.filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                       filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
            f = open(filename, "w")
            a = self.txtbox.get(1.0, tk.END)

            f.write(a)
            f.close()
            obj2 = filename_provider(self.filename)
            namecopy = obj2.get()
            self.anoynymous_save(namecopy)
            ################# adding the files word to words library file ################self.anoynymous_save()###
            lis = words_filter(a)
            listofwords = lis.output()
            obj = Words_adder(listofwords)

        except:
            pass
        self.status.config(image=self.logo3)
        self.update()

    def create_file(self):
        self.status.config(image=self.logo4)
        self.update()
        self.win1 = tk.Toplevel(self)
        message = tk.Label(self.win1, text='Are you sure you want to delete the content and want new file?')
        message.pack()
        button1 = tk.Button(self.win1, text='Yes', command=self.confirm_new_file)
        button1.pack()
        button2 = tk.Button(self.win1, text='No', command=self.cancel_new_file)
        button2.pack()

    def cancel_new_file(self):
        self.win1.destroy()
        self.status.config(image=self.logo3)
        self.update()

    def confirm_new_file(self):
        self.win1.destroy()
        self.filename_pointer = ""
        self.file_address_label.config(text='untitled')
        self.txtbox.delete(1.0, tk.END)
        self.status.config(image=self.logo3)
        self.update()

    def open_file(self):

        self.status.config(image=self.logo4)
        self.update()

        filename = tk.filedialog.askopenfilename(initialdir="/", title="Select file",
                                                 filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
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
