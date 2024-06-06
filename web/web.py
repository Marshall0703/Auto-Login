import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title("WebStuff")
root.geometry("450x400")


#Change username, password and login-button if needed.
def auto():
 options = webdriver.ChromeOptions()
 options.add_experimental_option("detach", True)
 driver = webdriver.Chrome(options=options)
 driver.get(url)
 login = driver.find_element(By.NAME, "username")
 login.send_keys(username)
 password2 = driver.find_element(By.NAME, "password")
 password2.send_keys(password3)
 driver.find_element(By.ID, "login-button").click()

#Search function
def search2():
 search_string = search.get()
 search_string = search_string.replace(' ', '+')
 options = webdriver.ChromeOptions()
 options.add_experimental_option("detach", True)
 browser = webdriver.Chrome(options=options)
 for i in range(1):
  matched_elements = browser.get("https://www.google.com/search?q=" + search_string + "&start=" + str(i))

#Open google function
def web():
 webbrowser.open("www.google.com")

#Search entry box
search = Label(text = "Search", bg = "black", fg = "white")
search = Entry(root, width = 20, font = ('Arial',16,'bold'), fg = "black")
search.grid(row = 2, column = 2)

#Change text of button if you want.\/
button3 = Button(root, text = "Auto Login", command = auto, fg = "white", bg = "black", padx = 10, pady = 5, width = 15, height = 3)
button3.grid(row = 2, column = 1)

#Google search button
button2 = Button(root, text = "Google Search", command = search2, bg = "black", fg = "white", padx = 10, pady = 5, width = 15, height = 3)
button2.grid(row = 1, column = 2)

#Open google button 
button1 = Button(root, text = "Google", command = web, fg = "white", bg = "black", padx = 10, pady = 5, width = 15, height = 3)
button1.grid(row = 1, column = 1)

#Username, Password and Url Change these to yours for auto login function
username = "Username"
password3 = "Password"
url = "URL of auto login you want"


root.mainloop()