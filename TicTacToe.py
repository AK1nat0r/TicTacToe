# --------------------------------------------
# 11AS7A
# Elias Jäger, Nauris Dubauskas
# LF6
# 2018 | ALL RIGHTS RESERVED
# --------------------------------------------

#Recources
from tkinter import *
import random
import time
import socket

import sys
import os


try:
    print ("Importing required Pillow Library..\n")
    import PIL.Image
    import PIL.ImageTk
    print('Starting Game..\n')
except ImportError:
    print ("Please wait..\n")
    print ("Checking and upgrading PIP Library..\n")
    os.system('python -m pip install --upgrade pip')
    print ("Downloading and installing Pillow Library..\n")
    os.system('python -m pip install Pillow')
    print ("Starting Game..\n")
import PIL.Image
import PIL.ImageTk



class Game_Gui:
    def __init__(self):
        self.window = Tk()
        self.window.config(bg='#232323')
        self.window.attributes("-fullscreen", False)

        self.window.rowconfigure(1, weight=5)
        self.window.columnconfigure(1, weight=5)
        self.window.rowconfigure(6, weight=5)
        self.window.columnconfigure(1, weight=5)

        self.window.title("TicTacToe")
        self.state = True
        self.window.attributes("-fullscreen", True)
        self.window.bind("<F11>", self.toggle_fullscreen)
        self.window.bind("<Escape>", self.end_fullscreen)

        # Settings - icon
        setsrc = PIL.Image.open("res/settings.png")
        setimg = PIL.ImageTk.PhotoImage(setsrc)

        self.Settings_btn = Button(self.window, image=setimg, width=100,height=100,border=0,bg="#232323",fg ="white",font=2,command=lambda:self.settings())
        self.Settings_btn.image = setimg
        self.Settings_btn.grid(row=0,column=0)
        # --------

        # Close - icon
        closesrc = PIL.Image.open("res/close.png")
        closeimg = PIL.ImageTk.PhotoImage(closesrc)

        self.Close_btn = Button(self.window, image=closeimg, width=100,height=100,border=0,bg="#232323",fg ="white",font=2,command=lambda:self.close())
        self.Close_btn.image = closeimg
        self.Close_btn.grid(row=0,column=3)
        # --------

        # Logo
        logosrc = PIL.Image.open("res/logo.png")
        logoimg = PIL.ImageTk.PhotoImage(logosrc)

        self.logo = Label(self.window, image=logoimg, width=600,height=150,border=0,bg="#232323",fg ="white",font=2,text="Restart")
        self.logo.image = logoimg
        self.logo.grid(row=2,column=1)
        # --------


        # Menu
        com_btn = Button(self.window,width=40,height=1,bg="#232323",fg="white",font=2,text="1 Player", command=lambda:self.vsCom())
        com_btn.grid(row=3,column=1)

        ovo_btn = Button(self.window,width=40,height=1,bg="#232323",fg="white",font=2,text="2 Player", command=lambda:self.ovo_btn())
        ovo_btn.grid(row=4,column=1)
        # --------

        self.window.mainloop()
        
    def close(self):
        self.window.destroy()
        
    def settings(self):
        self.window.destroy()
        Settings()

    def ovo_btn(self):
        self.window.destroy()
        onevsone()

    def vsCom(self):
        self.window.destroy()
        vsCom()
        
    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.window.attributes("-fullscreen", self.state)
        self.window.config(width=500, height=500)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.window.attributes("-fullscreen", False)
        self.window.config(width=500, height=500)
        return "break"
    
class Settings:
    def __init__(self):
        self.window = Tk()
        self.window.config(bg='#232323', width=False, height=False)
        self.window.title("Settings | TicTacToe")

        self.state = True
        self.window.attributes("-fullscreen", True)
        self.window.bind("<F11>", self.toggle_fullscreen)
        self.window.bind("<Escape>", self.end_fullscreen)

        self.window.rowconfigure(1, weight=0)
        self.window.columnconfigure(0, weight=0)
        self.window.rowconfigure(2, weight=2)
        self.window.columnconfigure(1, weight=1)


        # Menu - Icon
        menusrc = PIL.Image.open("res/menu.png")
        menuimg = PIL.ImageTk.PhotoImage(menusrc)

        self.Menu_btn = Button(self.window, image=menuimg, width=200,height=100,border=0,bg="#232323",fg ="white",font=2,text="←",command=lambda:self.Back())
        self.Menu_btn.image = menuimg  # keep a reference!
        self.Menu_btn.grid(row=0,column=0)
        # --------

        # Logo
        logosrc = PIL.Image.open("res/logo.png")
        logoimg = PIL.ImageTk.PhotoImage(logosrc)   

        self.logo = Label(self.window, image=logoimg, width=500,height=150,border=0,bg="#232323",fg ="white",font=2)
        self.logo.image = logoimg
        self.logo.grid(row=0,column=1)
        # --------

        self.credits = Label(self.window,width=150,height=20,border=0,bg="#232323",fg ="white",font=2,text="Coded by:\n\n Elias Jäger\nNauris Dubauskas\n\n\n\nProject for:\nWerner-Von-Siemens Schule\n\n\n\n© 2018 | Nauris Dubauskas, Elias Jäger, Antonio Balbi | ALL RIGHTS RESERVED")
        self.credits.grid(row=2,column=1)

        self.window.mainloop()

    def Back(self):
        self.window.destroy()
        Game_Gui()

    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.window.attributes("-fullscreen", self.state)
        self.window.config(width=500, height=500)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.window.attributes("-fullscreen", False)
        self.window.config(width=500, height=500)
        return "break"
    
