
import requests         #替代python2和python3里的url_lib，很好用
import json


class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key           #给api_key实例化
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "#这里缺少云片网里的模板，模板需要网站域名才可以".format(code=code)
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict

if __name__ == "__main__":
    yun_pian = YunPian("bc9adac425c9fafcdc91194ada06e149")  #这里的API_KEY是从云片网获得
    yun_pian.send_sms("2020", "17380128079")



