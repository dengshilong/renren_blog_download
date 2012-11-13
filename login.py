import urllib.request

class Renren:

    def __init__(self):
        self.operate = ''
        try:
            self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
            urllib.request.install_opener(self.opener)
        except Exception as e:
            print(str(e))
        
    def login(self,email,pwd):
        ERROR_URL_PREFIX = "http://www.renren.com/SysHome.do?origURL=http%3A%2F%2F"
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent}
        params = {'domain':'renren.com','origURL':'http://www.renren.com/indexcon','email':email,'password':pwd}
        params = urllib.parse.urlencode(params)
        params = params.encode('ISO-8859-1')
        req = urllib.request.Request('http://www.renren.com/PLogin.do',params,headers)
        self.operate = self.opener.open(req)
        url =  self.operate.geturl()
        if ERROR_URL_PREFIX in url:
            return False
        else:
            return url      




    
    
   
    



