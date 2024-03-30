from turtle import*
import colorsys
h=0.7
speed(0)
bgcolor('black')
pensize(2)
for i in range(180):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.004
    fd(i)
    rt(20)
    circle(190-i,80)
    lt(80)
    circle(190-i,80)
    for j in range(2):
        rt(40)
        lt(20)
    rt(120)
done()