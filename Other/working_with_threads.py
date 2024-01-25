from threading import Thread
# source https://www.youtube.com/watch?v=jkwhht2gXB8&list=PLI4OVrCFuY57b_16D8xs7-hmABHncVD_w&index=4
def threading_informations():
    print(Thread.current_thread())
    print(Thread.current_thread().name)
    print(Thread.current_thread().ident)
    print(Thread.current_thread().is_alive())

def display(n,msg):
    for i in range(n):
        print(msg)

t1 = Thread(target=display,args=(4,"Hello")) #new thread here
t1.start()
