import re

some_list = '00:10:13,24 --> ~00:11:13,567 ~00:00:00,345 --> 00:34:34,234'

find = re.findall(r'~\d{2}:\d{2}:\d{2}',some_list)

if (any(find)):
    res = ' '.join(map(str,find))
    print(res.replace('~',''))
