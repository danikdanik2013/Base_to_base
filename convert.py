#utf - 8 python3. Created by Danyil. 
import math

#import unittest

def convertor(number, to_base, base):
	num10 = to10(number, to_base)
	result_num = from10(num10, base)
	print (result_num, base, to_base)
	return result_num
	    



def to10(number, base):

	number = str(number).lower()
	base = int(base)
	known_digits = '0123456789abcdefghijklmnopqrstuvwxyz'
	value  = { ch:val for val, ch in enumerate(known_digits) if val < base } 
	if number[0] == '-':
		sign = -1
		number = number[1:]
	else:
		sign = 1
	total = 0
	for d in number:
		try:
			total = total * base + value[d]
		except KeyError:
			if d in known_digits:
				raise ValueError("invalid digit '{0}' in base {1}".format(d, base))
			else:
				raise ValueError("value of digit {0} is unknown".format(d))
	number = sign * total
	pass
	return number

def from10(number, to_base):
    converted_string, modstring = "", ""
    currentnum = number
    if not 1 < to_base < 37:
        raise ValueError("base must be between 2 and 36")
    if not number:
        return 'Error'
    while currentnum:
        mod = currentnum % to_base
        currentnum = currentnum // to_base
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    number = converted_string
    return number
    pass

convertor("1111", 16, 8)