# main.py -- put your code here!
from pyb import UART, SPI, Pin, Timer
import random


#liste ennemy
ennemy = [] #tableau pour stocker les robots ennemy
nb_missile = [] #tableau pour stocker les missiles

#init uart2, 115200 bauds, 8bits
numero_uart = 2
uart = UART(numero_uart)
uart.init(115200, bits=8, parity=None, stop=1) 


#init timer
t = Timer(4, freq = 1)
t1 = Timer(2, freq = 2)

#init chip select
CS = Pin("PE3", Pin.OUT_PP)
 
#init spi
SPI_1 = SPI(
	    1,  # SPI1: PA5, PA6, PA7
	    SPI.MASTER,
	    baudrate=50000,
	    polarity=0,
	    phase=0,)


#init button, valeur par défaut = 0
push_button = Pin("PA0", Pin.IN,Pin.PULL_DOWN) 

#init taille ecran
SCREEN_HEIGTH = 50
SCREEN_LENGTH = 200


#declaration vt100
def clear_screen():
	uart.write("\x1b[2J\x1b[.25l")
	
def move(x, y):
	uart.write("\x1b[{};{}H".format(y, x))


#fonction SPI
def read_reg(addr):
	CS.low()
    	SPI_1.send(addr | 0x80)  # 0x80 pour mettre le R/W à 1
    	tab_values = SPI_1.recv(1)  # je lis une liste de 1 octet
    	CS.high()
    	return tab_values[0]


def write_reg(addr, value):
	CS.low()
    	SPI_1.send(addr | 0x00)  # write
    	SPI_1.send(value)
    	CS.high()


def convert_value(high, low):
	value = (high << 8) | low
    	if value & (1 << 15):
        	# negative number
        	value = value - (1 << 16)
    	return value


def read_acceleration(base_addr):
	low = read_reg(base_addr)
    	high = read_reg(base_addr + 1)
    	return convert_value(high, low)


#affichage ecran jeu
def affichage_ecran():
    
    for i in range (SCREEN_LENGTH) : #affichage ligne
        move(i,0)
        uart.write("#")
        move(i,SCREEN_HEIGTH)
        uart.write("#")
        
    for j in range (SCREEN_HEIGTH) : #affichage colonne
        move(0,j)
        uart.write("#")
        move(SCREEN_LENGTH,j)
        uart.write("#")
	

#classe 
class Vaisseau:
	def init(self, x, y, skin):
		self.x = x
		self.y = y
		self.skin = skin


#missile
class Missile:
	def init(self, x, y, skin, nb_missile_max):
		self.x = x
		self.y = y
		self.skin = skin
		self.nb_missile_max = nb_missile_max
	


class Robot_ennemy:
	def init(self, x, y, skin):
		self.x = x
		self.y = y
		self.skin = skin
	nb_robot = 0
	


class Missile_mechant:
	def init(self, x, y, skin):
		self.x = x
		self.y = y
		self.skin = skin


def affichage_vaisseau(x, y, skin):
	move(x,y)
	uart.write(skin)


def affichage_robot_ennemy(Robot_ennemy r1):
	r1.y = 0 #affichage robot ennemy à partir de la première colonne
	r1.skin = "v=A=v"
	while r1.y>= 4: #affichage sur 4 colonne
		r1.x = 0
		while r1.x<SCREEN_LENGTH: #affichage sur toute la ligne
			uart.write(r1.skin) # affichage skin robot ennemi
			r1.x+=10 #espace de 10 cases entre les robots 
			move(r1.x,r1.y) 
			ennemy.append(r1) #ajout robot ennemi dans le tableau
			r1.nb_robot++ #ajout nombre robot ennemi
		r1.y--

i = 0
def tir_missile(Missile m1, Robot_ennemy r1, Vaisseau v):
	while i<m1.nb_missile_max:
		if push_button == 1: #appui sur le bouton
			v.skin = "0X0"
			m1.visible = True
			m1.nb_missile.append(m1.skin)#ajout missile
		while m1.visible = True:
			uart.write(m1.skin)
			if r1.x == m1.x and r1.y = m1.y:#position missile = position robot ennemi
				m1.visible = False
				destruct_robot_ennemy(r1)
			elif m1.x == SCREEN_HEIGTH: #missile en fin de course
				m1.visible = False
			else: #pas d'obstacle
				uart.write(" ")
				m1.x++	
				move(m1.x, m1.y)
		i++	
		
def mouv_vaisseau(x,y, skin):
	addr_who_I_am = 0x0F
	addr_x_accel = 0x28

	value = read_reg(addr_who_I_am)


	addr_ctrl_reg4 = 0x20
	write_reg(addr_ctrl_reg4, 0x77)
	x_accel = read_acceleration(addr_x_accel)
	
	if x_accel>=300 and v.x<SCREEN_LENGTH: #carte penchée vers la droite
		x += 1
	elif x_accel<=-300 and v.x>0: #carte penchée vers la gauche
		x -=1
	else:
		x = x
	uart.write(" ")#suppression de l'ancien vaisseau	
	affichage_vaisseau(x, y, skin) #affichage vaisseau


def mouv_robot_ennemy(Robot_ennemy r): #mouvement robot ennemi (ne fonctionne pas)
	r.x++
	r.y++
	move(r.y, r.x)
	uart.write(r.skin)


def destruct_vaisseau(Vaisseau v): #destruction de notre vaisseau
	clear_screen()
	uart.write("BOOM , LOOSER")	


def destruct_robot_ennemy(Robot_ennemy r):
	move(r.x, r.y)
	uart.write(" ") #destruction robot ennemi
	r.nb_robot-- #suppression d'un robot ennemi


def tir_ennemy(Missile_mechant m, Robot_ennemy r, Vaisseau v):
	robot = choice().ennemy #choix dans le tableau des ennemis
	robot.y = m.y #definition du point de départ de notre missile
	
	if m.x == v.x and m.y == v.y: #position missile = position vaisseau
		destruct_vaisseau(v)
	elif m.x==0: #missile en fin de course
		move(m.x, m.y)
		uart.write(" ") #suppression missile
	else: #pas d'obstacle
		move(m.x, m.y)
		uart.write(m.skin)
		m.x++ #missile qui descend
		
	



def main():
	x_vaisseau=100
	y_vaisseau = 15
	skin_vaisseau = "0_0"
	v = Vaisseau(x_vaisseau, y_vaisseau, skin_vaisseau)
	r1 = Robot_ennemi(0,0, "v=A=v")
	Missile m(v.x, v.y, "°")
	Missile_mechant mm(r1.x, r1.y, "|")
	
	
	
	while True:
		affichage_ecran() 
		affichage_robot_ennemy(r1) 
		while r1.nb_robot>0: #tant qu'il y a des robot ennemis
			mouv_vaisseau(x_vaisseau, y_vaisseau, skin_vaisseau) # fonction mouvement de notre vaisseau
			tir_missile(m, r1, v) #fonction du tir de notre vaisseau
			t.callback(mouv_robot_ennemy(r1)) #fait bouger les robots ennemis à chaque seconde
			t1.callback(tir_ennemy(mm, r1, v)) #tir ennemi toutes les 0.5 seconde
			
		move(50,25)	
		uart.write("C'est une belle victoire qu'on a là")

clear_screen()
main()
