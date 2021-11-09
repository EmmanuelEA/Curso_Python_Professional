#Serie de fibonnacci
import time

class FiboIter():

    def __init__(self,num:int):
        self.number = num

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    
    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2   
        elif self.n2 > self.number:
            raise StopIteration
        else:
            self.aux = self.n1 + self.n2
            #self.n1 = self.n2
            #self.n2 = self.aux
            #Swapping
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux


if __name__ == "__main__":
    num = int(input("break number: "))
    fibonnacci = FiboIter(num)

    for element in fibonnacci:
        print(element)
        time.sleep(1)