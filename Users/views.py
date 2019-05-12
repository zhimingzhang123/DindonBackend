from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from Users.models import VerifyCode, User
from Users.serializers import VerifyCodeSerializer, UserRegisterSerializer
from Utils.tools import generate_code


class VerifyCodeAPIView(CreateAPIView):
    serializer_class = VerifyCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data["phone_number"]
        # code = generate_code()
        code = "1234"
        # TODO:发送短信的逻辑 可能要异步处理
        err_msg = "发送失败"
        successfully_send = True
        headers = self.get_success_headers(serializer.data)
        if successfully_send:
            code = VerifyCode(phone_num=phone_number, code=code)
            code.save()
            return Response(
                {
                    "phone_number": phone_number
                },
                status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(
                {
                    "phone_number": err_msg
                },
                status=status.HTTP_400_BAD_REQUEST)


class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.perform_create(serializer)

        # phone_number = serializer.validated_data['phone_number']
        # password = serializer.validated_data['password']
        # username = serializer.validated_data['username']
        #
        # user = User(phone_number=phone_number, username=username)
        # user.set_password(password)
        # user.save()
        re_dict = serializer.data
        # payload = jwt_payload_handler(user)
        # re_dict["token"] = jwt_encode_handler(payload)
        # re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(
            re_dict,
            status=status.HTTP_201_CREATED,
            headers=headers)
