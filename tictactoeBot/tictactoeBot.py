import random as rand

class Game:
	def __init__(self,p1,p2,n):
		self.p1=p1
		self.p2=p2
		self.it=n
		self.xStats=[]
		self.oStats=[]
		return
	def shuffle(self):
		r=rand.randint(0,1)
		if r==0:
			self.p1,self.p2=self.p2,self.p1
		else:
			pass
		return
		
	def run(self):
		for x in range(self.it):
			self.bd=board()
			self.shuffle()
			#print(self.p1.tok)
			d=0
			while True:
				bdState=self.bd.draw()
				#print(bdState)
				move=self.p1.think(self.bd.pieces)
				move=move.split(" ")
				self.bd.makeMove(move[0],int(move[1]))
				state=self.bd.gameStatus()
				if state[0]:
					#print(bd.draw())
					if state[1]=="win":
						#print(f"{state[2]} won")
						if state[2]=="x":
							self.xStats.append(1)
						else:
							self.oStats.append(1)
					else:
						d+=1
					break
			
				move2=self.p2.think(self.bd.pieces)
				move2=move2.split(" ")
				self.bd.makeMove(move2[0],int(move2[1]))
			
				state=self.bd.gameStatus()
				if state[0]:
					#print(bd.draw())
					if state[1]=="win":
						#print(f"{state[2]} won")
						if state[2]=="x":
							self.xStats.append(1)
						else:
							self.oStats.append(1)
					else:
						d+=1
						
					break
		return 
		
	def Stats(self):
		s= ["x", len(self.xStats)]
		s2=["o",len(self.oStats)]
		s3= self.it-( len(self.xStats)+len(self.oStats))
		
		
		return s, s2, s3






class bot:
	
	def __init__(self, symbol,engine="v1"):
		self.tok=symbol
		if engine=="v1":
			self.engine=self.v1
		else:
			self.engine=self.v0
		return
	def think(self,board):
		move="0 0"
		#spaces=[1,3,6,8,11,13]
		possible=[]
		mine=[]
		opponent=[]
		b=list(board)
		c=0
		ind=-1
		while(c<len(b)):
			current=b[c]
			if current==" " or current=="x" or current=="o":
				ind+=1
				if current==" ":
					possible.append(ind)
				elif current==self.tok:
					mine.append(ind)
				elif current!=" " and current!= self.tok:
					opponent.append(ind)
			c+=1
		#print(possible)
		#print(mine)
		#print(opponent)
		lists=[possible,mine,opponent]
		if len(possible)>0:
			ix=self.engine(lists)
			#print(ix)
			
			move=f"{self.tok} {ix}"
		
				
		return move
		
	def v1(self,lists):
			central=[3,4,5]
			diagonal1=[0,4,9]
			diagonal2=[2,4,6]
			#lists[0].sort()
			ix=rand.randint(0,len(lists[0])-1)
			ix=lists[0][ix]
			mine=lists[1]
			opponent=lists[2]
			ranked=[]
			
			
			for i,j in enumerate(lists[0]):
				eval=0
				diagonal=getDiagonal(j)
				col=getColumn(j)
				
				if j in central:
					eval+=0.7
				if j-1 in mine or j+1 in mine:
					eval+=1
				if j-1 in mine and j+1 in mine:
					eval+=4
				if j-1 in opponent or j+1 in opponent:
					eval+=0.5
				if j-1 in opponent and j+1 in opponent:
					eval+=3
				if diagonal!= False:
					if diagonal[0] in mine or diagonal[1] in mine:
						eval+=1
					if diagonal[0] in mine and diagonal[1] in mine:
						eval+=4
					if diagonal[0] in opponent or diagonal[1] in opponent:
						eval+=0.5
					if diagonal[0] in opponent and diagonal[1] in opponent:
						eval+=3	
				if col[0] in mine or col[1] in mine:
						eval+=1
				if col[0] in mine and col[1] in mine:
					eval+=4
				if col[0] in opponent or col[1] in opponent:
					eval+=0.5
				if col[0] in opponent and col[1] in opponent:
					eval+=3
				
				
					
				ranked.append([j,eval])
			
					
			#ix=int(len(possible)/2)
			ranked=sorted(ranked, key= lambda x : x[1],reverse=True)
			#print(ranked)
			ix=ranked[0][0]
			
			
			
			return ix
	def v0(self, lists):
		ix=rand.randint(0,len(lists[0])-1)
		ix=lists[0][ix]
		
		return ix

