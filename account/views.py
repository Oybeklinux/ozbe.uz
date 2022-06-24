from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# Create your views here.
from .helpers import send_otp_to_phone
from .models import User
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, BasePermission


class validateOTP(APIView):

    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone_number', False)
        otp_sent = request.data.get('otp', False)


@api_view(["GET"])
def logout_user(request):
    request.user.auth_token.delete()
    logout(request)
    return Response('User Logged out successfully')


@api_view(['POST'])
def login_user(request):
    data = request.data
    phone = request.data.get('phone_number')
    sms = data.get('sms')

    if phone is None:
        return Response({
            'status': 400,
            'message': 'Telefon raqam talab etiladi'
        })

    if not phone.isdigit() or len(phone) != 12:
        return Response({
            'status': 400,
            'message': "Telefon raqam 998971234567 formatida bo'lishi kerak"
        })
    try:
        user = User.objects.get(phone_number=phone)
    except Exception as e:
        return Response({
            'status': 400,
            'message': "Bunday raqam bazada yo'q. Qayta ro'yxatdan o'ting"
        })

    try:
        token = Token.objects.get_or_create(user=user)[0].key

    except Exception as e:
        print(e)

    if sms is None:
        return Response({
            'status': 400,
            'message': 'sms talab etiladi'
        })

    if len(sms) != 6:
        return Response({
            'status': 400,
            "message": "sms 6 raqamdan iborat bo'lishi kerak"
        })

    user = None
    try:
        user = User.objects.get(phone_number=phone, otp=sms)
        user.is_phone_verified = True
        user.save()
    except Exception as e:
        return Response({
            'status': 400,
            'message': 'Raqam yoki sms kod xato'
        })

    # token = Token.objects.create(user=user)
    if user.is_active:
        login(request, user)
        return Response({
            'status': 200,
            'user_id': user.id,
            'token': token,
            "is_admin": user.is_staff,
            "name": user.first_name
        })
    else:
        raise Response({
            'status': 400,
            'message': 'Foydalnuvchi faollashtirilmagan'
        })


@api_view(['POST'])
def register_user(request):
    data = request.data
    full_name = request.data.get('full_name')
    phone = request.data.get('phone_number')
    if request.data.get('password', None) is not None:
        password = request.data.get('password')
    else:
        password = phone

    if full_name is None:
        return Response({
            'status': 400,
            'message': 'Ism talab etiladi'
        })

    if phone is None:
        return Response({
            'status': 400,
            'message': 'Telefon raqam talab etiladi'
        })

    if not phone.isdigit() or len(phone) != 12:
        return Response({
            'status': 400,
            'message': "Telefon raqam 998971234567 formatida bo'lishi kerak"
        })
    user = None
    try:
        user = User.objects.get(phone_number=phone)
    except Exception as e:
        pass

    if user:
        return Response({
            'status': 400,
            'message': 'Bu foydalanuvchi bor'
        })

    if password is None:
        return Response({
            'status': 400,
            'message': 'Parol talab etiladi'
        })

    try:
        sms = send_otp_to_phone(phone)
        if not sms:
            return Response({
                'status': 400,
                'message': 'SMS yuborishda xatolik. Qayta yuboring'
            })
        user = User.objects.create(
            phone_number=phone,
            password=password,
            first_name=full_name,
            otp=sms
        )

    except Exception as e:
        return Response({
            'status': 400,
            'message': 'Foydalanuvchi yaratishda xatolik yuz berdi'
        })

    return Response({
        'status': 200,
        'message': 'SMS yuborildi',
        'user_id': user.id,
        'sms': sms,
        "is_admin": user.is_staff
    })


@api_view(['POST'])
def send_sms_to_login(request):
    data = request.data
    phone = request.data.get('phone_number')

    if phone is None:
        return Response({
            'status': 400,
            'message': 'Telefon raqam talab etiladi'
        })

    if not phone.isdigit() or len(phone) != 12:
        return Response({
            'status': 400,
            'message': "Telefon raqam 998971234567 formatida bo'lishi kerak"
        })
    user = None
    try:
        user = User.objects.get(phone_number=phone)
    except Exception as e:
        return Response({
            'status': 400,
            'message': "Bunday foydalanuvchi mavjud emas. Ro'yxatdan o'ting"
        })

    sms = send_otp_to_phone(phone)
    if not sms:
        return Response({
            'status': 400,
            'message': 'SMS yuborishda xatolik. Qayta yuboring'
        })
    user.otp = sms
    user.save()
    return Response({
        'status': 200,
        'message': 'SMS yuborildi',
        'user_id': user.id,
        'sms': sms
    })
