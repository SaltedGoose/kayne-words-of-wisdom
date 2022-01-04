#----------------------------Imports----------------------------#
import smtplib
import requests
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
#----------------------------Functions----------------------------#
def quote():
    '''This function queries the Kayne Quotes API and 
    returns a random quote as a string'''
    response = requests.get('https://api.kanye.rest')
    data = response.json()
    quote = data['quote']
    return quote

def submit():
    global my_email, my_password
    success_label['text'] = ''
    if len(email_entry_textbox.get('1.0', END)) > 1:
        list_of_emails = email_entry_textbox.get('1.0', END).split(', ')
        for email in list_of_emails:
            ammend_email = email.replace('\n', '')
            new_quote = quote()
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=f'{ammend_email}',
                    msg=f'SUBJECT:Kanye Quote\n\n{new_quote}'
                )
        success_label['text'] = 'Success'
    else:
        messagebox.showerror('Empty Input Box', 'Input box can not be empty')
        success_label['text'] = 'Failed'
    email_entry_textbox.delete('1.0', END)
#----------------------------UI Setup----------------------------#
#screen setup
screen = Tk()
screen.title('Kanye Quote Email Sender')
screen.config(padx=50, pady=50)

kayne_image = PhotoImage(file='kanye.png')
#labels
email_entry_label = Label(text='''Please enter list of emails to send 
an email to seperated by a comma''')
email_entry_label.grid(row=1, column=1)

success_label = Label(text='')
success_label.grid(row=4, column=1)

title_label = Label(text='Kanye Words of wisdom', font=('Courier', 24, 'normal'), pady=20)
title_label.grid(row=0, column=1)
#Textbox
email_entry_textbox = Text(width=35, height=10)
email_entry_textbox.focus()
email_entry_textbox.grid(row=2, column=1)
#buttons
submit_button = Button(text='Submit', width=30, command=submit)
submit_button.grid(row=3, column=1)

kayne_button_1 = Button(image=kayne_image)
kayne_button_1.grid(row=0, column=0)
kayne_button_2 = Button(image=kayne_image)
kayne_button_2.grid(row=0, column=2)

my_email = simpledialog.askstring(title='Email', prompt='What is your email?')
my_password = simpledialog.askstring(title='Password', prompt='What is your password?')

screen.mainloop()