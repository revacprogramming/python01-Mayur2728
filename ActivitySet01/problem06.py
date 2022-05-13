def computepay(h, r):
    pay=h*r
    return pay

hrs = input("Enter Hours:")
h=float(hrs)
rate = input("Enter rate:")
r=float(rate)
if h<=40:
    p=computepay(h,r)
else:
    p=computepay(40,r)
    p=p+computepay((h-40),(1.5*r))
print("Pay", p)