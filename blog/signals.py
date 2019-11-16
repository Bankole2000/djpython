from django.db.models.signals import post_delete

from django.dispatch import receiver 
from django.contrib import messages
from .models import Post

# success_message = '📖 Post has been Deleted 💣 ✖️ 👍 '

# @receiver(post_delete, sender=Post)
# def delete_post(sender, instance, deleted, **kwargs): 
#   messages.success(sender.request, success_message)

def delete_post(sender, **kwargs): 
  print('Post Deleted')

post_delete.connect(delete_post, sender=Post)