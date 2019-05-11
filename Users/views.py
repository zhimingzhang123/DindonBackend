from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from Users.models import VerifyCode
from Users.serializers import VerifyCodeSerializer
from Utils.tools import generate_code


class VerifyCodeAPIView(CreateAPIView):
    serializer_class = VerifyCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_num = serializer.validated_data["phone_num"]
        # code = generate_code()
        code = "1234"
        # TODO:发送短信的逻辑 可能要异步处理
        err_msg = "发送失败"
        successfully_send = True
        headers = self.get_success_headers(serializer.data)
        if successfully_send:
            code = VerifyCode(phone_num=phone_num, code=code)
            code.save()
            return Response(
                {
                    "phone_num": phone_num
                },
                status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(
                {
                    "phone_num": err_msg
                },
                status=status.HTTP_400_BAD_REQUEST)


class UserRegisterView(CreateAPIView):
    pass
