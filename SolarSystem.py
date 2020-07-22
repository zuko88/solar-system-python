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
Draw("yellow", "orange", 120, -400)

# Mercury
Draw("gray", "gray", 10, -350)

# Venus
Draw("red", "red", 20, -250)

# Earth
Draw("green", "blue", 30, -150)

# Mars
Draw("orange", "orange", 25, -50)

#Jupiter
Draw("gold", "gold", 70, 250)

# Saturn
#Draw("yellow", "yellow", 65, 400)
turtle.mainloop()