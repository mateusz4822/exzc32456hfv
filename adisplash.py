import tkinter as tk
import webbrowser
from selenium import webdriver
from proxyfile import proxy
import random 



PROXY = "37.97.231.92:3128" 


url = "https:/adidas.pl/yeezy"
ip_check = "https://www.iplocation.net/find-ip-address"




def open_browser():

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--proxy-server=%s' % PROXY)

	chrome = webdriver.Chrome(options=chrome_options)
	chrome.get(ip_check)


HEIGHT = 700
WIDTH = 800


root = tk.Tk()

canvas = tk.Canvas(root, height= HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="light blue")
frame.place(relwidth = 1, relheight = 1)

entry = tk.Entry(frame, font=40)
entry.place(relx=0.5, rely=0.25, relwidth=0.3, relheight=0.04)



button = tk.Button(frame, text="open browser", font=40, command=lambda: open_browser())
button.place(relx=0.3, rely= 0.25, relwidth=0.2, relheight=0.05, anchor="n")



root.mainloop()

