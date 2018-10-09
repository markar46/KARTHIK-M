a=['1','2','3','4','5','6','7','8','9']

def printboard():
	print(a[0]+'|'+a[1]+'|'+a[2])
	print("----")
	print(a[3]+'|'+a[4]+'|'+a[5])
	print("----")
	print(a[6]+'|'+a[7]+'|'+a[8])

playeroneturn = True

for i in range(9):
	printboard()
	#player 1 plays
	if playeroneturn:
		printboard()
		p=input("player 1,choose your place:")
		if p in a:
			a[int(p)-1]='X'
			playeroneturn= not playeroneturn
		else:
			p=input("player 2,choose your place:")
			if p in a:
				a[int(p)-1] = 'O'
				playeroneturn = not playeroneturn
			else:
				print("computer's turn:")
				sleep(1)
				random_place()
				playeroneturn= not playeroneturn
			for x in range(0,3):
				y=x*3
				if(a[y]==a[(y+1)] and a[y]==a[(y+2)])
				winner=True
				printboard()
			if(a[x]==a[(x+3)] and a[x]==a[(x+6)])
				winner=True
				printboard()
				if((a[0]==a[4] and a[0==a[8]) or a[2==a[4] and a[2==a[6]) 


