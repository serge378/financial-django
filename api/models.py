from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class CategorieFormation(models.Model):
    class Meta:
        verbose_name = "Categorie de formation"
        verbose_name_plural = "Categorie de formation"

    nom = models.CharField(max_length=100)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Date de création"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Date de modification"
    )

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.nom = self.nom.capitalize()
        super(CategorieFormation, self).save(*args, **kwargs)


class VideoFormation(models.Model):
    class Meta:
        verbose_name = "Video de formation"
        verbose_name_plural = "Videos de formation"

    titre = models.CharField(max_length=100)
    video = models.FileField(upload_to="videos-formations", verbose_name="Video")
    prix = models.PositiveIntegerField(verbose_name="Prix")
    description = models.TextField(blank=True)
    downloadNumber = models.PositiveIntegerField(
        verbose_name="Nombre de téléchargements", default=0, editable=False
    )
    poster = models.ImageField(upload_to="videos", verbose_name="Poster")
    note = models.DecimalField(
        verbose_name="Note", default=0, max_digits=2, decimal_places=1, editable=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Date de création"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Date de modification"
    )
    categorie = models.ForeignKey(
        CategorieFormation, on_delete=models.CASCADE, related_name="videos"
    )
    access_by = models.ManyToManyField(
        User, related_name="video_formations", blank=True
    )

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        self.titre = self.titre.capitalize()
        super(VideoFormation, self).save(*args, **kwargs)


class PaymentVideo(models.Model):
    site_id = models.CharField(max_length=255)
    transaction_id = models.CharField(max_length=255)
    transaction_date = models.DateTimeField(
        verbose_name="Date et heure de la transaction",
        blank=True,
        null=True,
        auto_now_add=True,
    )
    amount = models.IntegerField(verbose_name="montant", blank=True, null=True)
    devise = models.CharField(max_length=4, blank=True, null=True)
    payment_method = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    phone_prefix = models.CharField(max_length=255, blank=True, null=True)
    error_message = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255)
    video = models.ForeignKey(
        VideoFormation, on_delete=models.CASCADE, related_name="payments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="paid_videos"
    )
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.transaction_id
