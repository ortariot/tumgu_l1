import time 
from threading import Thread

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
    temp = []
    
    t1 = Thread(target=worker, args=("Igor", 2, temp,))
    t2 = Thread(target=worker, args=("Alexey", 2, temp,))
    
    t1.start()
    t2.start()
    
    print(temp)
    
    print("Ждём завершения потоков")
    
    t1.join()
    t2.join()
