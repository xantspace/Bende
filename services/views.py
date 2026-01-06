from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Birth_certificate

# Create your views here.


def birth_cert(request):
    return render(request, 'birth_cert.html', {})


def marriage_reg(request):
    return render(request, 'marriage_reg.html', {})


def waste_mgt(request):
    return render(request, 'waste.html', {})


def permit(request):
    return render(request, 'permit.html', {})


def dashboard(request):
    return render(request, 'dashboard.html', {})


def birth_cert_view(request):  # ← Changed function name
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        surname = request.POST.get('surname')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        place_of_birth = request.POST.get('place_of_birth')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        phone = request.POST.get('phone')
        home_address = request.POST.get('home_address')

        # Now Birth_cert refers to the MODEL
        birth_certificate = Birth_certificate(
            user=request.user,
            first_name=first_name,
            surname=surname,
            dob=dob,
            gender=gender,
            place_of_birth=place_of_birth,
            father_name=father_name,
            mother_name=mother_name,
            phone=phone,
            home_address=home_address
        )
        birth_certificate.save()
        messages.success(
            request, "Birth certificate information saved successfully.")
        return redirect('birth_cert')

    return render(request, 'birth_cert.html', {})
