x = int(input())
operation = input()
y = int(input())
z = None

if operation == '+':
    z = x + y 
elif operation == '-':
    z = x - y
elif operation == '*':
    z = x * y 
elif operation == '/' and y != 0:
    z = x // y 
elif operation == '**':
    z = x ** y 
elif operation == 'rad' and y != 0:
    z = int(x ** (1 / y))

if z is None:
  print("Luffy, você SUUUUPER não sabe usar isso, chama o Sanji!")
else:
  print(f"O resultado é {z}.")