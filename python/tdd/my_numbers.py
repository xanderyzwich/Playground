import math

class MyNumber:
    def __init__(self, value):
        self.value = value

    def is_positive(self):
        return self.value >= 0

    def my_sqrt(self):
        return math.ceil(math.sqrt(self.value))

    def is_divisible_by(self, divisor):
        return self.value % divisor == 0

    def is_prime(self):
        if self.is_divisible_by(2):
            return False
        for i in range(2, self.my_sqrt()):
            if self.is_divisible_by(i):
                return False
        return True

if __name__ == '__main__':
    print(list(range(2,2)))
    # print(MyNumber(4).is_prime())
