my_dict = {
    'tuple': (7, None, 'cat', False, 1.41),
    'list': [3, None, 'cow', False, 2.42],
    'dict': {'one': 'myvalue', 'two': 'value2', 'three': 'value3', 'four': False, 'five': [1, 5, 8]},
    'set': {1, None, 'dog', False, 3.43}
}

print("Последний элемент tuple:", my_dict['tuple'][-1])

my_dict['list'].append("new_element")
del my_dict['list'][1]

my_dict['dict'][('i am a tuple',)] = "hello"
my_dict['dict'].pop('two')

my_dict['set'].add("new_value")
my_dict['set'].discard(None)

print(my_dict)
