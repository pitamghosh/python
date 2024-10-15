nested_dict = {
    'person1': {
        'name': 'Raj',
        'age': 30,
        'address': {
            'city': 'New York',
            'zipcode': '10001'
        }
    },
    'person2': {
        'name': 'Pitam',
        'age': 25,
        'address': {
            'city': 'Los Angeles',
            'zipcode': '90001'
        }
    }
}


person1_name = nested_dict['person1']['name']
print(person1_name) 


person2_city = nested_dict['person2']['address']['city']
print(person2_city) 
 

