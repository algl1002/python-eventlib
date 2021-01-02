from eventlib.api import sleep

i = 0
while i < 100:
    sleep(0.1)
    print('%d. Sleep .1 second' % i)
    i = i + 1

# from time import clock
# from eventlib.green.socket import gethostbyname
#
# st = clock()
# for i in range(100):
#     print(gethostbyname('ag-projects.com'))
# print('Time used: {}s'.format(clock() - st))
