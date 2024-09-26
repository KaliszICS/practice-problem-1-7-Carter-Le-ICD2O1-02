

def q1():
  #Write code here
  boo = True
  print(boo)

def q2():
  #Write code here
  boo = False
  inp = int(input("Input an integer: "))
  boo = inp > 5
  print(boo)


def q3():
  #Write code here
  letr = input("Input the letter a: ")
  boo = letr == "a"
  print(boo)

def q4():
  #Write code here
  dict = input("Input a word earlier in the dictionary than google: ")
  boo = dict < "google"
  print(boo)

def q5():
  #Write code here
  int1 = int(input("Input an integer: "))
  int2 = int(input("Input another integer: "))
  boo = int1 * int2 > 40
  print("Your numbers multiplied together are greater than 40: ", end = "")
  print(boo)

#Do edit the code below
#Comment the lines below when running your tests

# q1()
# q2()
# q3()
# q4()
# q5()
