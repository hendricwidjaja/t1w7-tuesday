def greet():
    print("I love coding!!")

greet()

scope_out = "outside"

def test_scope():
    print(scope_out)

test_scope()

def test_scope1():
    scope_in = "Inside"

# Doesn't get defined
print(scope_in)
