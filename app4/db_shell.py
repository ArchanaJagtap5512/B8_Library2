#exec(open(r'C:\Users\Devidas\Archu_Django08\Library2\app4\db_shell.py').read())


# how to  create users in db_shell 

# user create karne ke liye user model import karana hoga 

# instlled app ke -----auth app ---ke baydefault model hote hai 

# 1 usermodule

# from django.contrib.auth.models import User, Group

#print(User.objects.all())

# usser creste command


# only create kiya to password incript nhi hoga

#User.objects.create(username="supriya1", password="python@123", email="s1up@gmail.com")


# create user kiya to password incript hoga

# User.objects.create_user(username="supriya", password="python@123", email="sup@gmail.com")



# group ---all the default permission  which ever assign to group will be post on this user

# at time 15 user creae karana hai

# User.objects.create_user(username="supriya", password="python@123", email="sup@gmail.com")

# from django.utils.crypto import get_random_string

#print(get_random_string(5))               #capital , small, int allowed 



#--------------------------------------

# from django.contrib.auth.models import User
# user = User.objects.get(id=1)
# print(user)


# >>> exec(open(r'C:\Users\Devidas\Archu_Django08\Library2\app4\db_shell.py').read())
# devidas

#----------------------------------------------------------

# from django.contrib.auth.models import User
# user = User.objects.get(id=1).profile
# print(user)


#>>> exec(open(r'C:\Users\Devidas\Archu_Django08\Library2\app4\db_shell.py').read())
#Profile object (1)

#-------------------------------------------------------

# from django.contrib.auth.models import User
# user = User.objects.get(id=1).profile.location
# print(user)

# >>> exec(open(r'C:\Users\Devidas\Archu_Django08\Library2\app4\db_shell.py').read())
# pune