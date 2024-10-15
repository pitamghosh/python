def calculate(a,b):
    sum_val=a+b
    multiple_val=a*b
    substract_val=a-b
    devide_val=a/b
    return sum_val,multiple_val,substract_val,devide_val
x=int(input("enter any number: "))
y=int(input("enter any number: "))
su,m,s,d=calculate(x,y)
print(f"sum={su},multiple={m},substract={s},devide={d}")