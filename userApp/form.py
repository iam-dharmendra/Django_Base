from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth  import get_user_model
User=get_user_model()


class RegisterForm(UserCreationForm):

    class Meta:
        model=User
        fields=('first_name','email','phone_number')

""" another method to register in cutome user model"""

# class RegisterForm(forms.ModelForm):

#     password1=forms.CharField(max_length=20)
#     password2=forms.CharField(max_length=20)

#     class Meta:
#         model=User
#         fields=('first_name','email','phone_number')


#     def save(self,commit=True,**kwargs):

#         email=self.cleaned_data['email']
#         password=self.cleaned_data['password1']
#         first_name=self.cleaned_data['first_name']
#         phone_number=self.cleaned_data['first_name']

#         kwargs['first_name']=first_name
#         kwargs['phone_number']=phone_number

#         user=super().save(commit=False)
#         if user:
#             # user.save(password=password)
#             user=User.objects.create_user(email,password,**kwargs)
#         # return super().save()
#         return user     
""" another method to login"""


class LoginForm(forms.ModelForm):

    
    # email=forms.EmailField(required=True)
    password=forms.CharField(required=True)

    class Meta:
        model=User
        fields=('email','password')

    def clean(self,**kwargs):
        email=self.cleaned_data['email']
        password=self.cleaned_data['password']

        user=authenticate(email=email,password=password)
        if user is not None:
            self.cleaned_data['user']=user
            return self.cleaned_data
        raise ValueError('please chek email and password')
