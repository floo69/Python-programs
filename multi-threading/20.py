# Create 2 threads where one thread will print capital alphabets and one will print small alphabets

import threading

def caps():
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(char, end=' ')
    print()

def smals():
    for char in 'abcdefghijklmnopqrstuvwxyz':
        print(char, end=' ')
    print()

caps_t = threading.Thread(target=caps)
smals_t = threading.Thread(target=smals)

caps_t.start()
smals_t.start()

caps_t.join()
smals_t.join()


