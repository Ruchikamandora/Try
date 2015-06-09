from django.template import RequestContext, loader
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout
from django.contrib.auth.models import User
from pconspectus.models import Profile, Book, BookChapter, Rpaper, Cpaper
from django.template import Context, Template
from pconspectus.forms import ProfileForm, BookForm, BookChapterForm, RpaperForm, CpaperForm

def login_user(request):
    #c = {}
    #c.update(csrf(request))
    return render_to_response('pfaculty/tlogin.html')

@csrf_exempt 
def save(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            fullname = request.user.get_full_name
            form = BookForm()
            try:
                #form = Profile.objects.get(pk = request.user.get_full_name)
                form1 = Profile.objects.get(pk = request.user.get_full_name)
            except:
                form = "----"
            return render_to_response('pfaculty/profile.html', {'form' : form, 'fullname':fullname, 'form1': form1})

           # return render_to_response('pfaculty/loggedin.html',{'fullname':request.user.get_full_name, 'form': form})
        else:
            return render_to_response('pfaculty/Loginerror.html')
        
def profile(request):
    fullname = request.user.get_full_name
    form = BookForm()
    #form1 = Profile.objects.get(pk = fullname)
    try:
        form1 = Profile.objects.get(pk = request.user.get_full_name)
    except:
        form1 = "----"
    #return render_to_response('pfaculty/loggedin.html',{'fullname':request.user.get_full_name, 'form': form})

    return render_to_response('pfaculty/profile.html', {'form' : form, 'fullname':fullname, 'form1': form1})
    
def logout_view(request):
    logout(request)
    return render_to_response('pfaculty/loggedout.html')

def changepassword(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('pfaculty/changepassword.html', c)

def adminlogin(request):
    return render_to_response('pfaculty/adminlogin.html')

def userlogin(request):
    return render_to_response('pfaculty/userlogin.html')

def developer(request):
    return render_to_response('pfaculty/developer.html')

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
    return HttpResponse('You have entered wrong username or password!!')
    
@csrf_exempt         
def pedit(request):
    fullname = request.user.get_full_name
    form = ProfileForm()
    return render_to_response('pfaculty/pedit.html', {'form' : form, 'fullname': fullname})

@csrf_exempt    
def createprofile(request):
    fullname = request.user.get_full_name
    if request.POST:
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('pfaculty/loggedin.html',{'fullname':request.user.get_full_name, 'form': Profile.objects.get(pk = fullname)})
        return render_to_response('pfaculty/deleteform.html')

@csrf_exempt    
def deleteform(request):
    fullname = request.user.get_full_name
    try:
        u = Profile.objects.get(pk= fullname)
        u.delete()
        return render_to_response('pfaculty/loggedin.html',{'fullname':request.user.get_full_name})

    except:
        return HttpResponse('Error')

def book(request):
    fullname = request.user.get_full_name
    form = BookForm()
    return render_to_response('pfaculty/book.html', {'form' : form, 'fullname': fullname})

def bookchapter(request):
    fullname = request.user.get_full_name
    form = BookChapterForm()
    return render_to_response('pfaculty/bookchapter.html', {'form' : form, 'fullname': fullname})

def rpaper(request):
    fullname = request.user.get_full_name
    form = RpaperForm()
    return render_to_response('pfaculty/rpaper.html', {'form' : form, 'fullname': fullname})

def cpaper(request):
    fullname = request.user.get_full_name
    form = CpaperForm()
    return render_to_response('pfaculty/cpaper.html', {'form' : form, 'fullname': fullname})
    
@csrf_exempt  
def booksave(request):
    if request.POST:
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            a = request.POST.get('abstract')
            book = Book.objects.get(abstract = a)
            t = Template('{{ stringvariable|slice:"1" }}')
            c = Context({'stringvariable': book.first_author_fname})
            f = t.render(c)
            aname = book.first_author_lname
            bname = book.second_author_lname
            pyear = book.publication_year
            title = book.title
            location = book.location
            t = Template('{{ stringvariable|slice:"1" }}')
            c = Context({'stringvariable': book.second_author_fname})
            s = t.render(c)
            if(book.third_author_fname == ""):
                if(book.second_author_fname == ""):
                    book.citation = aname +","+" "+f+". ("+ pyear + "). "+ title + ". " + location
                else:
                    book.citation = aname +","+" "+f+"., & "+ bname +","+" "+s+". ("+pyear + "). "+ title + ". " + location
            else:
                cname = book.third_author_lname
                t = Template('{{ stringvariable|slice:"1" }}')
                c = Context({'stringvariable': book.third_author_fname})
                th = t.render(c)
                book.citation = aname +","+" "+f+"., "+ bname +","+" "+s+"., & "+ cname +","+" "+th+". ("+pyear + "). "+ title + ". " + location              
            book.save()
            u = Book.objects.get(abstract = a)
            return render_to_response('pfaculty/bookedited.html', {'form' : u})
        return HttpResponse('Error')
    
@csrf_exempt      
def bookchaptersave(request):
    if request.POST:
        form = BookChapterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            a = request.POST.get('abstract')
            book = BookChapter.objects.get(abstract = a)
            t = Template('{{ stringvariable|slice:"1" }}')
            c = Context({'stringvariable': book.first_author_fname})
            f = t.render(c)
            aname = book.first_author_lname
            bname = book.second_author_lname
            pyear = book.publication_year
            titlebook = book.title_book
            titlechapter = book.title_chapter
            publisher = book.publisher
            location = book.location
            pages = book.pages
            state = book.state
            t = Template('{{ stringvariable|slice:"1" }}')
            c = Context({'stringvariable': book.second_author_fname})
            s = t.render(c)
            if(book.third_author_fname == ""):
                if(book.second_author_fname == ""):
                    book.citation = aname +","+" "+f+". ("+ pyear + "). "+ titlebook + ", " + titlechapter + " (" + pages + "). " + location + ", "+ state + ": " + publisher
                else:
                    book.citation = aname +","+" "+f+"., & "+ bname +","+" "+s+". ("+pyear + "). "+ titlebook + ", " + titlechapter + " (" + pages + "). " + location + ", "+ state + ": " + publisher
            else:
                cname = book.third_author_lname
                t = Template('{{ stringvariable|slice:"1" }}')
                c = Context({'stringvariable': book.third_author_fname})
                th = t.render(c)
                book.citation = aname +","+" "+f+"., "+ bname +","+" "+s+"., & "+ cname +","+" "+th+". ("+pyear + "). "+titlebook + ", " + titlechapter + " (" + pages + "). " + location + ", "+ state + ": " + publisher             
            book.save()
            u = BookChapter.objects.get(abstract = a)
            return render_to_response('pfaculty/bookchapteredited.html', {'form' : u})
        return HttpResponse('Error')

@csrf_exempt      
def rpapersave(request):
    if request.POST:
        form = RpaperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            a = request.POST.get('abstract')
            book = Rpaper.objects.get(abstract = a)
            t = Template('{{ stringvariable|slice:"1" }}')
            c = Context({'stringvariable': book.first_author_fname})
            f = t.render(c)
            aname = book.first_author_lname
            bname = book.second_author_lname
            pyear = book.publication_year
            title = book.title
            location = book.location
            state = book.state
            t = Template('{{ stringvariable|slice:"1" }}')
            c = Context({'stringvariable': book.second_author_fname})
            s = t.render(c)
            if(book.third_author_fname == ""):
                if(book.second_author_fname == ""):
                    book.citation = aname +","+" "+f+". ("+ pyear + "). "+ title + ", " + location + ": "+ state 
                else:
                    book.citation = aname +","+" "+f+"., & "+ bname +","+" "+s+". ("+pyear + "). "+  title + ", " + location + ": "+ state 
            else:
                cname = book.third_author_lname
                t = Template('{{ stringvariable|slice:"1" }}')
                c = Context({'stringvariable': book.third_author_fname})
                th = t.render(c)
                book.citation = aname +","+" "+f+"., "+ bname +","+" "+s+"., & "+ cname +","+" "+th+". ("+pyear + "). "+ title + ", " + location + ": "+ state         
            book.save()
            u = Rpaper.objects.get(abstract = a)
            return render_to_response('pfaculty/rpaperedited.html', {'form' : u})
        return HttpResponse('Error')

@csrf_exempt 
def cpapersave(request):
    if request.POST:
        form = CpaperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            a = request.POST.get('abstract')
            book = Cpaper.objects.get(abstract = a)
            t = Template('{{ stringvariable|slice:"1" }}')
            c = Context({'stringvariable': book.first_author_fname})
            f = t.render(c)
            aname = book.first_author_lname
            bname = book.second_author_lname
            pyear = book.publication_year
            titlepaper = book.title_paper
            titleconference = book.title_conference
            pages = book.pages
            location = book.location
            publicationplace = book.publication_place
            publisher = book.publisher
            t = Template('{{ stringvariable|slice:"1" }}')
            c = Context({'stringvariable': book.second_author_fname})
            s = t.render(c)
            if(book.third_author_fname == ""):
                if(book.second_author_fname == ""):
                    book.citation = aname +","+" "+f+". ("+ pyear + "). "+ titlepaper + ". " + titleconference + ", "+ location + " (" + pages + "). " + publicationplace + ": " + publisher
                else:
                    book.citation = aname +","+" "+f+"., & "+ bname +","+" "+s+". ("+pyear + "). "+  titlepaper + ". " + titleconference + ", "+ location + " (" + pages + "). " + publicationplace + ": " + publisher 
            else:
                cname = book.third_author_lname
                t = Template('{{ stringvariable|slice:"1" }}')
                c = Context({'stringvariable': book.third_author_fname})
                th = t.render(c)
                book.citation = aname +","+" "+f+"., "+ bname +","+" "+s+"., & "+ cname +","+" "+th+". ("+pyear + "). "+ titlepaper + ". " + titleconference + ", "+ location + " (" + pages + "). " + publicationplace + ": " + publisher        
            book.save()
            u = Cpaper.objects.get(abstract = a)
            return render_to_response('pfaculty/cpaperedited.html', {'form' : u})
        return HttpResponse('Error')
    
def myuploads(request):
    firstname = request.user.first_name
    lastname = request.user.last_name
    try:
        data1 = Book.objects.filter(first_author_fname__icontains = firstname, first_author_lname__icontains = lastname)
        data2 = Book.objects.filter(second_author_fname__icontains  = firstname, second_author_lname__icontains  = lastname)
        data3 = Book.objects.filter(third_author_fname__icontains  = firstname, third_author_lname__icontains  = lastname)
        data4 = BookChapter.objects.filter(first_author_fname__icontains = firstname, first_author_lname__icontains = lastname)
        data5 = BookChapter.objects.filter(second_author_fname__icontains  = firstname, second_author_lname__icontains  = lastname)
        data6 = BookChapter.objects.filter(third_author_fname__icontains  = firstname, third_author_lname__icontains  = lastname)
        data7 = Book.objects.filter(first_author_fname__icontains = firstname, first_author_lname__icontains = lastname)
        data8 = Rpaper.objects.filter(second_author_fname__icontains  = firstname, second_author_lname__icontains  = lastname)
        data9 = Rpaper.objects.filter(third_author_fname__icontains  = firstname, third_author_lname__icontains  = lastname)
        data10 = Cpaper.objects.filter(first_author_fname__icontains  = firstname, first_author_lname__icontains  = lastname)
        data11 = Cpaper.objects.filter(second_author_fname__icontains  = firstname, second_author_lname__icontains  = lastname)
        data12 = Cpaper.objects.filter(third_author_fname__icontains  = firstname, third_author_lname__icontains  = lastname)
        return render_to_response('pfaculty/myuploads.html', {'data1' : data1, 'data2' : data2, 'data3': data3, 'data4': data4, 'data5' : data5, 'data6': data6, 'data7': data7, 'data8': data8, 'data9': data9, 'data10' : data10, 'data11': data11, 'data12': data12 })
    except:
        return HttpResponse('There is no content to show')

def Myalluploads(request):
    firstname = request.user.first_name
    lastname = request.user.last_name
    try:
        data1 = Book.objects.filter(first_author_fname__icontains = firstname, first_author_lname__icontains = lastname)
        data2 = Book.objects.filter(second_author_fname__icontains  = firstname, second_author_lname__icontains  = lastname)
        data3 = Book.objects.filter(third_author_fname__icontains  = firstname, third_author_lname__icontains  = lastname)
        data4 = BookChapter.objects.filter(first_author_fname__icontains = firstname, first_author_lname__icontains = lastname)
        data5 = BookChapter.objects.filter(second_author_fname__icontains  = firstname, second_author_lname__icontains  = lastname)
        data6 = BookChapter.objects.filter(third_author_fname__icontains  = firstname, third_author_lname__icontains  = lastname)
        data7 = Book.objects.filter(first_author_fname__icontains = firstname, first_author_lname__icontains = lastname)
        data8 = Rpaper.objects.filter(second_author_fname__icontains  = firstname, second_author_lname__icontains  = lastname)
        data9 = Rpaper.objects.filter(third_author_fname__icontains  = firstname, third_author_lname__icontains  = lastname)
        data10 = Cpaper.objects.filter(first_author_fname__icontains  = firstname, first_author_lname__icontains  = lastname)
        data11 = Cpaper.objects.filter(second_author_fname__icontains  = firstname, second_author_lname__icontains  = lastname)
        data12 = Cpaper.objects.filter(third_author_fname__icontains  = firstname, third_author_lname__icontains  = lastname)
        #return HttpResponse('working')
        return render_to_response('pfaculty/Myalluploads.html', {'data1' : data1, 'data2' : data2, 'data3': data3, 'data4': data4, 'data5' : data5, 'data6': data6, 'data7': data7, 'data8': data8, 'data9': data9, 'data10' : data10, 'data11': data11, 'data12': data12 })
    
    except:
        return HttpResponse('There is no content to show')


                                             
def title(request, title):
    try:
        book = Book.objects.get(title = title)
        return render_to_response('pfaculty/bookview.html', {'book': book})
    except:
        try:
            book = BookChapter.objects.get(title_chapter = title)
            return render_to_response('pfaculty/bookchapterview.html', {'book': book})
        except:
            try:
                book = Rpaper.objects.get(title = title)
                return render_to_response('pfaculty/rpaperview.html', {'book': book})
            except:
                try:
                    book = Cpaper.objects.get(title_paper = title)
                    return render_to_response('pfaculty/cpaperview.html', {'book': book})
                except:
                    return HttpResponse('There is an error')

def name(request, name):
    words = name.split()
    firstname = words[0]
    lastname = words[-1]
    try:
        form = Profile.objects.get(pk = name)
        data1 = Book.objects.filter(first_author_fname__icontains = firstname, first_author_lname__icontains = lastname)
        data2 = Book.objects.filter(second_author_fname__icontains  = firstname, second_author_lname__icontains  = lastname)
        data3 = Book.objects.filter(third_author_fname__icontains  = firstname, third_author_lname__icontains  = lastname)
        data4 = BookChapter.objects.filter(first_author_fname__icontains = firstname, first_author_lname__icontains = lastname)
        data5 = BookChapter.objects.filter(second_author_fname__icontains  = firstname, second_author_lname__icontains  = lastname)
        data6 = BookChapter.objects.filter(third_author_fname__icontains  = firstname, third_author_lname__icontains  = lastname)
        data7 = Book.objects.filter(first_author_fname__icontains = firstname, first_author_lname__icontains = lastname)
        data8 = Rpaper.objects.filter(second_author_fname__icontains  = firstname, second_author_lname__icontains  = lastname)
        data9 = Rpaper.objects.filter(third_author_fname__icontains  = firstname, third_author_lname__icontains  = lastname)
        data10 = Cpaper.objects.filter(first_author_fname__icontains  = firstname, first_author_lname__icontains  = lastname)
        data11 = Cpaper.objects.filter(second_author_fname__icontains  = firstname, second_author_lname__icontains  = lastname)
        data12 = Cpaper.objects.filter(third_author_fname__icontains  = firstname, third_author_lname__icontains  = lastname)
        return render_to_response('pfaculty/registeredf.html', {'form': form, 'data1' : data1, 'data2' : data2, 'data3': data3, 'data4': data4, 'data5' : data5, 'data6': data6, 'data7': data7, 'data8': data8, 'data9': data9, 'data10' : data10, 'data11': data11, 'data12': data12 })
    except:
        return HttpResponse("No data entered yet!")

@csrf_exempt    
def search(request):
    if request.POST:
        try:
            key = request.POST.get('search')
            book = Book.objects.all()
            bookchapter = BookChapter.objects.all()
            rpaper = Rpaper.objects.all()
            cpaper = Cpaper.objects.all()
            return render_to_response('pfaculty/search.html', {'cpaper' : cpaper, 'rpaper' : rpaper, 'bookchapter' : bookchapter, 'key':key, 'book':book})
        except:
            return HttpResponse("Error")
    return HttpResponse("No post")

@csrf_exempt
def advancedsearch(request):
    return render_to_response('pfaculty/advancedsearch.html')

@csrf_exempt
def advanceysearch(request):
    if request.POST:
        try:
            key = request.POST.get('yearsearch')
            book = Book.objects.all()
            bookchapter = BookChapter.objects.all()
            rpaper = Rpaper.objects.all()
            cpaper = Cpaper.objects.all()
            return render_to_response('pfaculty/advanceysearch.html', {'cpaper' : cpaper, 'rpaper' : rpaper, 'bookchapter' : bookchapter, 'key':key, 'book':book})
        except:
            return HttpResponse("Error")
    return HttpResponse("No post")

@csrf_exempt
def advanceasearch(request):
    if request.POST:
        try:
            key = request.POST.get('authorsearch')
            words = key.split()
            firstname = words[0]
            lastname = words[-1]
            data1 = Book.objects.filter(first_author_fname__icontains = firstname, first_author_lname__icontains = lastname)
            data2 = Book.objects.filter(second_author_fname__icontains  = firstname, second_author_lname__icontains  = lastname)
            data3 = Book.objects.filter(third_author_fname__icontains  = firstname, third_author_lname__icontains  = lastname)
            data4 = BookChapter.objects.filter(first_author_fname__icontains = firstname, first_author_lname__icontains = lastname)
            data5 = BookChapter.objects.filter(second_author_fname__icontains  = firstname, second_author_lname__icontains  = lastname)
            data6 = BookChapter.objects.filter(third_author_fname__icontains  = firstname, third_author_lname__icontains  = lastname)
            data7 = Book.objects.filter(first_author_fname__icontains = firstname, first_author_lname__icontains = lastname)
            data8 = Rpaper.objects.filter(second_author_fname__icontains  = firstname, second_author_lname__icontains  = lastname)
            data9 = Rpaper.objects.filter(third_author_fname__icontains  = firstname, third_author_lname__icontains  = lastname)
            data10 = Cpaper.objects.filter(first_author_fname__icontains  = firstname, first_author_lname__icontains  = lastname)
            data11 = Cpaper.objects.filter(second_author_fname__icontains  = firstname, second_author_lname__icontains  = lastname)
            data12 = Cpaper.objects.filter(third_author_fname__icontains  = firstname, third_author_lname__icontains  = lastname)
            return render_to_response('pfaculty/advanceasearch.html', {'key': key, 'data1' : data1, 'data2' : data2, 'data3': data3, 'data4': data4, 'data5' : data5, 'data6': data6, 'data7': data7, 'data8': data8, 'data9': data9, 'data10' : data10, 'data11': data11, 'data12': data12 })
        except:
            return HttpResponse("Pease Enter Author Name!")
    return HttpResponse("No post")
