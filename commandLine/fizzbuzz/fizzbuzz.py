class FizzBuzz(object):
  def __init__(self, number):
    self.number = number

  def check(self):
    if self.number % 3 == 0:
      return "Fizz"
    elif self.number % 5 ==0:
      return "Buzz"