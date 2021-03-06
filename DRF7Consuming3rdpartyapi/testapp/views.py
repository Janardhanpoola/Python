from django.shortcuts import render

import requests

# Create your views here.

def get_geographic_info(request):
    
    ip=request.META.get('HTTP_X_FORWARDED_FOR',"") or request.META.get('REMOTE_ADDR')

    #http://api.ipstack.com/116.197.184.16?access_key=e54a0447077a957f6d4deee9815a63c1
     
    #url="http://api.ipstack.com/"+ip+"?access_key=e54a0447077a957f6d4deee9815a63c1"


    url="http://api.ipstack.com/116.197.184.16?access_key=e54a0447077a957f6d4deee9815a63c1"
    response=requests.get(url)

    data=response.json()
    print(data)
    
#    return render(request,'testapp/smpl.html',{'data':data}) # data is dictionary..so we can use {{data.ip}} in smpl.html

    return render(request,'testapp/smpl.html',data) #this is context..where the keys of json data can be directly accessed ..i.e {{ip}} in smpl.html


