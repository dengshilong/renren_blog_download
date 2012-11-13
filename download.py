import re
from login import *
      

def get_page(url):#得到网页的内容
        sock = urllib.request.urlopen(url)
        page = sock.read().decode('utf-8')
        return page

def clean_blog_content(content):
    content = re.sub(r'[0-9]?&[a-z]+?;',"",content)#去除&gt等
    content = re.sub(r'\n',"",content)#去除换行符
    content = re.sub(r"<.+?>\.|<.+?>","",content)#去除<p>等
    return content



def get_blog(home,path):#输入首页，得到所有日志
    blog_home = home + "/profile#pblog"#日志首页
    page = get_page(blog_home)
    m = re.search(r'<div class="content-main.+?>[\s\S]+?</div>',page)
    m = re.search('href="(http:.+?)"',m.group(0))
    url = m.group(1)#找到第一篇日志的URL
    f = open(path,'w+')
    while url:
        page = get_page(url)
        m = re.search(r'<div id="blog.*?>([\s\S]+?)</div>',page)#得到日志的内容
        content = m.group(1)
        content = clean_blog_content(content)
        m = re.search(r'<strong>(.+?)</strong>',page)#得到日志的标题
        title = m.group(1)
        m = re.search(r'<span class="timestamp.+?>(.+?) <',page)#得到日志的时间
        time = m.group(1)
        f.write(title + ' ' + time + '\n')
        f.write(content + '\n\n')
        m = re.search(r'<a href="(http://.+?)" title="(.+?)">较旧一篇',page)
        if  m:
            if re.match(r"没有较旧一篇啦",m.group(2)):
                url = []
            else:
                url = m.group(1)#得到下一篇文章URL
        else:
            url = []
    f.close()

if __name__ == '__main__':
    email = ''
    password = ''
    path = r''
    rr = Renren()
    home = rr.login(email,password)
    get_blog(home,path)
    	
    
    
   
    



