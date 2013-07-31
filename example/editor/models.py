from django.db import models
from django.core.urlresolvers import reverse


class Comment(models.Model):
    comment = models.TextField()

    def __unicode__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("comments_comment_detail", kwargs={"pk": self.id})