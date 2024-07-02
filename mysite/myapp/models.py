# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import uuid
from . import utils
from django.contrib.auth.models import User


class Users(models.Model):
    id = models.AutoField(
        db_column="ID", primary_key=True
    )  # Field name made lowercase.
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True, null=True)
    personid = models.CharField(
        db_column="personID",
        unique=True,
        max_length=12,
        default=utils.generate_personid,
    )  # Field name made lowercase.

    uuid = models.CharField(
        db_column="Uuid", unique=True, max_length=100, default=uuid.uuid4
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "users"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="custom_pictures")

    def __str__(self):
        return f"{self.user.username} Profile"
