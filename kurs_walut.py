from tkinter import *
from tkinter import messagebox as mb
import requests
from tkinter import ttk


def exchange():
    first_code = combobox.get().upper()
    second_code = second_combobox.get().upper()
    target = target_combobox.get().upper()

    if first_code and second_code and target:
        try:

            response_first = requests.get(f"https://open.er-api.com/v6/latest/{first_code}")
            data_first = response_first.json()

            response_second = requests.get(f"https://open.er-api.com/v6/latest/{second_code}")
            data_second = response_second.json()

            if target in data_first["rates"] and target in data_second["rates"]:
                # Получаем обменный курс для первой базовой валюты
                first_exchange_rate = data_first["rates"][target]

                second_exchange_rate = data_second["rates"][target]

                first_base = popular_cur[first_code]
                second_base = popular_cur[second_code]
                cur_name = popular_cur[target]
                message = (
                    f"Курс: {first_exchange_rate:.2f} {cur_name} за 1 {first_base}.\n"
                    f"Курс: {second_exchange_rate:.2f} {cur_name} за 1 {second_base}."
                )
                mb.showinfo("Курсы обмена", message)
            else:
                mb.showerror("Ошибка", f"Валюта {target} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", e)
    else:
        mb.showwarning("Внимание!", "Вы не ввели коды валют.")


def update_label(event):
    code = combobox.get()
    name = popular_cur[code]
    cur_label["text"] = name

popular_cur = {
    "EUR": "Евро", "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар", "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк","CNY": "Китайский юань",
    "RUB": "Российский рубль","KZT": "Казахстанский тенге","UZS": "Узбекский сум",
    "USD": "Американский доллар"}


window = Tk()
window.title("Курс обмена валют")
window.geometry("450x200")


Label(text="Выберите первую базовую валюту:").pack()
combobox = ttk.Combobox(values=list(popular_cur.keys()))
combobox.pack()
combobox.bind("<<ComboboxSelected>>", update_label)


Label(text="Выберите вторую базовую валюту:").pack()
second_combobox = ttk.Combobox(values=list(popular_cur.keys()))
second_combobox.pack()
second_combobox.bind("<<ComboboxSelected>>", update_label)


Label(text="Выберите целевую валюту:").pack()
target_combobox = ttk.Combobox(values=list(popular_cur.keys()))
target_combobox.pack()
target_combobox.bind("<<ComboboxSelected>>", update_label)
Button(text="Получить курс обмена", command=exchange).pack()


cur_label = Label(height=2)
cur_label.pack()

window.mainloop()