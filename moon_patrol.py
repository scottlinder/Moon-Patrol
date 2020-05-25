import turtle
import random
 
timer = 0
score = 0
ufoX_speed = 4.0
ufoY_speed = 2.0
fight_time = 200
bombs_total = 5
bomb_speed = 5
missile_speed = 10
bomb_drop_rate = 40
bomb_spread = 1
off_screenX = 600
off_screenY = 0
off_screenX2 = -600
off_screenY2 = 0
on_screenX = -300
on_screenY = 200
ground_level = -300
ground_speed = 5
left_border = on_screenX
right_border = on_screenX + 400
top_border = on_screenY + 50
bottom_border = on_screenY - 50
timebarX = 1.0

jumping = False
falling = False

ground = []
holes = []
hills1 = []
hills2 = []
rocks = []
wheels = []
player = []
missiles = []
bombs = []

wn = turtle.Screen()
wn.setup(1000, 700)
wn.bgcolor('black')
wn.tracer(0)

# the stars

for i in range(0, 20):
	x = turtle.Turtle()
	x.color('white')
	x.shape('circle')
	r1 = random.uniform(-0.25, 0.25)
	x.shapesize(r1, r1)
	x.penup()
	rX = random.uniform(-600, 600)
	rY = random.uniform(0, 300)
	x.goto(rX, rY)

# the mountains

for i in range(0, 20):
	x = turtle.Turtle()
	x.color('blue')
	x.shape('triangle')
	x.left(90)
	sizeX = random.randint(20, 30)
	sizeY = random.randint(10, 30)
	x.shapesize(sizeX, sizeY)
	x.penup()
	x.goto(-1000 + (i * 80), ground_level + 150)
	hills2.append(x)

for i in range(0, 20):
	x = turtle.Turtle()
	x.color('darkgreen')
	x.shape('triangle')
	x.left(90)
	sizeX = random.randint(50, 100)
	sizeY = random.randint(15, 25)
	x.shapesize(sizeX, sizeY)
	x.penup()
	x.goto(-1000 + (i * 320), ground_level + 80)
	hills1.append(x)

# the holes

for i in range(0, 3):
	x = turtle.Turtle()
	x.color('darkgreen')
	x.shape('square')
	x.shapesize(2, 4)
	x.penup()
	dist = random.randint(900, 1200)
	x.goto(2000 + (i * dist), ground_level + 40)
	holes.append(x)

# the ufo

ufo = turtle.Turtle()
ufo.color('darkgray')
ufo.shape('circle')
ufo.shapesize(1, 2)
ufo.penup()
ufo.goto(off_screenX, off_screenY)
ufo.live = False

# the decorative pieces for the ufo

piece1 = turtle.Turtle()
piece1.color('black')
piece1.shape('square')
piece1.shapesize(0.1, 2)
piece1.penup()

piece2 = turtle.Turtle()
piece2.color('black')
piece2.shape('circle')
piece2.shapesize(0.5, 0.5)
piece2.penup()

piece3 = turtle.Turtle()
piece3.color('red')
piece3.shape('circle')
piece3.shapesize(0.3, 0.3)
piece3.penup()

# the ufo's bombs

for i in range(0, bombs_total):
	x = turtle.Turtle()
	x.color('darkred')
	x.shape('circle')
	x.size = 1
	x.shapesize(x.size, x.size)
	x.penup()
	x.goto(off_screenX, off_screenY)
	x.fired = False
	x.jitter = random.uniform(-bomb_spread, bomb_spread)
	bombs.append(x)

# the rocks

for i in range(0, 5):
	x = turtle.Turtle()
	x.color('orange')
	x.shape('circle')
	x.shapesize(4, 4)
	x.penup()
	dist = random.randint(900, 1200)
	x.goto(500 + (i * dist), ground_level + 100)
	rocks.append(x)

# the ground

for i in range (0, 100):
	x = turtle.Turtle()
	x.color('red')
	x.shape('square')
	x.shapesize(8, 1.2)
	x.penup()
	r = random.randint(-6, 6)
	x.goto(-800 + (i * 21), ground_level + r)
	ground.append(x)

# the player

box = turtle.Turtle()
box.color('pink')
box.shape('square')
box.shapesize(1, 6)
box.penup()
box.goto(-250, ground_level + 110)
player.append(box)

ball = turtle.Turtle()
ball.color('pink')
ball.shape('circle')
ball.shapesize(2, 2)
ball.penup()
ball.goto(-200, ground_level + 120)
player.append(ball)

tri = turtle.Turtle()
tri.color('pink')
tri.shape('triangle')
tri.left(90)
tri.penup()
tri.goto(-270, ground_level + 120)
player.append(tri)

# the wheels

for i in range(0, 3):
	x = turtle.Turtle()
	x.color('black')
	x.shape('circle')
	x.shapesize(1.5, 1.5)
	x.fired = False
	x.penup()
	x.goto(-200 - (i * 50), ground_level + 100)
	wheels.append(x)
	player.append(x)

