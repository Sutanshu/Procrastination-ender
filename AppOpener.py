import subprocess, time
from random import randint
import tkinter as tk

class Constraints:
    def __init__(self,choice = None,duration = None, restriction = None):
        self.choice = choice
        self.duration = duration
        self.restriction = restriction

    def setpath(self):
        self.path = '/Applications/'+self.choice+'.app'+"/Contents/MacOS/"+self.choice

    def getsubprocess(self):
        self.process = subprocess.Popen(self.path)
        return self.process

    def setchoice(self):
        self.choice = input("Which application do you want to open? ")

    def setduration(self):
        try:
            self.duration = int(input("How long do you want to run the application for? In seconds"))
        except:
            print("Please enter a number")

    def getduration(self):
        return self.duration

    def setrestriction(self):
        try:
            self.restriction = input("Do you want a time limit on your usage? Please enter Y for yes and N for no. ")
            if self.restriction.lower()!='y' and self.restriction.lower()!='n':
                print("Please enter 'y' or 'n'. ")
        except TypeError:
            print("Please enter y or n.")

    def getrestriction(self):
        return self.restriction

    def getpath(self):
        return self.path

    def create_popup(self):
        self.popup = tk.Tk()
        self.popup.wm_title("Reminder")
        self.label = tk.Label(self.popup, text = random_text())
        self.label.pack(fill = 'x')
        #self.button = tk.Button(self.popup, text = "Okay",command = self.popup.destroy)
        #self.button.pack()
        self.button2 = tk.Button(self.popup, text = "Close the window", command = self.process.kill)
        self.button2.pack()
        self.popup.after((self.duration//4)*1000,self.popup.destroy)
        self.popup.mainloop()


def random_text():
    text= ["Remember the time you turned in the essay but regretted starting late? Don't repeat your mistakes!",
    "Remember the time before your exam when you felt you needed more time to prepare/ do better? Well that time is now, don't waste it!",
    "Remember the times before an exam when you took too long to understand a topic because when you had time, you thought you could do it later? Do it now. Come on!",
    "Time to be productive! Let's go! "]
    randchoice = randint(0,3)
    return text[randchoice]


def main():
    if __name__ == '__main__':
        print("Hello!")
        constraints = Constraints()
        constraints.setchoice()
        constraints.setpath()
        constraints.setrestriction()
        restriction = constraints.getrestriction()
        if restriction.upper() == 'Y':
            constraints.setduration()
            constraints.getsubprocess()
            time.sleep(constraints.getduration()//4)
            constraints.create_popup()
            #time.sleep(constraints.getduration()//4)
            constraints.create_popup()
            #time.sleep(constraints.getduration()//4)
            constraints.create_popup()
            
        else:
            constraints.getsubprocess()

main()