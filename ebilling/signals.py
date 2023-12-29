from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from ebilling.utils import Log
from django.contrib.auth.models import User
from ebilling.models import History


@receiver(user_logged_in)
def login_signal(sender, user, request, **kwargs):
    Log(request,f"{user.username} has login to system from IP:{request.META['REMOTE_ADDR']}")
 
@receiver(user_logged_out)
def loginOut_signal(sender, user, request, **kwargs):
    Log(request,f"{user.username} has logout to system from IP:{request.META['REMOTE_ADDR']}")
 
@receiver(user_login_failed)
def login_faild_signal(sender, request,user=None, **kwargs):
    
    user = User.objects.get(username=kwargs['credentials']['username'])
    if user:
        History.objects.create(user=user,task=f"invalid login attempt from IP:{request.META['REMOTE_ADDR']}")