# the weapons

for i in range(0, 5):
	x = turtle.Turtle()
	x.color('white')
	x.shape('square')
	x.shapesize(0.5, 0.1)
	x.fired = False
	x.penup()
	x.goto(-600, 0)
	missiles.append(x)

bullet = turtle.Turtle()
bullet.color('white')
bullet.shape('square')
bullet.shapesize(0.3, 1)
bullet.fired = False
bullet.penup()
bullet.goto(0, -600)

# the scoreboard

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(480, 310)
pen.color('white')
pen.write('{}'.format(score), align = 'right', font = ('Courier', 30, 'bold'))

# the instructions

pen2 = turtle.Turtle()
pen2.hideturtle()
pen2.penup()
pen2.goto(-490, 310)
pen2.color('dark gray')
pen2.write('(SPACE)JUMP (F)IRE (Q)UIT', align = 'left', font = ('Courier', 30, 'bold'))

# the time bar

timebar = turtle.Turtle()
timebar.color('darkred')
timebar.shape('square')
timebar.shapesize(1, timebarX)
timebar.penup()
timebar.goto(-500, -320)
ufo.live = False

# the functions

def quit_game():
	print('Program quit successfully.')
	turtle.mainloop()

def jump():
	global jumping
	if jumping == False:
		jumping = True

def fire_weapons():
	for i in missiles:
		if not i.fired:
			i.goto(box.xcor() - 20, box.ycor() + 10)
			i.fired = True
			break

	if not bullet.fired:
		bullet.goto(box.xcor() + 80, box.ycor())
		bullet.fired = True

# the key bindings

turtle.listen()
turtle.onkey(quit_game, 'q')
turtle.onkey(jump, 'space')
turtle.onkey(fire_weapons, 'f')

#############################
# T H E   G A M E   L O O P #
#############################


