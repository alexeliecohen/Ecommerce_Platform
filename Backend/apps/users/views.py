from django.shortcuts import render

# Create your views here.
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from random import choice
from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler

from users.models import VerifyCode
from .serializers import SmsSerializer, UserRegSerializer, UserDetailSerializer

User = get_user_model()


class CustomBackend(ModelBackend):
    """
    Costumed User Verification

    """

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class SmsCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    Send Registration Code
    """
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        Generate a four-digit code
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data["mobile"]
        return Response({
            "mobile": mobile
        }, status=status.HTTP_201_CREATED)
        #
        # yun_pian = YunPian(APIKEY)
        #
        # code = self.generate_code()
        #
        # sms_status = yun_pian.send_sms(code=code, mobile=mobile)
        #
        # if sms_status["code"] != 0:
        #     return Response({
        #         "mobile": sms_status["msg"]
        #     }, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     code_record = VerifyCode(code=code, mobile=mobile)
        #     code_record.save()
        #     return Response({
        #         "mobile": mobile
        #     }, status=status.HTTP_201_CREATED)



class UserViewset(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    Users
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        elif self.action == "create":
            return UserRegSerializer

        return UserDetailSerializer

    # permission_classes = (permissions.IsAuthenticated, )
    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []

        return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["username"] = user.first_name if user.first_name else user.username
        # If there is any other files to add, just appendix below
        # re_dict["lastname"] = user.last_name if user.last_name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()
