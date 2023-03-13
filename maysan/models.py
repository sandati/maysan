from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        # manage = False
        db_table = 'user'


class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    from_msg = models.ForeignKey(User, on_delete=models.CASCADE, related_name="from_msg")
    to_msg = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_msg")
    object_message = models.CharField(max_length=100)
    content = models.CharField(max_length=8000)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    seen = models.BooleanField(default=False)

    class Meta:
        # manage = False
        db_table = 'message'