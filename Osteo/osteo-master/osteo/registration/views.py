from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from . models import *
from . forms import *
from django.urls import reverse
from keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from os import remove as rem
import os



# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    var=True
    if request.method == 'POST':
        
        form = ImgForm(request.POST, request.FILES)         
        print(form)
        if form.is_valid():
            fm = form.save(commit=False)
            fm.img = request.FILES['img']
            file_type = fm.img.url
            print(file_type)
            fm.save()
            abpath=os.path.dirname(os.path.abspath(__file__))
               
            model = load_model(f"{abpath}\osteox.h5")

            impath=os.path.join(settings.MEDIA_ROOT,"osteo")
            print(impath)
            path=impath
            test_data = ImageDataGenerator(rescale=1./255)
            test_img= test_data.flow_from_directory(
                    path,
                    target_size=(150, 150),
                    batch_size=1,
                    class_mode='binary')
            
            pred = model.predict(test_img)

            nor_msg="Osteoarthritis not detected! The patient is normal!"
            ost_msg = "Detected! The patient is suffering from Osteoarthritis!"
            
            if(pred[0][0]<0.5):
                messages.success(request, "Osteoarthritis not detected! The patient is normal!")
            elif(pred[0][0]>=0.5):
                messages.success(request, "Detected! The patient is suffering from Osteoarthritis!")
                


            rem(os.path.join(settings.MEDIA_ROOT,str(fm.img)))
            
            return HttpResponseRedirect(reverse("home")) 
    else:
        form = ImgForm()
    return render(request,'home.html',{'form':form,"var":var})

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse('both password must be same')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')    
    return render(request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


