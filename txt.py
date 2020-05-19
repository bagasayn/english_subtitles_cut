import re
import subprocess as sp
import sys as s

bad_words = ['-->']


with open('{0}'.format(s.argv[1]),'r') as oldfile, open('{0}'.format(s.argv[2]), 'w') as newfile, open('list_time.txt', 'a') as list_time:
    for line in oldfile:
		find = re.findall(r'~',line)
		if any(find):
			res = re.findall(r'\d{2}:\d{2}:\d{2}',line) 
			
			print(' '.join(map(str,res)))
			list_time.writelines(' '.join(map(str,res)) + '\n')
			print(res)
			
		'''if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)'''
   



