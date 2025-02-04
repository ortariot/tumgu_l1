import time
import asyncio


async def worker(name: str, count: int):
    cnt = 0
    while True:
        await asyncio.sleep(1)
        print(f"процесс {name}")
        cnt += 1
        
        if cnt == count:
            break
        
async def runner():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(worker("Elena", 3))
        task2 = tg.create_task(worker("Nadezda", 4))
        
        
if __name__ == "__main__":
    
    asyncio.run(runner())