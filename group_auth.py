import numpy as np
from scipy.interpolate import lagrange
import threading
from queue import Queue

class DevThread(threading.Thread):
    def __init__(self, dev_name, func=None, args=None):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.attri = None
        self.token = None
        self.name = dev_name
    
    def run(self):
        self.func(*self.args)

def init_poly(group_size):
    rd_coef = np.random.randint(1,10,group_size)
    return np.poly1d(rd_coef)

def disclose_token(attr, token, t_q):
    t_q.put((attr,token))
    
def group_auth(np_devs, np_tokens, result_queue):
    result_queue.put(lagrange(np_devs, np_tokens).c)

def get_devs_and_tokens(t_q, group_size):
    np_dev = np.zeros(group_size)
    np_token = np.zeros(group_size)
    ind = 0

    while not t_q.empty():
        (temp_dev,temp_token) = t_q.get()
        t_q.task_done()
        np_dev[ind] = temp_dev
        np_token[ind] = temp_token
        ind += 1

    return np_dev, np_token


if __name__ == '__main__':
    group_size = 7
    token_queue = Queue(maxsize=group_size)
    result_queue = Queue(maxsize=group_size)
    poly = init_poly(group_size)                      # Generate a new random polynomial
    devs_attri = np.random.randn(group_size)          # Initialize the public attribute for every device
    print(poly)
    devs = []

    for i in range(group_size):
        dev = DevThread('Device'+str(i))
        dev.attri = devs_attri[i]
        dev.token = poly(dev.attri)
        dev.func = disclose_token
        dev.args = (dev.attri, dev.token, token_queue)
        devs.append(dev)

    for dev in devs:
        dev.start()
    
    for dev in devs:
        dev.join()
    
    # go back to main thread and extract device identifiers, tokens from the token queue
    np_devs, np_tokens = get_devs_and_tokens(token_queue, group_size)
    new_poly = lagrange(np_devs, np_tokens)
    print(new_poly)

    devs = []
    for i in range(group_size):
        dev = DevThread('Device'+str(i))
        dev.func = group_auth
        dev.args = (np_devs, np_tokens, result_queue)
        devs.append(dev)
    
    for dev in devs:
        dev.start()
    
    for dev in devs:
        dev.join()
    
    while not result_queue.empty():
        new_coef = result_queue.get()
        result_queue.task_done()
        print(new_coef)
        if new_coef[-1].astype(np.int32) == poly.c[-1]:
            print('Device authenticate successfully.')