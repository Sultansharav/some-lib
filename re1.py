import re
s = '99051617'
if re.match('[0-9]{8}$', s):
    print('yes')
else: print('no')