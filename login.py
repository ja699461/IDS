# The login function

# user names and passwords are maintained in a dictionary
users = {"Jack":1111, "Jill":2222, "Pam":3333, "Sam":4444}


#----------------------------------------------------
# Check to see if the username and password are valid
#----------------------------------------------------
def login(uname, passwd):
     if users.__contains__(uname):
          if users[uname]==passwd:
               return True
     else:
          return False


#----------------------------------------------------
# Register a new user
#----------------------------------------------------
def register(uname, passwd):
     if not(users.__contains__(uname)):
          users[uname]=passwd
          return True
     else:
          return False
     

#-------------------------------------------------------
# Prompt user for a uname and passwd
#-------------------------------------------------------

done=False
while not (done):
     try:
          uname = input("Please enter your username: ")
          passwd = int(input("Please enter your passwd: "))
     except ValueError as ve:
          print("Error in input.", ve)
     else:
          done=True
     
if login(uname,passwd):
     print ("Valid login for user %s" % (uname))
else:
     register(uname, passwd)
     
     
     
