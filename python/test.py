import sys
print("Hello World")
print("\nName of Python script:", sys.argv[1])

input_a=str(sys.argv[1])
print("outside function call---> "+input_a)
def sample_fun(x):
  print("inside function: "+str(x))
sample_fun(input_a)
