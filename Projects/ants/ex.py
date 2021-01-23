def f(x):
    return x

for i in range(5):
    f(i)

list(map(f, range(5)))

class Random:
    def __init__(self, x):
        self.prop = x
    
    def p(self):
        print(self.prop)

random_instance = Random('hi')
random_instance.p()