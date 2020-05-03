from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
# Create your models here.

class UserProfileManager(BaseUserManager):
    """manager for user profiles"""

    def create_user(self, email, name, location, password=None):
        """create a new user profile"""
        if not email:
            raise ValueError('User must have an email')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, location=location)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, location, password):
        """create a super user with given detail"""
        user = self.create_user(email, name, location, password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """database user model for the system"""

    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=225)
    location = models.CharField(max_length=225)

    

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'location']

    def get_full_name(self):
        """retrive full name of user """
        return self.name
    
    def get_short_name(self):
        """retrive short name of user"""
        return self.name
    def get_location(self):
        """retirve location of user"""
        return self.location

    def __str__(self):
        return self.name

# class UserProfileActivity(models.Model):
#     """user activity periods """
#     user_profile = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )


