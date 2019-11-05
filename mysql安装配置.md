# mysql安装配置

- 安装

参考地址：

https://www.runoob.com/mysql/mysql-install.html


独立下载mysql仓库

wget -i -c http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm
yum -y install mysql57-community-release-el7-10.noarch.rpm

报错

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