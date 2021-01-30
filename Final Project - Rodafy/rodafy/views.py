from django import forms
import math
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.response import TemplateResponse
from django.db.models import Q



from .models import User, Parking_Space, Message

# Create your views here.
def index(request):

    return render(request, "rodafy/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "rodafy/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "rodafy/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "rodafy/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "rodafy/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "rodafy/register.html")


def profile(request, username):
    if request.method == 'GET':
        currentuser = request.user
        profileuser = get_object_or_404(User, username=username)
        parking = Parking_Space.objects.filter(user=profileuser).order_by('id').reverse()
        if request.user.is_anonymous:
            return redirect('login')
        else:

            context = {
                'profileuser': profileuser,
                'parking': parking,
            }

            return render(request, "rodafy/profile.html", context)


def add_space(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST["title"]
        address = request.POST["address"]
        length = request.POST["length"]
        width = request.POST["width"]
        amount_vehicles_allowed = request.POST["amount_vehicles_allowed"]
        price = request.POST["price"]
        description = request.POST["description"]

        parking_space = Parking_Space.objects.create(user=user, title=title, address=address, length=length, width=width, amount_vehicles_allowed=amount_vehicles_allowed, price=price, description=description)
        parking_space.save()
        return render(request, "rodafy/add_space.html")


    else:
        return render(request, "rodafy/add_space.html")


def listing(request, id):
    if request.method == "GET":
        listing = Parking_Space.objects.filter(id=id)


        return render(request, 'rodafy/listing.html', {'listing':listing})

def edit_listing(request, id):
    if request.method == 'POST':
        parking = Parking_Space.objects.get(pk=id)
        parking.price = request.POST["form-control-price"]
        parking.width = request.POST["form-control-width"]
        parking.length = request.POST["form-control-length"]
        parking.address = request.POST["form-control-address"]
        parking.amount_vehicles_allowed = request.POST["form-control-availability"]
        parking.description = request.POST["form-control-description"]

        
        parking.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def search(request):
    if request.method == 'POST':
        address = request.POST["search"]
        finds = Parking_Space.objects.filter(address__icontains=address)

        return render(request, 'rodafy/search_results.html', {'finds':finds} )


def search_results(request):

    if request.method == 'GET':
        return render(request, "rodafy/search_results.html")

def messages(request, user_id):

    if request.method == "GET":

        sender = request.user.id
        
        #Filter for messages where with sender and user
        messages_all = Message.objects.filter(Q(user_id=user_id, sender_id=sender) |Q(user_id=sender, sender_id=user_id)).order_by('id')
        username = messages_all.values('user').distinct().exclude(sender_id=user_id)

        #Filter for unique usernames the sender has exchanged messages with
        unique_sendersy = Message.objects.filter(Q(user_id=user_id, sender_id=sender) |Q(user_id=sender, sender_id=user_id))
        unique_sendersu = Message.objects.select_related('user')
        unique_senders = unique_sendersu.values('user').distinct()

        return render(request, "rodafy/messages.html", {'messages_all':messages_all, 'user_id':user_id, 'unique_senders':unique_senders, 'username':username})

    else:
        sender = request.user.id
        receiver = user_id
        content = request.POST["new_message_content"]

        new_message = Message.objects.create(sender_id=sender, user_id=receiver, content=content)
        new_message.save()
        

        messages_all = Message.objects.filter(Q(user_id=user_id, sender_id=sender) |Q(user_id=sender, sender_id=user_id)).order_by('id')

        return render(request, "rodafy/messages.html", {'messages_all':messages_all, 'user_id':user_id})
    





