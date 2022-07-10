import requests, statistics,re
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import pandas as pd
pw="Tomnook21@1960870"
db ="gpu"
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = create_db_connection("localhost", "root", pw, db)

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


#def addToSheet(mean, median,productName):
  #  cwd = os.getcwd()
    

   # workbook = xlsxwriter.Workbook('Graphics card List.xls')
   # worksheet = workbook.add_worksheet()
  #  loc = cwd + "\Graphics card List.xls"
   # print("Location is: "+loc)
   # readbook=xlrd.open_workbook(loc)
   # sheet = readbook.sheet_by_index(0)
  #  for  cell in range(sheet.ncols):
   #     if productName in sheet.cell_value(0,cell):
   #         root.mainloop()
   #     worksheet.write(sheet.ncols,0,productName)

     #   return

        
    
 #   workbook.close()


  #  return

def Average(lst):
    return sum(lst)/len(lst)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def webScrape(searchItem):
    

    firstString = searchItem.get()

    tempStr = firstString.replace(" ","+")
    URL = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + tempStr + "&_sacat=0&rt=nc&LH_Sold=1&LH_Complete=1"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="srp-river-main")
    priceList = []
    flag =1
    ignore =1
    item_elements = results.find_all("div", class_="s-item__info clearfix")
    for item_element in item_elements:
        if flag == 0:
            title_element = item_element.find("h3", class_="s-item__title")
            price_element = item_element.find("span", class_="s-item__price")
            price_element =price_element.text.strip()

            title_element = title_element.text.strip()

            searchList = firstString.split()
        

            count = 0





            
            
            if cardSelect.get()==1:
                if "Broken"  in title_element or "BROKEN" in title_element or "broken" in title_element or "parts" in title_element or "Parts" in title_element or "PARTS" in title_element or "just box" in title_element or "Just box" in title_element or "Just Box" in title_element or "JUST BOX" in title_element or "bracket" in title_element or "Bracket" in title_element or "power cable" in title_element or "Power Cable" in title_element or "blower" in title_element or "Blower" in title_element or "power adapter" in title_element or "Power Adapter" in title_element or "cable" in title_element or "Cable" in title_element:
                    ignore=0
                    print("ignored: "+ title_element)
            
            realprice=price_element[1:]

            if is_number(realprice) and ignore ==1:
                realprice=float(realprice)
                priceList.append(realprice)
        
            #print(title_element.text.strip())
            #print(realprice)
            ignore =1
        
        flag = 0
    mean =round(Average(priceList),2)
    median =round(statistics.median(priceList),2)
    meanText.set("Average is: $"+str(mean))
    medianText.set("Median is: $"+ str(median))

    if(mean >= 50 and median >=50 and cardSelect.get()==1 ):
        create_gpu_insert = """
        INSERT INTO gpuprices(gpu_name, gpu_price)
        VALUES("""+'"'+ firstString+'"'+", "+str(mean)+""");"""
        print(create_gpu_insert)
        connection = create_db_connection("localhost", "root", pw, db) # Connect to the Database
        execute_query(connection, create_gpu_insert) # Execute our defined query
    pricelist=[]
    
    return

    
root=Tk()
root.title("Ebay Web Scraper")
root.geometry('600x300')
root.resizable(FALSE,False)
frm = ttk.Frame(root, padding=2)
frm.grid()
product = StringVar(frm)
meanText = StringVar(frm)
meanText.set("Average is: ")
medianText = StringVar(frm)
medianText.set("Median is: ")
cardSelect = IntVar(frm)
Entrybox = ttk.Entry(frm,textvariable=product).grid(column=0,row=0,  padx=200,pady=50)
searchButton =ttk.Button(frm, text="Search",command=lambda: webScrape(product)).grid(column = 0, row= 1,pady=10)
meanLabel = ttk.Label(frm,textvariable=meanText).grid(column=0,row=2)
medianLabel = ttk.Label(frm,textvariable=medianText).grid(column=0,row=3)

cardRadio=ttk.Checkbutton(frm,text="Is this a gpu?", variable=cardSelect).place(x=400,y=50)




root.mainloop()


