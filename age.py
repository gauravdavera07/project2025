
 
from tkinter import *                  
from tkinter import messagebox as mb    
from datetime import date               
  
 
def different_date():  
   
    given_year_field.config(state = "normal")  
    given_month_field.config(state = "normal")  
    given_day_field.config(state = "normal")  
      
   
    different_date_button.config(state = "disabled")  
      
 
    current_date_button.config(state = "normal")  
  
 
def current_date():  
    
    given_year_field.config(state = "disabled")  
    given_month_field.config(state = "disabled")  
    given_day_field.config(state = "disabled")  
      
  
    different_date_button.config(state = "normal")  
      
 
    current_date_button.config(state = "disabled")  
  
  
    given_year_var.set(current_year)  
    given_month_var.set(current_month)  
    given_day_var.set(current_day)  
  

def reset_entries():  
   
    birth_year_field.delete(0, END)  
    birth_month_field.delete(0, END)  
    birth_day_field.delete(0, END)  
  
  
    given_year_field.config(state = "disabled")  
    given_month_field.config(state = "disabled")  
    given_day_field.config(state = "disabled")  


    different_date_button.config(state = "normal")  
  
 
    current_date_button.config(state = "disabled")  
  
    
    given_year_var.set(current_year)  
    given_month_var.set(current_month)  
    given_day_var.set(current_day)  
  
 
    age_var.set("")  
  
  
    birth_year_field.focus_set()  
  

def reset():  

    reset_entries()  
  
 
    mb.showinfo("Reset Entries", "All Entries are reset successfully!")  
  
 
def check_for_errors():  
 
    if (birth_year_field.get() == "" or birth_month_field.get() == "" or birth_day_field.get() == "" or given_year_field.get() == "" or given_month_field.get() == "" or given_day_field.get() == ""):  
       
        mb.showerror("Input Error", "Invalid Format! Please Try Again.")  
          
     
        reset_entries()  
  
        return -1  
  

def calculate_age():  
     
    val = check_for_errors()  
      
 
    if val == -1:  
       
        return  
  
    else:  
    
        birth_year = int(year_var.get())  
        birth_month = int(month_var.get())  
        birth_day = int(day_var.get())  
  
        given_year = int(given_year_var.get())  
        given_month = int(given_month_var.get())  
        given_day = int(given_day_var.get())  
 
        try:  
 
            birth_date = date(birth_year, birth_month, birth_day)  
            given_date = date(given_year, given_month, given_day)  
    
            if (birth_date < given_date):  
   
                days_left = given_date - birth_date  
                  
          
                age = int(abs((days_left.total_seconds()) / (365.242 * 24 * 3600)))  
  
                 
                age_var.set(str(age) + " Years Old")  
  
            else:  
              
                mb.showerror("Input Error", "Birth Date exceeds Given Date.")  
              
                reset_entries()  
  
          
        except ValueError:  
  
            mb.showerror("Out of Range", "Entered Date is out of range.")  
           
            reset_entries()  
  
