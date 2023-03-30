import sys

class Jar:
    def __init__(self, capacity=12):
        if(capacity<=0):
            self._capacity=0
            raise ValueError("ValueError")
        else:
            self._capacity=capacity
        self._size=0

    def __str__(self):
        self._s=""
        for x in range(self._size):
            self._s+="🍪"
        return self._s

    def deposit(self, n):
        if(self._size+n > self._capacity):
            raise ValueError("ValueError")
        else:
            self._size+=n

    def withdraw(self, n):
        if(n > self._size):
            raise ValueError("ValueError")
        else:
            self._size-=n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = get_jar()
    print(jar)
    jar.deposit(6)
    print(jar.size," : ",jar.capacity)
    print(jar)
    jar.withdraw(1)
    print(jar.size," : ",jar.capacity)
    print(jar)

def get_jar():
    c = input("capacity: ")
    return Jar(c)

if __name__ == "__main__":
    main()