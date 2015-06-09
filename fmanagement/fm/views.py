from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout
from django.contrib.auth.models import User
from fm.models import Profile
from django.template import Context, Template

def login_user(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('faculty/login.html', c)

def save(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render_to_response('faculty/loggedin.html',{'fullname':request.user.get_full_name})
        else:
            return HttpResponse('You have entered wrong username or password!!')

def logout_view(request):
    logout(request)
    return HttpResponse('You are successfully logged out!!')

def profile(request):
    fullname = request.user.get_full_name
    try:
        profile = Profile.objects.get(pk = fullname)
        contact = profile.contactno
        acedemic_qualification = profile.academic_qualifiacation
        experience = profile.experience
        subjects_profeciencies = profile.subjects_profeciencies
        return render_to_response('faculty/profile.html', {'fullname': fullname, 'contact':contact, 'acedemic_qualification':acedemic_qualification,'experience':experience, 'subjects_profeciencies':subjects_profeciencies})
    except Profile.DoesNotExist:
        return render_to_response('faculty/profile2.html', {'fullname': fullname})

def profile_edit(request):
    c = {}
    c.update(csrf(request))
    c['fullname'] = request.user.get_full_name
    return render_to_response('faculty/profileedit.html', c)    

def saveprofile(request):
    if request.POST:
        fullname = request.user.get_full_name
        contact = request.POST.get('contactno')
        acedemic_qualification = request.POST.get('acedemic_qualifications')
        experience = request.POST.get('experience')
        subjects_profeciencies = request.POST.get('subject_profeciencies')
        try:
            profile = Profile.objects.get(pk = fullname)
            profile.contactno = contact
            profile.academic_qualifiacation = acedemic_qualification
            profile.experience = experience
            profile.subjects_profeciencies = subjects_profeciencies
        except Profile.DoesNotExist:
            profile = Profile(full_name = fullname, contactno = contact, academic_qualification = acedemic_qualification, experience = experience, subjects_profeciencies = subjects_profeciencies)
        profile.save()
        return render_to_response('faculty/profile.html', {'fullname': fullname, 'contact':contact, 'experience':experience, 'acedemic_qualification':acedemic_qualification, 'subjects_profeciencies':subjects_profeciencies})
    return HttpResponse("Hello, world. You're at the poll index.")

def changepassword(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('faculty/changepassword.html', c)

def passwordchanged(request):
    if request.POST:
        uname = request.POST.get('username')
        password = request.POST.get('password')
        npassword = request.POST.get('npassword')
        if(password == ""):
            return HttpResponse("You haven't entered any password!")
        else:
            if(password == npassword):
                try:
                    u = User.objects.get(username = uname)
                    u.set_password(npassword)
                    u.save()
                    return HttpResponse("Your password is changed now!!")
                except UserDoesNotExist:
                    return HttpResponse("You have entered wrong username!!")
            else:
                return HttpResponse("Your New password is not matching with re-entered password")
    
    
    
    
                                      
