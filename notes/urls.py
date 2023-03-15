from django.urls import path
from notes.views import notes_list, note_create, note_update, note_delete

urlpatterns = [
    path('', notes_list, name='list'),
    path('create/', note_create, name='create'),
    path('update/<int:pk>/', note_update, name='update'),
    path('delete/<int:pk>/', note_delete, name='delete'),
]
