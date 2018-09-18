from pyquery import PyQuery as pq
import requests 
import log
import time
import notify

# 南航招生信息列表
url = 'http://cmee.nuaa.edu.cn/news_more.asp?lm2=9'

# 模拟请求头
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3534.4 Safari/537.36',
          'Host':'cmee.nuaa.edu.cn',}

# 请求html页面
def get_page(url):
    res = requests.get(url,headers=headers)
    if res:
        log.log_info('fetch:访问'+url)
        page = res.content.decode('GBK')
        return page,url
    else:
        log.log_error('fetch:访问'+url+'失败')

# 解析新闻列表
def get_news_list(param):
    ob_url = param[1]
    page = param[0]
    doc = pq(page)
    try:
        trs = doc('td[valign="top"] tr tr:eq(4) table tr').items()
        news_list = []
        for tr in trs:
            news = {}
            #新闻日期
            date = tr('td:eq(2)').text().replace('(','').replace(')','').strip()
            news['date'] = date
            #新闻url
            url = tr('td:eq(1) a').make_links_absolute('http://cmee.nuaa.edu.cn/').attr.href
    #         print(url)
            news['url'] = url
            #新闻标题
            title = tr('td:eq(1) a font').text()
            news['title'] = title

            news_list.append(news)
        if news_list:
            log.log_debug('fetch:解析列表成功'+ str(news_list))
            return news_list
        else:
            log.log_error('fetch:解析列表错误'+ob_url+'网站规则可能发生变化')
    except:
        log.log_exception('fetch:解析列表错误'+ob_url+'网站规则可能发生变化')
        

if __name__ == '__main__':
    log.log_debug('fetch:初始化')
    page = get_page(url)
    news_list = get_news_list(page)
    orgin_new = news_list[0]['title']
#     orgin_new = '机电学 院 2018年招收工程博士招考拟录取名单第二批'
    while(True):
        page = get_page(url)
        news_list = get_news_list(page)
        if news_list:
            news = news_list[0]['title']
            if news != orgin_new:
                log.log_info('fetch:检测到信息更新')
                html,url = get_page(news_list[0]['url'])
    #             log.log_debug('fetch:'+html)
                notify.send(news,html)
                orgin_new = news
        log.log_debug('fetch:暂停300s')
        time.sleep(300)