# Value Sort in Dictionary
my_dict={'apple':5,'banana':7,'cerry':2}

my_result=dict(sorted(my_dict.items(), key=lambda item:item[1]))

print(my_result)
