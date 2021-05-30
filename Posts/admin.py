from django.contrib import admin
from .models import PostModel,PostImageModel,PositiveVote,NegativeVote


admin.site.register(PostModel)
admin.site.register(PostImageModel)
admin.site.register(PositiveVote)
admin.site.register(NegativeVote)
