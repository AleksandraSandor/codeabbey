from pyx import *
c=canvas.canvas()
#p=path.path(path.moveto(0,0),path.lineto(1,1))
#c=canvas.canvas()
#c.stroke(p)
triangle1=path.path(path.moveto(0,0),path.lineto(1,0),path.lineto(0.5,0.5),path.closepath())
c.stroke(triangle1,[deco.filled([color.rgb.green])])
triangle2=path.path(path.moveto(-0.25,-0.5),path.lineto(1.25,-0.5),path.lineto(0.5,0),path.closepath())
c.stroke(triangle2,[deco.filled([color.rgb.red])])
triangle3=path.path(path.moveto(-0.55,-1),path.lineto(1.5,-1),path.lineto(0.5,-0.5),path.closepath())
c.stroke(triangle3,[deco.filled([color.rgb.blue])])
c.writePDFfile("pyx4")
#circle=path.circle(0,0,1)
#line1=path.line(-1.5,1,1.5,-1)
#line2=path.line(2,1,-2,-1)
#c.stroke(circle,[style.linewidth.Thick])
#c.stroke(line1,[style.linewidth.Thick])
#c.stroke(line2,[style.linewidth.Thick])
#c.writeEPSfile("radii")
#c.writePDFfile("radii")
