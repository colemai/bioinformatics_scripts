#!/usr/bin/python3

import sys
input_list = sys.argv[1:]
summed = 0
the_sentence = ''

def add_inputs (numbers):
 for i in numbers:
	global summed
	summed += int(i)

def test_numbers_only (numbers):
 for i in range(0,len(numbers)):
  assert numbers[i].isnumeric(), 'Invalid input - numbers only please'

def make_sentence (sentence, numbers):
 for i in range(0,len(numbers)):
  if i != len(numbers)-1:
   sentence += numbers[i] + '+'
  else:
   sentence += numbers[i] + '='
 sentence += str(summed)
 print sentence

test_numbers_only
add_inputs(input_list)
make_sentence(the_sentence, input_list)	
