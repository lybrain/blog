from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from user.personal_info.models import PersonalInfo
from django.contrib.auth.models import PermissionsMixin


from user.managers import UserManager

def avatar_directory_path(instance, filename):
    return 'user/{1}/avatar/{1}'.format(instance.username, filename)
    
class User(AbstractBaseUser,PermissionsMixin):
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    username = models.EmailField(max_length=255, unique=True) 
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False, help_text='админ')
    avatar = models.ImageField(upload_to=avatar_directory_path, null=True, blank=True)
    personal_info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE, null=True, related_name="user")

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def check_is_admin(self, request=None):
        return self.is_staff
    
    def get_full_name(self):
        return "{0} {1} {2}".format(self.personal_info.last_name,self.personal_info.first_name, self.personal_info.middle_name)
    
    def __str__(self) -> str:
        return self.username
    
    def delete(self, *args, **kwargs):
        if self.avatar:
            self.avatar.delete()
        super().delete(*args, **kwargs)
    
   