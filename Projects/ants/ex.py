a = [0,1,2,3,4]

def f(x):
    return x

for i in a:
    f(i)

list(map(f, a))

class Random:
    def __init__(self, x):
        self.prop = x
    
    def p(self):
        print(self.prop)

random_instance = Random('hi')
random_instance.p()