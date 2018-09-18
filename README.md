# info_notify
> 需要*requests* *pyquery*库，需要一台服务器

1. ssh连接服务器

2. 下载源代码`git clone git@github.com:wzx140/info_notify.git`
3. 按照注释，修改notify.py中的**my_sender** , **my_pass** , **my_user**变量
4. 使得会话持久化`screen -S info_notify`
5. 运行脚本`python info_notify/fetch.py`
> 注：需要python 3.5以上版本

------------


日志文件在`info_notify/log.txt`中