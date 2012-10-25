# vim: set ts=2 sw=2 expandtab:

class Rational:

  def __init__(self, numerator, denominator):
    """
    Initialise a rational number with the specified numerator and denominator
    """
    if denominator == 0:
      raise ValueError("Denominator must be non-zero")
    gcd = self.__gcd(numerator, denominator)
    self.numerator = numerator / gcd
    self.denominator = denominator / gcd

  def neg(self):
    """
    Return the negated version of this rational
    """
    return Rational(-self.numerator, self.denominator)

  def reciprocal(self):
    """
    Return the reciprocal version of this rational
    """
    return Rational(self.denominator, self.numerator)

  def add(self, other):
    """
    Return the sum of this rational and the specified other
    """
    return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                    self.denominator * other.denominator)

  def subtract(self, other):
    """
    Return the subtraction of the specified other from this rational
    """
    return self.add(other.neg())

  def multiply(self, other):
    """
    Return the product of this rational and the specified other
    """
    return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

  def divide(self, other):
    """
    Return the division of this rational by the specified other
    """
    return self.multiply(other.reciprocal())

  def less(self, other):
    """
    Return true if this rational is less than the specified other, false otherwise
    """
    return self.numerator * other.demoninator < other.numerator * self.denominator

  def max(self, other):
    """
    Return the larger of this rational and the specified other
    """
    return other if self.less(other) else self
  
  def __repr__(self):
    """
    Return the string representation of this rational
    """
    return str(self.numerator) + '/' + str(self.denominator)

  def __gcd(self, a, b):
    """
    Private funciton to calculate the greatest common divisor of two integers using
    Euclid's method
    """
    while (b != 0):
			tmp = a
			a = b
			b = tmp % b
    return -a if a < 0 else a

if __name__ == "__main__":
  #
  # Example usage
  #
  x = Rational(1, 3)
  y = Rational(5, 7)
  z = Rational(3, 2)

  print x.subtract(y).subtract(z)
  print y.add(y)
  print x.multiply(z)
