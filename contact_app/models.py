from django.db import models



class DeliverMassage(models.Model):
    name = models.CharField(max_length=20, verbose_name="نام")
    subject = models.CharField(max_length=50, verbose_name="عنوان")
    email = models.EmailField(verbose_name="ایمیل")
    message = models.TextField(verbose_name="متن پیام")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "پیام دریافتی"
        verbose_name_plural = "پیام های دریافتی"


class EditInformation(models.Model):
    phone_number = models.CharField(max_length=13, verbose_name="شماره تماس")
    email = models.EmailField(verbose_name="ایمیل")
    address = models.CharField(max_length=100, verbose_name="آدرس")


    class Meta:
        verbose_name = "راه ارتباط"
        verbose_name_plural = "راه های ارتباطی"



