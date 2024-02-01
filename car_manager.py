import random  # Importa el módulo random para generar números aleatorios.
from turtle import Turtle  # Importa la clase Turtle del módulo turtle.

# Define la distancia inicial que los carros se moverán en cada paso.
# STARTING_MOVE_DISTANCE = 5  

# Define la cantidad que se incrementará la distancia de movimiento de los carros.
# MOVE_INCREMENT = 5  

#TODO: crear clase de los carros
class CarManager(Turtle):  
    def __init__(self, speed):
        # Llama al método de inicialización de la clase padre (Turtle).
        super().__init__()  
         # Establece la forma de los carros a 'square'.
        self.shape('square') 

        # Levanta el lápiz de los carros para que no dibujen una línea cuando se mueven.
        self.penup() 
        
        # Establece el tamaño de los carros a 1 de alto y 2 de ancho.
        self.shapesize(stretch_wid=1, stretch_len=2)  
        
        # Llama al método para establecer un color aleatorio para los carros.    
        self.random_color()      
        
        # Llama al método para establecer una posición aleatoria para los carros.
        self.car_position()  
        
        self.speed=speed      
          
          
    #Funcion para agregar un carro a la lista de carros, recibe 2 parametros el car creado y total_cars que es la lista de carros    
    def car_list_add(self, total_cars, car):
        
        # Agrega el carro a la lista de carros.
        total_cars.append(car)  
        
            
         
    #TODO: los carros se mueven desde la derecha a la izquierda
    def movement(self):
        
        # Mueve los carros hacia atrás la distancia definida self.speed
        self.backward(self.speed)  
        
        
    
        
        
        
        
    def random_color(self):
        R=random.random()  # Genera un número aleatorio para el componente rojo del color.
        B=random.random()  # Genera un número aleatorio para el componente azul del color.
        G=random.random()  # Genera un número aleatorio para el componente verde del color.
        self.color(R,B,G)  # Establece el color de los carros a un color aleatorio.
        
    #TODO：la posicion de los carros se crea en forma aleatoria
    def car_position(self):
        # position_x=random.randint(50, 300)
        
        # Genera un número aleatorio para la posición_y de los carros.
        position_y=random.randint(-240, 260)  
        
        # Mueve los carros a una posición aleatoria en el eje y.
        self.goto(300, position_y)  
