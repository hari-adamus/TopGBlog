from django.shortcuts import render, redirect
from .models import post
from datetime import datetime
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def index(request):
    posts=post.objects.all()
    return render(request, 'index.html',{'posts':posts})

def posts(request,pk):
    if pk=='create':
        if request.user.is_authenticated:
            return render(request, 'create_post.html')
        else:
            messages.info(request,'Must have an account to perform that action!')
            return redirect('/')
    
    elif pk=='added':
        
        title=str(request.POST['title_textbox'])
        body=str(request.POST['body_textbox'])
        date_made=str(datetime.now())
        comments=str('')
        post_username=request.user.username
        

        post.objects.create(title=title,body=body,date_made=date_made,comments=comments
                            ,post_username=post_username)
        return redirect('/')

    elif pk[-7:]=='comment':
        if request.user.is_authenticated:
            comments=post.objects.get(id=pk.split('!')[0])

            now = datetime.now()
            now = now.strftime("%m/%d/%Y|%H:%M")

            comments.comments=request.POST['comment']+'<><>'+request.user.username+'<><>'+now+'!~!'+comments.comments
            
            comments.save()

            posts=post.objects.get(id=pk.split('!')[0])
            

            return redirect('/post/'+pk.split('!')[0])
        else:
            messages.info(request,'Must have an account to perform that action!')
            return redirect('/post/'+pk.split('!')[0])

    else:
        posts=post.objects.get(id=pk)

        comments={}
        
        try:
            for comment in posts.comments[:-3].split('!~!'):
                print(comment)
                comment,name,date= comment.split('<><>')
                print(name)
                print(comment)
                print(date)

                

                comments['Comment uploaded '+date+' by '+name]=comment

                

        except Exception as e:
            print(e)
        
        
        return render(request, 'post.html',{'post':posts, 'comments': comments})

def register(request):
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        gender=request.POST['gender']


        if len(name) >4 and len(email)>5 and len(password) >4:        

            if password == password2:
                if User.objects.filter(username=name).exists():
                    messages.info(request,'Name already taken!')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email already taken!')
                    return redirect('register')
                elif gender.upper() != 'MALE' and gender.upper() != 'FEMALE':
                    messages.info(request,'Gender invalid!')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=name, email=email,first_name=gender,password=password)
                    user.save();
                    return render(request,'/')
                
    else:
        return render(request, 'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == "POST" and request.POST.get('name',False):
        username=request.POST.get('name',False)
        password=request.POST.get('password',False)
        
        
        user =auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        else:
            messages.info(request, 'Invalid Credentials!')
            return redirect('login')

    else:
        return render(request, 'log_in.html')