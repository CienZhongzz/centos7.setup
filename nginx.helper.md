# nginx命令帮助文档


### 1.安装

> pass


### 2.启动和查看
#### 2.1.查看nginx进程
> ps -ef|grep nginx

#### 2.2.检测nginx配置文件是否正确
> /usr/local/webserver/nginx/sbin/nginx -t

#### 2.3.启动nginx
> /usr/local/webserver/nginx/sbin/nginx

#### 2.4.重启nginx
> /usr/local/webserver/nginx/sbin/nginx -s reload



### 3.配置

#### 3.1.配置新网站

​<code><pre>server
server {
    listen 80;
    server_name imgsite.cienhub.com;
    client_max_body_size 200m;
    location / {
        root /usr/local/www/imgsite; #html访问路径  
        index index.html;
    }
}
​</pre></code>

#### 3.2 配置php解析

<code><pre>
    location ~ \.php$ {
        root           html;
        fastcgi_pass   127.0.0.1:9000;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME  /usr/local/nginx/html$fastcgi_script_name;
        include        fastcgi_params;
    }
</pre></code>

- 说明

a、fastcgi_pass 用来指定php-fpm监听的地址或者socket；

b、fastcgi_index 设定访问根目录默认去找的文件；

c、fastcgi_param设置访问根目录时默认寻找的文件;
