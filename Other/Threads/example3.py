from threading import Thread, current_thread
import os

def display():
    for i in range(4):
        print("Hello World")
def show():
    for i in range(3):
        print("Welcome!")

t1 = Thread(target=display)
t2 = Thread(target=show)
t1.start()
t2.start()
t1.name="T1"
print(f"T1 ident: {t1.ident}")
current_thread().name="Jay"
print(f"T2 name: {t2.name}")
print(f"T2 native id: {t2.native_id}")
print(f"Pid: {os.getpid()}")
