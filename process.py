import time
import os

from multiprocessing import Process, Manager

def worker(name: str, count: int, tmp: list):
    cnt = 0
    tmp.append(name)
    while True:
        time.sleep(1)
        print(f"процесс {name}")
        cnt += 1
        
        if cnt == count:
            break
        
        
if __name__ == "__main__":
    # worker("Igor", 2)
    
    # temp = []
    m = Manager()
    
    temp = m.list()
    
    p1 = Process(target=worker, args=("Igor", 2, temp,))
    p2 = Process(target=worker, args=("Alexey", 2, temp,))
    
    p1.start()
    p2.start()
        
    print("Ждём завершения процессов")
    print("general id", os.getpid())
    
    print("general p1", p1.pid)
    print("general p2", p2.pid)
    
    p1.join()
    p2.join()
    
    print(f"My list {temp}")