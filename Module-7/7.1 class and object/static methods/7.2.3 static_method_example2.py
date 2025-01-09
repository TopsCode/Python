class Sample:
    like = 0 
    score = 10 

    @staticmethod
    def addCount(self,count):
        self.score = self.score + count
        print(self.score)

    

obj1 = Sample()   # 1st object creation 
obj1.like += 1
print(obj1.like)

obj1.like += 1
print(obj1.like)
print("------------")

obj2 = Sample()   # 2nd object creation 
obj2.like += 1
print(obj2.like)

Sample.addCount(Sample,10)   # expected output : 20 
Sample.addCount(Sample,50)   # expected output : 70 

# bcs, static allocate memory once in a program 