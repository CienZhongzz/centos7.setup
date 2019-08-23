# 在Linux上安装redis

1. 下载最新稳定版本到默认目录，笔者这里下载的是5.0.5版本
> 官网下载地址：http://redis.io/download 

<code><pre>
    wget http://download.redis.io/releases/redis-5.0.5.tar.gz
</pre></code>

2. 解压文件夹
<code><pre>
    tar xvf redis-5.0.5.tar.gz
</pre></code>

3. 建立一个redis目录的软连接，指向redis-5.0.5
<code><pre>
    ln -s redis-5.0.5 redis
</pre></code>

4. 进入redis目录
<code><pre>
    cd redis
</pre></code>

5. 编译（编译前确保操作系统已经安装了gcc）
<code><pre>
    make
</pre></code>

6. 进入src安装，指定安装目录
<code><pre>
    cd src
    make install PREFIX=/usr/local/redis
</pre></code>

7. 将Redis的相关运行文件放到/usr/local/bin下(这样可以在任意目录下执行Redis的命令)
<code><pre>
    mv /usr/local/redis/redis-server /usr/local/bin/
    mv /usr/local/redis/redis-cli /usr/local/bin/
</pre></code>

8. 查看redis版本
<code><pre>
    redis-cli -v
</pre></code>
> 显示redis-cli 5.0.5表示安装成功

9. 在redis安装位置创建一个存放配置文件的目录
<code><pre>
    mkdir /usr/local/redis/etc
</pre></code>

10. 把配置文件放到刚刚创建的目录中
<code><pre>
    mv redis/redis.conf /usr/local/redis/etc
</pre></code>

11. 配置redis为后台启动
<code><pre>
    vi /usr/local/redis/etc/redis.conf
    // 编辑内容
    daemonize no
    // 改为
    daemonize yes
</pre></code>

12. 将redis加入到开机启动
<code><pre>
    vi /etc/rc.local
    // 内容后面增加：
    redis-server /usr/local/redis/etc/redis.conf
</pre></code>

13. 启动redis服务
<code><pre>
    redis-server /usr/local/redis/etc/redis.conf
</pre></code>

14. 设置redis密码（不重启redis，当redis重启时密码依然有效）
<code><pre>
    // 密码会设置在配置文件redis.conf中requirepass test123
    config set requirepass test123
    // 后面启动客户端查询需要密码验证
    auth test123
</pre></code>

15. Redis可执行文件说明

| 可执行文件 | 作用 |
| :--- | :--- |
| redis-server | 启动Redis |
| redis-cli | Redis命令行客户端 |
| redis-benchmark | Redis基准测试工具 |
| redis-check-aof | RedisAOF持久化文件检测和修复工具 |
| redis-check-dump | RedisRDB持久化文件检测和修复工具 |
| redis-sentinel | 启动Redis Sentinel |

16. 其他常用命令
<code><pre>
    //停止redis
    pkill redis  
    
    //卸载redis：
    rm -rf /usr/local/redis //删除安装目录
    rm -rf /usr/bin/redis-* //删除所有redis相关命令脚本
</pre></code>