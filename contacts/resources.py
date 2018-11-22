from django.contrib.auth import authenticate
from django.contrib.auth.models import AnonymousUser, User


#  def authenticateUser(request):
userName = 'kevin'
userPassword = 'adminkevin'
user = authenticate(username=userName, password=userPassword)
if user.is_authenticated():
    print("User is authenticated")

    if user.is_active():
        print("User is valid, active and authenticated")
    elif user.is_anonymous():
        print("User is valid, anonymous and authenticated")
    else:
        print("The password is valid, but the account has been disabled!")
else:
    # the authentication system was unable
    # to verify the username and password
    print("The username and password were incorrect.")
