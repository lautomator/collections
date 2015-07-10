from django.db import models


class Publication(models.Model):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    pub_date = models.IntegerField()  # Format ex: 1970
    # The categories list (genres):
    CATEGORIES = (
        ('OTH', 'Other'),
        ('PHI', 'Philosophy'),
        ('FIC', 'Fiction'),
        ('NON', 'Non-Fiction'),
        ('PER', 'Performing Arts'),
        ('VIS', 'Visual Arts'),
        ('WEB', 'Web Authoring'),
        ('COM', 'Computer Science'),
    )
    category = models.CharField(
        max_length=3,
        choices=CATEGORIES,
        default='OTH',
    )

    def __unicode__(self):
        return self.title
