#write a programm to generate game rock paper siecer
import random
d={1:'r',2:'p',3:'s'}
c=d[random.randint(1,3)]
while(1):
	p=input("enter'r','p','s':")
	print("computer",c)
	if(c==d):
		print("tie")
	elif((c=='r'and p=='s') or (c=='p'and p=='r') or (c=='s'and p=='p')):
		print("computer wins..")
	else:
		print("the player won.")


enter'r','p','s':r
computer s
the player won.
enter'r','p','s':r
computer s
the player won.
enter'r','p','s':r
computer s
the player won.
enter'r','p','s':r
computer s
the player won.
enter'r','p','s':r
computer s
the player won.
enter'r','p','s':r
computer s
the player won.
enter'r','p','s':r
computer s
the player won.
enter'r','p','s':r
computer s
the player won.
enter'r','p','s':r
computer s
the player won.
enter'r','p','s':rr
computer s
the player won.
enter'r','p','s':r
computer s
the player won.
enter'r','p','s':
computer s
the player won.
enter'r','p','s':r
computer s
the player won.
enter'r','p','s':s
computer s
the player won.
enter'r','p','s':r
computer s
the player won.
enter'r','p','s':p
computer s
computer wins..
enter'r','p','s':s   
computer s
the player won.
enter'r','p','s':s
computer s
the player won.
enter'r','p','s':s
computer s
the player won.
enter'r','p','s':s
computer s
the player won.
enter'r','p','s':s
