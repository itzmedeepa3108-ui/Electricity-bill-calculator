Connection_type=input()
units_consumed=int(input())
if Connection_type == "Non Commercial Connection":
    if units_consumed<=200:
        amount=0
        bill=0
    elif units_consumed<=500:
        amount=4
        bill=(units_consumed-200)*amount
    elif units_consumed<=2000:
        amount=8
        bill=units_consumed*amount
    else:
        amount=10
        bill=units_consumed*amount
else:
    if units_consumed<=500:
        amount=6
    elif units_consumed<=1000:
        amount=9
    elif units_consumed<=5000:
        amount=12
    else:
        amount=15

    bill=units_consumed*amount  

print("total_bill:₹",bill)
        