def getDiagonal(position):
    l1=[0, 4, 8]
    l2=[2, 4, 6]
    # Top-left to bottom-right diagonal
    if position in l1:
        l1.remove(position)
        return l1
    # Top-right to bottom-left diagonal
    elif position in l2 :
        l2.remove(position)
        return l2
    else:
        return False # Position is not on a diagonal
def getColumn(position):
	c1=[0,3,6]
	c2=[1,4,7]
	c3=[2,5,8]
	if position in c1:
		c1.remove(position)
		return c1
	elif position in c2:
		c2.remove(position)
		return c2
	else:
		c3.remove(position)
		return c3




class board:
	pieces=" | | _ | | _ | | "
	def __init__(self):
		return
	def draw(self):
		self.board=""
		p=list(self.pieces)
		for x,px in enumerate(p):
			if px !="_" and px!="|":
				self.board+=f"{px}"
			elif px=="|":
				self.board+="|"
			else:
				self.board+="\n"
				self.board+="-----\n"
		return f"{self.board}\n"
		
	def makeMove(self, tok,coor):
		if tok=="0":
			return
		s=""
		c=0
		ind=-1
		while(c<len(self.pieces)):
			current=self.pieces[c]
			if current==" " or current=="x" or current=="o":
				ind+=1
				if ind==coor and current==" ":
					s+=tok
				else:
					s+=current
			else:
				s+=current
			c+=1
		self.pieces=s
		
		return
		
	def isWinning(self):
		val=False
		winningPos=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
		x,o=self.positions(self.pieces)
		for elem in winningPos:
			win=""
			if elem[0] in x and elem[1] in x and elem[2] in x:
				val=True
				win="x"
				return val, win
			elif elem[0] in o and elem[1] in o and elem[2] in o:
				val=True
				win="o"
				return val, win		
		#print(x)
		#print(o)
		return val, win
	def positions(self,s):
		x=[]
		o=[]
		c=0
		ind=-1
		b=list(s)
		while(c<len(s)):
			current=s[c]
			if current==" " or current=="x" or current=="o":
				ind+=1
				if current=="x":
					x.append(ind)
				elif current=="o":
					o.append(ind)
			c+=1
		return x,o
		
	def isDraw(self):
		winningPos=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
		x,o = self.positions(self.pieces)
			
		if len(x)>=4 and len (o)>=4:
			if len(x)==4 and len(o)==4:
				for elem in winningPos:
					if elem[0] in x and elem[1] in x and elem[2] not in o:
						return False
					elif elem[1] in x and elem[2] in x and elem[0] not in o:
						return False
					elif elem[0] in x and elem[2] in x and elem[1] not in o:
						return False
					elif elem[0] in o and elem[1] in o and elem[2] not in x:
						return False
					elif elem[1] in o and elem[2] in o and elem[0] not in x:
						return False
					elif elem[0] in o and elem[2] in o and elem[1] not in x:
						return False
					
			return True
		
		return False
		
	def gameStatus(self):
		w=self.isWinning()
		d=self.isDraw()
		if w[0]:
			return True, 'win', w[1]
		elif d:
			return True, 'draw'
		else:
			return False,""
		
		
def main():
	last=""
	#bd=board()
	#print(bd.draw())
	b1=bot("o", "v0")
	b2=bot("x")
	game=Game(b1,b2,1000)
	game.run()
	g=game.Stats()
	print(f"x won {g[0][1]} times\no won {g[1][1]} times\nwith {g[2]} draws")
	
		
		
		
	
	
	
main()