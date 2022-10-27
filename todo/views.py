from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("get_todo_list")

    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    # use to say we want to get an instance of the item model
    # With an ID equal to the item ID that was passed into the view via the URL.
    # This method will either return the item if it exists. Or a 404 page not found if not.
    # To pre-populate the form with the items current details.
    # We can pass an instance argument to the form.
    # Telling it that it should be prefilled with the information for the item we just got from the database.
    item = get_object_or_404(Item, id=item_id)
    # copy the entire handler from the add item view and paste it in here.
    # Making only one small change and that's to give our form the specific item instance we want to update.
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("get_todo_list")
    # create an instance of our item form and return it to the template in the context.
    # instance item is same item used in line above
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect("get_todo_list")


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.delete()
    return redirect("get_todo_list")