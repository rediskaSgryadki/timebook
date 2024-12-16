from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from calendar import monthrange
from .models import Note
from .forms import NoteForm

# Главная страница, отображающая список заметок текущего пользователя
def home(request):
    return render(request, 'account/index.html')

# Страница создания новой заметки
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('account_home')
    else:
        form = NoteForm()
    return render(request, 'account/zametka.html', {'form': form})

# Страница календаря с возможностью фильтрации заметок по дате
def kalendar(request):
    current_year = int(request.GET.get('year', datetime.now().year))
    current_month = int(request.GET.get('month', datetime.now().month))
    years = range(2020, 2031)
    months = [
        ("1", "Январь"), ("2", "Февраль"), ("3", "Март"), ("4", "Апрель"),
        ("5", "Май"), ("6", "Июнь"), ("7", "Июль"), ("8", "Август"),
        ("9", "Сентябрь"), ("10", "Октябрь"), ("11", "Ноябрь"), ("12", "Декабрь")
    ]
    first_day_of_month, last_day_of_month = monthrange(current_year, current_month)
    days_in_month = [datetime(current_year, current_month, day) for day in range(1, last_day_of_month + 1)]
    days_count = len(days_in_month)
    missing_days = 7 - (days_count % 7) if days_count % 7 != 0 else 0
    missing_days_list = list(range(1, missing_days + 1)) if missing_days else []
    selected_date = request.GET.get('selected_date')
    if selected_date:
        selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
        notes = Note.objects.filter(user=request.user, created_at__date=selected_date)
    else:
        notes = None
    return render(
        request,
        'account/kalendar.html',
        {
            'current_year': current_year,
            'current_month': current_month,
            'years': years,
            'months': months,
            'days_in_month': days_in_month,
            'missing_days': missing_days_list,
            'notes': notes,
        }
    )

# Страница для просмотра деталей заметки
def zametka_detail(request, id):
    note = get_object_or_404(Note, id=id)
    return render(request, 'account/zametka_detail.html', {'note': note})
