from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string



# class Command(BaseCommand):
#     help = 'Displays current time'
#     def handle(self, *args, **kwargs):    # what is args and kwaegs imp interview   
#         time = timezone.now().strftime('%X')
#         self.stdout.write("It's now %s" % time)


# (b8_env1) C:\Users\Devidas\Archu_Django08\Library2>py manage.py what_time_is_it                                      
#It's now 11:02:55                   

