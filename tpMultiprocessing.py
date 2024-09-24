from multiprocessing import Process, Queue
import os, time

def function_hijo(q, nProcess):
    print(f"Proceso {nProcess}, PID: {os.getpid()}")
    time.sleep(nProcess)
    q.put(f"{os.getpid()}\t")


if __name__ == "__main__":
    q = Queue()
    sumaSegundos = 0
    for i in range(10):
        sumaSegundos += (i+1)/2
        p = Process(target=function_hijo, args=(q,i+1))
        p.start()
        p.join()

    print("Padre leyendo contenido de la cola...")
    time.sleep(1)

    for i in range(10):
        print(q.get())
