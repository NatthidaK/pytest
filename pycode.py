quit = False
while quit == False:
  print("Welcome to calculator.py")
  print("your option are: \n")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplicaton")
  print("4. Division")
  print("5. Quit calculator.py \n")
  x = input("Choose your option: ")
  if x == '1':
    add = int(input("Add this: "))
    adder = int(input("by this: "))
    addans = add + adder
    print(add ,"+" ,adder ,"=", addans," \n" )
  elif x == '2':
    sub = int(input("Subtract this: "))
    subber = int(input("by this: "))
    subans = sub - subber
    print(sub ,"-" ,subber ,"=", subans," \n" )
  elif x == '3':
    mul =  int(input("Multiply this: "))
    muller = int(input("by this: "))
    mulans = mul * muller
    print(mul ,"*" ,muller ,"=", mulans,  " \n")
  elif x == '4':
    div =  int(input("Divide this: "))
    diver =  int(input("by this: "))
    divans = div/diver
    print(div ,"/" ,diver ,"=", divans, " \n")
  elif x == '5':
    quit =True
    print("Thank you for using calculator.py! \n")
  else :
    print("Please input valid option!!! Try again.\n")
