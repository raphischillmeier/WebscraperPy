from bs4 import BeautifulSoup
import tkinter as tk
import requests

urlTes = "https://www.deraktionaer.de/aktien/kurse/tesla-US88160R1014.html"
resultTes = requests.get(urlTes)
docTes = BeautifulSoup(resultTes.text, "html.parser")

urlApp = "https://www.deraktionaer.de/aktien/kurse/apple-US0378331005.html"
resultApp = requests.get(urlApp)
docApp = BeautifulSoup(resultApp.text, "html.parser")

urlCoca = "https://www.deraktionaer.de/aktien/kurse/thecoca-colacompany-US1912161007.html"
resultCoca = requests.get(urlCoca)
docCoca = BeautifulSoup(resultCoca.text, "html.parser")

spanTes = docTes.find_all("div", class_="stock-info-abs")
spanApp = docApp.find_all("div", class_="stock-info-abs")
spanCoca = docCoca.find_all("div", class_="stock-info-abs")


resultTes = spanTes[0].text
resultApp = spanApp[0].text
resultCoca = spanCoca[0].text

root = tk.Tk()
root.configure(bg="black")
root.geometry("600x800")
root.title("Webscraper")
root.resizable(width=False, height=False)

frame = tk.Frame(root, background="green")
frame.place(relwidth=0.8, relheight=0.77, relx=0.1, rely=0.1)

labelTesla = tk.Label(frame, text="Tesla" + resultTes, width=22, height=5, background="grey")
labelTesla.grid(row=1, column=1, columnspan=1, sticky="nsew")

labelApple = tk.Label(frame, text="Apple" + resultApp, width=22, height=5, background="grey")
labelApple.grid(row=2, column=2, columnspan=1, sticky="nsew")

labelCoca = tk.Label(frame, text="Coca Cola" + resultCoca, width=22, height=5, background="grey")
labelCoca.grid(row=3, column=3, columnspan=1, sticky="nsew")

root.mainloop()




