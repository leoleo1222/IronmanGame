def setup():
    global xPos , yPos, xDir, yDir, ironman, track, life, dx, dy
    global shield, shieldX, shieldY, shieldW, shieldH, bullet
    global tower, shield_life
    global y_change, gravity
    shield = loadImage("shield.png")
    ironman = loadImage("ironman.png")
    bullet = loadImage("bullet.png")
    tower = loadImage("Avengers_Tower.png")
    y_change = 0
    gravity = 0
    xPos = 200
    yPos = 300
    dx = 10
    dy = 10
    xDir= 0
    yDir = 0
    life = 3
    shield_life = 3
    shieldW = 100
    shieldH = 100
    shieldX = random(0, width - shieldW)
    shieldY = random(0, height/2 - shieldH)
    size(1000,562)




def draw():
    global xPos, yPos, xDir, ironman, yDir, dx, dy
    global shieldX, shieldY, shieldW, shieldH, life, bullet, bulletX, bulletY
    global tower, shield_life
    if shield_life == 0:
        textSize(100)
        fill(250, 0, 0)
        text("You Win", 200, 300)
    elif life == 0:
        textSize(100)
        fill(250, 0, 0)
        text("You Lose", 200, 300)
    else:
        background(tower)
        stroke(255,250,250)
        strokeWeight(20)
        line(0,400,1000,400)
        image(ironman, xPos, yPos, 100, 100)
        image(shield, shieldX, shieldY, shieldW, shieldH)
        shieldX = shieldX + dx
        shieldY = shieldY + dy
        if shieldX < 0 or shieldX > width - shieldW:
            dx = -dx
        if shieldY < 0 or shieldY > (height - 140) - shieldH:
            dy = -dy
        if shieldX + shieldW >= xPos and shieldX <= xPos + 50 and shieldY + shieldH >= yPos and shieldY <= yPos + 50:
            life = life - 1
            shieldX = int(random(0, width - shieldW)) 
            shieldY = int(random(0 , height/2 - shieldH))
        xPos += xDir
        yPos += yDir
        if (key == "E" or key == "e"):
            image(bullet, xPos + 80, yPos, 100, 100)
            bulletX = xPos + 80
            bulletY = yPos
            if shieldX + shieldW >= bulletX and shieldX <= bulletX + 50 and shieldY + shieldH >= bulletY and shieldY <= bulletY + 50:
                shield_life = shield_life - 1
        if (key == "D" or key == "d"):
            xDir = 5
        if (key == "a" or key == "A"):
            xDir = -5 
        if (key == "w" or key == "W"):
            yDir = -5
        if (key == "s" or key == "S"):
            yDir = 5    
        if(xPos> 900):
            xDir = -5
        if(xPos < 10):
            xDir = 5
        if(yPos < 10):
            yDir = 5
        if(yPos > 300):
            yDir = -5    
        textSize(50)
        fill(255,250,250)
        text("Your Life:" + str(life), 28, 100)
        text("Shield Life:" + str(shield_life), 628, 100)
        text("Restart [r]", 28, 460)
        text("Bullet [e]", 328, 460)
        text("UP [w]", 28, 520)
        text("DOWN [s]", 228, 520)
        text("LEFT [a]", 498 ,520)
        text("RIGHT [d]", 728, 520)
                
def keyPressed():
    if (key == "R" or key == "r"):
        setup()
    
    

            

                
                                              
