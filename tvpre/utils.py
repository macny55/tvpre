# -*- encoding: utf-8 -*-
import json,urllib2,urllib
import datetime
import contextlib
from BeautifulSoup import BeautifulSoup
# KEYとURLはsettings.pyにある
from settings import *

class ProgramList(object):
    def __init__(self,user_id=None):
        self.user_id = user_id
        
    def _search_content(self,response_data,pg_list):
        for response in response_data:
            score = self._cal_score(response['title'].encode('utf-8') + response['subtitle'].encode('utf-8'))
            pg_dict = {'pg_id':response['id'],'start_time':response['start_time'],'end_time':response['end_time'],'title':response['title'].encode("utf-8"),'sub_title':response['subtitle'].encode("utf-8"),'score':score}
            pg_list.append(pg_dict)
        return pg_list

    def _cal_score(self,strings):
        # like_wordsは本来はDBから取ってくる辞書{単語:点数(抽出数)}
        like_words = {u'マッサン':10,u'スポーツ':20}
        params = urllib.urlencode({'appid':YAHOO_API_KEY, 'results':'ma', 'filter':'9', 'sentence':strings})
        nouns = urllib2.urlopen(YAHOO_API_URL,params)
        soup = BeautifulSoup(nouns.read())
        noun_list = [w.surface.string for w in soup.ma_result.word_list]
        score = sum([like_words[i] for i in noun_list if like_words.has_key(i)])
        return score

    def recommend_pg_list(self,area,service):
        pg_list = []
        for s in service:
            url_list_today    = [area,s,str(datetime.date.today())]
            url_list_tomorrow = [area,s,str(datetime.date.today() + datetime.timedelta(days=1))]
            url_today    = NHK_API_URL + '/'.join(url_list_today) + '.json?key=' + NHK_API_KEY
            url_tomorrow = NHK_API_URL + '/'.join(url_list_tomorrow) + '.json?key=' + NHK_API_KEY
            with contextlib.closing(urllib2.urlopen(url_today)) as r_today:
                response_today = json.loads(r_today.read())
                pg_list = self._search_content(response_today['list'][str(s)],pg_list)
            with contextlib.closing(urllib2.urlopen(url_tomorrow)) as r_tomorrow:
                response_tomorrow = json.loads(r_tomorrow.read())
                pg_list = self._search_content(response_tomorrow['list'][str(s)],pg_list) 
        return sorted(pg_list, key=lambda x:x['score'],reverse=True)


