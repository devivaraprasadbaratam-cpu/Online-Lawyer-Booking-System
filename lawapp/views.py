from django.contrib import messages
from django.shortcuts import render, redirect
from lawapp.models import Contact, Notifications
from lawapp.forms import ContactForm, NotificationsForm
from clientapp.models import Client, Feedback, Admin
from clientapp.forms import ClientForm
from lawyerapp.models import Lawyer
from lawyerapp.forms import LawyerForm

# Create your views here.

def index(request):
    feedback = Feedback.objects.all()
    return render(request, "index.html", {"feedback": feedback})

def about(request):
    feedback = Feedback.objects.all()
    return render(request, "about.html", {"feedback": feedback})




def attorney(request):
    return render(request, "attorney.html", {})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/contact?success=true")  # Redirect to prevent resubmission

    msg = "Thanks For Contacting Us" if request.GET.get("success") else ""
    return render(request, "contact.html", {"msg": msg})



def client_registration(request):
    return render(request, "client_registration.html", {})


# def client_reg(request):
#     if request.method == 'POST':
#         form = ClientForm(request.POST, request.FILES)
#         email = request.POST['email']
#         if form.is_valid():
#             email=form.cleaned_data["email"]
#             if Client.objects.filter(email=email).exists():
#                 return render(request, 'client_registration.html', {"msg": "This Email is Already Exists"})
#             else:
#                 form.is_valid()
#                 form.save()
#                 messages.success(request, "Successfully Register")
#                 return redirect('/client_login')
#         else:
#             return render(request, 'client_registration.html', {"msg": "Invalid Data"})
#     else:
#         form = ClientForm()
#         return render(request, 'client_registration.html', {"form":form})

#
# def client_reg(request):
#     if request.method == 'POST':
#         form = ClientForm(request.POST, request.FILES)
#         email = request.POST['email']
#
#         # Check if the email already exists before form validation
#         if Client.objects.filter(email=email).exists():
#             return render(request, 'client_registration.html', {"form": form, "msg": "This Email Already Exists"})
#
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Successfully Registered")
#             return redirect('/client_login')
#         else:
#             return render(request, 'client_registration.html', {"form": form, "msg": "Invalid Data"})
#     else:
#         form = ClientForm()
#         return render(request, 'client_registration.html', {"form": form})


from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages


def client_reg(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        email = request.POST['email']

        # Check if the email already exists before form validation
        if Client.objects.filter(email=email).exists():
            return render(request, 'client_registration.html', {"form": form, "msg": "This Email Already Exists"})

        if form.is_valid():
            form.save()

            # ✅ Send Thank You Email after saving
            subject = "Thanks for registering with us!"
            message = f"""Dear {form.cleaned_data.get('full_name')},
            Thank you for registering with Online Lawyer Booking.
            You can now book appointments with trusted lawyers easily.
            Regards,  
            Online Lawyer Booking Team"""

            from_email = 'devteamhub25@gmail.com'
            recipient_list = [email]

            try:
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            except Exception as e:
                print("Error sending email:", e)

            messages.success(request, "Successfully Registered")
            return redirect('/client_login')
        else:
            return render(request, 'client_registration.html', {"form": form, "msg": "Invalid Data"})
    else:
        form = ClientForm()
        return render(request, 'client_registration.html', {"form": form})



#
# #
# def client_reg(request):
#     if request.method == 'POST':
#         print("hi")
#         email = request.POST['email']
#         if Client.objects.filter(email=email).exists():
#             print("email taken")
#             return render(request, "client_registration.html", {"msg": "Email Already Exists"})
#         else:
#             form = ClientForm(request.POST, request.FILES)
#             print(form.errors)
#             if form.is_valid():
#                 form.save()
#                 return render(request, "client_registration.html", {"msg": "Inserted Success", "form": form})
#             else:
#                 return render(request, "client_registration.html", {})
#     else:
#         client = ClientForm()
#         return render(request, "client_registration.html", {"msg": "", "form": client})


def client_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, "", password)
        login = Client.objects.filter(email=email, password=password)
        if login.exists():
            print("hi")
            if login[0].status == "Accepted":
                request.session['email'] = email
                client = Client.objects.get(email=email)
                return render(request, "client_home.html", {"msg": "Login Successfully"})
            else:
                return render(request, "client_login.html", {"msg": "Your Account Is On Hold !"})
        else:
            return render(request, "client_login.html", {"msg": "Invalid Data"})
    return render(request, "client_login.html", {})




def lawyer_registration(request):
    return render(request, "lawyer_registration.html", {})

# def lawyer_reg(request):
#     if request.method == 'POST':
#         form = LawyerForm(request.POST, request.FILES)
#         email = request.POST['email']
#         if form.is_valid():
#             email=form.cleaned_data["email"]
#             if Lawyer.objects.filter(email=email).exists():
#                 return render(request, 'lawyer_registration.html', {"msg": "This Email is Already Exists"})
#             else:
#                 form.is_valid()
#
#
#                 form.save()
#                 messages.success(request, "Successfully Register")
#                 return redirect('/lawyer_login')
#         else:
#
#
#
#
#             return render(request, 'lawyer_registration.html', {"msg": "Invalid Data"})
#     else:
#         form = LawyerForm()
#         return render(request, 'lawyer_registration.html', {"form":form})


