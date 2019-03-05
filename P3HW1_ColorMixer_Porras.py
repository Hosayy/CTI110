#This Program that prompts the user to enter the names of two primary colors to mix.
#CTI-110
#P3HW1 - Color Mixer
#Jose Porras
#3-5-19

#Get the colors to mix from different choices
color1 = input("Please pick a color to mix with. (red, blue, yellow) :")
color2 = input("Please pick a second color to mix with. (red, blue, yellow) :")

#Get the colors mixed and display the color after mixed
if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
    print("Your result is purple")
elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
    print("Your result is orange")
elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
    print("Your result is green")



