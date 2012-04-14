from polls.models import Poll
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
  fields = ['pub_date', 'question']

admin.site.register(Poll, PollAdmin)