import random as r
import pygame as p
import math as m

y_axis = []
x_axis = []

#out_array = []

x = 0

time = 0

x_screen = 1800

y_screen = 1000

x_interval = 50

amount = 100

number = 1

t = True

top = 300

bottom = 100

line_len = 2

num = 0

y_new = []

y_new2 = []

final_y = []

final_y2 = []


while ((x_interval * amount) > x_screen):
    amount -= 1
    t = False
    #print("hi")


while t:
    if ((x_interval * amount) - x_interval < x_screen):
        amount+=1
    if ((x_interval * amount) > x_screen):
        t = False
        #print("hi2")
    

for i in range(amount):
    y = r.randint(top,y_screen-bottom)

    y_axis.append(y)
    x_axis.append(x)
    x += int(x_interval)


for i in range(amount-2):
    y_new.append(int((y_axis[num] + y_axis[1+num] + y_axis[2+num])/3))
    num+=1
    #print( "                                                     ")

    #print(y_new,amount)
    

y_new.append(int((y_axis[len(y_axis)-2]+y_axis[len(y_axis)-1])/2))
#print(y_new,amount)

y_new.append(int(y_axis[len(y_axis)-1]))
#print(len(y_new),len(y_axis))

num = 0
# gets the middle average of each line, not ezact because of floats but good for know? 
for i in range(amount-1):
    y_new2.append(int((y_axis[num] + y_axis[1+num])/2))
    print(y_new2)
    num +=1

y_new2.append(y_axis[num])
print(len(y_new2))
print(amount)

num = 0

# averages both middle y and average y 
for i in range(amount):
    final_y.append(int((y_new[num] + y_new2[num]+y_axis[num])/3))
    num +=1

num = 0
for i in range(amount):
    final_y2.append(int((y_new2[num]+y_new2[num]+y_new[num] + y_new2[num]+y_new[num])/5))
    num +=1

p.init()

screen = p.display.set_mode([x_screen, y_screen])

running = True
rects = []
rects2 = []

screen.fill((205,205,205))
while running:

    for event in p.event.get():

        if event.type == p.QUIT:

            running = False

    
    
    while(time < amount):
        #p.draw.rect(screen, (0,0,255), (x_axis[time],0,x_interval,y_axis[time]))
        rects.append((x_axis[time],y_axis[time],x_interval, y_screen-y_axis[time]))

        #p.draw.rect(screen, (200,0,255), (rects[time] ))
        #Pure random (multiple lines) black
        p.draw.circle(screen, (0, 0, 0), ( x_axis[time], y_axis[time]), 5)
        p.draw.line(screen,(0,0,0),(x_axis[time],y_axis[time]),(x_axis[time+number],y_axis[time+number]),line_len)

        #Avg of 3 points (triangle) green
        #p.draw.circle(screen, (0, 255, 0), ( x_axis[time], y_new[time]), 5)
        #p.draw.line(screen,(0,255,0),(x_axis[time],y_new[time]),(x_axis[time+number],y_new[time+number]),line_len+1)

        #avg of 2 points (line) red
        #p.draw.circle(screen, (255, 0, 0), ( x_axis[time], y_new2[time]), 5)
        #p.draw.line(screen,(255,0,0),(x_axis[time],y_new2[time]),(x_axis[time+number],y_new2[time+number]),line_len+1)

        # avg of all 3 list blue
        p.draw.circle(screen, (0, 0, 255), ( x_axis[time], final_y[time]), 5)
        p.draw.line(screen,(0,0,255),(x_axis[time],final_y[time]),(x_axis[time+number],final_y[time+number]),line_len+1)

        # avg of 
        #rects2.append((x_axis[time],final_y[time],x_interval, y_screen-final_y[time]))
       # p.draw.rect(screen, (20,0,25), (rects2[time] ))


        p.draw.circle(screen, (200, 0, 255), ( x_axis[time], final_y2[time]), 5)
        p.draw.line(screen,(200,0,255),(x_axis[time],final_y2[time]),(x_axis[time+number],final_y2[time+number]),line_len+1)

        time += 1
        #print(time)

        if time > len(x_axis)-2:
            number = 0
            #print("X AXIS VALUE: ")
            #print(x_axis[len(x_axis)-1])

            #p.draw.circle(screen, (0, 0, 255), (x_screen, y_axis[len(y_axis)-1]), 5)

            #p.draw.line(screen,(255,0,77), ((x_axis[len(x_axis)-1]), (y_axis[len(y_axis)-1])), (x_screen, y_axis[len(y_axis)-1]),line_len)
            

            p.draw.circle(screen, (200, 0, 255), (x_screen, final_y2[len(final_y2)-1]), 5)

            p.draw.line(screen,(200, 0, 255), ((x_axis[len(x_axis)-1]), (final_y2[len(final_y2)-1])), (x_screen, final_y2[len(final_y2)-1]),line_len)

        #print(rects)
        p.display.update()

p.quit()
