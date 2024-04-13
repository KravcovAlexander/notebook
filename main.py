from tkinter import *
from tkinter import simpledialog
from tkinter.constants import END
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog

def open_file():
        file_path = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
            text_widget.delete('1.0', END)
            text_widget.insert(END, content)



def find(event=None):  
    global text_widget
    find_text = simpledialog.askstring("поиск", "что нужно найти")
    if find_text:
        content = text_widget.get('1.0', END)
        search = content.lower().find(find_text.lower())
        if search != -1:
            start = f"1.{search}"
            end = f"{start}+{len(find_text)}c"
            text_widget.tag_add('найдено', start, end)
            text_widget.tag_config('найдено', background='yellow')

def save_file():
    global text_widget
    name = simpledialog.askstring("Сохранить", "Введите имя файла:")
    if name:
        content = text_widget.get("1.0", END)
        with open(name, "w") as f:
            f.write(content)

def main():
    global text_widget
    root = Tk()
    root.title("Простой блокнот")
    root.geometry('400x250')

    text_widget = ScrolledText(root)
    text_widget.pack(fill=BOTH, expand=True, padx=10, pady=10)

    menu = Menu(root)
    file_menu = Menu(menu)
    file_menu.add_command(label='Сохранить', command=save_file)
    file_menu.add_command(label="Найти", command=find)
    file_menu.add_command(label="Открыть файл", command=open_file)
    menu.add_cascade(label='Файл', menu=file_menu)
    root.config(menu=menu)

    root.bind("<Control-s>", lambda event: save_file())
    root.bind("<Control-f>", find)

    root.mainloop()

if __name__ == '__main__':
    main()