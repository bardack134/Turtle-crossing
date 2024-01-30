from turtle import Turtle


FONT = ("Courier", 18, "bold")

#clase que maneja el nivel en que se encuentra el jugador chan
class Scoreboard(Turtle):
    
    #funcion de inicializacion
    def __init__(self):
        #hereda la funcion init de la clase Turtle
        super().__init__()
        
        #parametros de nuestra clase
        self.hideturtle()
        
        self.penup()
        
        self.goto(-220, 260)
        
        self.user_level=1
        
        self.player_level()
        
        
    #TODO: diferentes niveles de juego, escribir en la parte izq superior de la pantalla el nivel del juego    
    def player_level(self):
        # level=1
        #escribe nivel del jugador
        self.write(f'Level: {self.user_level}', False, align='center', font=FONT)
