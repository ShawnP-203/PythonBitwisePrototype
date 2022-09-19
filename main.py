# Shawn Plackiyil
# 9-16-2022 (last update 9-19-2022)
# Credit to Wikipedia for instructions on subtraction and especially addition. See these URLs:
# https://en.wikipedia.org/wiki/Special:PermanentLink/1094113375#Example:_a_simple_addition_program
# https://en.wikipedia.org/wiki/Special:PermanentLink/1110485797#Subtraction
# Arithmeticless Math
# Adds and subtracts without any arithmetic operators (assumes == and != are okay).
# There are two known limitations:
# 1. Can only use positive integers
# 2. The second integer must be higher than the first
class Binary(): # Program reuses a LOT of variables between methods, which is why I use a class.
  def __init__(self, integer1 = 0, integer2 = 0, finalSum = 0, sumInvertedSecond = 0, finalDifference = 0):
    self.integer1 = integer1
    self.integer2 = integer2
    self.finalSum = finalSum
    self.sumInvertedSecond = sumInvertedSecond
    self.finalDifference = finalDifference
  def __greaterThan(self, expr1, expr2): # Assuming that >, >=, <, and <= count as arithmetic operators
      """Returns True if expr2 is greater than expr1; False if vice versa"""
      # General notes:
      # bin() converts numbers to binary.
      # [2:] truncates annoying "0b"s from their beginnings.
      # .zfill() adds zeros to their beginnings until they reach a certain length (128 bits here).
      # .ljust() adds choosable characters to their ENDS until they reach a certain length.
      expr1 = bin(expr1)[2:].zfill(128)
      expr2 = bin(expr2)[2:].zfill(128)
      for bitCount, bits in enumerate(expr1):
        if expr1[bitCount] == "0" and expr2[bitCount] == "1": return True
        elif expr1[bitCount] == "1" and expr2[bitCount] == "0": return False
  def __positiveIntInput(self, question, callIteration): # Leading underscores = do not call method outside of the class
    """Asks for a positive integer and repeats the question if the user inputs otherwise"""
    try:
      assignTo = int(input(question).strip().replace(",", ""))
      # .strip().replace(",", "") removes whitespace and commas from the input.
      if "b" in bin(assignTo)[2:]:
        print("Integer may not be negative.") # Negative binaries have "b" in them
      #                       The code below equals 2 ** 127 - 1
      elif self.__greaterThan(int("0".ljust(128, "1"), base = 2), assignTo) and callIteration == 1 \
      or   self.__greaterThan(int("1".ljust(128, "0"), base = 2), assignTo) and callIteration == 2: 
        print("Integer is too big.")
      else: return assignTo # If input is acceptable
    except ValueError:
      print("Please enter a *positive integer* (no negatives or non-numeric characters).")
    return 0 # There is a reason for invalid input getting a return value here —
             # because otherwise it would evaluate to "NoneType" which causes a TypeError
             # in the greaterThan() method.
  def questions(self):
    """Run with no arguments to see this program's questions"""
    while not self.integer1:
      self.integer1 = self.__positiveIntInput("Enter a positive integer: ", 1)
    while True:
      self.integer2 = self.__positiveIntInput("Enter an integer bigger than {:,}: " \
                                              .format(self.integer1), 2)
      if self.integer2 != 0:
        if self.__greaterThan(self.integer1, self.integer2): break
  def calculateSumDifference(self, integer1Bin, integer2Bin):
    """Converts two integers to binary and calculates the sum and difference"""
    integer1Bin = int(bin(self.integer1)[2:], base = 2) # Potentially important retrospective note:
    integer2Bin = int(bin(self.integer2)[2:], base = 2) # The parameters in greaterThan() get strings
    def __add(addend1, addend2):                        # while these variables get integers.
      """Call once for addition and thrice (resembling a + ~b + 1) for subtraction"""
      sum = addend1 ^ addend2 # XOR operator. Has nothing to do with exponents.
      carryTo = addend1 & addend2 # AND operator.
      while carryTo:
        carryTo <<= 1 # Left shift operator. Has nothing to do with less than or equal to.
        addend1 = sum
        addend2 = carryTo
        sum = addend1 ^ addend2
        carryTo = addend1 & addend2
      return sum
    self.finalSum = __add(integer1Bin, integer2Bin)
    # Bitwise subtraction is adding integer1, the OPPOSITE of integer2, and 1.
    integer2Bin =~ integer2Bin
    # ~ is the complement operator, equivalent to -x - 1.
    # It's also why the second limitation (see comment header) exists. The method for adding numbers
    # apparently goes haywire if two things are true:
    # 1. The second number is negative — which is what ~ converts a positive integer to.
    # 2. The second number's absolute value is less than the first number's.
    self.sumInvertedSecond = __add(integer1Bin, integer2Bin)
    self.finalDifference = __add(1, self.sumInvertedSecond)
    print("\nSum: {:,}\nDifference: {:,}\n".format(self.finalSum, self.finalDifference))
def main():
  """Call with no arguments to see the program"""
  program = Binary()
  program.questions()
  program.calculateSumDifference(Binary().integer1, Binary().integer2)
main()
input("Press ENTER to exit. ")
