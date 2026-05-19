
class Employee:
    def __init__(self,name):
        self.name = name
    
    
    name = "Sadiq"      # Mujhey iska length bhi return karwana hein   
    def __len__(self):  # mainey define kara isey __len__ se par code main use kiya without underscores, isiliye unko boltey hein magic methods
        i = 0
        for c in self.name:
            i = i + 1
        return i
    
    def __str__(self):
        return f"The name of the employee is {self.name} str"
    
    # Agar 'str' nahi dikha to repr par ye fallback karjata hein
    # repr, basically ek method hein jo ki represent kar raha hein ek object ke us tarikey ko jissey usey recreate kar sakta hein
    def __repr__(self):
        return f"The name of the employee is ('{self.name}') repr"
    
    def __call__(self):
        print("Hey I am good under the call method")
    