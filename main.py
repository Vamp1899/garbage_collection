''' Garbage collection is a periodic task which happens in python
 automatically we can manually trigger it to enhance python program processsing
 g0, g1, g2 whose periodic checking can be altered '''


import gc, sys
import time

gc.set_debug(True)
# gc.set_threshold(20000,50,100)
# gc.disable()
# gc.enable()

class Link:

    def __init__(self, next_link, value:int):
        self.next_link = next_link
        self.value = value

    def __repr__(self):
        return self.value


l = Link(None, 'Main Link')

mylist = []
start = time.perf_counter()
for i in range(5000):
    l_temp = Link(l, 'L')
    mylist.append(l_temp)

end = time.perf_counter()
print(end-start)

''' I can manually collect garbage based upon generation 
gc.collect(0)
gc.collect(1)
gc.collect(2)
gc.disable()
gc.enable()
gc.collect()
'''
