from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from notes.models import Note
from notes.forms import NoteForm

def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': notes})

def note_create(request):
    form = NoteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return render(request, 'notes/create_success.html')

    return render(request, 'notes/note_create.html', {'form': form})

def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    form = NoteForm(request.POST or None, instance=note)

    if form.is_valid():
        form.save()
        return render(request, 'notes/update_success.html')

    return render(request, 'notes/note_update.html', {'form': form})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    
    note.delete()
    return render(request, 'notes/delete_success.html', {'note': note})
