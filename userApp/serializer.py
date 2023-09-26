from rest_framework import serializers
from django.contrib.auth import get_user_model
User=get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    # password1=serializers.CharField(read_only=True)
    password2=serializers.CharField(read_only=True)

    class Meta:
        model=User
        fields=('first_name','email','password','password2')


    def validate(self,attrs):
        password1=self.initial_data.get('password')
        password2=self.initial_data.get('password2') 

        if password1!=password2:
            raise serializers.ValidationError('both passeord must same')
        return super().validate(attrs)
    
    def save(self, **kwargs):
            
            email=self.validated_data['email']
            password=self.validated_data['password']

            # user=super().save(commit=False)
            user=User.objects.create_user(email=email,password=password,**kwargs)
            return User 
    

class UpdateUserApi(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=('first_name','email','phone_number')

    def validate(self, attrs):
        phone_number=attrs.get('Phone_number')

        if len(str(phone_number).strip())!=10:
                return super().validate(attrs)
        raise serializers.ValidationError('kindly check phone number')
    