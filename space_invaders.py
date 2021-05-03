# main.py -- put your code here!
from pyb import UART, SPI, Pin, Timer

#init uart2, 9600 bauds, 8bits
numero_uart = 2
uart = UART(numero_uart)
uart.init(9600, bits=8, parity=None, stop=1) 


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
def affiche_ecran():
	i=0
	j=0
	while i<SCREEN_LENGTH:
		move(i,0)
		uart.write("#")
		move(i,SCREEN_HEIGTH)
		uart.write("#")
		i++
	while j<SCREEN_HEIGTH:
		move(0,j)
		uart.write("#")
		move(SCREEN_LENGTH,j)
		uart.write("#")
		j++

#classe 
class Vaisseau:
	def init(self, x, y):
		self.x = x
		self.y = y
	skin

#missile
class Missile:
	def init(self, x, y):
		self.x = x
		self.y = y
	skin

class robot_ennemi:
	def init(self, x, y):
		self.x = x
		self.y = y
	skin
	

#fonction vaisseau
def affichage_vaisseau(Vaisseau v):
	move(v.x,v.y)
	uart.write(v.skin)

def mouv_vaisseau(Vaisseau v):
	addr_who_I_am = 0x0F
	addr_x_accel = 0x28
	addr_y_accel = 0x2A
	addr_z_accel = 0x2C
	
	value = read_reg(addr_who_I_am)

	if value != 63:
		print("error")
	else
		clear_screen()
		uart.write(v.skin)
		addr_ctrl_reg4 = 0x20
		write_reg(addr_ctrl_reg4, 0x77)
		x_accel = read_acceleration(addr_x_accel)
		
		if x_accel<=300
			v.x += 1
		elif x_accel>=-300
			v.x -=1
		else
			v.x = v.x	
		move(v.x, v.y)

def mouv_missile(Vaisseau v1, robot_ennemi r1):
	if push_button.value() = 1:
		m = Missile(v1.x, v1.y, "°")
		v1.skin = "0x0"
		while !r1.x | !r1.y:
			m.y+=1
			move(m.x,m.y)
			
			
#fonction robot_ennemy
def affichage_robot_ennemy(robot_ennemi r1, colonne):
	r1.x = 0
	r1.y = SCREEN_HEIGTH
	r1.skin = "v=A=v"
	i=0
	while i<colonne:
		if i<SCREEN_LENGTH
			uart.write(r1.skin)
			r1.x+=3
			move(r1.x,r1.y)
		i++
		

def tir_ennemi():
	


def main():
	v = Vaisseau(100,15,"0_0")
	r1 = robot_ennemi(0,0, "v=A=v")
	#mouv_vaisseau()
	#affichage_robot_ennemy(r1,3)
	#mouv_missile(v,r1)
	while True:
		affichage_ecran()
		affichage_vaisseau(v)
	
	

