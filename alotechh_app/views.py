import datetime
import json

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from .models import CallList
from django.http import HttpResponse, JsonResponse

def home_view(request):
    return render(request, 'index.html')


def search_view(request):
    if request.method == "POST":
        if 'get-call-info' in request.POST:
            call_id = request.POST.get('call-id')
            query_result = CallList.objects.get(id=call_id)
            return HttpResponse(json.dumps({'call-date': query_result.calldate,'call-num': query_result.called_num,
                                            'call-Id': query_result.callid,
                                            'duration': query_result.duration,
                                            'answered': query_result.answered,
                                            'campaign_name': query_result.campaign_name,
                                            'voicemail': query_result.Voicemail,
                                            'channel': query_result.channel,
                                            'agent': query_result.agent,},
                                           cls=DjangoJSONEncoder), content_type='application/json')
        start_date = request.POST.get('Call-date')
        hang_date = request.POST['Hang-date']
        call_list = CallList.objects.filter(calldate__contains=start_date, hangupdate__contains=hang_date)
        print(call_list.count())
        call_list_count = call_list.count()
    return render(request, 'search-listing.html', {'call_list': call_list, 'call_list_count': call_list_count})



