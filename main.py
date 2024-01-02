import turtle
import random
screen=turtle.Screen()
screen.addshape("mcQueen.correctPic.png")
screen.addshape("correcPicMater.png")
screen.addshape("DocHudsoncorrectPic.png")
screen.addshape("jacksonCorrectpIc.png")
p1=turtle.Turtle()
PScore = turtle.Turtle()  


t1=turtle.Turtle()
t1.shape("mcQueen.correctPic.png")
t2=turtle.Turtle()
t2.shape("correcPicMater.png")
t3=turtle.Turtle()
t3.shape("DocHudsoncorrectPic.png")
t4=turtle.Turtle()
t4.shape("jacksonCorrectpIc.png")

turtList=[t1, t2, t3, t4]
y = 150
for t in turtList:
  t.speed(0)
  t.lt(90)
  t.penup()
  t.goto(-150,y)
  y -= 100
  t.speed(0)
  

def finishLine():
  p1.speed(0)
  p1.penup()
  p1.goto(200,200)
  p1.seth(270)
  p1.color("red")
  p1.pendown()
  p1.fd(400)

WinsList = [0, 0, 0, 0]


def UpdateScore():
  
  PScore.clear()
  PScore.speed(0)
  for t in turtList:
    PScore.penup()
    PScore.goto(-150, t.ycor()-45)
    PScore.pendown()
    winIndex=turtList.index(t)
    PScore.write(WinsList[winIndex])

def CarsMovingForward():
  for i in range(4):
    racing = True
    numRaces = 3-i
    while racing:
      for x in range(4):
        s = random.randint(0,10)
        Random = random.randint(0, 3)
        n=random.randint(5, 10)
        j=turtList[Random]
        j.speed(s)
        j.goto(j.xcor()+n, j.ycor())
        if j.xcor() >= 200:
          for q in turtList:
            q.speed(0)
            q.goto(-150, q.ycor())
          racing = False
          winIndex=turtList.index(j)
          print("Car #" + str(winIndex + 1) + " won this race! " + str(numRaces) + " more races to go!")
          WinsList[winIndex] += 1
          UpdateScore()

def properInput():
  choice = int(input("Who do you think will win? (choose from cars 1 - 4): "))
  while True:
    if choice > 4:
      print("Invalid! please choose numbers from 1-4")
      choice = int(input("Who do you think will win? (choose from cars 1 - 4): "))
    elif choice < 1:
      print("Invalid! please choose numbers from 1-4")
      choice = int(input("Who do you think will win? (choose from cars 1 - 4): "))
    else:
      return choice
  
def checkScore(choice_car):
  print(WinsList)
  MaxVal = max(WinsList)
  MaxValIndex=WinsList.index(MaxVal)
  if MaxValIndex + 1 == choice_car:
    print("Yes! you chose the correct car!")
  else:
    print("Sorry you chose wrong! car #" + str(MaxValIndex + 1) + " won")
  
  
selection=properInput()
PScore.ht()
p1.ht()
finishLine()
CarsMovingForward()
checkScore(selection)