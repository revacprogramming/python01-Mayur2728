hrs =  input('enter the number of hours')
rate = input('enter rate per hour')
h = float(hrs)
r = float(rate)
if h<=40:
    pay =h*r
    
else:
    pay = 40*r
    pay = pay+((h-40)*(1.5*r))
    
print(pay)