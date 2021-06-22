#environement
#print => python <name>.pow

#intro
print("\n ***** Welcome to my first job founder quiz in Python! *****\n")
playing = input("Do you want to play ?") # space in ? " allows visable anwser

if playing != "yes":
  print("I am sorry. It is painfull reading this. I hope you come back later\n")
  quit()
print("Ok! Let's play the Job Recrutement's Game \n")
score = 0

#Question 1
answer = input ("What is my the name? ").lower()
if (answer == "mario carvalho" or "mario"):
  print('Correct, next question!\n ')
  score += 1
elif (answer == "mario carvallo" or "carvalho"):
  print ("really?...almost there!\n")
  score +=0.5
else:
  print("Incorrect..nice try!\n")

#question2
answer = input ("How many languages I speak ? ").lower()
if (answer == "4"):
  print("Correct! You really paid atention. \n")
  score += 1
elif (answer == "3" ):
  print ("yes, you can say that\n")
  score +=1
else:
  print("Nop..sorry\n")

#Question 3
answer = input ("What is my nationality ?\n ").lower()
if (answer == "portugese" or "Portugese"):
  print("YES I AM!..You scored +1!\n")
  score += 1
else:
  print("You are not intirelly incorrect..but, no\n")

#Question 4
answer = input ("How many programming languages I can code ? ").lower()
if (answer == "4"):
  print("You are right!\n")
  score += 1
elif (answer == "3" ):
  print ("Oh yeah, nicelly done. But I usually say almost 4!\n")
else:
  print("Really?! Are you sure?.. :/ \n")

#Question 5
answer = input ("Do I know about React (Native&Expo), Express.js and Node.js ? ").lower()
if (answer == "yes"):
  print("Yes, You know me!\n")
  score += 1
else:
  print("humm, well.. I am quite sure you aren't correct\n")

#Question 6
answer = input ("Did I already work with Git, GitHub and Bash ? ").lower()
if (answer == "yes"):
  print("In deed! \n")
  score += 1
elif (answer == "no" ):
  print ("Well, can you read again my skills description collumn, please ?\n")
else:
  print("lol\n")

#Question 7
answer = input ("Am I Prince2 and MBA certification, or only one? in this case, witch one? ").lower()
if (answer == "yes"):
  print("Oh yeah! I AM!\n")
  score += 1
elif (answer == "Prince2" or "MBA"):
  print ("really?...almost there!\n")
else:
  print("whats happened here?!..let's see next question..\n")

#Question 8
answer = input ("What I like most: surf or diving? ").lower()
if (answer == "surf"):
  print("Right, and next time, we will go together !\n")
  score += 1
elif (answer == "diving" ):
  print ("It doesn't appear on my CV..!\n")
else:
  print("ai ai ai caramba\n")

#Question 9
answer = input ("Did I alreafy work with:\na) MySQL, PostMAN and Node.Js\nb) a bit of postgreSQL, and a)\nc) None of above ?\n").lower()
if (answer == "b" or "b)"):
  print ("CORRECT, it is b!\n")
  score += 1
elif (answer == "a" or "a)"):
  print("almost!..it is b\n")
else:
  print("Ups..no..sorry\n")

#Question 10
answer = input ("Last one, do I like manager some projects? yes or no?  ").lower()
if (answer == "yes"):
  print("I can't hide.. You are right!\n")
  score += 1
elif (answer == "no\n" ):
  print ("we must know each other..")
else:
  print("no..not that..\n")

##score
if (score == 10):
  print("All questions are correct. Nice one! As you can see, I do Python prety well, for a beginer, don't I ? ")  
elif  (score == 0):
  print("Sorry, we must get to know each other better. Why not let me assign the job contract and found out what else I can do ? ")
else:
  print("You got " + str(score) + " points on this questions.") #correct questions number  
  print("that means then " + str((score/10) *100) + " % of this answers are correct. Nice job, you are almost thre!\n Another game?")#percentage

quit()

#finished