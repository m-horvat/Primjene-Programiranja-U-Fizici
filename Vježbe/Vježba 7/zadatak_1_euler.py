import projectile as proj

x0 = 0
y0 = 0

theta = 30
v0 = 5

ro = 2.34
A = 0.015
C = 1.05

m = 2
dt = 0.00001

p1 = proj.Projectile(x0,y0,m,v0,theta,ro,A,C,dt)
p1.calculate(dt,'euler')