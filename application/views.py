from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Hemis_admin, Moodle_admin, KeroControl_admin, Username
from .forms import SignUpForm, LoginForm, form_validation_error, ArizaForm
from django.contrib.auth.models import User


def index(request):
    return render(request, 'home.html')


def register_user(request):
    msg = None
    success = False

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'Foydalanuvchi yaratildi'
            success = True
        else:
            msg = 'Shakl haqiqiy emas'
    else:
        form = SignUpForm()
    return render(request, "login-register/register.html", {"form": form, "msg": msg, "success": success})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                msg = 'Login yoki Parol xato!'
        else:
            messages.error(request, form_validation_error(form))
            msg = "Ma'lumotni tekshirishda xatolik yuz berdi"

    return render(request, "login-register/login.html", {"form": form, "msg": msg})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    user = request.user

    # Foydalanuvchi admin profili bo'lishini tekshiramiz
    if not (hasattr(user, 'Hemis_admin') or hasattr(user, 'Moodle_admin') or hasattr(user, 'KeroControl_admin')):
        return redirect('admin_dashboard')  # Foydalanuvchi admin profili emas, login sahifasiga yo'naltiriladi

    return render(request, 'user-dashboard/user_dashboard.html')


@login_required
def admin_dashboard(request):
    user = request.user

    # Hemis_admin profili bo'lishini tekshiramiz
    if hasattr(user, 'Hemis_admin'):
        admin_profile = user.Hemis_admin

    elif hasattr(user, 'Moodle_admin'):
        admin_profile = user.Moodle_admin

    elif hasattr(user, 'KeroControl_admin'):
        admin_profile = user.KeroControl_admin

    else:
        return redirect('dashboard')

    ctx = {
        'admin_profile': admin_profile,
    }
    return render(request, 'admin-dashboard/admin_dashboard.html', {'ctx': ctx})

# @login_required
# def ariza_yuborish(request):
#     if request.method == 'POST':
#         form = ArizaForm(request.POST)
#         if form.is_valid():
#             foydalanuvchi_id = form.cleaned_data['foydalanuvchi_id']
#             admin_turi = form.cleaned_data['admin_turi']
#             malumotlar = form.cleaned_data['malumotlar']
#
#             # Foydalanuvchi va adminni topamiz
#             foydalanuvchi = User.objects.get(pk=foydalanuvchi_id)
#             admin = None
#
#             if admin_turi == 'hemis':
#                 admin = Hemis_admin.objects.get(user=foydalanuvchi)
#             elif admin_turi == 'moodle':
#                 admin = Moodle_admin.objects.get(user=foydalanuvchi)
#             elif admin_turi == 'kerocontrol':
#                 admin = KeroControl_admin.objects.get(user=foydalanuvchi)
#
#             if admin:
#                 # Ariza yaratish
#                 Username.objects.create(foydalanuvchi=foydalanuvchi, admin=admin, malumotlar=malumotlar)
#                 return redirect('dashboard')  # Muvaffaqiyatli yuborilganini bildirish sahifaga yo'naltirish
#     else:
#         form = ArizaForm()
#
#     return render(request, 'ariza_form.html', {'form': form})


# @login_required
# def javob_berish(request, ariza_id):
#     ariza = Username.objects.get(id=ariza_id)
#     if request.user == ariza.admin:
#         if request.method == 'POST':
#             ariza.javob = request.POST['javob']
#             ariza.save()
#             return redirect('ariza_list')
#         return render(request, 'javob_berish.html', {'ariza': ariza})
#     else:
#         return redirect('ariza_list')
