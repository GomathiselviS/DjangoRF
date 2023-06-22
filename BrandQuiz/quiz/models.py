from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quizzes(models.Model):
    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ["id"]

    title = models.CharField(
        max_length=255, default=_("New Quiz"), verbose_name=_("Quiz Title")
    )
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Updated(models.Model):
    date_updated = models.DateTimeField(verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True


class Slogan(Updated):
    class Meta:
        verbose_name = _("Slogan")
        verbose_name_plural = _("Slogans")
        ordering = ["id"]

    quiz = models.ForeignKey(
        Quizzes, related_name="slogan", on_delete=models.DO_NOTHING
    )
    question = models.CharField(max_length=255, verbose_name=_("TagLine"))
    date_created = models.DateTimeField(auto_now=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return self.question


class Brand(Updated):
    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")
        ordering = ["id"]

    slogan = models.ForeignKey(
        Slogan, related_name="brand", on_delete=models.DO_NOTHING
    )
    brand_text = models.CharField(max_length=255, verbose_name=_("Brand Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.brand_text
