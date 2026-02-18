class Patient:
    def __init__(self, id, age, heart_rate):
        self.id = id
        self.age = age
        self._heart_rate = heart_rate
    
    def update_heartrate(self, new_hr):
        # Ensure that data is an integer
        if not isinstance(new_hr, int):
            raise ValueError(f"new_hr was not an integer. was {type(new_hr)}")
        # Ensure that integer is between 0 and 250
        if not  (0 < new_hr < 250):
            raise ValueError(f"Værdi skal være mellem 0 og 250. den var : {new_hr}")
        # Set heart rate
        self._heart_rate = new_hr

    def __str__(self):
        return f"Patient(id={self.id}, age={self.age}, heartrate={self._heart_rate})"
    

p = Patient(1,65, 72)
p.update_heartrate(120)
print(p)

# p.update_heartrate(1313) # Throws error