class onevsone:
    def __init__(self):
        self.window = Tk()
        self.window.config(bg='#232323', width=False, height=False)
        
        self.window.title("2 Player | TicTacToe")
        self.state = True
        self.window.attributes("-fullscreen", True)
        self.window.bind("<F11>", self.toggle_fullscreen)
        self.window.bind("<Escape>", self.end_fullscreen)

        # Required variablen      
        self.t1 = 0
        self.c1 = 1
        self.won = 0
        self.player_one = "X"
        self.player_two = "O"
        self.X_count= 0
        self.O_count= 0
        self.fos = 0

        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=4)
        self.window.rowconfigure(8, weight=3)
        self.window.columnconfigure(8, weight=5)
        # --------

        # Points Counter
        self.Counter = Label(self.window,width=12,height=1, font=(None, 30),bg="#232323",fg="white",text="X : O")
        self.Counter.grid(row=0,column=5)
        # --------

        

        # Restart - Icon
        restartsrc = PIL.Image.open("res/restart.png")
        restartimg = PIL.ImageTk.PhotoImage(restartsrc)

        self.Restart_btn = Button(self.window, image=restartimg, width=200,height=100,border=0,bg="#232323",fg ="white",font=2,text="Restart",command=lambda:self.Restart())
        self.Restart_btn.image = restartimg
        self.Restart_btn.grid(row=3,column=0)
        # --------

        # Menu - Icon
        menusrc = PIL.Image.open("res/menu.png")
        menuimg = PIL.ImageTk.PhotoImage(menusrc)

        self.Back_btn = Button(self.window, image=menuimg, width=200,height=100,border=0,bg="#232323",fg ="white",font=2,text="←",command=lambda:self.Back())
        self.Back_btn.image = menuimg
        self.Back_btn.grid(row=0,column=0)
        # --------


        # Replay - Icon
        replaysrc = PIL.Image.open("res/replay.png")
        replayimg = PIL.ImageTk.PhotoImage(replaysrc)

        self.Again_btn = Button(self.window, image=replayimg, width=200,height=100,border=0,bg="#232323",fg ="white",font=2,text="Again",command=lambda:self.Again())
        self.Again_btn.image = replayimg
        self.Again_btn.grid(row=5,column=0)
        # --------



        # Field Markings
        self.bx1 = Label(self.window, width=1,height=1,bg="grey",fg="white",text="")
        self.bx1.grid(row=2,column=3,sticky='we')

        self.bx2 = Label(self.window, width=1,height=1,bg="grey",fg="white",text="")
        self.bx2.grid(row=2,column=5,sticky='we')

        self.bx3 = Label(self.window, width=1,height=1,bg="grey",fg="white",text="")
        self.bx3.grid(row=2,column=7,sticky='we')

        self.bx4 = Label(self.window, width=1,height=1,bg="grey",fg="white",text="")
        self.bx4.grid(row=4,column=3,sticky='we')

        self.bx5 = Label(self.window, width=1,height=1,bg="grey",fg="white",text="")
        self.bx5.grid(row=4,column=5,sticky='we')

        self.bx6 = Label(self.window, width=1,height=1,bg="grey",fg="white",text="")
        self.bx6.grid(row=4,column=7,sticky='we')

        # ---

        self.by1 = Label(self.window, width=1,height=12,bg="grey",fg="white",text="")
        self.by1.grid(row=1,column=4,sticky='we')
        
        self.by2 = Label(self.window, width=1,height=12,bg="grey",fg="white",text="")
        self.by2.grid(row=1,column=6,sticky='we')

        self.by3 = Label(self.window, width=1,height=12,bg="grey",fg="white",text="")
        self.by3.grid(row=3,column=4,sticky='we')
        
        self.by4 = Label(self.window, width=1,height=12,bg="grey",fg="white",text="")
        self.by4.grid(row=3,column=6,sticky='we')

        self.by5 = Label(self.window, width=1,height=12,bg="grey",fg="white",text="")
        self.by5.grid(row=5,column=4,sticky='we')
        
        self.by6 = Label(self.window, width=1,height=12,bg="grey",fg="white",text="")
        self.by6.grid(row=5,column=6,sticky='we')
        # --------


        # Game Field | 1 - 3
        self.First_btn = Button(self.window, width=5,height=2,highlightbackground="#232323",bg="#232323",fg="white",font=(None, 45),text="",border=0,command=lambda:self.X_or_O_1())     
        self.First_btn.grid(row=1,column=3,sticky='we')
        
        self.Second_btn = Button(self.window,width=5,height=2, bg="#232323",fg="white",text="",font=(None, 45),border=0,command=lambda:self.X_or_O_2())
        self.Second_btn.grid(row=1,column=5,sticky='we')      

        self.Third_btn = Button(self.window,width=5,height=2, bg="#232323",fg="white",text="",font=(None, 45),border=0,command=lambda:self.X_or_O_3())
        self.Third_btn.grid(row=1,column=7,sticky='we')
        # --------

        
        # Game Field | 4 - 6
        self.Fourth_btn = Button(self.window,width=5,height=2, bg="#232323",fg="white",text="",font=(None, 45),border=0,command=lambda:self.X_or_O_4())
        self.Fourth_btn.grid(row=3,column=3,sticky='we')

        self.Fifth_btn = Button(self.window,width=5,height=2, bg="#232323",fg="white",text="",font=(None, 45),border=0,command=lambda:self.X_or_O_5())
        self.Fifth_btn.grid(row=3,column=5,sticky='we')      

        self.Sixth_btn = Button(self.window,width=5,height=2, bg="#232323",fg="white",text="",font=(None, 45),border=0,command=lambda:self.X_or_O_6())
        self.Sixth_btn.grid(row=3,column=7,sticky='we')
        # --------


        # Game Field | 7 - 9
        self.Seventh_btn = Button(self.window,width=5,height=2, bg="#232323",fg="white",text="",font=(None, 45),border=0,command=lambda:self.X_or_O_7())
        self.Seventh_btn.grid(row=5,column=3,sticky='we')

        self.Eight_btn = Button(self.window,width=5,height=2, bg="#232323",fg="white",text="",font=(None, 45),border=0,command=lambda:self.X_or_O_8())
        self.Eight_btn.grid(row=5,column=5,sticky='we')      

        self.Ninth_btn = Button(self.window,width=5,height=2, bg="#232323",fg="white",text="",font=(None, 45),border=0,command=lambda:self.X_or_O_9())
        self.Ninth_btn.grid(row=5,column=7,sticky='we')
        # --------

        # Won images
        self.wons_x_src = PIL.Image.open("res/won_x.png")
        self.won_x_img = PIL.ImageTk.PhotoImage(self.wons_x_src)

        self.Won_X_img = Label(self.window,image="", width=0,height=0,border=0,bg="#232323",fg ="white",font=2)
        self.Won_X_img.image = self.won_x_img
        self.Won_X_img.grid(row=0,column=3)

        self.wons_o_src = PIL.Image.open("res/won_o.png")
        self.won_o_img = PIL.ImageTk.PhotoImage(self.wons_o_src)

        self.Won_O_img = Label(self.window,image="",width=0,height=0,border=0,bg="#232323",fg ="white",font=2)
        self.Won_O_img.image = self.won_o_img
        self.Won_O_img.grid(row=0,column=7)
        # --------
        


        self.window.mainloop()
        
    def Back(self):
        self.window.destroy()
        Game_Gui()

    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.window.attributes("-fullscreen", self.state)
        self.window.config(width=500, height=500)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.window.attributes("-fullscreen", False)
        self.window.config(width=500, height=500)
        return "break"

    def Again(self):
        self.t1 = 0
        if self.fos % 2:
            self.c1 = 1
        else:
            self.c1 = 0
            
        self.won = 0
        self.fos += 1

        self.First_btn["text"] = ""
        self.Second_btn["text"] = ""
        self.Third_btn["text"] = ""
        self.Fourth_btn["text"] = ""
        self.Fifth_btn["text"] = ""
        self.Sixth_btn["text"] = ""
        self.Seventh_btn["text"] = ""
        self.Eight_btn["text"] = ""
        self.Ninth_btn["text"] = ""

        self.First_btn["fg"] = "white"
        self.Second_btn["fg"] = "white"
        self.Third_btn["fg"] = "white"
        self.Fourth_btn["fg"] = "white"
        self.Fifth_btn["fg"] = "white"
        self.Sixth_btn["fg"] = "white"
        self.Seventh_btn["fg"] = "white"
        self.Eight_btn["fg"] = "white"
        self.Ninth_btn["fg"] = "white"

        self.Won_X_img["image"]=""
        self.Won_O_img["image"]=""

        

        self.Counter["fg"]= "white"
        self.Counter["text"]=("%s : %s" %(self.X_count,self.O_count))
       


        
    def Restart(self):
        self.t1 = 0
        self.c1 = 1
        self.won = 0

        self.First_btn["text"] = ""
        self.Second_btn["text"] = ""
        self.Third_btn["text"] = ""
        self.Fourth_btn["text"] = ""
        self.Fifth_btn["text"] = ""
        self.Sixth_btn["text"] = ""
        self.Seventh_btn["text"] = ""
        self.Eight_btn["text"] = ""
        self.Ninth_btn["text"] = ""

        self.First_btn["fg"] = "white"
        self.Second_btn["fg"] = "white"
        self.Third_btn["fg"] = "white"
        self.Fourth_btn["fg"] = "white"
        self.Fifth_btn["fg"] = "white"
        self.Sixth_btn["fg"] = "white"
        self.Seventh_btn["fg"] = "white"
        self.Eight_btn["fg"] = "white"
        self.Ninth_btn["fg"] = "white"

        self.X_count= 0
        self.O_count= 0

        self.Won_X_img["image"]=""
        self.Won_O_img["image"]=""

        
        self.Counter["fg"]= "white"
        self.Counter["text"]=("%s : %s" %(self.X_count,self.O_count))

        
        
   
    def draw(self):
        if (self.First_btn["text"] == "X" or self.First_btn["text"] == "O") and (self.Second_btn["text"] == "X" or self.Second_btn["text"] == "O") and (self.Third_btn["text"] == "X" or self.Third_btn["text"] == "O") and (self.Fifth_btn["text"] == "X" or self.Fifth_btn["text"] == "O") and (self.Sixth_btn["text"] == "X" or self.Sixth_btn["text"] == "O") and (self.Seventh_btn["text"] == "X" or self.Seventh_btn["text"] == "O") and (self.Eight_btn["text"] == "X" or self.Eight_btn["text"] == "O") and (self.Ninth_btn["text"] == "X" or self.Ninth_btn["text"] == "O"):
            self.Counter["fg"]= "lightgreen"
            self.Counter["text"]=("TIE")
            self.Won_X_img["image"] = ""
            self.Won_O_img["image"] = ""

    def Win_X(self):
        

        if self.won == 0:
            if self.First_btn["text"] == "X" and self.Second_btn["text"] == "X" and self.Third_btn["text"] == "X" or self.Fourth_btn["text"] == "X" and self.Fifth_btn["text"] == "X" and self.Sixth_btn["text"] == "X" or self.Seventh_btn["text"] == "X" and self.Eight_btn["text"] == "X" and self.Ninth_btn["text"] == "X":
                if self.First_btn["text"] == "X" and self.Second_btn["text"] == "X" and self.Third_btn["text"] == "X":
                    self.First_btn["fg"] = "red"
                    self.Second_btn["fg"] = "red"
                    self.Third_btn["fg"] = "red"
                if self.Fourth_btn["text"] == "X" and self.Fifth_btn["text"] == "X" and self.Sixth_btn["text"] == "X":
                    self.Fourth_btn["fg"] = "red"
                    self.Fifth_btn["fg"] = "red"
                    self.Sixth_btn["fg"] = "red"
                if self.Seventh_btn["text"] == "X" and self.Eight_btn["text"] == "X" and self.Ninth_btn["text"] == "X":
                    self.Seventh_btn["fg"] = "red"
                    self.Eight_btn["fg"] = "red"
                    self.Ninth_btn["fg"] = "red"
                self.won = 1
                self.X_count += 1
                self.Counter["fg"]= "red"
                self.Counter["text"]=("X won!")
                self.Won_X_img["image"]= self.won_x_img

                

                

                
            elif self.First_btn["text"] == "X" and self.Fourth_btn["text"] == "X" and self.Seventh_btn["text"] == "X" or self.Second_btn["text"] == "X" and self.Fifth_btn["text"] == "X" and self.Eight_btn["text"] == "X" or self.Third_btn["text"] == "X" and self.Sixth_btn["text"] == "X" and self.Ninth_btn["text"] == "X":
                if self.First_btn["text"] == "X" and self.Fourth_btn["text"] == "X" and self.Seventh_btn["text"] == "X":
                    self.First_btn["fg"] = "red"
                    self.Fourth_btn["fg"] = "red"
                    self.Seventh_btn["fg"] = "red"
                if self.Second_btn["text"] == "X" and self.Fifth_btn["text"] == "X" and self.Eight_btn["text"] == "X":
                    self.Second_btn["fg"] = "red"
                    self.Fifth_btn["fg"] = "red"
                    self.Eight_btn["fg"] = "red"
                if self.Third_btn["text"] == "X" and self.Sixth_btn["text"] == "X" and self.Ninth_btn["text"] == "X":
                    self.Third_btn["fg"] = "red"
                    self.Sixth_btn["fg"] = "red"
                    self.Ninth_btn["fg"] = "red"
                self.won = 1
                self.X_count += 1
                self.Counter["fg"]= "red"
                self.Counter["text"]=("X won!")
                self.Won_X_img["image"]= self.won_x_img
                
                
            elif self.First_btn["text"] == "X" and self.Fifth_btn["text"] == "X" and self.Ninth_btn["text"] == "X" or self.Third_btn["text"] == "X" and self.Fifth_btn["text"] == "X" and self.Seventh_btn["text"] == "X":
                if self.First_btn["text"] == "X" and self.Fifth_btn["text"] == "X" and self.Ninth_btn["text"] == "X":
                    self.First_btn["fg"] = "red"
                    self.Fifth_btn["fg"] = "red"
                    self.Ninth_btn["fg"] = "red"
                if self.Third_btn["text"] == "X" and self.Fifth_btn["text"] == "X" and self.Seventh_btn["text"] == "X":
                    self.Third_btn["fg"] = "red"
                    self.Fifth_btn["fg"] = "red"
                    self.Seventh_btn["fg"] = "red"
                self.won = 1
                self.X_count += 1
                self.Counter["fg"]= "red"
                self.Counter["text"]=("X won!")
                self.Won_X_img["image"]= self.won_x_img

                
                
            else:
                self.draw()
        
    def Win_O(self):
        
        
        if self.won == 0:
            if self.First_btn["text"] == "O" and self.Second_btn["text"] == "O" and self.Third_btn["text"] == "O" or self.Fourth_btn["text"] == "O" and self.Fifth_btn["text"] == "O" and self.Sixth_btn["text"] == "O" or self.Seventh_btn["text"] == "O" and self.Eight_btn["text"] == "O" and self.Ninth_btn["text"] == "O":
                if self.First_btn["text"] == "O" and self.Second_btn["text"] == "O" and self.Third_btn["text"] == "O":
                    self.First_btn["fg"] = "orange"
                    self.Second_btn["fg"] = "orange"
                    self.Third_btn["fg"] = "orange"
                if self.Fourth_btn["text"] == "O" and self.Fifth_btn["text"] == "O" and self.Sixth_btn["text"] == "O":
                    self.Fourth_btn["fg"] = "orange"
                    self.Fifth_btn["fg"] = "orange"
                    self.Sixth_btn["fg"] = "orange"
                if self.Seventh_btn["text"] == "O" and self.Eight_btn["text"] == "O" and self.Ninth_btn["text"] == "O":
                    self.Seventh_btn["fg"] = "orange"
                    self.Eight_btn["fg"] = "orange"
                    self.Ninth_btn["fg"] = "orange"
                self.won = 1               
                self.O_count += 1
                
                self.Counter["fg"]= "Orange"
                self.Counter["text"]=("O won!")
                self.Won_O_img["image"]= self.won_o_img

                
                self.Won_O_img.grid(row=0,column=7)
            elif self.First_btn["text"] == "O" and self.Fourth_btn["text"] == "O" and self.Seventh_btn["text"] == "O" or self.Second_btn["text"] == "O" and self.Fifth_btn["text"] == "O" and self.Eight_btn["text"] == "O" or self.Third_btn["text"] == "O" and self.Sixth_btn["text"] == "O" and self.Ninth_btn["text"] == "O":
                if self.First_btn["text"] == "O" and self.Fourth_btn["text"] == "O" and self.Seventh_btn["text"] == "O":
                    self.First_btn["fg"] = "orange"
                    self.Fourth_btn["fg"] = "orange"
                    self.Seventh_btn["fg"] = "orange"
                if self.Second_btn["text"] == "O" and self.Fifth_btn["text"] == "O" and self.Eight_btn["text"] == "O":
                    self.Second_btn["fg"] = "orange"
                    self.Fifth_btn["fg"] = "orange"
                    self.Eight_btn["fg"] = "orange"
                if self.Third_btn["text"] == "O" and self.Sixth_btn["text"] == "O" and self.Ninth_btn["text"] == "O":
                    self.Third_btn["fg"] = "orange"
                    self.Sixth_btn["fg"] = "orange"
                    self.Ninth_btn["fg"] = "orange"
                self.won = 1
                self.O_count += 1
                self.Counter["fg"]= "Orange"
                self.Counter["text"]=("O won!")
                self.Won_O_img["image"]= self.won_o_img

                
                
            elif self.First_btn["text"] == "O" and self.Fifth_btn["text"] == "O" and self.Ninth_btn["text"] == "O" or self.Third_btn["text"] == "O" and self.Fifth_btn["text"] == "O" and self.Seventh_btn["text"] == "O":
                if self.First_btn["text"] == "O" and self.Fifth_btn["text"] == "O" and self.Ninth_btn["text"] == "O":
                    self.First_btn["fg"] = "orange"
                    self.Fifth_btn["fg"] = "orange"
                    self.Ninth_btn["fg"] = "orange"
                if self.Third_btn["text"] == "O" and self.Fifth_btn["text"] == "O" and self.Seventh_btn["text"] == "O":
                    self.Third_btn["fg"] = "orange"
                    self.Fifth_btn["fg"] = "orange"
                    self.Seventh_btn["fg"] = "orange"
                self.won = 1
                self.O_count += 1
                self.Counter["fg"]= "Orange"
                self.Counter["text"]=("O won!")
                self.Won_O_img["image"]= self.won_o_img

                
                
            else:
                self.draw()                  


    def X_or_O_1(self):
        if self.won == 0:
            if self.First_btn["text"] == "":
                if self.c1 % 2:
                    self.First_btn["text"] = "X"
                    self.c1 += 1
                    self.Win_X()
                else:
                    self.First_btn["text"] = "O"
                    self.c1 += 1
                    self.Win_O()
            
    def X_or_O_2(self):        
        if self.won == 0:
            if self.Second_btn["text"] == "":
                if self.c1 % 2:
                    self.Second_btn["text"] = "X"
                    self.c1 += 1
                    self.Win_X()
                else:
                    self.Second_btn["text"] = "O"
                    self.c1 += 1
                    self.Win_O()

    def X_or_O_3(self):
        if self.won == 0:
            if self.Third_btn["text"] == "":
                if self.c1 % 2:
                    self.Third_btn["text"] = "X"
                    self.c1 += 1
                    self.Win_X()
                else:
                    self.Third_btn["text"] = "O"
                    self.c1 += 1
                    self.Win_O()

    def X_or_O_4(self):
        if self.won == 0:
            if self.Fourth_btn["text"] == "":
                if self.c1 % 2:
                    self.Fourth_btn["text"] = "X"
                    self.c1 += 1
                    self.Win_X()
                else:
                    self.Fourth_btn["text"] = "O"
                    self.c1 += 1
                    self.Win_O()

    def X_or_O_5(self):
        if self.won == 0:
            if self.Fifth_btn["text"] == "":
                if self.c1 % 2:
                    self.Fifth_btn["text"] = "X"
                    self.c1 += 1
                    self.Win_X()
                else:
                    self.Fifth_btn["text"] = "O"
                    self.c1 += 1
                    self.Win_O()

    def X_or_O_6(self):
        if self.won == 0:
            if self.Sixth_btn["text"] == "":
                if self.c1 % 2:
                    self.Sixth_btn["text"] = "X"
                    self.c1 += 1
                    self.Win_X()
                else:
                    self.Sixth_btn["text"] = "O"
                    self.c1 += 1
                    self.Win_O()

    def X_or_O_7(self):
        if self.won == 0:
            if self.Seventh_btn["text"] == "":
                if self.c1 % 2:
                    self.Seventh_btn["text"] = "X"
                    self.c1 += 1
                    self.Win_X()
                else:
                    self.Seventh_btn["text"] = "O"
                    self.c1 += 1
                    self.Win_O()

    def X_or_O_8(self):
        if self.won == 0:
            if self.Eight_btn["text"] == "":
                if self.c1 % 2:
                    self.Eight_btn["text"] = "X"
                    self.c1 += 1
                    self.Win_X()
                else:
                    self.Eight_btn["text"] = "O"
                    self.c1 += 1
                    self.Win_O()

    def X_or_O_9(self):
        if self.won == 0:
            if self.Ninth_btn["text"] == "":
                if self.c1 % 2:
                    self.Ninth_btn["text"] = "X"
                    self.c1 += 1
                    self.Win_X()
                else:
                    self.Ninth_btn["text"] = "O"
                    self.c1 += 1
                    self.Win_O()







