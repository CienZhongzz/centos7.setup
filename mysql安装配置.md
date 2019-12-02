# mysql安装配置

- 安装

参考地址：

https://www.runoob.com/mysql/mysql-install.html


独立下载mysql仓库

<code><pre>
wget -i -c http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm

yum -y install mysql57-community-release-el7-10.noarch.rpm
</pre></code>


- 报错

No package matched to upgrade: mysql57-community-release
--> Finished Dependency Resolution
Error: mysql57-community-release conflicts with mysql-community-release-el6-5.noarch
You could try using --skip-broken to work around the problem
You could try running: rpm -Va --nofiles --nodigest


rpm -qa |grep mysql 查看有如下内容

> mysql-community-release-el6-5.noarch
> mysql-community-common-5.6.44-2.el6.x86_64

操作一下 卸载了

> rpm -e --nodeps mysql-community-release-el6-5.noarch
> rpm -e --nodeps mysql-community-common-5.6.44-2.el6.x86_64

重新升级

> rpm -Uvh mysql57-community-release-el7-10.noarch.rpm



- 下一步，继续安装
<code><pre>
    yum update

    yum install mysql-server
</pre></code>

设置权限
<code><pre>
    chown mysql:mysql -R /var/lib/mysql
</pre></code>

初始化 MySQL
<code><pre>
    mysqld --initialize
</pre></code>

启动 MySQL
<code><pre>
    systemctl start mysqld
</pre></code>

查看 MySQL 运行状态
<code><pre>
    systemctl status mysqld
</pre></code>

<br><br>

### 问题解决办法收集

> 内存不足导致mysql经常自动停止服务

**创建 SWAP 分区**

- a.逐条运行下面的命令

<code><pre>
    sudo /bin/dd if=/dev/zero of=/var/swap.1 bs=1M count=1024
    sudo /sbin/mkswap /var/swap.1
    sudo /sbin/swapon /var/swap.1
</pre></code>

- b.将下面一行添加到 /etc/fstab,服务器重启时自动启动swap

<code><pre>
    /var/swap.1 swap swap defaults 0 0
</pre></code>

- c.降低数据库 InnoDB 引擎的缓冲区大小，以及限制 MySQL 的最大连接数(max_connections)
<code><pre>
    在/etc/mysql/my.cnf 的 mysqld 下添加或修改下面两句：

    降低 InnoDB 缓冲区大小为 64M 或者 32M
    innodb_buffer_pool_size = 64M
    
    限制最大连接数为100，在服务器配置很低时可以继续降低
    max_connections = 100
</pre></code>

- d.修改完重启 MySQL
<code><pre>
    service mysqld restart
</pre></code>
