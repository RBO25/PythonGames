from tkinter import *
from tkinter import messagebox
import time

tk = Tk()
app_running = True

size_canvas_x = 600
size_canvas_y = 600
s_x = s_y = 9 #размер игрового поля
step_x = size_canvas_x // s_x       #шаг по горизонтали
step_y = size_canvas_y // s_y       #шаг по вертикали
size_canvas_x = step_x*s_x
size_canvas_y = step_y*s_y

menu_x = 250 #область для кнопок

def on_closing():   #функция для вывода окна с закрытием игры
    global app_running
    if messagebox.askokcancel("Game over", "Exit?"):
        app_running = False
        tk.destroy()

tk.protocol("WM_DELETE_WINDOW", on_closing)#параметры игры
tk.title("BattleSeaGame")
tk.resizable(0, 0) #фиксирует размер игры
tk.wm_attributes("-topmost", 1) #окно игры всегда сверху других приложений
canvas = Canvas(tk, width=size_canvas_x+menu_x, height=size_canvas_y, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="light blue")
canvas.pack()
tk.update()

def draw_table(): # рисует игровое поле (пересекающиеся линии)
    for i in range(0, s_x+1):
        canvas.create_line(step_x * i, 0, step_x * i, size_canvas_y)
    for i in range(0, s_y+1):
        canvas.create_line(0, step_y * i, size_canvas_x, step_y * i)



draw_table()



def button_show_enemy():
    pass

def button_begin_again():
    pass


b0 = Button(tk, text="Show enemy ships", command = button_show_enemy)
b0.place(x=size_canvas_x+20, y=30)

b1 = Button(tk, text="Start over", command = button_begin_again)
b1.place(x=size_canvas_x+20, y=70)


def add_to_all(event):
    _type = 0 #левая кнопка мыши
    if event.num == 3:
        _type = 1 #правая кнопка мыши
    #print(_type)
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    #print(mouse_x, mouse_y)
    ip_x = mouse_x // step_x
    ip_y = mouse_y // step_y
    print(ip_x, ip_y, "_type:", _type)

canvas.bind_all("<Button-1>", add_to_all) #левая кнопка мыши
canvas.bind_all("<Button-3>", add_to_all) #правая кнопка мыши


while app_running:
    if app_running:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)