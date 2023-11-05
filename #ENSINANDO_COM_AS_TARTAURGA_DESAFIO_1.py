#ENSINANDO_COM_AS_TARTAURGA
#ETAPA_1_DESENHANDO_ESTRELAS
#DESAFIO_1

from turtle import*
color("WhiteSmoke")
bgcolor("Midnight Blue")

pendown()
begin_fill()

for side in range(5):
    left (144)
    forward(50)

end_fill()
penup()

forward(100)
done()