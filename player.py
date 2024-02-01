from turtle import Turtle  # Importa la clase Turtle del módulo turtle.
# Define la posición inicial de la tortuga.
STARTING_POSITION = (0, -280)  

# Define la distancia que la tortuga se moverá en cada paso.
MOVE_DISTANCE = 10  

# Define la posición y de la línea de meta.
FINISH_LINE_Y = 280  

#TODO:create turtle class
class Player(Turtle):  
    
    #hereda del modulo Turtle
    # Define el método de inicialización para la clase Player.
    def __init__(self):  
        
        # Llama al método de inicialización de la clase padre (Turtle).
        super().__init__()  
        
         # Levanta el lápiz de la tortuga para que no dibuje una línea cuando se mueve.
        self.penup() 
        
        # Establece la forma de la tortuga a 'turtle'.
        self.shape('turtle')  
        
        # Establece la dirección inicial de la tortuga a 90 grados (hacia arriba).
        self.setheading(90)  
        
        # Coloca la tortuga en la posición inicial.
        self.setposition(STARTING_POSITION) 
        
    # Define el método de movimiento para la clase Player.
    def movement(self):  
        
        # Mueve la tortuga hacia adelante la distancia definida en MOVE_DISTANCE.
        self.forward(MOVE_DISTANCE)  
        
        
    #TODO:cuando la tortuga cruza la carretera vuelve a su posicion de origen en la parte de abajo
    # Define el método para resetear la posición de la tortuga.
    def reset_position(self):  
        # Si la tortuga ha cruzado la línea de meta.
        if self.ycor()==FINISH_LINE_Y:  
            
            # Mueve la tortuga de vuelta a la posición inicial.
            self.goto(STARTING_POSITION) 

    
