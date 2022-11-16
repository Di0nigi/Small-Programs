import pygame
import os
import threading
import time
from pygame.locals import *
fir=True
pygame.init()
w=2400
h=1080
color=(255,255,255)
fps=60
dist=35
vel=3
fleet=[]
bullets=[]
first=True
font = pygame.font.SysFont(pygame.font.get_default_font(), 80)
img = font.render('Shoot', True, (255,255,255))
font1= pygame.font.SysFont(pygame.font.get_default_font(), 150)
start_text= font1.render('Press to start', True, (0,0,0))
font2= pygame.font.SysFont(pygame.font.get_default_font(), 200)
title= font2.render('Space Invaders',True,(160,32,240))
back=(255,255,255)
start_time=pygame.time.get_ticks()

startframe=pygame.display.set_mode((w,h))
frame= pygame.display.set_mode((w,h))
surface2=pygame.Surface((50,100))
button=pygame.Surface((1080,130))
pygame.display.set_caption("ep")

#firstelem=pygame.image.load("Memoria interna/DCIM/Camera/IMG_20220802_085425.jpg")

class gameThread(threading.Thread):
	def __init__(self,bullet):
		self.ind=-1
		self.flag=True
		threading.Thread.__init__(self)
		self.obj=bullet
	def run(self):
		clk=pygame.time.Clock()
		bullets.append(self.obj)
		#while self.flag:
			#clk.tick(fps+2)
		#	self.obj.coory-=4
	#		frame.blit(self.obj.sur,(self.obj.coorx,self.obj.coory))''
					
			
			
		#	pygame.display.update(p
			#pygame.display.flip()


class emptyship:
	def __init__(self,x,y,dimx,dimy):
		self.type=False
		self.currentx=x
		self.currenty=y
		self.sur=pygame.Surface((dimx,dimy))
		self.hitbox=pygame.Rect(x,y,dimx,dimy)
class ship:
	def __init__(self,x,y,dimx,dimy):
		self.type=True
		self.currentx=x
		self.currenty=y
		self.sur=pygame.Surface((dimx,dimy))
		self.hitbox=pygame.Rect(x,y,dimx,dimy)
		
class projectile:
			def __init__(self,x,y,dimx,dimy):
				self.coorx=x
				self.coory=y
				self.sur=pygame.Surface((dimx,dimy))
				self.sur.fill((0,0,0))
				self.hitbox=pygame.Rect(x,y,dimx,dimy)
				#self.hitbox=self.sur.get_rect()
				
			
			

def fleetmaker(numb):
	r=65
	y=50
	
	for x in range(numb):
		
		globals()[f"variable1{x}"]=ship(r,y,50,50)
#		globals()[f"variable1{x}"].sur.fill((0,0,0))
		fleet.append(globals()[f"variable1{x}"])
		r+=100
		if r>=1000:
			r=65
			y+=100
		
def starting_screen():
	frame.blit(start_text,(300,1000))
	frame.blut(title,(300,100))
	
	
	
	
	
	
	
	
	
	
def color(player,fleet,it,moved,direction,mouse):
	for x in fleet:
		if x.type:
			for y in bullets:
				if x.hitbox.colliderect(y.hitbox):
					x.sur.fill(back)
					emp=emptyship(0,0,0,0)
					fleet.insert(fleet.index(x),emp)
					fleet.remove(x)
				
					#not really destroying, just changing color for index porpuses TO FIX
					bullets.remove(y)
		else:
			pass
	
	
	
	eo=False
	#button.fill((0,0,0))
	frame.fill((255,255,255))
	surface2.fill((0,0,0))
	frame.blit(button,(0,2050))
	button.blit(img,(455,30))
	 
	frame.blit(surface2,(mouse[0],1900))
	
	for y in bullets:
		y.coory-=5
		y.hitbox.y-=5
		frame.blit(y.sur,(y.coorx,y.coory))
	if it==0:
		fleetmaker(40)
		for x in range(len(fleet)):
			frame.blit(fleet[x].sur,(fleet[x].currentx,fleet[x].currenty))
		
	else:
		
		if it%50==0:
			right=True
		else:
			right=False
		for x in range(len(fleet)):
			if it%3==0:
				fleet[x].currenty+=vel
				fleet[x].hitbox.y+=vel
					
			if x<=9 or (30>x>=20):
				if right:
					if direction:
						if moved%2==0:
							fleet[x].currentx+=dist
							fleet[x].hitbox.x+=dist
						else:
							fleet[x].currentx-=dist
							fleet[x].hitbox.x-=dist
					else:
						if moved%2==0:
							fleet[x].currentx-=dist
							fleet[x].hitbox.x-=dist
						else:
							fleet[x].currentx+=dist
							fleet[x].hitbox.x+=dist
			else:
					if right:
						if direction:
							if moved%2==0:
								fleet[x].currentx-=dist
								fleet[x].hitbox.x-=dist
							else:
								fleet[x].currentx+=dist
								fleet[x].hitbox.x+=dist
						else:
							if moved%2==0:
								fleet[x].currentx+=dist
								fleet[x].hitbox.x+=dist
							else:
								fleet[x].currentx-=dist
								fleet[x].hitbox.x-=dist
					
			frame.blit(fleet[x].sur,(fleet[x].currentx,fleet[x].currenty))
		
	pygame.display.flip()
	pygame.display.update()
	
def main():
 count=0
 c=0
 it=-1
 moved=0
 direction=True
 first=True
 player= pygame.Rect(50,1900,50,100)
 clock=pygame.time.Clock()
 run=True
 mouse_pos=(500,1900)
 
 #while True:
 	#pygame.init()
 	#clock.tick(fps)
 	#startframe.fill(back)
 #	startframe.blit(surface2,(300,40))
 	#for event in pygame.event.get():
 	#	if event.type==pygame.QUIT:
 		#	break
 		#if event.type==MOUSEBUTTONDOWN:
 		#	startframe.fill((255,4,30))
 			
 		
 		
 
 while run :
 	clock.tick(fps)
	 count+=1
	 pygame.init()
	 it+=1
 	
 	color(player, fleet, it, moved,direction,mouse_pos)
 	moved+=1
 	if it%50==0:
 		moved+=1
 	for event in pygame.event.get():	
	 		if event.type==pygame.QUIT:
	 			run= False
	 		if event.type==MOUSEBUTTONDOWN:
	 			c+=1
	 			mouse_pos=pygame.mouse.get_pos()
	 			if mouse_pos[1]>2000 and c>=1:
	 				t=gameThread(projectile(mouse_pos[0]+20,1900,8,30))								     
 					t.start()
 			else:
 				pass
 				
 #	if it%100
 	#	direction=False
 #	elif it%200==0:
 	#	direction=True
		 
 		
 pygame.quit()
 
 
main()
 
 