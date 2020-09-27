#!/usr/bin/python3

print('Content-Type: text/html')
print()


import cgi
import subprocess as sp

cmd_dict = { "date":"date","calender":"cal"}

option = cgi.FieldStorage()
value = option.getvalue('command')


output = sp.getstatusoutput(value)

status = output[0]
result = output[1]
if status == 0:
    print("<pre style='text-align:center'>")
    print(result)
    print("</pre>")
else:
    print(f'ERROR: {result}')


print("<br>")
print("<br>")
print("<br>")
print("<br>")
print("<p style='text-align:center'><a  href='http://192.168.43.173/assistant.html'>Back</a></p> ")





        



