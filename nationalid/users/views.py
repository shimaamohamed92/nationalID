from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from rest_framework import mixins
from django.views.generic import DetailView, RedirectView, UpdateView
from rest_framework.views import APIView
from nationalid.users.serializers import NationalSerializer
from datetime import datetime
from nationalid.users.models import NationalId
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import serializers


User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return self.request.user.get_absolute_url()  # type: ignore [union-attr]

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()



class NationalCreateAPI(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = NationalId.objects.all()
    serializer_class = NationalSerializer

    def post(self, request, pk=None):
        birthday_format = "%y%m%d"
        nationalid = request.data.get("nantional_id")
        national, created  = NationalId.objects.get_or_create(nantional_id=nationalid)
        print(national)
        length = len(str(national.nantional_id))
        if length == 14 and str(national.nantional_id).isdigit():
            specific_birthday = nationalid[1:7]
            birth = datetime.strptime(specific_birthday, birthday_format)
            national.birth = birth
            specific_country_code = nationalid[7:9]
            if specific_country_code == '01':
                country = "Cairo"
            elif specific_country_code == '03':
                country = "Port Said"
            elif specific_country_code == '04':
                country = "Suez"
            elif specific_country_code == '11':
                country = "Damietta"
            elif specific_country_code == '12':
                country = "Dakahlia"
            elif specific_country_code == '13':
                country = "Al Sharqia"
            elif specific_country_code == '14':
                country = "Al Kaliobeya"
            elif specific_country_code == '15':
                country = "Kafr El Sheikh"
            elif specific_country_code == '16':
                country = "Al Gharbia"
            elif specific_country_code == '17':
                country = "Monoufia"
            elif specific_country_code == '18':
                country = "El Beheira"
            elif specific_country_code == '19':
                country = "El Ismailia"
            elif specific_country_code == '21':
                country = "El Giza"
            elif specific_country_code == '22':
                country = "Beni Suef"
            elif specific_country_code == '23':
                country = "El Fayoum"
            elif specific_country_code == '24':
                country = "El Menia"
            elif specific_country_code == '25':
                country = "Assiut"
            elif specific_country_code == '26':
                country = "Sohag"
            elif specific_country_code == '27':
                country = "Qena"
            elif specific_country_code == '28':
                country = "Aswan"
            elif specific_country_code == '29':
                country = "Luxor"
            elif specific_country_code == '31':
                country = "Red Sea"
            elif specific_country_code == '32':
                country = "New Valley"
            elif specific_country_code == '33':
                country = "Matrouh"
            elif specific_country_code == '34':
                country = "North Sinai"
            elif specific_country_code == '35':
                country = "South Sinai"
            elif specific_country_code == '88':
                country = "Foreign"
            national.country = country
            gender_code = nationalid[12]
            if int(gender_code) % 2 == 0:
                gender = 'Female'
            else:
                gender =  'Male'
            national.gender = gender
            national.save()

            serializer = NationalSerializer(national)

            return Response(serializer.data)
        else:
            raise serializers.ValidationError("This is fake national ID")
   
