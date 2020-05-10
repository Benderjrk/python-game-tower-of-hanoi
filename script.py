from stack import Stack
import numbers

print(
  """
  Welcome to the Tower of Hanoi!!
  Have fun!!
  """
)

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(right_stack)
stacks.append(middle_stack)

#Set up the Game

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


# Setting Disk Amount
number_of_disks = enter_disk_amount()

create_disks(number_of_disks)
print("Stack Size" ,left_stack.get_size())
#Get User Input

        
#Play the Game