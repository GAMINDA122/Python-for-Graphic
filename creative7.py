from turtle import*
import colorsys
tracer(2)
bgcolor('black')
pensize(1)
h=0.2


for i in range(700):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.004
    fd(i)
    rt(40)
    fd(100)
    rt(120)

done()