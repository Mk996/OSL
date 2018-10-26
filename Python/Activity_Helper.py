import tkinter as tk
import time 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def openwatchguard():
    driver = webdriver.Chrome(r'C:\Users\TLF\Downloads\OSL-master\chromedriver.exe')
    driver.get("https://10.2.19.27:4100/logon.shtml")
    s=E1.get()
    p=E2.get()
    driver.find_element_by_name("fw_username").send_keys(s)
    driver.find_element_by_name("fw_password").send_keys(p)
    driver.find_element_by_xpath("//*[@id='hsFormId']/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td[2]/table/tbody/tr[6]/td[2]/select/option[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='hsFormId']/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td[2]/table/tbody/tr[8]/td[2]/div/input[1]").click()
	

def opengoogle():
    driver = webdriver.Chrome(r'C:\Users\dev\Desktop\chromedriver.exe')
    driver.get("http://www.gmail.com")
    s=E1.get()
    p=E2.get()
    driver.find_element_by_name("identifier").send_keys(s)
    driver.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()
    time.sleep(2)
    driver.find_element_by_name("password").send_keys(p)
    driver.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()

def openfb():
    driver = webdriver.Chrome(r'C:\Users\dev\Desktop\chromedriver.exe')
    driver.get("http://www.facebook.com")
    s=E1.get()
    p=E2.get()
    driver.find_element_by_xpath("//*[@id='email']").send_keys(s)
    driver.find_element_by_xpath("//*[@id='pass']").send_keys(p)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='loginbutton']").click()

def openinsta():
    driver = webdriver.Chrome(r'C:\Users\dev\Desktop\chromedriver.exe')
    driver.get("http://www.instagram.com")
    s=E1.get()
    p=E2.get()
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/span/button").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='email']").send_keys(s)
    driver.find_element_by_xpath("//*[@id='pass']").send_keys(p)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='loginbutton']").click()
    time.sleep(2)
    """driver.find_element_by_xpath("//*[@id='platformDialogForm']/div[2]/table/tbody/tr/td[2]/button[2]").click()"""
    
root = tk.Tk()
frame3 = tk.Frame(root)
frame3.pack()
frame2 = tk.Frame(root)
frame2.pack()
frame = tk.Frame(root)
frame.pack()


L1 = tk.Label(frame3, text="User Name")
L1.pack( side = tk.LEFT)
E1 = tk.Entry(frame3, bd =5)
E1.insert(0,"abc@xyz.com")
E1.pack(side = tk.RIGHT)

L2 = tk.Label(frame2, text="Password")
L2.pack( side = tk.LEFT)
E2 = tk.Entry(frame2, show="*",bd =5)
E2.insert(0,"yourpasswordhere")
E2.pack(side = tk.RIGHT)

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)

watchg = tk.Button(frame,
                   text="WatchGuard",
                   command=openwatchguard)
watchg.pack(side=tk.LEFT)

goog = tk.Button(frame,
                   text="Google",
                   command=opengoogle)
goog.pack(side=tk.LEFT)

face = tk.Button(frame,text="Facebook",command=openfb)
face.pack(side=tk.LEFT)

inst = tk.Button(frame,text="Instagram",command=openinsta)
inst.pack(side=tk.LEFT)

root.mainloop()



