from django.shortcuts import redirect
from django.contrib.auth import logout


def logout_view(request):
    """Log the user out."""
    logout(request)
    return redirect('learning_logs:index')