while True:
	wn.update()

	# Update the timer on each loop. 
	timer = timer + 1
	timebarX = timebarX + 0.05
	timebar.shapesize(1, timebarX)
	if timer > 2000:
		pen2.clear()
		pen2.color('white')
		pen2.write('OUT OF TIME', align = 'left', font = ('Courier', 30, 'bold'))
		turtle.mainloop()


	########################################
	# O B S T I C L E    H A N D E L I N G #
	########################################


	# Move the hills.

	for i in range(0, 20):
		hills1[i].setx(hills1[i].xcor() - 3)
		hills2[i].setx(hills2[i].xcor() - 1)

		if hills1[i].xcor() < -800:
			hills1[i].setx(800)

		if hills2[i].xcor() < -800:
			hills2[i].setx(800)

	# Check the ground pieces.

	for i in ground:

		# Move the ground.

		i.setx(i.xcor() - ground_speed)

		# Reset rock to the other side of the screen.

		if i.xcor() < -1000:
			i.setx(1000)

		# Check if the ground is close to a hole.

		for j in holes:

			# If a ground is near a hole, move the ground down.

			if i.distance(j) < 100:
				i.sety(i.ycor() - 5)

		for j in wheels:
			if i.distance(j) < 100:
				j.sety(i.ycor() + 90)

	# Check the holes.

	for i in holes:

		# Set the hole to move with the ground.

		i.setx(i.xcor() - ground_speed)

		# Check the holes against themselves.

		for j in holes:
			if j.distance(i) < 400 and j != i:
				j.setx(j.xcor() + 1000)

		# Reset rock to the other side of the screen.

		if i.xcor() < -1000:
			i.setx(1000)

		# Check if the player hits a hole.

		if box.distance(i) < 80:
			pen2.clear()
			pen2.color('white')
			pen2.write('GAME OVER', align = 'left', font = ('Courier', 30, 'bold'))
			turtle.mainloop()

	# Check the rocks.

	for i in rocks:

		# Set the rock to move with the ground.

		i.setx(i.xcor() - ground_speed)

		# Check the rocks against themselves.

		for j in rocks:
			if j.distance(i) < 400 and j != i:
				j.setx(j.xcor() + 1000)

		# Reset rock to the other side of the screen.

		if i.xcor() < -1000:
			i.setx(1000)

		# Check the rocks against the holes.

		for j in holes:
			if i.distance(j) < 400:
				i.setx(1000)
				break

		# Check if a bullet hits a rock.

		if bullet.distance(i) < 50:
			r = random.randint(-400, 400)
			i.setx(2000 + r)
			bullet.goto(-600, 0)
			bullet.fired = False

			score = score + 10
			pen.clear()
			pen.write('{}'.format(score), align = 'right', font = ('Courier', 30, 'bold'))

		# Player hits a rock.

		if box.distance(i) < 50:
			pen2.clear()
			pen2.color('white')
			pen2.write('GAME OVER', align = 'left', font = ('Courier', 30, 'bold'))
			os.system("afplay explode.wav&")
			turtle.mainloop()


	#####################################
	#  P L A Y E R   H A N D E L I N G  #
	#####################################


	# Move player left when cursor is on the left side.

	if wn.getcanvas().winfo_pointerx() < 1000:
		for i in player:
			i.setx(i.xcor() - 5)

	# Move player right when cursor is on the right side.
 
	if wn.getcanvas().winfo_pointerx() > 1300:
		for i in player:
			i.setx(i.xcor() + 5)

	# Jumping

	if jumping == True:
		box.sety(box.ycor() + 4)
		ball.sety(ball .ycor() + 4)
		tri.sety(tri .ycor() + 4)
		for i in wheels:
			i.sety(box.ycor() - 10)
		if box.ycor() > ground_level + 200:
			jumping = False    
			falling = True
			
	# Falling

	if falling == True:
		jumping = False  
		for i in player:
			i.sety(i.ycor() - 4)
		if box.ycor() < ground_level + 110:
			falling = False

	# Check all the missiles.

	for i in missiles:

		# If a missile is fired, it moves upward.

		if i.fired == True:
			i.sety(i.ycor() + missile_speed)

		# If missile strikes the ufo, reset the ufo.

		if i.distance(ufo) < 10:
			i.fired = False
			i.goto(off_screenX2, off_screenY2)
			ufo.goto(off_screenX, off_screenY)

			score = score + 100
			pen.clear()
			pen.write('{}'.format(score), align = 'right', font = ('Courier', 30, 'bold'))

		#  If a missile goes off screen, reset it.

		if i.ycor() > 500:
			i.fired = False
			i.goto(off_screenX2, off_screenY2)

	# Move the bullet forward.

	if bullet.fired:
		bullet.setx(bullet.xcor() + 8)

	# Reset missed bullet.

	if bullet.xcor() > (box.xcor() + 500):
		bullet.goto(-600, 0)
		bullet.fired = False


	##############################
	# U F O    H A N D E L I N G #
	##############################


	# ufo drops a bomb periodically.

	if timer % bomb_drop_rate == 0:
		for i in bombs:
			if not i.fired and ufo.live:
				i.goto(ufo.xcor(), ufo.ycor() - 8)
				i.fired = True
				break

	# Move ufo into the scene.

	if timer % fight_time == 0:
		ufo.goto(on_screenX, on_screenY)
		ufo.live = True

	# Remove ufo from the scene.

	if timer % (fight_time * 2) == 0:
		ufo.goto(off_screenX, off_screenY)
		ufo.live = False
		bomb_speed = bomb_speed + 0.1
		ufoX_speed = ufoX_speed + 0.2

	# After awhile, change the color of the ufo.

	if timer % (fight_time * 4) == 0:
		ufo.color('darkred')
		piece3.color('white')

	# if ufo is in the scene 

	if ufo.live:

		# ufo goes toward an x,y coordinate

		ufo.goto(ufo.xcor() + ufoX_speed, ufo.ycor() + ufoY_speed)

		# Use "if" conditions to switch the ufo's direction by multiplying it by -1.

		if ufo.xcor() > right_border:
			ufoX_speed *= -1

		if ufo.xcor() < left_border:
			ufoX_speed *= -1

		if ufo.ycor() > top_border:
			ufoY_speed *= -1

		if ufo.ycor() < bottom_border:
			ufoY_speed *= -1

	# These are ufo decorative pieces. They go whereever the ufo goes.

	piece1.goto(ufo.xcor(), ufo.ycor())
	piece2.goto(ufo.xcor(), ufo.ycor())
	piece3.goto(ufo.xcor(), ufo.ycor())

	# Check all the bombs.

	for i in bombs:

		# Fired bombs go down with a little jitter.

		if i.fired == True:
			i.goto(i.xcor() + i.jitter, i.ycor() - bomb_speed)

		# if the bomb hits the ground, reset it.

		if i.ycor() < ground_level:
			i.goto(off_screenX, off_screenY)
			i.fired = False

		# Check if a bomb hits a missile.

		for j in missiles:
			if i.distance(j) < 30:
				i.goto(off_screenX, off_screenY)
				j.goto(off_screenX2, off_screenY2)
				i.fired = False
				j.fired = False

				score = score + 1
				pen.clear()
				pen.write('{}'.format(score), align = 'right', font = ('Courier', 30, 'bold'))

		# Check if a bomb hits a bullet.

		if i.distance(bullet) < 30:
			i.goto(off_screenX, off_screenY)
			bullet.goto(off_screenX2, off_screenY2)
			i.fired = False
			bullet.fired = False

			score = score + 1
			pen.clear()
			pen.write('{}'.format(score), align = 'right', font = ('Courier', 30, 'bold'))

		# Check if a bomb hits the player.

		if i.distance(box) < 50:
			pen2.clear()
			pen2.color('white')
			pen2.write('GAME OVER', align = 'left', font = ('Courier', 30, 'bold'))
			turtle.mainloop()











































	

			


