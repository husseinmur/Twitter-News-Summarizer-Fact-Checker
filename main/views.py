from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import os

def index(request):
    return render(request, 'index.html')

def get_data(t,s,p):
    if (t=='1'):
        df = pd.read_parquet(os.path.join(os.path.dirname(os.path.dirname(__file__)),'static\dfs\lebanon.parquet'))
    elif (t=='2'):
        df = pd.read_parquet(os.path.join(os.path.dirname(os.path.dirname(__file__)),'static\dfs\elon.parquet'))
    elif (t=='3'):
        df = pd.read_parquet(os.path.join(os.path.dirname(os.path.dirname(__file__)),'static\dfs\messi.parquet'))     
    elif (t=='5'):
        df = pd.read_parquet(os.path.join(os.path.dirname(os.path.dirname(__file__)),'static\dfs\exit.parquet')) 
    if (p=='24'):
        date = '2019-11-25';
    elif (p=='48'):
        date = '2019-11-24';
    elif (p=='72'):
        date = '2019-11-23';
    return df[df['datetime']>date][df['show']&df['lang'].str.contains('en')]['text'][:int(s)].tolist()
    
def ajax(request):
    if request.is_ajax() and request.method == 'POST':
        topic = request.POST['topic']
        size = request.POST['size']
        period = request.POST['period']
        resp_data = {
            'data': get_data(topic,size,period),
        }
        return JsonResponse(resp_data, status=200)