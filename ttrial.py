class Human:
    def __init__(self, s, a):
        self.name = s 
        self.occupation = a
    def do_work(self):
        if self.occupation == "Agent":
            print(self.name, "Tags images")
        elif self.occupation == "Human Resource Manager":
            print(self.name, "Hires and fire")
    def annotates(self):
        print(self.name, "Tags images")

Hellen = Human("Hellen Savalla", "Human Resource Manager")
Hellen.do_work()

aloyce = Human("aloyce Maigo", "Agent")
aloyce.do_work()
aloyce.annotates()