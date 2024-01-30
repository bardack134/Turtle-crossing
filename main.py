import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


#TODO: configuracion del ancho y largo de la pantalla
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()


screen.listen()

# TODO: Turtle movements,  the turtle se mueve SOLO hacia delante precionando el boton 'up'
screen.onkeypress(player.movement, 'Up')


scoreboard=Scoreboard()

game_is_on = True
while game_is_on:
    #La pantalla se va actualizar cada 0.1 segundos, dentro de nuestro while el codigo correra cada 0.1 segundos
    time.sleep(0.1)
    screen.update()
    player.reset_position()







# Permite que el programa continue corriendo hasta que hagamos click en la pantalla , debemos crear un objeto de la clase Screen() para usar el metodo exitonclick()
# Debe ir al final de nuestro codigo
# Cierra la ventana al hacer click en la pantalla
screen.exitonclick()