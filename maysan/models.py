from django.db import models

class User(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    name = models.CharFiled(db_column='name', max_length=100, null=False, unique=True)
    email = models.EmailFiled(db_column='email', max_length=100, null=False)
    password = models.CharFiled(db_column='password', max_length=100, null=False)

    class Meta:
        manage = False
        db_table = 'user'


class Message(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    from_ = models.IntegerField(db_column='from_', null=False)
    to_ = models.IntegerField(db_column='to_', null=False)
    object_message = models.CharFiled(db_column='object_message', max_length=100, null=True)
    content = models.CharFiled(db_column='content', max_length=8000, null=True)
    date_time = models.DateTimeFiled(db_column='date_time', auto_now_add=True)
    seen = models.BooleanField(db_column='seen', default=False, null=False)

    class Meta:
        manage = False
        db_table = 'message'