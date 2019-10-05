import re # register shalgah
s = 'ИТ99051617'
if re.match('[А-Я]{2}$[0-9]{8}$', s):
    print('yes')
else: print('no')