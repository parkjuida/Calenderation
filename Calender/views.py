from django.shortcuts import render
from django.views.generic import View
import datetime
import calendar

class FullCalenderView(View):
    def get(self, request, *args, **kwargs):
        today_datetime = datetime.datetime.today()
        this_year = today_datetime.year
        this_month = today_datetime.month
        start_day = calendar.monthrange(this_year, this_month)[0]
        end_date = calendar.monthrange(this_year, this_month)[1]
        return render(request, 'calender.html',
                      {'this_year': this_year, 'this_month': this_month, 'start_day': start_day, 'end_date': end_date})

class DiaryView(View):
    def get(self, request):
        time = request.GET['time']
        return render(request, 'diary.html', {'year': time, })