#ENSINANDO_COM_AS_TARTAURGA
#ETAPA_4_Funções_dentro_de_funções


from turtle import*
from random import*

#uma função para desenhar uma estrela de um tamanho especifico
def moveToRandomLocation():
    penup()
    setpos(randint(-400 , 400), randint(-400 , 400))
    pendown()
    
    
def drawStar(starSize,starColor):
    color(starColor)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward (starSize)
    end_fill()
    penup()


def drawGalaxy(numberOfStars):
    starColours = ["#058396", "#0275a6", "#827e01"]
    moveToRandomLocation()
    for star in range(numberOfStars):
        penup()
        left(randint(-180 , 180))
        forward (randint(5,20))
        drawStar(2,choice(starColours))
speed(11)

    
#isso vai desenhar uma estrela cinza clara em um fundo azul escuro

bgcolor("MidnightBlue")

#use a função para desenhar estrelas!
for star in range(30):
    moveToRandomLocation()
    drawStar(randint(5,25), "White")
    
for galaxy in range(3):
    drawGalaxy(40)
    
hideturtle()
done()
