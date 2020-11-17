# 在Linux上安装配置redis

### 1. 下载最新稳定版本到默认目录，笔者这里下载的是5.0.5版本
```
// 官网下载地址：http://redis.io/download

wget http://download.redis.io/releases/redis-5.0.5.tar.gz
```

### 2. 解压文件夹
```
tar xvf redis-5.0.5.tar.gz
```

### 3. 建立一个redis目录的软连接，指向redis-5.0.5
```
ln -s redis-5.0.5 redis
```

### 4. 进入redis目录, 编译（编译前确保操作系统已经安装了gcc）
```
cd redis

make
```

### 5. 进入src安装，指定安装目录
```
cd src

make install PREFIX=/usr/local/redis
```

### 6. 将Redis的相关运行文件放到/usr/local/bin下(这样可以在任意目录下执行Redis的命令)
```
mv /usr/local/redis/bin/redis-server /usr/local/bin/
mv /usr/local/redis/bin/redis-cli /usr/local/bin/
```

### 7. 查看redis版本
```
    redis-cli -v
    // 显示redis-cli 5.0.5表示安装成功
```

### 8. 在redis安装位置创建一个存放配置文件的目录
```
mkdir /usr/local/redis/etc
```

### 9. 把配置文件放到刚刚创建的目录中
```
mv redis/redis.conf /usr/local/redis/etc
```

### 10. 配置redis为后台启动
```
vi /usr/local/redis/etc/redis.conf
// 编辑内容
daemonize no
// 改为
daemonize yes
```

### 11. 将redis加入到开机启动
```
vi /etc/rc.local
// 内容后面增加：
redis-server /usr/local/redis/etc/redis.conf
```

### 12. 启动redis服务
```
redis-server /usr/local/redis/etc/redis.conf
```

### 13. 设置redis密码（不重启redis，当redis重启时密码依然有效）
```
// 密码会设置在配置文件redis.conf中requirepass test123
config set requirepass test123
// 后面启动客户端查询需要密码验证
auth test123
```

### 14. Redis可执行文件说明

| 可执行文件 | 作用 |
| :--- | :--- |
| redis-server | 启动Redis |
| redis-cli | Redis命令行客户端 |
| redis-benchmark | Redis基准测试工具 |
| redis-check-aof | RedisAOF持久化文件检测和修复工具 |
| redis-check-dump | RedisRDB持久化文件检测和修复工具 |
| redis-sentinel | 启动Redis Sentinel |

### 15. 其他常用命令
```
//停止redis
pkill redis  

//卸载redis：
rm -rf /usr/local/redis //删除安装目录
rm -rf /usr/bin/redis-* //删除所有redis相关命令脚本
```

### 16. 允许redis局域网访问

假设A B 两台机器<br/>

在B（ip:192.168.1.99）机器上修改redis配置文件<br/>

```
bind 192.168.1.99
```

关闭防火墙的情况下 局域网内的机器都能访问到该redis了。可以再设置一个密码。<br/>

```
requirepass  youpassword
```

重启redis<br/>

```
redis-server /usr/local/redis/etc/redis.conf
```
