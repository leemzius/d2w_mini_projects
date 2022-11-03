

def mergesort(array, byfunc=None):
  def merge(p, q, r):
      nleft, nright = q - p + 1, r - q
      left_array, right_array = array[p:q+1], array[q+1:r+1]
      left, right = 0, 0
      dest = p
      while left < nleft and right < nright:
          if byfunc(left_array[left]) <= byfunc(right_array[right]):
              array[dest] = left_array[left]
              left += 1
          else:
              array[dest] = right_array[right]
              right += 1
          dest += 1
      while left < nleft:
          array[dest] = left_array[left]
          left += 1
          dest += 1
      while right < nright:
          array[dest] = right_array[right]
          right += 1
          dest += 1
      
  def msort(p, r):
      if r - p > 0:
          q = (p + r) // 2
          msort(p, q)
          msort(q+1, r)
          merge(p, q, r)

  msort(0, len(array)-1)

class Stack:
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items += [item]

    def pop(self):
        if self.__items:
            removed = self.__items[-1]
            self.__items = self.__items[:-1]
            return removed
        else:
            return None

    def peek(self):
        return self.__items[-1] if self.__items else None

    @property
    def is_empty(self):
        return self.__items == []

    @property
    def size(self):
        return len(self.__items)

class EvaluateExpression:

  valid_char = '0123456789+-*/() '
  operands = '0123456789'
  operators = '+-*/() '
  ops = {'+': (lambda x, y: x + y),
        '-': (lambda x, y: x - y),
        '*': (lambda x, y: x * y),
        '/': (lambda x, y: x // y)}

  def __init__(self, string=""):
    self.expression = string

  @property
  def expression(self):
    return self._expression

  @expression.setter
  def expression(self, new_expr):
    if [x for x in new_expr if x not in EvaluateExpression.valid_char] == []:
      self._expression = new_expr
    else:
      self._expression = ""

  def insert_space(self):
    res = [(" " + x + " ") if x in "+-*/()" else x for x in self.expression]
    return "".join(res)

  def process_operator(self, operand_stack, operator_stack):
    o = operator_stack.pop()
    r = operand_stack.pop()
    l = operand_stack.pop()
    operand_stack.push(EvaluateExpression.ops[o](l, r))

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()
    
    for t in tokens:
      if t == ' ':
        continue
      elif t in EvaluateExpression.operands:
        operand_stack.push(int(t))
      elif t in '+-':
        while (not operator_stack.is_empty) and (operator_stack.peek() not in '()'):
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(t)
      elif t in '*/':
        while (not operator_stack.is_empty) and (operator_stack.peek() in '*/'):
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(t)
      elif t in '(':
        operator_stack.push(t)
      elif t in ')':
        while (not operator_stack.is_empty) and (operator_stack.peek() not in '('):
          self.process_operator(operand_stack, operator_stack)
        if operator_stack.peek() in '(':
          operator_stack.pop()
      # print(operand_stack._Stack__items, operator_stack._Stack__items)
    
    while (not operator_stack.is_empty):
      self.process_operator(operand_stack, operator_stack)

    return operand_stack.pop()

def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





