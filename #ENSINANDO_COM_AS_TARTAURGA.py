#ENSINANDO_COM_AS_TARTAURGA
#ETAPA_1_DESENHANDO_ESTRELAS

from turtle import*

#isso vai desenhar uma estrela cinza clara em um fundo azul escuro 
color("WhiteSmoke")
bgcolor("Midnight Blue")

pendown()
begin_fill()

#desenha a forma da estrela

for side in range(5):
    left (144)
    forward(50)

end_fill()
penup()

forward(100)
done()