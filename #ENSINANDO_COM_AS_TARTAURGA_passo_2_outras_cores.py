#ENSINANDO_COM_AS_TARTAURGA
#ETAPA_2_PASSANDO_DADOS_PARA_AS_FUNÇÕES


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

drawStar(50, "Red")
forward (100)
drawStar(30,"White")
left(120)
forward(150)
drawStar(70,"Green")

hideturtle()
done()
