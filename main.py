import random
import threading
import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



#TODO: configuracion del ancho y largo de la pantalla
screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic(picname="background.png")

screen.tracer(0)

player=Player()



screen.listen()


# TODO: Turtle movements,  the turtle se mueve SOLO hacia delante precionando el boton 'up'
screen.onkeypress(player.movement, 'Up')


scoreboard=Scoreboard()





total_cars=[]

   

game_is_on = True


def new_car():
    random_chance = random.randint(1,6)
    
    if random_chance == 1:
        car=CarManager()    

        #Agrega el carro a la lista de carros   
        total_cars.append(car)
        
    


       
while game_is_on:
    #La pantalla se va actualizar cada 0.1 segundos, dentro de nuestro while el codigo correra cada 0.1 segundos
    time.sleep(0.1)
    
    screen.update()
    
    #este cilco recorre cada carro de la lista de carro y llama al metodo movement de la class CarManager para ponerlos a mover
    for car in total_cars:
        car.movement()
        
    
    
    
    player_position=player.ycor()
    
    print(player_position)
    
    #si la posicion y es mayor a 270 
    if player_position >270:
        
        player.reset_position()
        print('el nivel del player debe subir en 1')
        scoreboard.new_player_level()
    
   
    new_car()
          
    
        


    







# Permite que el programa continue corriendo hasta que hagamos click en la pantalla , debemos crear un objeto de la clase Screen() para usar el metodo exitonclick()
# Debe ir al final de nuestro codigo
# Cierra la ventana al hacer click en la pantalla
screen.exitonclick()