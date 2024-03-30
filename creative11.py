from turtle import*
import colorsys

speed(0)
bgcolor('black')
h=0.8
pensize(2)

for i in range(70):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    for j in range(17):
        fd(0.2*i*j)
        lt(33/0.01)

done()