from turtle import Turtle  # Importa la clase Turtle del módulo turtle.

FONT = ("Courier", 18, "bold")  # Define la fuente que se utilizará para escribir en la pantalla.

#clase que maneja el nivel en que se encuentra el jugador chan
class Scoreboard(Turtle):  
    
    #funcion de inicializacion
    def __init__(self): 
        #hereda la funcion init de la clase Turtle
        super().__init__()  
        
        #parametros de nuestra clase
        # Oculta la tortuga para que no se vea en la pantalla.
        self.hideturtle()  
        
        # Levanta el lápiz de la tortuga para que no dibuje una línea cuando se mueve.
        self.penup()  
        
        # Mueve la tortuga a la posición (-220, 260) en la pantalla.
        self.goto(-220, 260)  
        
        # Inicializa el nivel del jugador a 1.
        self.user_level=1  
        
        # Llama al método para escribir el nivel del jugador en la pantalla.
        self.player_level()  
        
        
    #TODO: diferentes niveles de juego, escribir en la parte izq superior de la pantalla el nivel del juego    
    # Define el método para escribir el nivel del jugador en la pantalla.
    def player_level(self): 
        # level=1
        #escribe nivel del jugador
        # Escribe el nivel del jugador en la pantalla.
        self.write(f'Level: {self.user_level}', False, align='center', font=FONT)  


    #TODO: funcion que sube nivel y muestra el nuevo nivel
    
    # Define el método para incrementar el nivel del jugador y mostrar el nuevo nivel.
    def new_player_level(self):  
        
        # Incrementa el nivel del jugador en 1.
        self.user_level += 1  
        
        # Borra lo que la tortuga ha escrito en la pantalla.
        self.clear()  
        
        #escribe nivel del jugador
        # Escribe el nuevo nivel del jugador en la pantalla.
        self.write(f'Level: {self.user_level}', False, align='center', font=FONT)  
        
    #funcion que corre cuando el jugador pierde    
    def end_game(self):
        
        # Mueve la tortuga al origen (0 , 0)
        self.goto(0, 0) 
        
        self.write(f'Game Over', False, align='center', font=("Courier", 22, "bold"))     
