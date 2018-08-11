from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    path = models.CharField(max_length=10, default='')
    tile = models.ImageField()
    img_main = models.ImageField(blank=True)
    description = models.TextField(blank=True, default='')
    text = models.TextField(blank=True, default='')
    detail = models.TextField(blank=True, default='')
    created = models.DateField(default='')
    is_published = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created',)


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()
    bg_color = models.CharField(max_length=7, default='#f2f2f2')

    DESK = 'Desk'
    MOBI = 'Mobile'
    LOGO = 'Logo'
    FULL = 'Full Width'
    IMAGE_TYPE_CHOICES = (
        (DESK, 'Desktop'),
        (MOBI, 'Mobile'),
        (LOGO, 'Logo'),
        (FULL, 'Full Width'),
    )
    image_type = models.CharField(
        max_length=4,
        choices = IMAGE_TYPE_CHOICES,
        default = DESK,
    )

    def has_bar(self):
        if image_type == DESK:
            return True
        elif image_type == LOGO:
            return False
        else:
            pass
