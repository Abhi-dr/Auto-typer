from django.shortcuts import render, redirect
import keyboard
from django.contrib import messages
import time

def index(request):
    
    if request.method == "POST":
        data = request.POST["data"]
        speed = float(request.POST["speed"])
        print(speed)
        
        for character in data:
            time.sleep(speed)
            keyboard.write(character)            

        messages.success(request, "Task has been completed successfully!")   
        return redirect("/")
    
    return render(request, "index.html")




