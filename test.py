import requests
comid=34667
# tethys.icimod.org
# AuthorizationToken='Token 93eae5155d3c551cd5d449e896cf707869b63eb2'

# 197
# AuthorizationToken='Token 5dbd19a9260f6b5c8dbace67aa2894ee66879ba8'

# localhost
AuthorizationToken='Token 44f3bf6a3c2ba05a104a709f15319416659aec6c'

# APIHost='http://tethys.icimod.org'
# APIHost='http://110.34.30.197'
APIHost='http://localhost:8000'
url=APIHost+'/apps/apicenter/ECMWFapi/getEnsembleCSVECMWF'
# url=APIHost+'/apps/streamflowhkh/chart'
request_params1={"comid":comid,'cty':'nepal','stID':comid}
request_headers1={'Authorization':AuthorizationToken}

with requests.Session() as s:
    response = s.get(url,params=request_params1,headers=request_headers1)
    print(response.text)


