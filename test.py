#This code is used to print my name in three lines
import random
string = 'Tanjim\r\nMinhaz\r\nKoushikk'

formatted_string_list = string.split('\r\n')
list_with_index = list(enumerate(formatted_string_list))
winner = random.choice(list_with_index)
print(winner[1])
