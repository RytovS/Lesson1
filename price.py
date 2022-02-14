def get_summ(one, two, delimiter='&'):
  one = str(one).upper()
  two = str (two).upper()
  return one + str(delimiter) + two
 
a = 'Learn'
b = 'python'
print(get_summ(a, b))




