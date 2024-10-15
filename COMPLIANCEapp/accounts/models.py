from django.contrib.auth.models import User

def create_user(username, first_name, last_name, email, password):
    user = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password
    )
    return user
