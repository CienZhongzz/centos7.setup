# PHP7安装

- 先修改yum源

> https://webtatic.com 

<code><pre>
    rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
    rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
</pre></code>

- 安装PHP7

<code><pre>
    yum install php70w-devel php70w.x86_64 php70w-cli.x86_64 php70w-common.x86_64 php70w-pdo.x86_64 php70w-mysqlnd php70w-fpm php70w-opcache php70w-process.x86_64 php70w-mbstring.x86_64
</pre></code>

- 命令

<code><pre>
    # 启动
    systemctl start php-fpm
    # 重启
    systemctl restart php-fpm
    # 查看状态
    systemctl status php-fpm
    # 停止命令
    pkill php-fpm
</pre></code>