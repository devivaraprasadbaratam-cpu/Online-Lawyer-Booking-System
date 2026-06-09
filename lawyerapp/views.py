from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, reverse
from lawyerapp.models import Lawyer, Services
from lawyerapp.forms import LawyerForm, ServicesForms, Queries_RepliesForms
from clientapp.models import Book_lawyer, Feedback, Book_Services, Add_Feedback, Add_Queries, Manage
from lawapp.models import Notifications
from clientapp.forms import Add_QueriesForms, Books_lawyerForm, Manage_Forms

# Create your views here.


def lawyer_is_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def lawyer_home(request):
    return render(request, "lawyer_home.html", {})


def lawyer_details(request):
    email = request.session["email"]
    lawyer = Lawyer.objects.get(email=email)
    print(email)
    return render(request, "lawyer_details.html", {"lawyer": lawyer})


# def lawyer_change_password(request):
#     email = request.session["email"]
#     if lawyer_is_login(request):
#         if request.method == "POST":
#             email = request.session["email"]
#             password = request.POST["password"]
#             newpassword = request.POST["newpassword"]
#             try:
#                 user = Lawyer.objects.get(email=email, password=password)
#                 user.password = newpassword
#                 user.save()
#                 msg = 'Successfully Password Update'
#                 return render(request, "lawyer_login.html", {"msg": msg})
#             except:
#                 msg = 'Invalid Data'
#                 return render(request, "lawyer_change_password.html", {"msg": msg,"email":email})
#         return render(request, "lawyer_change_password.html", {"email":email})
#     else:
#         return render(request, "lawyer_login.html", {})



def lawyer_change_password(request):
    email = request.session['email']
    if lawyer_is_login(request):
        if request.method == "POST":
            password= request.POST["old_password"]
            new_password= request.POST["new_password"]
            if password == new_password:
                return render(request,"lawyer_change_password.html",{"msg":"Your Old And New Passwords Are Same","email":email})

            try:
                users = Lawyer.objects.get(email=email,password=password)
                users.password = new_password
                users.save()
                messages.success(request,"Successfully Password Updated")
                return redirect('/lawyer_login')
            except Exception as e:
                print(e)

                return render(request,'lawyer_change_password.html',{"msg":"Invalid Creditinals","email":email})
        return render(request,'lawyer_change_password.html',{"email":email})
    else:
        return redirect('/lawyer_login')

def lawyer_edit(request, email):
    lawyer = Lawyer.objects.get(email=email)
    return render(request, "lawyer_update.html", {"lawyer": lawyer})


def lawyer_update(request):
    if request.method == 'POST':
        email = request.POST["email"]
        lawyers = Lawyer.objects.get(email=email)
        form = LawyerForm(request.POST, request.FILES, instance=lawyers)
        print(form.errors)
        if form.is_valid():
            form.save()
        return redirect('/lawyer_details')
    return render(request, 'lawyer_update.html', {})


def lawyer_delete(request, email):
    lawyer = Lawyer.objects.get(email=email)
    lawyer.delete()
    return redirect("/lawyer_registration")


def view_booking(request):
    email = request.session["email"]
    lawyer = Book_lawyer.objects.filter(lawyer_id=email)
    return render(request, "view_booking.html", {"lawyer": lawyer})


def booking_approve(request, id):
    lawyer = Book_lawyer.objects.get(id=id)

    if request.method == 'POST':
        form = Books_lawyerForm(request.POST, instance=lawyer)
        print(form.errors)

        if form.is_valid():
            lawyer = form.save(commit=False)
            lawyer.status = "1"
            lawyer.save()
            return redirect('view_booking')

    return render(request, "booking_approve.html", {"lawyer": lawyer})

