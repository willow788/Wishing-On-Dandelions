import turtle

t = turtle.Turtle()
t.hideturtle()

t.screen.bgcolor("black")
t.pensize(2)
t.speed(100)
t.color("green")
t.left(90)
t.backward(100)
t.shape("turtle")

def tree(i):
    if i < 10:
        return
    else:
        t.forward(i)     #move t pointer forward
        t.color("orange") # colour of t is orange
        t.circle(2)       #draw the leaf or flower petal or whatever 
        t.color("brown")  #change the t color to brown for a woody appearance
        t.left(30)        #move the pointer to left by 30 degree
        tree(3 * i/4)     #draw a smaller branch
        t.right(60)       #move right by 60 degree
        tree(3 * i/4)    #draw smaller branch again
        t.left(30)       #back to orginal position
        t.backward(i)    #otherwise you will run away

tree(100)
turtle.done()
