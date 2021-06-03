from django.contrib import admin
from .models import PostModel,PostImageModel,PositiveVote,NegativeVote,PostComment


admin.site.register(PostModel)
admin.site.register(PostImageModel)
admin.site.register(PositiveVote)
admin.site.register(NegativeVote)
admin.site.register(PostComment)
