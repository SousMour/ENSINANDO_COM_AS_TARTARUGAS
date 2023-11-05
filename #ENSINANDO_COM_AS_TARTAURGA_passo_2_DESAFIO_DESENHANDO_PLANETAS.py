from turtle import*

#uma função para desenhar uma estrela de um tamanho especifico


def drawPlanet(planetSize,planetColor):
    color(planetColor)
    pendown()
    begin_fill()
    for side in range(34):
        left(10)
        forward (planetSize)
    end_fill()
    penup()

#isso vai desenhar uma estrela cinza clara em um fundo azul escuro

bgcolor("MidnightBlue")

#use a função para desenhar estrelas!

drawPlanet(10, "Red")
forward (200)
drawPlanet(20,"White")
left(250)
forward(250)
drawPlanet(30,"Green")

hideturtle()
done()

