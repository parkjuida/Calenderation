from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from .forms import DiaryForm
from django.utils import timezone
from .models import Diary
from django.core import serializers

import datetime
import calendar
import json

class FullCalenderView(View):
    def get(self, request, *args, **kwargs):
        today_datetime = datetime.datetime.today()
        this_year = today_datetime.year
        this_month = today_datetime.month
        start_day = calendar.monthrange(this_year, this_month)[0]
        end_date = calendar.monthrange(this_year, this_month)[1]
        diary = Diary.objects.filter(date__year=this_year, date__month=this_month)
        diary_dict = dict()
        for dia in diary:
            diary_dict[dia.date.day] = dia.title
        print(diary_dict)
        return render(request, 'calender.html',
                      {'this_year': this_year, 'this_month': this_month,
                       'start_day': start_day, 'end_date': end_date, 'diary_dict': json.dumps(diary_dict)})

class DiaryView(View):
    def get(self, request):
        time = request.GET['time']
        form = DiaryForm()
        return render(request, 'diary.html', {'time': time, 'form': form})

    def post(self, request):
        form = DiaryForm(request.POST)
        date = request.POST['date']
        if form.is_valid():
            diary = form.save(commit=False)
            diary.modified_date = timezone.now()
            diary.date = date
            diary.save()
            return redirect('/')