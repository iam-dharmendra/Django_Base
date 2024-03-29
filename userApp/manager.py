from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class MyManager(BaseUserManager):

    def create_user(self,email,password,**kwargs):

        if not email:
            raise ValueError(_('email should not be blank'))
        email=self.normalize_email(email)
        user=self.model(email=email,**kwargs)
        user.set_password(password)
        user.save()
        return user
    


        
        # if not email:
        #     raise ValueError(_("The Email must be set"))
        # email = self.normalize_email(email)
        # user = self.model(email=email, **extra_fields)
        # user.set_password(password)
        # user.save()
        # return user


    def create_superuser(self,email,password,**kwargs):


        # Create and save a SuperUser with the given email and password.
    
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if kwargs.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        
        return self.create_user(email, password, **kwargs)

