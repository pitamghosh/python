# Value Sort in Dictionary

my_dire={'m':2,'p':1,'r':3}
shorted_dire=dict(sorted(my_dire.items(),key=lambda item: item[1]))

print(shorted_dire)