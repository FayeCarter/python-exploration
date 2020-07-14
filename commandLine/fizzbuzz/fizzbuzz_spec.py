import pytest

def test_returns_fizz():
  from fizzbuzz import FizzBuzz
  fizzbuzz = FizzBuzz(3)
  assert fizzbuzz.check() == "Fizz"

def test_returns_buzz():
  from fizzbuzz import FizzBuzz
  fizzbuzz = FizzBuzz(5)
  assert fizzbuzz.check() == "Buzz"

def test_returns_fizzbuzz():
  from fizzbuzz import FizzBuzz
  fizzbuzz = FizzBuzz(15)
  assert fizzbuzz.check() == "Fizzbuzz"