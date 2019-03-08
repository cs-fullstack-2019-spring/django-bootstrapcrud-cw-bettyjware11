from django.shortcuts import render, redirect, get_object_or_404
from .forms import GarbageSellModel, GarbageSellForm


# function for homepage to display all of all items in model.
def index(request):
    # blank form will be rendered to enter information
    allEntries = GarbageSellModel.objects.all()
    context = {
        "allEntries": allEntries
    }
    return render(request, 'BootCRUDApp/index.html', context)

# function that allows user to add item to the database
def addItem(request):
    form = GarbageSellForm(request.POST or None)
    if request.method == "POST":
        # if the blank form is filled out and submitted it will be saved to the database
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        "form": form
    }
    # back to homepage updated with new item
    return render(request, "BootCRUDApp/addItem.html", context)

# function to edit an item recorded in the GarbageSell model and update the homepage
def editItem(request, name):
    garbagesellmodel = get_object_or_404(GarbageSellModel, pk=name)
    edit_form = GarbageSellForm(request.POST or None, instance=garbagesellmodel)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('index')

    return render(request, 'BootCRUDApp/editItem.html', {'garbagesellform': edit_form})


