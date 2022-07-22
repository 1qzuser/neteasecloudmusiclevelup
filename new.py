import json
import requests
import ahttp

api = ""  ###双引号里填你的api，可以本地的3000 也可以拿gitch搭一个 最后那个/要删掉
paassword = ""  ###  把密码用md532位小写加密后的字符串填入双引号里
phone = ""  ###填手机号
countrycode = 1  ###国家码 中国为86

class music163():
    def __init__(self, account, password, api, countrycode):
        self.password = password
        self.account = account
        self.api = api
        self.countrycode = countrycode
        self.session = ahttp.Session()

        self.musiclist = []

        self.headers = {
            "Host": "adventurous-beneficial-centaur.glitch.me",  ###如果修改api记得改头文件
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": '1',

        }


    def login(self):
        data = {
            "phone": self.account,
            "md5_password": self.password,
            "countrycode": self.countrycode,  ##国家码  86为中国
        }
        url = self.api + "/login/cellphone"
        print('下面是登录的账户名称,如果出错则失败')
        self.cookies = self.session.get(url, params=data, headers=self.headers).run().cookies





    def MusicList(self):

        url = self.api + "/personalized?limit=300"
        ##获取推荐歌单列表

        res = json.loads(self.session.get(url).run().text)
        albumlist = res['result']
        print(albumlist)
        count = 1

        for album in albumlist:  ##对获取的推荐歌单列表遍历每一个歌单
            id = album['id']
            url = self.api + "/playlist/track/all"
            data = {
                "id": id,
                "limit": '300'
            }
            musiclist = json.loads(self.session.get(url, params=data).run().text)['songs']
            ##得到某个歌单包含的音乐列表
            for music in musiclist:  ##刷歌
                songid = music['id']
                name = music['name']
                data = {
                    "id": songid,
                    "sourceid": id,

                }
                self.musiclist.append(data)
                count = count+1
                if (count == 320):
                    ##添加到320首歌退出
                    return
    def check(self,datalist):

        url = self.api + "/scrobble"
        reqs = [self.session.get(url, params=data,cookies = self.cookies) for data in datalist]
        resps = ahttp.run(reqs)
        print(resps)


    def main(self):
        self.login()
        self.MusicList()

        self.check(self.musiclist)


def main(event, content):
    music163(phone, paassword, api, countrycode).main()


if __name__ == '__main__':
    music163(phone, paassword, api, countrycode).main()