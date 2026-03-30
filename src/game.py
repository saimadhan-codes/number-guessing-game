import random
num = random.randint(1,100)
count = 0 #initial

while True : #loop condition
	user = int(input("guess a number between 1 to 100   :"))
	count += 1
	difference = abs(num-user)
	if num == user :
		print(f"you guessed the number correctly and the number is {num}")
		break    #exit from the lool
		
	elif difference >= 50 : #difference blw them
		if num > user :
			print("guess is too low!, try again!(high)")
		else :
			print("guess is too high!,try again !(low)")
	else :
		if num > user and difference < 50 :
			print("guess is low and close!, try try try !(high)")
		elif user > num and difference < 50 :
			print("guess is high and close!. try try try !(low)")

# count difference and awarding score to the user			
if count <= 5 : print("cheers! your score is 100")
elif count > 5 and count <= 10 :
	print("great! your score is 50")
elif count > 10 and count <= 15 :
	print("sweet! your score is 25")
elif count > 15 and count <= 20 :
	print("ooh! your score is 10")
elif count > 20 :
	print("oops! your score is 0 !")
else :
	print("program executed successfully !")
print(f"your no of attempts is {count}")
print("thank you dear user ! try when you are free enough !")
