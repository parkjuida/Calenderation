from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from .forms import DiaryForm
from django.utils import timezone
from .models import Diary
from django.utils.datastructures import MultiValueDictKeyError

import datetime
import calendar
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class FullCalenderView(View):
    def get(self, request, *args, **kwargs):
        try:
            this_datetime = request.GET['date']
            this_datetime = datetime.datetime.strptime(this_datetime, '%Y-%m-%d')
        except MultiValueDictKeyError:
            this_datetime = datetime.datetime.today()
        this_year = this_datetime.year
        this_month = this_datetime.month
        start_day = calendar.monthrange(this_year, this_month)[0]
        end_date = calendar.monthrange(this_year, this_month)[1]
        diaries = Diary.objects.filter(created_date__year=this_year, created_date__month=this_month)
        diary_dict = dict()
        for diary in diaries:
            diary_dict[diary.date.day] = diary.title
        return render(request, 'calender.html',
                      {'this_year': this_year, 'this_month': this_month,
                       'start_day': start_day, 'end_date': end_date, 'diary_dict': json.dumps(diary_dict)})


class DiaryList(View):
    def get(self, request):
        this_datetime = request.GET['date']
        this_datetime = datetime.datetime.strptime(this_datetime, '%Y-%m-%d')
        diary = Diary.objects.filter(created_date__year=this_datetime.year,
                                     created_date__month=this_datetime.month,
                                     created_date__day=this_datetime.day)
        return render(request, 'diary.html', {'diary_list': diary, 'date': this_datetime})


class DiaryDetail(View):
    def get(self, request):
        this_datetime = request.GET['date']
        form = DiaryForm()
        return render(request, 'diary_detail.html', {'date': this_datetime, 'form': form})

    def post(self, request):
        form = DiaryForm(request.POST)
        date = request.POST['date']
        if form.is_valid():
            diary = form.save(commit=False)
            diary.modified_date = timezone.now()
            diary.date = date
            diary.save()
            return redirect('?time=' + date)
