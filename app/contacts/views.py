from django.shortcuts import render
from django.contrib

def Contact(request):
    if request.metod == "POST":
        user_id = request.POST['user_id']
        car_manager = request.POST['car_manager']
        car_id = request.POST['car_id']
        name= request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['text']
    if request.user.is_authenticated:
        user_id = request.user_id
        has_contacted = Contacts.objects.all().filter(
            car_id=car_id, user_id=user_id)
        if has_contacted:
            messages.error(request, "car allredy rented")
            return redirect("/carlist")
        contact = Contacts(car=car, car_id=car_id, name=name, email=email, phone=phone, t=message, user_id=user_id)
        contact.save()
        messages.succes(request, "Your")
    return redirect('/carlist'+car_id)
