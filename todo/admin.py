from django.contrib import admin

from .models import User, Task, SubTask, Block, SubBlock, Tag

admin.site.register(User)

admin.site.register(Task)
admin.site.register(SubTask)

admin.site.register(Block)
admin.site.register(SubBlock)


admin.site.register(Tag)