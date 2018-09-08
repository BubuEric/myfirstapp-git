import requests,re
from flask import Flask
from flask import request

@app.route('/zyw/zxdy/')
def bwzy_pc():  # 传进来的这个值是要搜索影视名
    value = request.args.get('s')
    zztj = '''<script type="text/javascript">var cnzz_protocol = (("https:" == document.location.protocol) ? " https://" : " http://");document.write(unescape("%3Cspan id='cnzz_stat_icon_1274386182'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s22.cnzz.com/z_stat.php%3Fid%3D1274386182%26show%3Dpic1' type='text/javascript'%3E%3C/script%3E"));</script>'''
    url = "http://www.baiwanzy.com/index.php?m=vod-search"
    data = {'wd': value, 'submit': 'search'}
    headers = {'Referer': 'http://www.baiwanzy.com/index.php?m=vod-search',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    try:
        req = (requests.post(url=url, data=data, headers=headers).text).encode('ISO-8859-1').decode(
            'utf-8')  # 以post提交数据
        re_url = re.findall('<div class="xing_vb">.*?<ul>.*?<li>.*?<a href="(.*?)".*?</ul>.*?</div>', req, re.S)[
            0]  # 比配搜索到的第一个链接
        url_b = 'http://www.baiwanzy.com'
        if (re_url == url_b):
            return ('嗷，居然没有找到！换个短的关键词试试！')  # 如果没有搜索结果则返回这个
        else:
            url_2 = url_b + re_url  # 拼接第二个URL
            req_url_2 = (requests.get(url_2).text).encode('ISO-8859-1').decode('utf-8')  # 以get的方式请求源码
            re_pm = re.findall('<div class="vodh">.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>', req_url_2, re.S)[0][
                0]  # 比配片名
            re_lj = re.findall('<div class="vodplayinfo">.*?<ul>(.*?)</ul>.*?</div>', req_url_2, re.S)[0]  # 比配播放链接
            re_lj = re_lj.strip()  # 去掉中前后的空白符
            re_mb = re.findall('<li>.*?/>(.*?)</li>', re_lj, re.S)  # 对数据进行最后的清洗
            r = 1
            html = ''
            for i in re_mb:
                re_i = re.findall('.*?http(.*)', i, re.S)[0]  # 考虑之后决定这里再比配一次链接
                htm = '第%d集<a href="http%s">http%s</a><br>' % (r, re_i, re_i)  # 这里拼接超链接
                r = r + 1
                html = html + htm
            return re_pm + '<br>' + html + zztj
    except:
        return '啥？出现未知错误。'  # 当爬虫出现错误时返回这个


if __name__ == '__main__':
    app.run(port='6600', host='0.0.0.0')  #