
import os
import platform

def available(op):
  print('''\u001b[32m''' + op[1] + ' available\u001b[0m')

def unavailable(op):
  print('''\u001b[31m''' + op[1] + ' unavilable\u001b[0m')

def try_chdir():
  os.chdir('/tmp')


ops = [
  [platform.uname, 'uname'],
  [try_chdir, 'chdir' ]
]

for op in ops:
  try:
    op[0]()
    available(op)
  except:
    unavailable(op)
  


