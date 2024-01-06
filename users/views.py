
from django.shortcuts import render
from rest_framework import generics,views,status
from rest_framework.response import Response
from users import serializers as user_serializers
from rest_framework.permissions import IsAuthenticated 
from users.models import User
from rest_framework.authtoken.models import Token



class UserRegister(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = user_serializers.UserRegisterSerializer

    def get_serializer_context(self, *args, **kwargs):
        return {
            "request": self.request,
            "args": self.args,
            "kwargs": self.kwargs
        }


class UserLoginView(views.APIView):

    def post(self,request,*args, **kwargs):
        data = request.data
        username = data.get('username',None)
        password = data.get('password',None)

        if not username or not password:
            return Response({'success':False, 'data':{}, 'message':'Provide username or password'},status=status.HTTP_400_BAD_REQUEST)
        
        user = None


        if username.isnumeric():
            user = User.objects.filter(mobile=username).first()
        else:
            user = User.objects.filter(email__iexact=username).first()
        
        if not user:
            return Response({'success':False, 'data':{}, 'message':'Invalid credentials! '},status=status.HTTP_403_FORBIDDEN)
        
        if user.check_password(password):
            if user.is_active:
                resp = {
                    'user_id': user.id,
                    'first_name' : user.first_name,
                    'last_name' : user.last_name,
                    'mobile' : user.mobile,
                    'email' : user.email,
                    'city' : user.city,
                    'state' : user.state,
                    'country':user.country,
                    'zipcode' : user.zipcode,
                    'address':user.address,
                    'active' : user.is_active,
                    'auth_token': self.get_auth_token(user)
                }
                return Response({'success':True, 'data':resp, 'message':'Successfully Logged In! '},status=status.HTTP_200_OK)
            else:
                return Response({'success':False, 'data':{}, 'message':'Account deactivated! Contant Admin.'},status=status.HTTP_403_FORBIDDEN)
            
        return Response({'success':False, 'data':{}, 'message':'Invalid credentials! , Check username or password '},status=status.HTTP_403_FORBIDDEN)
    

    def get_auth_token(self, user:User) ->dict:
        token, created = Token.objects.get_or_create(user=user)
        token_reponse = {
            'token' : str(token.key),
        }
        return token_reponse