from django.db import models


class Reader(models.Model):
    reader_title = models.CharField(max_length=80)
    reader_entry = models.TextField()
    reader_date = models.DateTimeField(auto_now=True)

    reader_author = models.CharField(
        max_length=80,
        default='admin'
    )

    def __unicode__(self):
        return self.reader_title