def manage(request,id):
    email = request.session["email"]
    lawyer = Book_lawyer.objects.get(id=id)
    if request.method == 'POST':
        form = Manage_Forms(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect(reverse("manage_files", args=[lawyer.id]))
    return render(request, "manage.html", {"lawyer":lawyer,"email":email})


def manage_files(request, id):
    email = request.session.get("email")  # Retrieve email from session
    lawyer = Book_lawyer.objects.get(id=id)
    files = Manage.objects.filter(lawyer_id=lawyer.id)

    return render(request, "manage_files.html", {"files": files, "email": email})

def delete_files(request, id):
    file = get_object_or_404(Manage, id=id)  # Using get_object_or_404 for safety
    lawyer_id = file.lawyer_id  # Store lawyer ID before deleting
    file.delete()
    return redirect(reverse("manage_files", args=[lawyer_id]))


def booking_reject(request, book_id):
    reject = Book_lawyer.objects.get(id=book_id)
    reject.status = 2
    reject.save()
    return redirect('/lawyer_details')


def client_feedback(request):
    email = request.session["email"]

    services = Services.objects.filter(email=email)

    feedback = Add_Feedback.objects.filter(
        services_id__in=services.values_list('id', flat=True)
    )

    return render(request, "client_feedback.html", {"feedback": feedback})

def lawyer_logout(request):
    if request.session.has_key('email'):
        del request.session['email']
    return redirect("/lawyer_login")


def lawyer_view_notification(request):
    lnote = Notifications.objects.all()
    return render(request, 'lawyer_view_notification.html', {"lnote": lnote})

# def add_services(request):
#     email = request.session["email"]
#     if request.method == 'POST':
#         form = ServicesForms(request.POST,request.FILES)
#         print(form.errors)
#         if form.is_valid():
#             form.save()
#             return redirect("/my_services")
#     return render(request, "add_services.html", {"email":email})
#

def add_services(request):
    email = request.session["email"]

    if request.method == 'POST':
        form = ServicesForms(request.POST, request.FILES)
        title = request.POST.get('title')  # Get the title from the form

        # Check for duplication
        if Services.objects.filter(title=title).exists():
            return render(request, "add_services.html", {
                "email": email,
                "form": form,
                "msg": "This Service Title Already Exists"
            })

        if form.is_valid():
            form.save()
            return redirect("/my_services")
        else:
            print(form.errors)
            return render(request, "add_services.html", {
                "email": email,
                "form": form,
                "msg": "Invalid Data"
            })

    else:
        form = ServicesForms()
        return render(request, "add_services.html", {
            "email": email,
            "form": form
        })


def my_services(request):
    email = request.session["email"]
    services = Services.objects.filter(email=email)
    return render(request,"my_services.html",{"services":services})

def view_bookings_services(request,id):
    services = Services.objects.get(id=id)
    bookings = Book_Services.objects.filter(services_id=services.id)
    return render(request,"view_bookings_services.html",{"bookings":bookings})


def bookings_services_approve(request,id):
    bookings = Book_Services.objects.get(id=id)
    bookings.status = "Accepted"
    bookings.save()
    return redirect(f'/view_bookings_services/{bookings.services_id}')


def bookings_services_reject(request,id):
    bookings = Book_Services.objects.get(id=id)
    bookings.status = "Rejected"
    bookings.save()
    return redirect(f'/view_bookings_services/{bookings.services_id}')


def view_services_feedbacks(request,id):
    services = Services.objects.get(id=id)
    feedbacks = Add_Feedback.objects.filter(services_id=services.id)
    return render(request,"view_services_feedbacks.html",{"feedbacks":feedbacks})

def view_quries(request):
    email = request.session['email']
    quries = Add_Queries.objects.filter(lawyers_id=email)

    return render(request,"view_quries.html",{"quries":quries})


def lawyer_replies(request,id):
    quries = Add_Queries.objects.get(id=id)
    if request.method == 'POST':
        id = request.POST["id"]
        form = Queries_RepliesForms(request.POST, request.FILES, instance=quries)

        print(form.errors)
        if form.is_valid():
            form.save()
        return redirect('/view_quries')
    return render(request, 'lawyer_replies.html', {"quries":quries})

