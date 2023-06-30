#working on BMI calculator(BODY MASS INDEX)
height=float(input("enter height in metres "))
weight=int(input("enter the weight  "))
#according to body mass index if bmi is between 18.5 to 24.5 then the person is healthy
#based on this terminology we'll determine the health status of a person by entering his/her weight
bodymassindex=(weight/(height**2))       #formula for bodymassindex
if bodymassindex<18.5 and bodymassindex<24.5:
    print("person is unhealthy with a body mass index",bodymassindex)
elif bodymassindex>18.5 and bodymassindex<24.5:
    print("person is healthy with a bmi",bodymassindex)
elif bodymassindex>18.5 and bodymassindex>24.5:
    print("overweight with BMI",bodymassindex)
else:
    print("obesity")
    