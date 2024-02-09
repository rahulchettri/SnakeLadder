#Snake Ladder Game
import random
game=[
      [25, 26, 27, 28, 29, 30],
      [19, 20, 21, 22, 23, 24], 
      [13, 14, 15, 16, 17, 18], 
      [7, 8, 9, 10, 11, 12], 
      [1, 2, 3, 4, 5, 6]]
      
ladder={3:22,5:8,11:26,20:29}      
snake={27:1,21:9,17:4,19:7}
player1,player2=1,1
gameFinish=False
checkPlayer=1
winner=None
while gameFinish is False:
  curCount=0
  if checkPlayer%2==0:
    #player1 plays
    k=0
    while k!=1:
       toBeIncreased=random.randint(0,6) 
       curCount+=1
       if toBeIncreased+player1<=30:
         player1+=toBeIncreased
         if player1==30:
           winner="Player 1"
           gameFinish=True
           break
         if player1 in ladder:
          player1=ladder[player1]
         elif player1 in snake:
          player1=snake[player1]
         if curCount==3 or toBeIncreased!=6:
            k=1
       else:
         k=1
       #print("player1 Dice Val",toBeIncreased,"Player 1 reached",player1)  
         
         
  else:
    #player2 plays
    k=0
    while k!=1:
       toBeIncreased=random.randint(0,6) 
       if toBeIncreased+player2<=30:
         curCount+=1 
         player2+=toBeIncreased
         if player2==30:
           winner="Player 2"
           gameFinish=True
           break
         if player2 in ladder:
           player2=ladder[player2]
         elif player2 in snake:
            player2=snake[player2]
         if curCount==3 or toBeIncreased!=6:
            k=1
       else:
         k=1
       #print("player2 Dice Val",toBeIncreased, "player 2 reached",player2)    
  checkPlayer+=1
  #print(player1,player2)
print(winner)  
  
  
         
         
  
  
    
    
  
  