import tkinter as tk

root = tk.Tk()
root.title("Лічильник кліків")

click_count = 0
label_text = "Привіт"

def change_text():
    global click_count, label_text
    click_count += 1
    if click_count % 2 == 1:
        label_text = "Папа"
    else:
        label_text = "Привіт"
    label.config(text=label_text)
    update_title()

def update_title():
    root.title(f"Кількість кліків: {click_count}")

label = tk.Label(root, text=label_text)
label.pack(pady=20)

button = tk.Button(root, text="Зміна тексту", command=change_text)
button.pack()

update_title()

root.mainloop()


