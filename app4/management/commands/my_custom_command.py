# kuch nhi hai data tab


# AttributeError: module 'app4.management.commands.my_coustom_command' has no attribute 'Command'


# print(" in my custom command ")

# in my custom command 

# AttributeError: module 'app4.management.commands.my_custom_command' has no attribute 'Command'

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from django.utils import timezone


# class Command(BaseCommand):
#      #pass  # NotImplementedError: subclasses of BaseCommand must provide a handle() method
#     def handle(self, *args, **kwargs):     # overwrite
        # print("hi hello")



# class Command(BaseCommand):
#     help = 'Displays current time'
#     def handle(self, *args, **kwargs):     
#         time = timezone.now().strftime('%X')
#         self.stdout.write("It's now %s" % time)

#---------------------------------------------------------------------------------

# class Command(BaseCommand):
#     help = 'Create random users'
#     def add_arguments(self, parser):
#         parser.add_argument('total', type=int, help='Indicates the number of users to be created')

#     def handle(self, *args, **kwargs):
#         print(kwargs)
        

# (b8_env1) C:\Users\Devidas\Archu_Django08\Library2>py manage.py my_custom_command
# usage: manage.py my_custom_command [-h] [--version] [-v {0,1,2,3}] [--settings SETTINGS] [--pythonpath PYTHONPATH]
#                                    [--traceback] [--no-color] [--force-color] [--skip-checks]
#                                    total
# manage.py my_custom_command: error: the following arguments are required: total


# (b8_env1) C:\Users\Devidas\Archu_Django08\Library2>py manage.py my_custom_command 10
# {'verbosity': 1, 'settings': None, 'pythonpath': None, 'traceback': False, 'no_color': False, 'force_color': False, 'skip_checks': False, 'total': 10}


#(b8_env1) C:\Users\Devidas\Archu_Django08\Library2>py manage.py my_custom_command hjuy
#manage.py my_custom_command: error: argument total: invalid int value: 'hjuy'



#---------------------------------------------------

# class Command(BaseCommand):
#     help = 'Create random users'

#     def add_arguments(self, parser):
#         parser.add_argument('total', type=int, help='Indicates the number of users to be created')

#     def handle(self, *args, **kwargs):
#         total = kwargs['total']
#         for i in range(total):
#             User.objects.create_user(username=get_random_string(5), email='', password='123')

# database me 5 entry hoti hai 