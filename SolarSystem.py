import turtle

window = turtle.Screen()


#Set background color
turtle.bgcolor("black")



def Draw(color1, color2, radius, xcor):
    # Draw a planet or star
    turtle.penup()
    turtle.goto(xcor, -1 * radius)
    turtle.pendown()
    turtle.color(color1, color2)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.hideturtle()

#  Sun
Draw("yellow", "orange", 120, -600)

# Mercury
Draw("gray", "gray", 10, -430)

# Venus
Draw("red", "red", 20, -330)

# Earth
Draw("green", "blue", 30, -230)

# Mars
Draw("orange", "orange", 25, -130)

#Jupiter
Draw("gold", "gold", 70, 80)

# Saturn
Draw("yellow", "yellow", 60, 230)
turtle.mainloop()

# Uranus
Draw("gray", "gray", 45, 530)

# Neptune
Draw("blue", "blue", 40, 880)