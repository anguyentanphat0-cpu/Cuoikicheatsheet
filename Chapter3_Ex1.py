sh = input('Enter Hours: ')
sr = input('Enter Rate: ')
try:
    h = float(sh)
    r = float(sr)
except:
    print('Error, please enter numeric input')
    quit() 
standard_hours = 40
if h > standard_hours:
    standard_pay = standard_hours * r
    overtime_hours = h - standard_hours
    overtime_rate = r * 1.5
    overtime_pay = overtime_hours * overtime_rate
    total_pay = standard_pay + overtime_pay
else:
    total_pay = h * r
print('Pay:', total_pay)