from django.db import models
import uuid

# C
class Bathroom(models.Model):
    owner = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image = models.TextField(null=True, blank=True)
    reviews = models.TextField(max_length=2000)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null= True, blank=True)
    vote_ratio = models.IntegerField(default=0, null= True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    
    def __str__(self):
        return self.owner
class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'UP VOTE'),
        ('down', 'Down VOTE'),
    )
    #owner = models.CharField(max_length=)
    Bathroom = models.ForeignKey(Bathroom, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value

class ImageUpload(models.Model):

    bathroom = models.ForeignKey(
        Bathroom,
        on_delete=models.CASCADE,
        related_name='imagesUploads',
    )
    preview_url = models.CharField(max_length=200, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.preview_url

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name