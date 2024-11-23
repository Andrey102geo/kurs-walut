from tkinter import *
from tkinter import messagebox as mb
import requests


def exchange():
    code=entry.get().upper()
    if code:
        try:
            response=requests.get("https://open.er-api.com/v6/latest/USD")
            data=response.json()
            if code in data["rates"]:
                exchange_rate=data["rates"][code]
                mb.showinfo("Курс обмена",
                            f"Курс к доллару: {exchange_rate} {code} за 1 доллар.")
            else:
                mb.showerror("Ошибка",f"Валюта {code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка",e)
    else:
        mb.showwarning("Внимание!","Вы не ввели код валюты.")




window=Tk()
window.title("Курс обмена валют")
window.geometry("500x500")

Label(text="Введите код валюты: ").pack()

entry=Entry()
entry.pack()

Button(text="Получить курс обмена", command=exchange).pack()

window.mainloop()