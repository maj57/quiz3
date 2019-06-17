class FizzBuzzer:

    def __init__(self,start=0):
        self.number = start
    def next(self):
        self.number+=1
        if (self.number%3 == 0) and (self.number%5 == 0):
          return 'FizzBuzzeruzz'
        elif self.number == 3 or (self.number%3 == 0):
          return 'fizz'
        elif self.number == 5 or (self.number%5 == 0):
          return 'buzz'
        else:
          return str(self.number)

if __name__ == '__main__':
    buzzer = FizzBuzzer()
    print(buzzer.next())
    print(buzzer.next())
    print(buzzer.next())
