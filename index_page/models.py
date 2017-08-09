from django.db import models


class TypeImage(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
# Create your models here.


class Image(models.Model):
    JPEG = 'JPEG'
    PNG = 'PNG'
    IMAGE_EXTENSION = (
        (JPEG, 'jpeg'),
        (PNG, 'png'),
    )
    name = models.CharField(max_length=60)
    extension = models.CharField(max_length=4,
                                 choices=IMAGE_EXTENSION,
                                 default=JPEG)
    image = models.FileField(upload_to='img/gallery', blank=False, null=True)
    type_image = models.ForeignKey(TypeImage, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def slice_ref(self):
        ref = str(self.image)
        i = ref.find('img/')
        return ref[i:len(ref)]






