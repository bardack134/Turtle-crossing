from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

#TODO:create turtle class
class Player(Turtle):
    
   
    #hereda del modulo Turtle
    def __init__(self):
        #valores de nuestra funcion inical, la que corre cuando se crea un objeto de la clase
        super().__init__()
        
        self.penup()
        
        self.shape('turtle')
        
        self.setheading(90)
        
        self.setposition(STARTING_POSITION)
        
    
    def movement(self):
        
        self.forward(MOVE_DISTANCE)
        
        
    #TODO:cuando la tortuga cruza la carretera vuelve a su posicion de origen en la parte de abajo
    def reset_position(self):
        
        if self.ycor()==FINISH_LINE_Y:
            self.goto(STARTING_POSITION)    
        
    
