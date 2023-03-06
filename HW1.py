import turtle

tao = turtle.Pen()
tao.hideturtle()
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
for i in range(260):
    tao.speed(10)
    tao.pencolor(colors[i % 6])  # 6 คือจำนวนสี
    tao.width(i // 100 + 1)
    tao.forward(i)
    tao.left(59)
