from django.db import models
import datetime
from django.utils import timezone

class Article(models.Model):
	article_title = models.CharField('Название статьи', max_length = 200)
	article_text = models.TextField('Текст статьи')
	pub_date = models.DateTimeField('Дата публикации')

	def __str__(self):
		return self.article_title

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name = models.CharField('Имя пользователя', max_length = 200)
	comment_text = models.TextField('Текст комментария')
	comment_date = models.DateTimeField('Дата публикации', default=timezone.now)

	def __str__(self):
		return self.author_name
	
	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'