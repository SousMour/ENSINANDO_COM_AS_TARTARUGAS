#ENSINANDO_COM_AS_TARTAURGA
#ETAPA_3_ESTRELAS_ALEATORIAS


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

#isso vai desenhar uma estrela cinza clara em um fundo azul escuro

bgcolor("MidnightBlue")

#use a função para desenhar estrelas!
for star in range(30):
    moveToRandomLocation()
    drawStar(randint(5,25), "White")
hideturtle()
done()
