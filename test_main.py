class Dog:

    def __init__(self, aa):
        self.aa = aa

    def __str__(self):
        print(super().__str__())
        return f"Dog:{self.name}"
    
    def __getattribute__(self, name):
        print(f"they want to get {name}")
        return "haha"
jia = Dog("jia")
print(jia.aa)