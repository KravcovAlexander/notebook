from tkinter import *
from tkinter import simpledialog
import re


def find(event=None):  
    find_text = simpledialog.askstring("поиск", "что нужно найти")
    if find_text:
        content = text.get('1.0', END)
        search = re.search(find_text, content)
        if search:
            start = text.search(find_text, '1.0', stopindex=END)
            text.tag_add('found', start, f'{start}+{len(find_text)}c')
            text.tag_config('found', background='yellow')

def save_file(text):
    name = simpledialog.askstring("cохранить", "Введите имя файла:")
    if name:
        content = text.get("1.0", END) 
        if len(content) >= 4:
            with open(name, "w+") as f:
                f.write(content)

root = Tk()
root.title("Простой блокнот")
root.geometry('400x250')

text = Text(root)
text.pack(fill=BOTH, expand=True, padx=10, pady=10)

menu = Menu(root)
file_menu = Menu(menu)
file_menu.add_command(label='Сохранить',  command=lambda: save_file(text))
file_menu.add_command(label="найти", command=find)
menu.add_cascade(label='Файл', menu=file_menu)
root.config(menu=menu)


root.bind("<Control-s>", lambda event: save_file(text))

root.bind("<Control-f>", find)

root.mainloop()