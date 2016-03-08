import urllib2, urllib, cookielib

class Renren:

    def __init__(self):
        self.operate = ''
        cookie = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        urllib2.install_opener(self.opener)
        
    def login(self,email,pwd):
        ERROR_URL_PREFIX = "http://www.renren.com/SysHome.do?origURL=http%3A%2F%2F"
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent}
        params = {'domain':'renren.com','origURL':'http://www.renren.com/indexcon','email':email,'password':pwd}
        params = urllib.urlencode(params)
        params = params.encode('ISO-8859-1')
        req = urllib2.Request('http://www.renren.com/PLogin.do',params,headers)
        self.operate = self.opener.open(req)
        url =  self.operate.geturl()
        if ERROR_URL_PREFIX in url:
            return False
        else:
            return url      
