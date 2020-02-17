from django.shortcuts import render,redirect
from .models import PetModel
from .forms import PetForm
def pet_list(request):
    context = {
        "pets":PetModel.objects.all()
    }
    return render(request, 'list.html', context)

def pet_detail(request, pet_id):
    context = {
        "pet":PetModel.objects.get(id=pet_id)
    }
    return render(request, 'detail.html', context)

def pet_create(request):
    form = PetForm()
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pet-list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)

def pet_update(request, pet_id):
    pet = PetModel.objects.get(id=pet_id)
    form = PetForm(instance=pet)
    if request.method == "POST":
        form = PetForm(request.POST,request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-list')
    context = {
        "form":form,
        "pet":pet,
    }
    return render(request, 'update.html', context)

def pet_delete(request, pet_id):
    pet = PetModel.objects.get(id = pet_id)
    pet.delete()
    return redirect("pet-list")
