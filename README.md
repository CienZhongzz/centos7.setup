# Linux命令学习，以centos7.x为例

日常工作中所用到的命令、安装指引和库相关信息收集
- [git](https://github.com/Cienzhong/linux.study/blob/master/git.helper.md)
- [golang](https://github.com/Cienzhong/linux.study/blob/master/go%E5%AE%89%E8%A3%85%E5%92%8C%E9%83%A8%E7%BD%B2.md)
- [挂载共享目录](https://github.com/Cienzhong/linux.study/blob/master/linux%E4%BD%BF%E7%94%A8mount%E5%91%BD%E4%BB%A4%E6%8C%82%E8%BD%BDwindows%E5%85%B1%E4%BA%AB%E6%96%87%E4%BB%B6%E5%A4%B9.md)
- [mysql](https://github.com/Cienzhong/linux.study/blob/master/mysql%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE.md)
- [redis](https://github.com/Cienzhong/linux.study/blob/master/redis%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%AE%89%E8%A3%85%E6%96%B9%E6%B3%95%E4%B8%8E%E5%90%AF%E5%8A%A8%E6%95%99%E7%A8%8B.md)
- [nginx](https://github.com/Cienzhong/linux.study/blob/master/nginx.helper.md)
- [python](https://github.com/Cienzhong/linux.study/blob/master/python.helper.md)
- [php](https://github.com/Cienzhong/linux.study/blob/master/php.setup.md)
- [uwsgi](https://github.com/Cienzhong/linux.study/blob/master/uwsgi.ini)
- [kratos](https://github.com/Cienzhong/linux.study/blob/master/go.kratos.helper.md)

### 1.查看日志常用命令
```
// 显示filename最后20行
tail -n 20 filename

// 查看当前文件大小
du -sh *

// 查看文件夹和挂载
df -h

// 检测远程IP端口是否能访问
telnet ip port (telnet baidu.com 80)
```

### 2.Linux之间实现远程传输文件
```
scp /home/helpteach/project/mallupload/1509681299449.png wasadmin@10.127.40.25:/home/test
// wasadmin@10.127.40.25:/home/test 为远程服务器的账号、IP、目录
```


### 3.创建用户并授权指定目录
```
// 在root下执行
groupadd  admin   // 创建一个组admin

// 创建用户
useradd -m -g admin wu    // 在用户组admin下新增用户wu

// 设置用户密码
passwd  wu     // 给用户wu设置密码，按回车输密码


// 切换到home目录，在root用户下给uiadm授权
chmod 775 -R wu
```

### 4.CURL 发送POST请求
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

