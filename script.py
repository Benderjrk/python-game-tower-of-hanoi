from node import Node

class Stack:
  def __init__(self, name):
    self.size = 0
    self.top_item = None
    self.limit = 1000
    self.name = name
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print("No more room!")

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    print("This stack is totally empty.")

  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  
  def get_size(self):
    return self.size
  
  def get_name(self):
    return self.name
  
  def print_items(self):
    pointer = self.top_item
    print_list = []
    while(pointer):
      print_list.append(pointer.get_value())
      pointer = pointer.get_next_node()
    print_list.reverse()
    print("{0} Stack: {1}".format(self.get_name(), print_list))
##
##
## This is the game
##
##
print(
  """
Welcome to the Tower of Hanoi!!
Have fun!!
  """
)
##
##
## Setup Game Funtions
##
##
#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# Set up the Game

# Setting Up Disk Amount Function
def enter_disk_amount(number=0):
  try:
    num_disks = input("\nHow many disks do you want to play with?\n")
    while int(num_disks) < 3:
      new_less_than_3_input = input("Enter a number greater than or equal to 3\n")
      num_disks = new_less_than_3_input
    return int(num_disks)
  except ValueError:
    print("\nEnter a number")
    return enter_disk_amount()

def create_disks(num):
  for i in range(num, 0, -1):
    left_stack.push(i)
def optimal_moves(num):
  return 2 ** num - 1
  
##
##
## Setup Up Game
##
##
# Setting Disk Amount
number_of_disks = enter_disk_amount()
create_disks(number_of_disks)

lowest_moves_string = "The fastest you can solve this game is in {move_number} moves\n".format(move_number=optimal_moves(number_of_disks))

print("\nYour stack size is:" ,left_stack.get_size())
print(lowest_moves_string)

##
##
## Getting User Inputs While Playing Function
##
##
def get_input():
  choices = [name.get_name()[0] for name in stacks]
  while True:
    
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {letter} for {name}".format(letter=letter, name=name))
    user_input = input("")
    direction = user_input.upper()

    if direction in choices:

      for i in range(len(stacks)):

        if direction == choices[i]:
          return stacks[i]

##
##
## Playing Game
##
##
num_user_moves = 0

# Initiate Game
while (right_stack.get_size() != number_of_disks):
  print("\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    if from_stack.is_empty():
      print("\nInvalid Move. Try Again")
    else:
      print("\nWhich stack do you want to move to?\n")
      to_stack = get_input()
      if to_stack.is_empty() or (from_stack.peek() < to_stack.peek()):
        disk = from_stack.pop()
        to_stack.push(disk)
        ++num_user_moves
      else:
        print("\n\nInvalid Move. Try Again")
    break

you_win = "\n\nYou completed the game in {user_moves} moves, and the optimal number of moves is {optimal_moves}".format(user_moves=num_user_moves, optimal_moves=optimal_moves(number_of_disks))
print(you_win)