from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create a Post Model
# keep track with DateTimeField()
#  auto_now=True; we could update the date posted
# to the current date time every time the post was updated
#  auto_now_add=True; set the date posted to the current date time only
# when the object is created. But it can't ever be updated.

# We need a author for each post. THe user who created the post.
# One user can have multiple posts. So its a one-to-many relationship.
# So Foreign key is used here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if user gets deleted then post will be deleted aswell
    
    # dunder(double underscore) STR method
    # magic methods
    def __str__(self):
        return self.title