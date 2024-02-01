import random
import time  # Importa el módulo time para trabajar con el tiempo.
from turtle import Screen, Turtle  
from player import Player  
from car_manager import CarManager  
from scoreboard import Scoreboard  

#TODO: configuracion del ancho y largo de la pantalla
 # Crea un nuevo objeto Screen
screen = Screen() 

# Configura el tamaño de la pantalla a 600x600.
screen.setup(width=600, height=600)  

# Establece la imagen de fondo de la pantalla a "background.png".
screen.bgpic(picname="background.png")  

# Desactiva la animación automática de la pantalla.
screen.tracer(0)  

 # Crea un nuevo objeto Player.
player=Player() 





# Pone la pantalla en modo de escucha para los eventos del teclado y del ratón.
screen.listen()  

# TODO: Turtle movements,  the turtle se mueve SOLO hacia delante precionando el boton 'up'
# Asigna la función de movimiento del jugador al evento de presionar la tecla 'Up'.
screen.onkeypress(player.movement, 'Up')  

# Crea un nuevo objeto Scoreboard.
scoreboard=Scoreboard()  

 # Crea una lista vacía para almacenar los carros.
total_cars=[] 

 # Establece la variable de control del bucle del juego a True.
game_is_on = True 

 # Establece la velocidad inicial de los carros a 5
speed=5 

# Define la función para crear un nuevo carro.
def new_car():  
    random_chance = random.randint(1,6) 
    
    # Si el número aleatorio es 1.
    if random_chance == 1:  
        
        # Crea un nuevo objeto CarManager con la velocidad actual.
        car=CarManager(speed)  

                    
        #Agrega el carro a la lista de carros   
        total_cars.append(car) 
        
while game_is_on: 
    #La pantalla se va actualizar cada 0.1 segundos, dentro de nuestro while el codigo correra cada 0.1 segundos
    time.sleep(0.1)  # Hace una pausa de 0.1 segundos.
    
    screen.update()  # Actualiza la pantalla.
    
    #este ciclo recorre cada carro de la lista de carro y llama al metodo movement de la class CarManager para ponerlos a mover
    for car in total_cars:  
        
        # Llama al método de movimiento del carro.
        car.movement()  
      
    
    # Obtiene la posición_y del jugador.
    player_position=player.ycor()  
    
    #si la posicion y es mayor a 270 
    if player_position >270:  
        
        # Resetea la posición del jugador.
        player.reset_position()  
        
          
        # Incrementa el nivel del jugador en el marcador.
        scoreboard.new_player_level()  

        # Incrementa la velocidad de los carros en 5.
        speed += 5  
   
    #recorremos carro por carro de la lista de carros
    for car in total_cars:
        
        #TODO: chequear si la tortuga choco un carro
        #miramos la distancia del carro a la tortuga 
        if car.distance(player)<20:
            
            #si la codicion se cumple significa que el carro se estrello y el juego finalizo
            game_is_on = False
            
            #Llama al metodo que muestra el mensaje de game over
            scoreboard.end_game()
            
            
   
   
    new_car()  # Crea un nuevo carro.
        
            
screen.exitonclick()  # Cierra la ventana cuando se hace clic en ella.
