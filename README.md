# centos7.setup
> Linux cmd library

*Linux各种命令学习文档，在这里收集*


- 查看日志常用命令
<code><pre>
//显示filename最后20行
tail -n 20 filename
</pre></code>


- linux之间实现远程传输文件
> 输入：scp /home/helpteach/project/mallupload/1509681299449.png wasadmin@10.127.40.25:/home/test
> wasadmin@10.127.40.25:/home/test 为远程服务器的账号、IP、目录


- 查看当前文件大小
> du -sh *


### 创建用户并授权指定目录

- 在root下执行
> groupadd  admin   // 创建一个组admin

- 创建用户
> useradd -m -g admin wu    // 在用户组admin下新增用户wu

- 设置用户密码
> passwd  wu     // 给用户wu设置密码，按回车输密码


- 切换到home目录，在root用户下给uiadm授权
> chmod 775 -R wu

### CURL 发送POST请求
```
curl -H "Content-Type: application/json" -X POST -d '{"user_id": "123", "coin":100, "success":1, "msg":"OK!" }' "http://192.168.0.1:8001/test"
```
| 参数 | 内容 | 参考 |
| ---- | ---- | ---- |
| -H | 请求头 | Content-Type: application/json |
| -d | POST内容 | {"user_id": "123", "coin":100} |
| -X | 请求协议 | POST |
| -A | 代理 | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36 |
| -b | Cookie | foo=bar&user=admin |

