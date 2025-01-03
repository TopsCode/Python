class Sample:
    def __init__(self,fname):
        self.fname = fname

    def __str__(self):
        return f"{self.fname}"
    
obj = Sample("Anjali Patel") 
print(obj)

