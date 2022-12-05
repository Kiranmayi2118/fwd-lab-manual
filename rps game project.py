import random as rand
choice={1:'rock',2:'paper',3:'scissor',4:'exit'}
temp=0
while(temp==0):
        r=rand.randint(1,3)
        comp=choice[r]
        num=int(input())
        if(num<1 | num>4):
            print('invalid')