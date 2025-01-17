from datetime import datetime
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login as auth_login
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import LogoutView
import json



# @login_required
def home(request):
    user = request.session.get('user', None)
    print(user)
    
    return render(request, 'index.html', {'user': user})

# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
       
        
#         access_token = data.get('access_token')
       
#         if access_token:
#             if request.session.get('access_token') == access_token:
#                 next_url = request.GET.get('next', '/')
#                 return JsonResponse({'next': next_url, 'status': 302}, status=302)
#             else:
#                 return JsonResponse({'detail': 'Invalid access token'}, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             username = data.get('username')
#             password = data.get('password')
#             user = authenticate(username=username, password=password)

#             if user is not None:
#                 # Check if the user is associated with a company
#                 if hasattr(user, 'company'):
#                     company = user.company

#                     # Check if the company's subscription is expired
#                     if company.subscription_end_date < datetime.now().date():
#                         return JsonResponse({'detail': 'Company subscription is expired'}, status=status.HTTP_403_FORBIDDEN)
#                 else:
#                     return JsonResponse({'detail': 'User is not associated with any company'}, status=status.HTTP_403_FORBIDDEN)

#                 # Log in the user if the subscription is valid
#                 auth_login(request, user)
#                 refresh = RefreshToken.for_user(user)
#                 access = str(refresh.access_token)
               

#                 create_token(user,refresh,access)
#                 request.method = 'GET'
#                 user_data = LoginSystemSerializer(user, context={'request': request}).data
#                 request.method = 'POST'
#                 request.session['access_token'] = access
#                 request.session['refresh_token'] = str(refresh)
#                 request.session['user'] = user_data
#                 response_data = {
#                     'access_token': access,
#                     'refresh_token': str(refresh),
#                 }
#                 return JsonResponse({'detail': 'Login Successful', 'data': response_data, 'status': 200}, status=status.HTTP_200_OK)
#             else:
#                 return JsonResponse({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#     # Render login page for GET requests
#     return render(request, 'login.html')

# def create_token(user, refresh,access):
#     try:
     
#         token = LoginSystem.objects.get(emp_id=user.emp_id)
#         token.access_token = str(access)
#         token.refresh_token = str(refresh)
#         token.save()

#     except LoginSystem.DoesNotExist:
#         print('fail to create token')
#     return token

# def register(request):
#     return render(request, 'register.html')

# def forget_password(request):
#     pass

class LogoutView(LogoutView):
    @method_decorator(login_required)  # Ensure the user is logged in
    def dispatch(self, request, *args, **kwargs):
        # Custom logic to set the token field to null
        user = request.user
        user.access_token = None
        user.refresh_token = None
        user.save()
        request.session.flush()
        # Call the parent dispatch method
        return super().dispatch(request, *args, **kwargs)

# def email():
#     print('calling')

#     subject = 'Django Server Testing'
#     message = 'This is the testing mail'
#     recipient_email = 'mundesatish2002@gmail.com'

#     # Render email templates
#     context = {'subject': subject, 'message': message}
#     html_message = render_to_string('email_template.html', context)

#     try:
#         email = EmailMultiAlternatives(
#             subject,
#             html_message,  # Plain text version of the email
#             settings.EMAIL_HOST_USER,  # From email
#             [recipient_email]  # To email
#         )
#         email.attach_alternative(html_message, "text/html")  # Attach HTML version of the email
#         email.send()
#         print('done')
#         return HttpResponse("Email sent successfully!")  # Return a success message
#     except Exception as e:
#         print({'error_message': str(e)})
#         return HttpResponse(f"Error sending email: {str(e)}")
