from quiz3monday import FizzBuzzer
from unittest import TestCase

# python3 -m unittest test3monday.py

class Test(TestCase):

    def testDefault(self):
        self.assertEqual(FizzBuzzer().number, 0, "x= FizzBuzzer(), x.number is 0")

    def testNext(self):
        fizzbuzz = FizzBuzzer()
        word = fizzbuzz.next()
        self.assertEqual(word, "1", "x=FizzBuzzer(), x.next() returns word '1' ")

    def testNext2(self):
        fizzbuzz = FizzBuzzer(2)
        word = fizzbuzz.next()
        self.assertEqual(word, "fizz", "x=FizzBuzzer(2), x.next() returns word 'fizz' ")
        word2 = fizzbuzz.next()
        self.assertEqual(word2, "4", "x=FizzBuzzer(2), x.next() returns fizz and returns word '4' ")
