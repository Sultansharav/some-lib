import re   
s = 'My 2 favourite numbers are 7 and 10'
lst = re.findall('[0-9]+', s)   
print(lst) 