# ----------------------------------------------------------------




    
class vsCom():
    def __init__(self):
        self.window = Tk()
        self.window.config(bg='#232323', width=False, height=False)
        
        self.window.title("1 Player | TicTacToe")
        self.state = True
        self.window.attributes("-fullscreen", True)
        self.window.bind("<F11>", self.toggle_fullscreen)
        self.window.bind("<Escape>", self.end_fullscreen)

        # Required variablen      
        self.t1 = 0
        self.c1 = 1
        self.won = 0
        self.player_one = "X"
        self.player_two = "O"
        self.X_count= 0
        self.O_count= 0
        self.fos = 0
        self.last = ["1","2","3","4","5","6","7","8","9"]

        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=4)
        self.window.rowconfigure(8, weight=3)
        self.window.columnconfigure(8, weight=5)
        # --------
        

        # Points Counter
        self.Counter = Label(self.window,width=12,height=1, font=(None, 30),bg="#232323",fg="white",text="X : O")
        self.Counter.grid(row=0,column=5)
        # --------


        # Restart - Icon
        restartsrc = PIL.Image.open("res/restart.png")
        restartimg = PIL.ImageTk.PhotoImage(restartsrc)

        self.Restart_btn = Button(self.window, image=restartimg, width=200,height=100,border=0,bg="#232323",fg ="white",font=2,text="Restart",command=lambda:self.Restart())
        self.Restart_btn.image = restartimg
        self.Restart_btn.grid(row=3,column=0)
        # --------

        # Menu - Icon
        menusrc = PIL.Image.open("res/menu.png")
        menuimg = PIL.ImageTk.PhotoImage(menusrc)

        self.Back_btn = Button(self.window, image=menuimg, width=200,height=100,border=0,bg="#232323",fg ="white",font=2,text="←",command=lambda:self.Back())
        self.Back_btn.image = menuimg
        self.Back_btn.grid(row=0,column=0)
        # --------


        # Replay - Icon
        replaysrc = PIL.Image.open("res/replay.png")
        replayimg = PIL.ImageTk.PhotoImage(replaysrc)

        self.Again_btn = Button(self.window, image=replayimg, width=200,height=100,border=0,bg="#232323",fg ="white",font=2,text="Again",command=lambda:self.Again())
        self.Again_btn.image = replayimg
        self.Again_btn.grid(row=5,column=0)
        # --------



        # Field Markings
        self.bx1 = Label(self.window, width=1,height=1,bg="grey",fg="white",text="")
        self.bx1.grid(row=2,column=3,sticky='we')

        self.bx2 = Label(self.window, width=1,height=1,bg="grey",fg="white",text="")
        self.bx2.grid(row=2,column=5,sticky='we')

        self.bx3 = Label(self.window, width=1,height=1,bg="grey",fg="white",text="")
        self.bx3.grid(row=2,column=7,sticky='we')

        self.bx4 = Label(self.window, width=1,height=1,bg="grey",fg="white",text="")
        self.bx4.grid(row=4,column=3,sticky='we')

        self.bx5 = Label(self.window, width=1,height=1,bg="grey",fg="white",text="")
        self.bx5.grid(row=4,column=5,sticky='we')

        self.bx6 = Label(self.window, width=1,height=1,bg="grey",fg="white",text="")
        self.bx6.grid(row=4,column=7,sticky='we')

        # ---

        self.by1 = Label(self.window, width=1,height=12,bg="grey",fg="white",text="")
        self.by1.grid(row=1,column=4,sticky='we')
        
        self.by2 = Label(self.window, width=1,height=12,bg="grey",fg="white",text="")
        self.by2.grid(row=1,column=6,sticky='we')

        self.by3 = Label(self.window, width=1,height=12,bg="grey",fg="white",text="")
        self.by3.grid(row=3,column=4,sticky='we')
        
        self.by4 = Label(self.window, width=1,height=12,bg="grey",fg="white",text="")
        self.by4.grid(row=3,column=6,sticky='we')

        self.by5 = Label(self.window, width=1,height=12,bg="grey",fg="white",text="")
        self.by5.grid(row=5,column=4,sticky='we')
        
        self.by6 = Label(self.window, width=1,height=12,bg="grey",fg="white",text="")
        self.by6.grid(row=5,column=6,sticky='we')
        # --------


        # Game Field | 1 - 3
        self.First_btn = Button(self.window, width=5,height=2,highlightbackground="#232323",bg="#232323",fg="white",font=(None, 45),text="",border=0,command=lambda:self.X_or_O_1())     
        self.First_btn.grid(row=1,column=3,sticky='we')
        
        self.Second_btn = Button(self.window,width=5,height=2, bg="#232323",fg="white",text="",font=(None, 45),border=0,command=lambda:self.X_or_O_2())
        self.Second_btn.grid(row=1,column=5,sticky='we')      

        self.Third_btn = Button(self.window,width=5,height=2, bg="#232323",fg="white",text="",font=(None, 45),border=0,command=lambda:self.X_or_O_3())
        self.Third_btn.grid(row=1,column=7,sticky='we')
        # --------

        
        # Game Field | 4 - 6
        self.Fourth_btn = Button(self.window,width=5,height=2, bg="#232323",fg="white",text="",font=(None, 45),border=0,command=lambda:self.X_or_O_4())
        self.Fourth_btn.grid(row=3,column=3,sticky='we')

        self.Fifth_btn = Button(self.window,width=5,height=2, bg="#232323",fg="white",text="",font=(None, 45),border=0,command=lambda:self.X_or_O_5())
        self.Fifth_btn.grid(row=3,column=5,sticky='we')      

        self.Sixth_btn = Button(self.window,width=5,height=2, bg="#232323",fg="white",text="",font=(None, 45),border=0,command=lambda:self.X_or_O_6())
        self.Sixth_btn.grid(row=3,column=7,sticky='we')
        # --------


        # Game Field | 7 - 9
        self.Seventh_btn = Button(self.window,width=5,height=2, bg="#232323",fg="white",text="",font=(None, 45),border=0,command=lambda:self.X_or_O_7())
        self.Seventh_btn.grid(row=5,column=3,sticky='we')

        self.Eight_btn = Button(self.window,width=5,height=2, bg="#232323",fg="white",text="",font=(None, 45),border=0,command=lambda:self.X_or_O_8())
        self.Eight_btn.grid(row=5,column=5,sticky='we')      

        self.Ninth_btn = Button(self.window,width=5,height=2, bg="#232323",fg="white",text="",font=(None, 45),border=0,command=lambda:self.X_or_O_9())
        self.Ninth_btn.grid(row=5,column=7,sticky='we')
        # --------

        # Won images
        self.wons_x_src = PIL.Image.open("res/won_x.png")
        self.won_x_img = PIL.ImageTk.PhotoImage(self.wons_x_src)

        self.Won_X_img = Label(self.window,image="", width=0,height=0,border=0,bg="#232323",fg ="white",font=2)
        self.Won_X_img.image = self.won_x_img
        self.Won_X_img.grid(row=0,column=3)

        self.wons_o_src = PIL.Image.open("res/won_o.png")
        self.won_o_img = PIL.ImageTk.PhotoImage(self.wons_o_src)

        self.Won_O_img = Label(self.window,image="",width=0,height=0,border=0,bg="#232323",fg ="white",font=2)
        self.Won_O_img.image = self.won_o_img
        self.Won_O_img.grid(row=0,column=7)
        # --------

        self.window.mainloop()
    
    def Back(self):
        self.window.destroy()
        Game_Gui()

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.window.attributes("-fullscreen", self.state)
        self.window.config(width=500, height=500)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.window.attributes("-fullscreen", False)
        self.window.config(width=500, height=500)
        return "break"
        
   
    def draw(self):
        if (self.First_btn["text"] == "X" or self.First_btn["text"] == "O") and (self.Second_btn["text"] == "X" or self.Second_btn["text"] == "O") and (self.Third_btn["text"] == "X" or self.Third_btn["text"] == "O") and (self.Fifth_btn["text"] == "X" or self.Fifth_btn["text"] == "O") and (self.Sixth_btn["text"] == "X" or self.Sixth_btn["text"] == "O") and (self.Seventh_btn["text"] == "X" or self.Seventh_btn["text"] == "O") and (self.Eight_btn["text"] == "X" or self.Eight_btn["text"] == "O") and (self.Ninth_btn["text"] == "X" or self.Ninth_btn["text"] == "O"):
            self.Counter["fg"]= "lightgreen"
            self.Counter["text"]=("TIE")
            self.Won_X_img["image"] = ""
            self.Won_O_img["image"] = ""
            
    def Again(self):
        self.t1 = 0
        self.c1 = 1
        self.won = 0

        self.last = ["1","2","3","4","5","6","7","8","9"]

        self.First_btn["text"] = ""
        self.Second_btn["text"] = ""
        self.Third_btn["text"] = ""
        self.Fourth_btn["text"] = ""
        self.Fifth_btn["text"] = ""
        self.Sixth_btn["text"] = ""
        self.Seventh_btn["text"] = ""
        self.Eight_btn["text"] = ""
        self.Ninth_btn["text"] = ""

        self.First_btn["fg"] = "white"
        self.Second_btn["fg"] = "white"
        self.Third_btn["fg"] = "white"
        self.Fourth_btn["fg"] = "white"
        self.Fifth_btn["fg"] = "white"
        self.Sixth_btn["fg"] = "white"
        self.Seventh_btn["fg"] = "white"
        self.Eight_btn["fg"] = "white"
        self.Ninth_btn["fg"] = "white"

        self.Counter["fg"]= "white"
        self.Counter["text"]=("%s : %s" %(self.X_count, self.O_count))

        self.Won_X_img["image"] = ""
        self.Won_O_img["image"] = ""


        
    def Restart(self):
        self.t1 = 0
        self.c1 = 1
        self.won = 0

        self.last = ["1","2","3","4","5","6","7","8","9"]

        self.First_btn["text"] = ""
        self.Second_btn["text"] = ""
        self.Third_btn["text"] = ""
        self.Fourth_btn["text"] = ""
        self.Fifth_btn["text"] = ""
        self.Sixth_btn["text"] = ""
        self.Seventh_btn["text"] = ""
        self.Eight_btn["text"] = ""
        self.Ninth_btn["text"] = ""

        self.First_btn["fg"] = "white"
        self.Second_btn["fg"] = "white"
        self.Third_btn["fg"] = "white"
        self.Fourth_btn["fg"] = "white"
        self.Fifth_btn["fg"] = "white"
        self.Sixth_btn["fg"] = "white"
        self.Seventh_btn["fg"] = "white"
        self.Eight_btn["fg"] = "white"
        self.Ninth_btn["fg"] = "white"

        self.X_count = 0
        self.O_count = 0

        self.Counter["fg"]= "white"
        self.Counter["text"]=("%s : %s" %(self.X_count, self.O_count))

        self.Won_X_img["image"] = ""
        self.Won_O_img["image"] = ""
        

    def Win_X(self):
        if self.won == 0:
            if self.First_btn["text"] == "X" and self.Second_btn["text"] == "X" and self.Third_btn["text"] == "X" or self.Fourth_btn["text"] == "X" and self.Fifth_btn["text"] == "X" and self.Sixth_btn["text"] == "X" or self.Seventh_btn["text"] == "X" and self.Eight_btn["text"] == "X" and self.Ninth_btn["text"] == "X":
                if self.First_btn["text"] == "X" and self.Second_btn["text"] == "X" and self.Third_btn["text"] == "X":
                    self.First_btn["fg"] = "red"
                    self.Second_btn["fg"] = "red"
                    self.Third_btn["fg"] = "red"
                if self.Fourth_btn["text"] == "X" and self.Fifth_btn["text"] == "X" and self.Sixth_btn["text"] == "X":
                    self.Fourth_btn["fg"] = "red"
                    self.Fifth_btn["fg"] = "red"
                    self.Sixth_btn["fg"] = "red"
                if self.Seventh_btn["text"] == "X" and self.Eight_btn["text"] == "X" and self.Ninth_btn["text"] == "X":
                    self.Seventh_btn["fg"] = "red"
                    self.Eight_btn["fg"] = "red"
                    self.Ninth_btn["fg"] = "red"
                self.won = 1
                self.X_count += 1
                self.Counter["fg"]= "red"
                self.Counter["text"]=("X Won!")

                self.Won_X_img["image"] = self.won_x_img

                
            elif self.First_btn["text"] == "X" and self.Fourth_btn["text"] == "X" and self.Seventh_btn["text"] == "X" or self.Second_btn["text"] == "X" and self.Fifth_btn["text"] == "X" and self.Eight_btn["text"] == "X" or self.Third_btn["text"] == "X" and self.Sixth_btn["text"] == "X" and self.Ninth_btn["text"] == "X":
                if self.First_btn["text"] == "X" and self.Fourth_btn["text"] == "X" and self.Seventh_btn["text"] == "X":
                    self.First_btn["fg"] = "red"
                    self.Fourth_btn["fg"] = "red"
                    self.Seventh_btn["fg"] = "red"
                if self.Second_btn["text"] == "X" and self.Fifth_btn["text"] == "X" and self.Eight_btn["text"] == "X":
                    self.Second_btn["fg"] = "red"
                    self.Fifth_btn["fg"] = "red"
                    self.Eight_btn["fg"] = "red"
                if self.Third_btn["text"] == "X" and self.Sixth_btn["text"] == "X" and self.Ninth_btn["text"] == "X":
                    self.Third_btn["fg"] = "red"
                    self.Sixth_btn["fg"] = "red"
                    self.Ninth_btn["fg"] = "red"
                self.won = 1
                self.X_count += 1
                self.Counter["fg"]= "red"
                self.Counter["text"]=("X Won!")

                self.Won_X_img["image"] = self.won_x_img
                
            elif self.First_btn["text"] == "X" and self.Fifth_btn["text"] == "X" and self.Ninth_btn["text"] == "X" or self.Third_btn["text"] == "X" and self.Fifth_btn["text"] == "X" and self.Seventh_btn["text"] == "X":
                if self.First_btn["text"] == "X" and self.Fifth_btn["text"] == "X" and self.Ninth_btn["text"] == "X":
                    self.First_btn["fg"] = "red"
                    self.Fifth_btn["fg"] = "red"
                    self.Ninth_btn["fg"] = "red"
                if self.Third_btn["text"] == "X" and self.Fifth_btn["text"] == "X" and self.Seventh_btn["text"] == "X":
                    self.Third_btn["fg"] = "red"
                    self.Fifth_btn["fg"] = "red"
                    self.Seventh_btn["fg"] = "red"
                self.won = 1
                self.X_count += 1
                self.Counter["fg"]= "red"
                self.Counter["text"]=("X Won!")

                self.Won_X_img["image"] = self.won_x_img
            else:
                self.draw()
        
    def Win_O(self):
        if self.won == 0:
            if self.First_btn["text"] == "O" and self.Second_btn["text"] == "O" and self.Third_btn["text"] == "O" or self.Fourth_btn["text"] == "O" and self.Fifth_btn["text"] == "O" and self.Sixth_btn["text"] == "O" or self.Seventh_btn["text"] == "O" and self.Eight_btn["text"] == "O" and self.Ninth_btn["text"] == "O":
                if self.First_btn["text"] == "O" and self.Second_btn["text"] == "O" and self.Third_btn["text"] == "O":
                    self.First_btn["fg"] = "orange"
                    self.Second_btn["fg"] = "orange"
                    self.Third_btn["fg"] = "orange"
                if self.Fourth_btn["text"] == "O" and self.Fifth_btn["text"] == "O" and self.Sixth_btn["text"] == "O":
                    self.Fourth_btn["fg"] = "orange"
                    self.Fifth_btn["fg"] = "orange"
                    self.Sixth_btn["fg"] = "orange"
                if self.Seventh_btn["text"] == "O" and self.Eight_btn["text"] == "O" and self.Ninth_btn["text"] == "O":
                    self.Seventh_btn["fg"] = "orange"
                    self.Eight_btn["fg"] = "orange"
                    self.Ninth_btn["fg"] = "orange"
                self.won = 1
                self.O_count += 1
                self.Counter["fg"]= "Orange"
                self.Counter["text"]=("O Won!")

                self.Won_O_img["image"] = self.won_o_img
            else:
                self.draw()
            
            if self.First_btn["text"] == "O" and self.Fourth_btn["text"] == "O" and self.Seventh_btn["text"] == "O" or self.Second_btn["text"] == "O" and self.Fifth_btn["text"] == "O" and self.Eight_btn["text"] == "O" or self.Third_btn["text"] == "O" and self.Sixth_btn["text"] == "O" and self.Ninth_btn["text"] == "O":
                if self.First_btn["text"] == "O" and self.Fourth_btn["text"] == "O" and self.Seventh_btn["text"] == "O":
                    self.First_btn["fg"] = "orange"
                    self.Fourth_btn["fg"] = "orange"
                    self.Seventh_btn["fg"] = "orange"
                if self.Second_btn["text"] == "O" and self.Fifth_btn["text"] == "O" and self.Eight_btn["text"] == "O":
                    self.Second_btn["fg"] = "orange"
                    self.Fifth_btn["fg"] = "orange"
                    self.Eight_btn["fg"] = "orange"
                if self.Third_btn["text"] == "O" and self.Sixth_btn["text"] == "O" and self.Ninth_btn["text"] == "O":
                    self.Third_btn["fg"] = "orange"
                    self.Sixth_btn["fg"] = "orange"
                    self.Ninth_btn["fg"] = "orange"
                self.won = 1
                self.O_count += 1
                self.Counter["fg"]= "Orange"
                self.Counter["text"]=("O Won!")

                self.Won_O_img["image"] = self.won_o_img
            else:
                self.draw()
                
            if self.First_btn["text"] == "O" and self.Fifth_btn["text"] == "O" and self.Ninth_btn["text"] == "O" or self.Third_btn["text"] == "O" and self.Fifth_btn["text"] == "O" and self.Seventh_btn["text"] == "O":
                if self.First_btn["text"] == "O" and self.Fifth_btn["text"] == "O" and self.Ninth_btn["text"] == "O":
                    self.First_btn["fg"] = "orange"
                    self.Fifth_btn["fg"] = "orange"
                    self.Ninth_btn["fg"] = "orange"
                if self.Third_btn["text"] == "O" and self.Fifth_btn["text"] == "O" and self.Seventh_btn["text"] == "O":
                    self.Third_btn["fg"] = "orange"
                    self.Fifth_btn["fg"] = "orange"
                    self.Seventh_btn["fg"] = "orange"
                self.won = 1
                self.O_count += 1
                self.Counter["fg"]= "Orange"
                self.Counter["text"]=("O Won!")

                self.Won_O_img["image"] = self.won_o_img
            else:
                self.draw()



            
                    
    def COM(self):
        rando = random.sample(self.last,  1)
        rand = int(rando[0])
        if rand == 1:
            if self.First_btn["text"] == "":
                self.First_btn["text"] = "O"
                
                
                self.last.remove("1")
                self.Win_O()
                self.draw()
            else:
                self.COM()
        if rand == 2:
            if self.Second_btn["text"] == "":
                self.Second_btn["text"] = "O"
                
                self.last.remove("2")
                self.Win_O()
                self.draw()
            else:
                self.COM()
        if rand == 3:
            if self.Third_btn["text"] == "":
                self.Third_btn["text"] = "O"
                
                self.last.remove("3")
                self.Win_O()
                self.draw()
            else:
                self.COM()
        if rand == 4:
            if self.Fourth_btn["text"] == "":
                self.Fourth_btn["text"] = "O"
                
                self.last.remove("4")
                self.Win_O()
                self.draw()
            else:
                self.COM()
        if rand == 5:
            if self.Fifth_btn["text"] == "":
                self.Fifth_btn["text"] = "O"
                
                self.last.remove("5")
                self.Win_O()
                self.draw()
            else:
                self.COM()
        if rand == 6:
            if self.Sixth_btn["text"] == "":
                self.Sixth_btn["text"] = "O"
                
                self.last.remove("6")
                self.Win_O()
                self.draw()
        if rand == 7:
            if self.Seventh_btn["text"] == "":
                self.Seventh_btn["text"] = "O"
                
                self.last.remove("7")
                self.Win_O()
                self.draw()
            else:
                self.COM()
        if rand == 8:
            if self.Eight_btn["text"] == "":
                self.Eight_btn["text"] = "O"
                
                self.last.remove("8")
                self.Win_O()
                self.draw()
            else:
                self.COM()
        if rand == 9:
            if self.Ninth_btn["text"] == "":
                self.Ninth_btn["text"] = "O"
               
                self.last.remove("9")
                self.Win_O()
                self.draw()
            else:
                self.COM()
        
    
        
        
                
                    

    def X_or_O_1(self):
        if self.won == 0:
            if self.First_btn["text"] == "":
                self.First_btn["text"] ="X"
                self.last.remove("1")
                self.Win_X()
                if self.won == 0:
                    self.COM()
                else:
                    self.Win_X()
    def X_or_O_2(self):        
        if self.won == 0:
            if self.Second_btn["text"] == "":
                self.Second_btn["text"] ="X"
                self.last.remove("2")
                self.Win_X()
                if self.won == 0:
                    self.COM()
                else:
                    self.Win_X()

    def X_or_O_3(self):
        if self.won == 0:
            if self.Third_btn["text"] == "":
                self.Third_btn["text"] ="X"
                self.last.remove("3")
                self.Win_X()
                if self.won == 0:
                    self.COM()
                else:
                    self.Win_X()
    def X_or_O_4(self):
        if self.won == 0:
            if self.Fourth_btn["text"] == "":
                self.Fourth_btn["text"] ="X"
                self.last.remove("4")
                self.Win_X()
                if self.won == 0:
                    self.COM()
                else:
                    self.Win_X()

    def X_or_O_5(self):
        if self.won == 0:
            if self.Fifth_btn["text"] == "":
                self.Fifth_btn["text"] ="X"
                self.last.remove("5")
                self.Win_X()
                if self.won == 0:
                    self.COM()
                else:
                    self.Win_X()

    def X_or_O_6(self):
        if self.won == 0:
            if self.Sixth_btn["text"] == "":
                self.Sixth_btn["text"] ="X"
                self.last.remove("6")
                self.Win_X()
                if self.won == 0:
                    self.COM()
                else:
                    self.Win_X()
                    

    def X_or_O_7(self):
        if self.won == 0:
            if self.Seventh_btn["text"] == "":
                self.Seventh_btn["text"] ="X"
                self.last.remove("7")
                self.Win_X()
                if self.won == 0:
                    self.COM()
                else:
                    self.Win_X()
    def X_or_O_8(self):
        if self.won == 0:
            if self.Eight_btn["text"] == "":
                self.Eight_btn["text"] ="X"
                self.last.remove("8")
                self.Win_X()
                if self.won == 0:
                    self.COM()
                else:
                    self.Win_X()

    def X_or_O_9(self):
        if self.won == 0:
            if self.Ninth_btn["text"] == "":
                self.Ninth_btn["text"] ="X"
                self.last.remove("9")
                self.Win_X()
                if self.won == 0:
                    self.COM()
                else:
                    self.Win_X()

Game_Gui()

