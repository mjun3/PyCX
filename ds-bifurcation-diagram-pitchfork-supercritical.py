from pylab import *

def xeq1(r):
    return r-r

def xeq2(r):
    return sqrt(r)

def xeq3(r):
    return -sqrt(r)

domain1 = linspace(-10, 0)
domain2 = linspace(0, 10)
plot(domain1, xeq1(domain1), 'b-', linewidth = 3)
plot(domain2, xeq1(domain2), 'r--', linewidth = 3)
plot(domain2, xeq2(domain2), 'b-', linewidth = 3)
plot(domain2, xeq3(domain2), 'b-', linewidth = 3)
plot([0], [0], 'go')
axis([-10, 10, -5, 5])
xlabel('r')
ylabel('x_eq')

show()
