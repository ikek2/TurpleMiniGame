import turtle
import random
import math
from PIL import Image

def set_fullscreen_background(image_path):
    # Получаем размеры изображения
    try:
        with Image.open(image_path) as img:
            width, height = img.size
    except Exception as e:
        print(f"Ошибка загрузки изображения: {e}")
        width, height = 800, 600  # Размеры по умолчанию

    # Настройка экрана
    screen = turtle.Screen()
    screen.title("Собери все точки")
    screen.setup(width, height)  # Устанавливаем размер окна
    screen.bgpic(image_path)  # Устанавливаем фон

    screen.tracer(0)
    screen.update()

    return screen, width, height

def move_up():

    x, y = turtle.pos()
    turtle.setheading(90)
    if -n/2<=x <= n / 2 and -m/2<=y + 20 <= m / 2:
        turtle.setposition(x, y + 20)
        del_point(lst)

def move_down():
    x, y = turtle.pos()
    turtle.setheading(270)
    if -n/2<=x <= n / 2 and -m/2<=y-20 <= m / 2:
        turtle.setposition(x, y - 20)
        del_point(lst)

def move_left():
    x, y = turtle.pos()
    turtle.setheading(180)
    if -n/2<=x - 20 <= n / 2 and -m/2<=y <= m / 2:
        turtle.setposition(x - 20, y)
        del_point(lst)

def move_right():
    x, y = turtle.pos()
    turtle.setheading(0)
    if -n/2<=x+20<=n/2 and -m/2<=y<=m/2:
       turtle.setposition(x + 20, y)
       del_point(lst)

def draw_point(lst):
    x, y = turtle.pos()
    turtle.tracer(0)
    turtle.clear()
    turtle.pensize(10)
    for i,j in lst:
        turtle.goto(i,j)
        turtle.pendown()
        turtle.dot(15, 'yellow')
        turtle.up()
    turtle.goto(x, y)
    turtle.tracer(1)

def del_point(lst):
    x, y = turtle.pos()
    for i, j in lst:
        if math.isclose(x, i, abs_tol=20) and math.isclose(y, j, abs_tol=20):
            lst.remove((i,j))
            if len(lst)==0:
                turtle.clear()
                turtle.color('yellow')
                turtle.tracer(0)
                turtle.goto(0,0)
                turtle.write('Вы все собрали :)', align='center', font=('Arial', 17, 'bold'))
                screen.title("Победа!")
                turtle.goto(x, y)
                turtle.tracer(1)
                turtle.done()
            draw_point(lst)
            break



#внешний вид
background = "background.gif"  # Путь к вашему изображению
screen,n,m = set_fullscreen_background(background)


#рисуем точки
turtle.up()
lst=[(random.randint(int(-n/2),int(n/2)), random.randint(int(-m/2),int(m/2))) for _ in range(10)]
draw_point(lst)

turtle.Screen().register_shape("bee.gif")
turtle.shape("bee.gif")


turtle.speed(0)
turtle.goto(0,0)
turtle.showturtle()  # отображаем черепашку

turtle.Screen().listen()  # устанавливаем фокус на экран черепашки

turtle.Screen().onkey(move_up, 'Up')  # регистрируем функцию на нажатие клавиши наверх
turtle.Screen().onkey(move_down, 'Down')  # регистрируем функцию на нажатие клавиши вниз
turtle.Screen().onkey(move_left, 'Left')  # регистрируем функцию на нажатие клавиши налево
turtle.Screen().onkey(move_right, 'Right')  # регистрируем функцию на нажатие клавиши направо

turtle.done()