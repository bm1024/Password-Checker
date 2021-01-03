'''
Created on Dec 29, 2020
@author: Bianca Magyar
Description: Python program using Tkinter to check password validity and strength.
Reference: Codewars, GeeksforGeeks
'''

from tkinter import Label, Entry, END, Button, Tk, LEFT, E, W

#check that password meets conditions
def check_password(pw):
    #print(s)
    special = "!@#$%^&*?-_=+(){}[]<>."
    reason = "Password missing:\n"
    #turn this into function
    if len(pw) < 8:
        reason += ("- length of at least 8 characters\n")
        #return False
    if len(pw) > 20:
        reason +=  ("- length of at most 20 characters\n")
        #return False
    if not any(ch.isupper() for ch in pw): 
        reason +=  ("- at least one upper case letter\n")
        #return False
    if not any(ch.islower() for ch in pw): 
        reason +=  ("- at least one lower case letter\n")
        #return False
    if not any(ch.isdigit() for ch in pw):
        reason +=  ("- at least one number\n")
        #return False
    if not any(ch in special for ch in pw):
        reason +=  ("- at least one special character out of " + special + "\n")    
    
    if reason == "Password missing:\n": return True
    return reason

#enter a valid password to check strength    
def password_strength(pw):
    length = len(pw)
    if length <= 11: return "Acceptable\n>> Strength of password is weak"
    elif length <= 16: return "Good\n>> Strength of password is medium"
    else: return "Excellent\n>> Strength of password is strong"

#run     
def main():
    
    #clear contents within entry box
    def clear():
        entry_box.delete(0, END)
    
    #submit entry box input to check whether it's a valid password
    def submit():
        pw = entry_box.get() #get and store pw string from entry box
        res = check_password(pw) #returns a True boolean value or error string        
        
        #display results or error message
        display = ""
        if res == True: 
            display = password_strength(pw)
        else: 
            display=res
        
        #set up gui for results window
        resultgui = Tk()
        resultgui.title("Result")
        resultgui.iconbitmap("lock-icon.ico")
        resultgui.geometry() #opens to appropriate size automatically
        
        #create label to display results    
        result_label = Label(resultgui, text=display, wraplength=370, font=("Calibri", 12), justify=LEFT)   
        result_label.grid(row=0, column=0, padx=40, pady=20)
        
        
    #set up gui for main window    
    maingui = Tk()
    maingui.title("Password Checker")
    maingui.iconbitmap("lock-icon.ico")
    maingui.geometry("470x230")
    
    #create labels
    title_label = Label(maingui, text="Password Validity", justify=LEFT, font=("Calibri", 14))
    title_label.grid(row=0, column=0, padx=10, pady=10)    
    
    directions = "Password must be between 8-20 characters in length and contain one upper case, one lower case, one number, and one special character."
    directions_label = Label(maingui, text=directions, wraplength=370, justify=LEFT, font=("Calibri", 12))
    directions_label.grid(row=1, column=0, columnspan=2, padx=(30,0), pady=10)
    
    prompt_label = Label(maingui, text="Check your password:", width=30, anchor=E)
    prompt_label.grid(row=2, column=0, padx=5)
    
    #create entry box to check password
    entry_box = Entry(maingui, width=30)
    entry_box.grid(row=2, column=1, padx=5)
    
    #create buttons
    clear_button = Button(maingui, text="Clear", command=clear)
    clear_button.grid(row=3, column=0, pady=15, ipadx=30, sticky=E)
    
    submit_button = Button(maingui, text="Submit", command=submit)
    submit_button.grid(row=3, column=1, pady=15, ipadx=30, sticky=W)
    
    maingui.mainloop()
    
if __name__ == '__main__':
    
    main()
