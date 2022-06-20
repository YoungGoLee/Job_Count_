from django.shortcuts import render

import datetime as dt
import pytz as tz


# Create your views here.
def home(request):
    return render(request, 'index.html')


def count(request):
    jobs = int(request.POST['jobs'])
    hours = int(request.POST['hours'])
    minutes = int(request.POST['minutes'])
    seconds = int(request.POST['seconds'])

    print(jobs)
    print(hours)
    print(minutes)
    print(seconds)

    job_out = 3600 / jobs

    print(job_out)

    now_time = dt.datetime.now(tz.timezone('Asia/Seoul')).time()
    end_time = dt.time(hours, minutes, seconds)

    def second_interval(start, end):
        reverse = False
        if start > end:
            start, end = end, start
            reverse = True

        delta = (end.hour - start.hour) * 3600 + (end.minute - start.minute) * 60 + (end.second - start.second)
        if reverse:
            delta = 24 * 60 * 60 - delta
        return delta

    job_count = second_interval(now_time, end_time) / job_out

    print(job_count)

    return render(request, 'count.html', {'job_count': job_count})