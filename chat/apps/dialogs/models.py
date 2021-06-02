from django.db import models


class Dialog(models.Model):
    dialog_theme = models.CharField('Тема диалога', max_length=200)

    def __str__(self):
        return self.dialog_theme

    class Meta:
        verbose_name = 'Беседа'
        verbose_name_plural = 'Беседы'


class Message(models.Model):
    dialog = models.ForeignKey(Dialog, on_delete=models.CASCADE)
    author_name = models.CharField('Имя участника', max_length=200)
    message_txt = models.TextField('Текст сообщения')

    def __str__(self):
        return self.message_txt

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
