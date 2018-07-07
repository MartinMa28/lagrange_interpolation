import threading
from time import sleep, ctime

loops = [4,2,1]

def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())

def main():
    print('starting at:', ctime())
    threads = []

    for i in range(len(loops)):
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)
    
    for i in range(len(loops)):
        threads[i].start()
    
    for i in range(len(loops)):
        threads[i].join()
    
    print('all DONE at:', ctime())

if __name__ == '__main__':
    main()
    


    