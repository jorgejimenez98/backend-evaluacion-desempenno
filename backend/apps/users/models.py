from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,\
    PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):
        """ Create and saves a new User """
        if not username:
            raise ValueError("User mas have a username")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self, username, password):
        """ Create a new Super User """
        user = self.create_user(username, password)
        user.is_staff = True 
        user.is_superuser = True 
        user.save(using=self._db)
        return user 
    

class User(AbstractBaseUser, PermissionsMixin):

    """ Custom user models that supports using email instead of username """
    username = models.CharField(max_length=255,  unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True)

    # ROLS
    is_staff = models.BooleanField(default=False)
    isFoodAndDrinkBoss = models.BooleanField(default=False)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'