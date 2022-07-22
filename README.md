##### 网易云快速刷歌300首 快速升级
# 食用方法
下载项目下的py文件，配好环境后在phone,api,countrycode,md5_password中填入对应的数据运行即可
mypy是同步请求  需要request库
asy post是异步请求 需要ahttp库
# 环境要求
#### 本地部署(每天手动执行)
安装request/ahttp库的python,node.js,Binaryify的网易云api 
https://github.com/Binaryify/NeteaseCloudMusicApi
api的安装方式在仓库里有


#### 云端部署 (需要服务器/github账号 云函数的账号 推荐华为云)
api部署到服务器的方式可以参考
https://zaincheung.gitee.io/netease-cloud/#/api/remix
大概流程如下
先复制网易云api的仓库地址
https://github.com/Binaryify/NeteaseCloudMusicApi
到https://glitch.me/ 新建项目，选择import form github
把复制的仓库地址拷贝进去，等待项目部署完成，拷贝api
python文件可以随便找个云函数来部署，云函数部署方式大差不差，注意下函数入口就是了，一般是“文件名.函数名的格式”,像本项目的文件应该是my.main 

## 说明
本地部署响应时间短，运行快，云端部署，api在国外服务器，响应时间长，运行速度偏慢，不过反正是云函数 也无所谓。
实现思路是获取推荐歌单，再获取歌单里面的歌曲，然后调用听歌打卡的接口刷歌，所以为了防止300首歌有重复的歌曲，每次都挺320首。
