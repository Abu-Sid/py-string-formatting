def say_hi(name):
    print("Hello, this is {}.".format(name));

say_hi("Abu");


#default parameter value
def say_hi(name = 'Abu'):
    print("Hello, this is {}.".format(name));

say_hi();
say_hi("jhon");

#default parameter value
def say_hello(name, age = 20):
    print("Hello, this is {} {}.".format(name, age));
say_hello("jhon", 25);
say_hello("jhon");

#build in help function
def say_hi(name = 'AAA'):
    "'This function will print hello message with name'"
    print("Hello, this is {}.".format(name));
help(say_hi);
