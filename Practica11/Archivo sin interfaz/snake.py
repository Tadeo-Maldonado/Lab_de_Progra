import turtle
import time
import random
score=0
high_score=0

posponer = 0.1 #Tiempo de movimiento del objeto

#Configuracion de la ventana
wn = turtle.Screen()
wn.title("Juego Snake")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)#Dimensiones de la pantalla
wn.tracer(0)#Mejor visibilidad

#Cabeza
cabeza=turtle.Turtle()#Se crea el objeto
cabeza.speed(0)
cabeza.shape("square") #Comando que ayuda a cambiar la forma del objeto
cabeza.penup() #Comando que ayuda a no dejar rastro el objeto
cabeza.color("green") #Comando para dar color al objeto
cabeza.goto(0,0) #Comando que te ayuda a darle posicion al objeto
cabeza.direction = "stop" #Direcciones del objeto

#Comida
comida=turtle.Turtle()#Se crea el objeto
comida.speed(0)
comida.shape("circle") #Comando que ayuda a cambiar la forma del objeto
comida.penup() #Comando que ayuda a no dejar rastro el objeto
comida.color("red") #Comando para dar color al objeto
comida.goto(0,100) #Comando que te ayuda a darle posicion al objeto

#Crear Marcador
texto =turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score:0        High Score:0", align = "center", font=("Courier", 24, "normal"))

#Cuerpo de serpiente
cuerpo= []

#Funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"

def mov():#Funcion de movimiento hacia los lados
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")
    
        
while True:
    wn.update()

    #Colisiones
    if cabeza.xcor() >380 or cabeza.xcor() < -380 or cabeza.ycor() >280 or cabeza.ycor() <-280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #Esconder segmentos si colisionamos
        for totalseg in cuerpo:
            totalseg.goto(1000, 1000)

        cuerpo.clear()
        score = 0
        texto.clear()
        texto.write("Score:{}        High Score:{}".format(score, high_score), align = "center", font=("Courier", 24, "normal"))

    #Colisiones con comida
    if cabeza.distance(comida)<20:
        y = random.randint(-280,280)
        x = random.randint(-380,380)
        comida.goto(x,y)

        Ncuerpo=turtle.Turtle()
        Ncuerpo.speed(0)
        Ncuerpo.shape("square") 
        Ncuerpo.penup() 
        Ncuerpo.color("light green") 
        cuerpo.append(Ncuerpo)

        #Aumentando marcados
        score +=10

        if score > high_score:
            high_score=score
        texto.clear()
        texto.write("Score:{}        High Score:{}".format(score, high_score), align = "center", font=("Courier", 24, "normal"))

    #Mover el cuerpo de la serpiente
    totalseg = len(cuerpo)
    for index in range(totalseg -1,0,-1):
        x = cuerpo[index-1].xcor()
        y = cuerpo[index-1].ycor()
        cuerpo[index].goto(x,y)
    if totalseg>0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        cuerpo[0].goto(x,y)
                
    mov()

    #Colisiones con el cuerpo
    for totalseg in cuerpo:
        if totalseg.distance(cabeza)<20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction="stop"
            for totalseg in cuerpo:
                totalseg.goto(1000, 1000)
            cuerpo.clear()
            texto.clear()
            score = 0
            texto.write("Score:{}        High Score:{}".format(score, high_score), align = "center", font=("Courier", 24, "normal"))
    time.sleep(posponer)
