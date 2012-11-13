import re
from login import *
      

def get_page(url):#get the content
        sock = urllib.request.urlopen(url)
        page = sock.read().decode('utf-8')
        return page

def clean_blog_content(content):
    content = re.sub(r'[0-9]?&[a-z]+?;',"",content)#clean &gt etc.
    content = re.sub(r'\n',"",content)#clean '\n'
    content = re.sub(r"<.+?>\.|<.+?>","",content)#clean <tag>
    return content



def get_blog(home,path):#input the homepage, get all blogs
    blog_home = home + "/profile#pblog"#blog home
    page = get_page(blog_home)
    m = re.search(r'<div class="content-main.+?>[\s\S]+?</div>',page)
    m = re.search('href="(http:.+?)"',m.group(0))
    url = m.group(1)#find the url of first blog
    f = open(path,'w+')
    while url:
        page = get_page(url)
        m = re.search(r'<div id="blog.*?>([\s\S]+?)</div>',page)#get the content
        content = m.group(1)
        content = clean_blog_content(content)
        m = re.search(r'<strong>(.+?)</strong>',page)#get title
        title = m.group(1)
        m = re.search(r'<span class="timestamp.+?>(.+?) <',page)#get time
        time = m.group(1)
        f.write(title + ' ' + time + '\n')
        f.write(content + '\n\n')
        m = re.search(r'<a href="(http://.+?)" title="(.+?)">较旧一篇',page)
        if  m:
            if re.match(r"没有较旧一篇啦",m.group(2)):
                url = []
            else:
                url = m.group(1)#get the url of next blog
        else:
            url = []
    f.close()

if __name__ == '__main__':
    email = ''#user name
    password = ''#password
    path = r''#file path
    rr = Renren()
    home = rr.login(email,password)
    get_blog(home,path)
    	
    
    
   
    