# main function  
if __name__ == "__main__":  
  
    gui_root = Tk()  

    gui_root.title("Age Calculator - JAVATPOINT")  
 
    gui_root.geometry("600x450+650+250")  
   
    gui_root.resizable(0, 0)  
 
    gui_root.config(bg = "#FEECCF")  

    gui_root.iconbitmap('calendar_img.ico')  
  

    header_frame = Frame(gui_root, bg = "#FEECCF")  
    entry_frame = Frame(gui_root, bg = "#FEECCF")  
    result_frame = Frame(gui_root, bg = "#FEECCF")  
  

    header_frame.pack(pady = 10)  
    entry_frame.pack(pady = 10)  
    result_frame.pack(pady = 10)  
  

    header_label = Label(  
        header_frame,  
        text = "AGE CALCULATOR",  
        font = ("verdana", "20", "bold"),  
        bg = "#FEECCF",  
        fg = "#C8871E"  
        )  
  

    header_label.pack(fill = "both", pady = 10)  
  

    year_label = Label(  
        entry_frame,  
        text = "Year",  
        font = ("verdana", "10"),  
        bg = "#FEECCF",  
        fg = "#000000"  
        )  
  
    month_label = Label(  
        entry_frame,  
        text = "Month",  
        font = ("verdana", "10"),  
        bg = "#FEECCF",  
        fg = "#000000"  
        )  
  
    day_label = Label(  
        entry_frame,  
        text = "Day",  
        font = ("verdana", "10"),  
        bg = "#FEECCF",  
        fg = "#000000"  
        )  
      
    dob_label = Label(  
        entry_frame,  
        text = "Date of Birth:",  
        font = ("verdana", "10", "bold"),  
        bg = "#FEECCF",  
        fg = "#000000"  
        )  
  
    given_date_label = Label(  
        entry_frame,  
        text = "Given Date:",  
        font = ("verdana", "10", "bold"),  
        bg = "#FEECCF",  
        fg = "#000000"  
        )  
      

    year_label.grid(row = 0, column = 1, padx = 10, pady = 10)  
    month_label.grid(row = 0, column = 2, padx = 10, pady = 10)  
    day_label.grid(row = 0, column = 3, padx = 10, pady = 10)      
      
    dob_label.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = W)  
    given_date_label.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = W)  
  

    current_year = date.today().year  
    current_month = date.today().month  
    current_day = date.today().day  
  
 
    year_var = StringVar(entry_frame)  
    month_var = StringVar(entry_frame)  
    day_var = StringVar(entry_frame)  
  
    given_year_var = StringVar(entry_frame)  
    given_month_var = StringVar(entry_frame)  
    given_day_var = StringVar(entry_frame)  
  
 
    year_var.set("")  
    month_var.set("")  
    day_var.set("")  
  
    given_year_var.set(current_year)  
    given_month_var.set(current_month)  
    given_day_var.set(current_day)  
  
   
    birth_year_field = Entry(  
        entry_frame,  
        width = 6,  
        font = ("verdana", "10"),   
        textvariable = year_var,   
        justify = CENTER,   
        relief = GROOVE  
        )  
  
    birth_month_field = Entry(  
        entry_frame,   
        width = 4,   
        font = ("verdana", "10"),   
        textvariable = month_var,   
        justify = CENTER,   
        relief = GROOVE  
        )  
  
    birth_day_field = Entry(  
        entry_frame,   
        width = 4,   
        font = ("verdana", "10"),   
        textvariable = day_var,   
        justify = CENTER,   
        relief = GROOVE  
        )  
  
    given_year_field = Entry(  
        entry_frame,   
        width = 6,   
        font = ("verdana", "10"),   
        textvariable = given_year_var,   
        justify = CENTER,   
        relief = GROOVE,   
        state = "disabled"  
        )  
  
    given_month_field = Entry(  
        entry_frame,   
        width = 4,   
        font = ("verdana", "10"),   
        textvariable = given_month_var,   
        justify = CENTER,   
        relief = GROOVE,   
        state = "disabled"  
        )  
  
    given_day_field = Entry(  
        entry_frame,   
        width = 4,   
        font = ("verdana", "10"),   
        textvariable = given_day_var,   
        justify = CENTER,   
        relief = GROOVE,   
        state = "disabled"  
        )  
  
    birth_year_field.grid(row = 1, column = 1, padx = 10, pady = 10)  
    birth_month_field.grid(row = 1, column = 2, padx = 10, pady = 10)  
    birth_day_field.grid(row = 1, column = 3, padx = 10, pady = 10)  
  
    given_year_field.grid(row = 4, column = 1, padx = 10, pady = 10)  
    given_month_field.grid(row = 4, column = 2, padx = 10, pady = 10)  
    given_day_field.grid(row = 4, column = 3, padx = 10, pady = 10)  
  
   
    different_date_button = Button(  
        entry_frame,   
        text = "Different Date?",   
        width = 14,   
        font = ("verdana", "10"),   
        relief = GROOVE,   
        command = different_date,   
        bg = "#FFB84B",   
        fg = "#000000",   
        disabledforeground = "#907957"  
        )  
          
    current_date_button = Button(  
        entry_frame,   
        text = "Current Date",   
        width = 14,   
        font = ("verdana", "10"),   
        relief = GROOVE,   
        state = "disabled",   
        command = current_date,   
        bg = "#FFB84B",   
        fg = "#000000",   
        disabledforeground = "#907957"  
        )  

    different_date_button.grid(row = 4, column = 4, padx = 10, pady = 10)  
    current_date_button.grid(row = 7, column = 4, padx = 10, pady = 10)  
  

    age_var = StringVar(result_frame)  
  

    age_var.set("")  
  

    footer_label = Label(  
        result_frame,   
        text = "The Calculated Age is:",   
        font = ("verdana", "10", "bold"),   
        bg = "#FEECCF",   
        fg = "#C8871E"  
        )  
  
    age_label = Label(  
        result_frame,   
        textvariable = age_var,   
        font = ("verdana", "10", "bold"),   
        bg = "#FEECCF",   
        fg = "#1FA73B"  
        )  
  

    footer_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = W)  
    age_label.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = W)  
  

    reset_button = Button(  
        result_frame,   
        text = "Reset Entries",   
        width = 12,   
        font = ("verdana", "10"),   
        relief = GROOVE,   
        command = reset,   
        bg = "#FF0000",   
        fg = "#FFFFFF"  
        )  
  
    calculate_button = Button(  
        result_frame,   
        text = "Calculate Age",   
        width = 12,   
        font = ("verdana", "10"),   
        relief = GROOVE,   
        command = calculate_age,   
        bg = "#00FF00",   
        fg = "#000000"  
        )  
 
    reset_button.grid(row = 1, column = 0, padx = 10, pady = 10)  
    calculate_button.grid(row = 1, column = 1, padx = 10, pady = 10)  
 
    gui_root.mainloop()  