class Employee:
   "Classes's docstring description always goes here"

   # Class variable
   empCount = 0

   #----------------------------------------------------------
   # __the CONSTRUCTOR has 2 leading and trailing underscroes__
   def __init__(self, name, salary):

      # Call a private method
      self.__set(name, salary)
      
      Employee.empCount += 1

   #----------------------------------------------------------
   # A __PRIVATE method has 2 leading underscores
   def __set(self, name, salary):

     # The instance variables do not need to be declared in advance
     self.name = name
     self.salary = salary
     
   #----------------------------------------------------------
   # A PUBLIC method
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   #----------------------------------------------------------
   # Another PUBLIC method
   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)


     
