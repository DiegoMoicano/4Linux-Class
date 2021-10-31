import turtle

tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.pensize(2)
tartaruga.speed(5)

num_de_formas = 5

tartaruga.setheading(45)
tartaruga.penup()
tartaruga.goto(20, 50)
tartaruga.pendown()

for shape in range(1, num_de_formas + 1):
    # Desenha o quadrado
    for sides in range(4):
        tartaruga.forward(20 + shape * 20)
        tartaruga.right(90)

    # Move a posição do próximo quadrado

    tartaruga.penup()
    tartaruga.left(90)
    tartaruga.forward(10)
    tartaruga.left(90)
    tartaruga.forward(10)
    tartaruga.left(180)
    tartaruga.pendown()

tartaruga.mainloop()

tartaruga.penup()
tartaruga.pensize(1)
tartaruga.setx(135)
tartaruga.penup()
tartaruga.back(122)
tartaruga.pendown()
tartaruga.sety(135)
tartaruga.back(121)
tartaruga.setx(135)
tartaruga.penup()
tartaruga.setpos(50, 50)
tartaruga.right(45)
