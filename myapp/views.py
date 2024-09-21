from django.shortcuts import render
from .models import Message

def index(request):
    messages = Message.objects.all()  # Fetch all messages from the database

    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        
        # Save the data to the database
        Message.objects.create(name=name, message=message)

        # Refresh the messages list after saving
        messages = Message.objects.all()

    return render(request, 'index.html', {'messages': messages})
