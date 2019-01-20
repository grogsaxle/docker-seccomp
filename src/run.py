import ctypes
import os
from pathlib import Path
import platform
import resource
import subprocess
import sys
import time

syscall = ctypes.CDLL(None).syscall

def available(op):
  print('''\u001b[32m''' + op[0] + ' available\u001b[0m')

def unavailable(op):
  print('''\u001b[31m''' + op[0] + ' unavilable\u001b[0m')

def try_chdir():
  os.chdir('/tmp')
  subprocess.Popen(['/usr/bin/cd', '/tmp'], stdout=subprocess.PIPE) 

def try_chmod():
  filename = '/tmp/test.txt'
  Path(filename).touch()
  os.chmod(filename, 444)

def try_getpid():
  syscall(39)

def try_setrlimit():
  resource.setrlimit(resource.RLIMIT_CPU, (2, 2)) 


def try_waitpid():
  pid = os.fork()
  if not pid:
    time.sleep(2)
    sys.exit(0)
  else:
    os.waitpid(pid, 0)



ops = [
  ['uname', platform.uname],
  ['chdir', try_chdir],
  ['chmod', try_chmod],
  ['getpid', try_getpid],
  ['setrlimit', try_setrlimit],
  ['waitpid', try_waitpid]
]

for op in ops:
  try:
    op[1]()
    available(op)
  except Exception as e:
    print(e)
    unavailable(op)
  
