# Dictionary Key Sort

my_direct={'m':2,'s':1,'p':7}
sorted_dire={key:my_direct[key] for key in sorted(my_direct,reverse=True)}

print(sorted_dire)
