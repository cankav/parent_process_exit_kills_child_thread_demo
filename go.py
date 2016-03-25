from threading import Thread
from multiprocessing import Process
import time

def child():
  while True:
    print 'child'
    time.sleep(1)
  
def parent():
  t = Thread(target=child)
  t.daemon = True
  t.start()

  while not stop:
    print 'parent'
    time.sleep(1)

p = Process(target=parent)
p.start()

i=0
while True:
  print i
  time.sleep(1)

  i+= 1
  if i == 5:
    p.terminate()

  if i == 8:
    break