def lawyer_reg(request):
    if request.method == 'POST':
        form = LawyerForm(request.POST, request.FILES)
        email = request.POST['email']

        # Check if the email already exists before form validation
        if Lawyer.objects.filter(email=email).exists():
            return render(request, 'lawyer_registration.html', {"form": form, "msg": "This Email Already Exists"})

        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Registered")
            return redirect('/lawyer_login')
        else:
            return render(request, 'lawyer_registration.html', {"form": form, "msg": "Invalid Data"})
    else:
        form = LawyerForm()
        return render(request, 'lawyer_registration.html', {"form": form})




# #
# def lawyer_reg(request):
#     if request.method == 'POST':
#         print("hi")
#         email = request.POST['email']
#         if Lawyer.objects.filter(email=email).exists():
#             print("email taken")
#             return render(request, "lawyer_registration.html", {"msg": "Email Already Exists"})
#         else:
#             form = LawyerForm(request.POST, request.FILES)
#             print(form.errors)
#             if form.is_valid():
#                 form.save()
#                 return render(request, "lawyer_registration.html", {"msg": "Inserted Success", "form": form})
#             else:
#                 return render(request, "lawyer_registration.html", {})
#     else:
#         lawyer = LawyerForm()
#         return render(request, "lawyer_registration.html", {"msg": "", "form": lawyer})


def lawyer_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, "", password)
        login = Lawyer.objects.filter(email=email, password=password)
        if login.exists():
            print("hi")
            if login[0].status == "Accepted":
                request.session['email'] = email
                client = Lawyer.objects.get(email=email)
                return render(request, "lawyer_home.html", {"msg": "Login Successfully"})
            else:
                return render(request, "lawyer_login.html", {"msg": "Your Account Is On Hold !"})
        else:
            return render(request, "lawyer_login.html", {"msg": "Invalid Data"})
    return render(request, "lawyer_login.html", {})


# def admin_login(request):
#     if request.method == "POST":
#         email = request.POST["email"]
#         password = request.POST["password"]
#         print(email, "", password)
#         user = Lawyer.objects.filter(email=email, password=password, )
#         if user.exists():
#             request.session['email'] = email
#             return render(request, "admin_home.html", {"msg": email})
#         else:
#             return render(request, "admin_login.html", {"msg": "Email or Password is Not Exist"})
#     return render(request, "admin_login.html", {"msg": ""})


def admin_home(request):
    return render(request, "admin_home.html", {})


def admin_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        log = Admin.objects.filter(email=email, password=password)
        try:
            if log.exists():
                request.session["email"] = email
                return render(request, "admin_home.html", {"msg": "Successfully Login"})
            return render(request, "admin_login.html", {"msg": "Incorrect Email Or Password"})
        except Exception as e:
            print(e)
            return render(request, "admin_home.html", {"msg": ""})
    return render(request, "admin_login.html", {"msg": ""})


def admin_view_lawyer(request):
    law = Lawyer.objects.all()
    return render(request, 'admin_view_lawyer.html', {"law": law})


def admin_view_client(request):
    clt = Client.objects.all()
    return render(request, 'admin_view_client.html', {"clt": clt})

#
# def admin_change_password(request):
#     email = request.session["email"]
#     if admin_is_login(request):
#         if request.method == "POST":
#             email = request.session["email"]
#             password = request.POST["password"]
#             newpassword = request.POST["newpassword"]
#             try:
#                 user = Admin.objects.get(email=email, password=password)
#                 user.password = newpassword
#                 user.save()
#                 msg = 'Successfully Password Update'
#                 return render(request, "admin_login.html", {"msg": msg,"email":email})
#             except:
#                 msg = 'Invalid Data'
#                 return render(request, "admin_change_password.html", {"msg": msg,"email":email})
#         return render(request, "admin_change_password.html", {"email":email})
#     else:
#         return render(request, "admin_login.html", {})

def admin_change_password(request):
    email = request.session['email']
    if admin_is_login(request):
        if request.method == "POST":
            password= request.POST["old_password"]
            new_password= request.POST["new_password"]
            if password == new_password:
                return render(request,"admin_change_password.html",{"msg":"Your Old And New Passwords Are Same","email":email})
            try:
                users = Admin.objects.get(email=email,password=password)
                users.password = new_password
                users.save()
                messages.success(request,"Successfully Password Updated")
                return redirect('/admin_login')
            except Exception as e:
                print(e)
                return render(request,'admin_change_password.html',{"msg":"Invalid Creditinals","email":email})
        return render(request,'admin_change_password.html',{"email":email})
    else:
        return redirect('/admin_login')


def admin_is_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def admin_logout(request):
    if request.session.has_key('email'):
        del request.session['email']
    return redirect("/admin_login")

def admin_add_notification(request):
    if request.method == "POST":
        form = NotificationsForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("/admin_view_notification")
        return render(request, "admin_add_notification.html", {})
    return render(request, "admin_add_notification.html", {})


def admin_view_notification(request):
    note = Notifications.objects.all()
    return render(request, 'admin_view_notification.html', {"note": note})


def accept_lawyer(request, email):
    laws = Lawyer.objects.get(email=email)
    laws.status = 'Accepted'
    laws.save()
    return redirect('/admin_view_lawyer')


def reject_lawyer(request, email):
    laws = Lawyer.objects.get(email=email)
    laws.save()
    return redirect('/admin_view_lawyer')


def accept_client(request, email):
    client = Client.objects.get(email=email)
    client.status = 'Accepted'
    client.save()
    return redirect('/admin_view_client')



def reject_client(request, email):
    client = Client.objects.get(email=email)
    client.status = 'Rejected'
    client.save()
    return redirect('/admin_view_client')

def del_notifications(request,id):

    users = Notifications.objects.get(id=id)
    users.delete()
    return redirect("/admin_view_notification")






