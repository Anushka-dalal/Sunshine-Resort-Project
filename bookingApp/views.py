from django.shortcuts import render,redirect
from rest_framework.decorators import api_view,APIView # type: ignore
from .models import *


class home(APIView):
    def get(self,request):
        return render(request,"bookingapp/index.html")

class booking(APIView):
    def get(self,request):
        return render(request,"bookingapp/booking.html") 
    
    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        people = request.POST.get('people')
        check_in = request.POST.get('check_in')
        room_type = request.POST.get('room_type')

        bookobj = Booking(name = name, email = email, mobile = mobile, people = people, check_in = check_in, room_type = room_type)
        bookobj.save()
        return redirect('/display/')
     
class display(APIView):
    def get(self,request):
        return render(request,"bookingApp/display.html",{"bookings" : Booking.objects.all()})

class update(APIView):
    def get(self,request,id):
        obj = Booking.objects.get(id = id)
        return render(request,'bookingapp/update.html',{"obj":obj})

    def post(self, request, id):
        obj = Booking.objects.get(id=id)
        obj.name = request.POST.get('name')
        obj.email = request.POST.get('email')
        obj.mobile = request.POST.get('mobile')
        obj.people = request.POST.get('people')
        obj.check_in = request.POST.get('check_in')
        obj.room_type = request.POST.get('room_type')

        obj.save()
        return redirect('/display/')

class delete(APIView):
    def get(self,request,id):
        obj = Booking.objects.get(id=id)
        return render(request,'bookingapp/delete.html',{"obj":obj})

    def post(self,request,id):
        obj = Booking.objects.get(id=id)
        obj.delete()
        return redirect('/display/')

@api_view(['GET'])
def gallery(request):
    return render(request,"bookingapp/gallery.html")

