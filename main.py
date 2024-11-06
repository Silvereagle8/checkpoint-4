from decimal import Decimal
import math

list_variable = ['element1', 'element2', 'element3']
tuple_variable = ('element1', 'element2', 'element3')
float_variable = 10.45
integer_variable = 10
decimal_variable = Decimal(10.45)
dictionary_variable = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
}

rounded_up_float = math.ceil(float_variable)
square_root_float = math.sqrt(float_variable)

first_dictionary_element = list(dictionary_variable.items())[0]
# or if we just want the value   list(dictionary_variable.values())[0]
# or   first_dictionary_element = dictionary_variable['key1']

second_tuple_element = tuple_variable[1]

list_variable.append('new_element') 
list_variable[0] = ('replaced_element')
list_variable.sort()

tuple_variable += ('new_element',)