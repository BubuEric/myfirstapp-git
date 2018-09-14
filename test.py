html = """
<ul class="pure-g">
    <li class="pure-u-1-2 pure-u-md-1-6"><i class="icon iconfont icon-shoucang"></i><a class="item" rel="7"
                                                                                       target="_blank"
                                                                                       href="https://rarbg.is/torrents.php">rarbg</a>
    </li>
    <li class="pure-u-1-2 pure-u-md-1-6"><i class="icon iconfont icon-shoucang"></i><a class="item" rel="9"
                                                                                       target="_blank"
                                                                                       href="https://limetorrents.unblocked.pl/">lime</a>
    </li>
    <li class="pure-u-1-2 pure-u-md-1-6"><i class="icon iconfont icon-shoucang"></i><a class="item" rel="10"
                                                                                       target="_blank"
                                                                                       href="https://monova.org/">Monova</a>
    </li>
    <li class="pure-u-1-2 pure-u-md-1-6"><i class="icon iconfont icon-shoucang"></i><a class="item" rel="11"
                                                                                       target="_blank"
                                                                                       href="http://rutracker.org/forum/index.php">俄站</a>
    </li>
    <li class="pure-u-1-2 pure-u-md-1-6"><i class="icon iconfont icon-shoucang"></i><a class="item" rel="13"
                                                                                       target="_blank"
                                                                                       href="https://eztv.ag/">eztv美剧</a>
    </li>
    <li class="pure-u-1-2 pure-u-md-1-6"><i class="icon iconfont icon-shoucang"></i><a class="item" rel="14"
                                                                                       target="_blank"
                                                                                       href="http://pianyuan.net/">片源网</a>
    </li>
    <li class="pure-u-1-2 pure-u-md-1-6"><i class="icon iconfont icon-shoucang"></i><a class="item" rel="15"
                                                                                       target="_blank"
                                                                                       href="https://torrentking.eu/">
        torrentking</a></li>
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
    print("insert into tagurl(name,url,addtime,tagname_id) values('{}','{}',now(),5);" .format(name,url))