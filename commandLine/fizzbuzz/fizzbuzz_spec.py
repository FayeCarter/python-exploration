import pytest

def test_returns_fizz():
  from fizzbuzz import FizzBuzz
  fizzbuzz = FizzBuzz(3)
  assert fizzbuzz.check() == "Fizz"