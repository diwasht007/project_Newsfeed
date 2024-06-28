from django.db import models

# Create your models here.
class Newsfeed(TimeStampedModel):
    id = UUIDField()
    post = models.TextField()
    file_url = models.TextField(null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_newsfeeds")
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL, related_name="client_newsfeeds")
    seen = models.ManyToManyField(NewsfeedStatus, blank=True, related_name="user_viewed_newsfeed")
    allow_comment = models.BooleanField(default=True)
    requires_confirmation = models.BooleanField(default=False)
    images = models.ImageField(upload_to="newsfeed/images", blank=True, null=True)
    shift = models.ForeignKey(Shifts, on_delete=models.CASCADE, related_name="newsfeed_shifts", null=True, blank=True)
    allowed_users = models.JSONField(default={})