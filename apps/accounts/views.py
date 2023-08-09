from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from apps.accounts.serializers import SignUpSerializer
from django.contrib.auth import authenticate, login


class SignUpView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'accounts/signup.html'
    def get(self, request):
        serializer = SignUpSerializer()
        return Response({'serializer': serializer})
    
    def post(self, request):
        serializer = SignUpSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('accounts:login')
        else:
            return Response({'serializer': serializer})
        

def login_view(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile:home')
        else:
            return render(request, 'accounts/login.html')    
    else:
        return render(request, 'accounts/login.html')