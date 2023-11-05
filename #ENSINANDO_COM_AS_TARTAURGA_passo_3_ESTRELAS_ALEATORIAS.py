#ENSINANDO_COM_AS_TARTAURGA
#ETAPA_3_ESTRELAS_ALEATORIAS


from turtle import*

#uma função para desenhar uma estrela de um tamanho especifico


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
penup()
setpos(200,200)
pendown

drawStar(50, "White")
hideturtle()
done()
