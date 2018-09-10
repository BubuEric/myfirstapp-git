html = """
<ul class="pure-g">
    <li class="pure-u-1-2 pure-u-md-1-6"><i class="icon iconfont icon-shoucang"></i><a
            class="item" rel="537" target="_blank"
            href="http://www.dasudy.com/vod-type-id-3-wd--letter--year-0-area--order-hits-p-2.html">达速动漫区</a>
    </li>
</ul>
insert into tagurl(name,url,addtime,tagname_id) values(8,8,now(),1);
"""
from pyquery import PyQuery as pq
doc = pq(html)
data = doc('li a').items()

for a in data:
    url = a.attr['href']
    name = a.text()
    #print("insert into tagurl(tagname_id) values(10);")
    print("insert into tagurl(name,url,addtime,tagname_id) values('{}','{}',now(),45);" .format(name,url))