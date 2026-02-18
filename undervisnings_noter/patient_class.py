class Patient:
    def __init__(self, id, age, heart_rate):
        self.id = id
        self.age = age
        self.heart_rate = heart_rate
    
    def __str__(self):
        return f"Patient(id={self.id}, age={self.age}, heartrate={self.heart_rate})"
    

p = Patient(1,65, 72)
p.heart_rate = 120
print(p)