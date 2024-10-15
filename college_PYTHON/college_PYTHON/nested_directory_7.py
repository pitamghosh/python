# Nested Dictionary Access

my_dict = {
    'person': {
        'name': 'RAj',
        'age': 30,
        'address': {
            'city': 'Kolkata',
            'zipcode': '700150'
        }
    }
}
# Accessing the name of the person
name = my_dict['person']['name']
print(name)  

# Accessing the city
city = my_dict['person']['address']['city']
print(city) 

