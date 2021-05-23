import webbrowser
print("Your Name?")
name=input()
print("Hello"+name)
print("Lets Calculate your daily calorie_intake and compare with a healthy diet.\n")
print("Provide the required data to calculate your calorie intake.")
print("Todays Date?")
date=input()
print("Gender? in small letter")
gender=input()
print("Breakfast calories_intake?")
breakfast = int(input())
print("Lunch calories_intake?")
lunch = int(input())
print("Dinner calories_intake?")
dinner = int(input())
print("Anytime Snack calories_intake?")
snack = int(input())
total = breakfast + lunch + dinner + snack
print("Your total calorie_intake is :"+ str(total))
print("Recommended daily calorie intakes in the US are around 2,500 for men and 2,000 for women")
if gender=="male":
   if total >2500:
     print("You need to decrease your calorie_intake")
     print("Do you need suggestion to balance your calorie_intake?type yes or no")
     balance=input()
     if balance=="yes":
     
        webbrowser.open("https://www.healthline.com/nutrition/how-many-calories-per-day")
   if total <2500: 
       print("You need to increase your calorie_intake")
       print("Do you need suggestion to balance your calorie_intake?type yes or no")
       balance=input()
       if balance=="yes":
          webbrowser.open("https://www.healthline.com/nutrition/3000-calorie-meal-plan")
   if total == 2500:
       print("You have a perfect calorie_intake")  
if gender=="female":
   if total>2000:
       print("You need to decrease your calorie_intake")
       print("Do you need suggestion to balance your calorie_intake?type yes or no")
       balance=input()
       if balance=="yes":
          webbrowser.open("https://www.healthline.com/nutrition/how-many-calories-per-day")
   if total<2000:
       print("You need to increase your calorie_intake")
       print("Do you need suggestion to balance your calorie_intake?type yes or no")
       balance=input()
       if balance=="yes":
           webbrowser.open("https://www.healthline.com/nutrition/3000-calorie-meal-plan")
   if total==2000:
       print("You have a perfect calorie_intake")  


