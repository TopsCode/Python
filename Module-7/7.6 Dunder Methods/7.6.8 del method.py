class Sample:
    def __del__(self):
        print("Object is being deleted")

obj = Sample()
del obj  # Output: Object is being deleted
