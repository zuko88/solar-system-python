import turtle

window = turtle.Screen()


#Set background color
turtle.bgcolor("black")

SUN = {
    "name": "Sun",
    "edge_color": "yellow",
    "fill_color": "orange",
    "radius" : 120,
    "xcor" : -600
}

MERCURY = {
    "name": "Mercury",
    "edge_color": "gray",
    "fill_color": "gray",
    "radius" : 10,
    "xcor" : -430
}

VENUS = {
    "name": "Venus",
    "edge_color": "red",
    "fill_color": "red",
    "radius" : 20,
    "xcor" : -330
}


planets = [SUN, MERCURY, VENUS]

def Draw(edge_color, fill_color, radius, xcor):
    # Draw a planet or star
    turtle.penup()
    turtle.goto(xcor, -1 * radius)
    turtle.pendown()
    turtle.color(edge_color, fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.hideturtle()

for  planet in planets:
    Draw(planet["edge_color"], planet["fill_color"], planet["radius"], planet['xcor'])

# #  Sun
# Draw("yellow", "orange", 120, -600)
#
# # Mercury
# Draw("gray", "gray", 10, -430)
#
# # Venus
# Draw("red", "red", 20, -330)
#
# # Earth
# Draw("green", "blue", 30, -230)
#
# # Mars
# Draw("orange", "orange", 25, -130)
#
# #Jupiter
# Draw("gold", "gold", 70, 80)
#
# # Saturn
# Draw("yellow", "yellow", 60, 230)
#
#
# # Uranus
# Draw("gray", "gray", 45, 530)
#
# # Neptune
# Draw("blue", "blue", 40, 880)

turtle.mainloop()