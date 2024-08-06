def outer():
    x = 10
    def inner():
        return x
    return inner

func = outer()
print(func())  # Outputs 10

func.__closure__[0].cell_contents = 20
print(func())  # Outputs 20


class MyClass:
    def __init__(self):
        self.__private = "You shouldn't access this!"

obj = MyClass()
print(obj._MyClass__private)  # Accessing the private variable


class MyClass:
    def __private_method(self):
        return "Private method called"

obj = MyClass()
print(obj._MyClass__private_method())  # Calls the private method


class MyClass:
    def __init__(self):
        self.value = 42

obj = MyClass.__new__(MyClass)
# obj.__init__() is not called, so obj.value doesn't exist yet


attributes = {
    'attr': 42,
    'method': lambda self: "Dynamic method"
}

DynamicClass = type('DynamicClass', (object,), attributes)
obj = DynamicClass()
print(obj.attr)         # Outputs 42
print(obj.method())     # Outputs "Dynamic method"


class MyClass:
    def __getattr__(self, name):
        return f"Attribute {name} not found"

    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}")
        super().__setattr__(name, value)

obj = MyClass()
print(obj.some_attribute)  # Outputs "Attribute some_attribute not found"
obj.new_attr = 123         # Outputs "Setting new_attr to 123"


class int(int):
    def __add__(self, other):
        return super().__add__(other) + 10

a = int(5)
b = int(3)
print(a + b)  # Outputs 18 (5 + 3 + 10)


class ImmutableClass:
    def __setattr__(self, name, value):
        raise AttributeError("Cannot modify immutable instance")


obj = ImmutableClass()
try:
    obj.attr = 10
except AttributeError as e:
    print(e)  # Outputs "Cannot modify immutable instance"


class MyClass:
    def __call__(self, *args, **kwargs):
        return "Instance called"

obj = MyClass()
print(obj())  # Outputs "Instance called"


class Base1:
    def method(self):
        return "Base1 method"

class Base2:
    def method(self):
        return "Base2 method"

class MyClass(Base1):
    pass

obj = MyClass()
print(obj.method())  # Outputs "Base1 method"

MyClass.__bases__ = (Base2,)
print(obj.method())  # Outputs "Base2 method"


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    pass

obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # Outputs True

