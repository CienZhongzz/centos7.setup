# nginx命令帮助文档
<br/>

### 1.安装
> pass

<br/>

### 2.启动和查看
#### 2.1.查看nginx进程
> ps -ef|grep nginx

#### 2.2.检测nginx配置文件是否正确
> /usr/local/webserver/nginx/sbin/nginx -t

#### 2.3.启动nginx
> /usr/local/webserver/nginx/sbin/nginx

#### 2.4.重启nginx
> /usr/local/webserver/nginx/sbin/nginx -s reload

<br/>

### 3.配置
#### 3.1.配置新网站
​```server
server {
    listen 80;
    server_name imgsite.cienhub.com;
    client_max_body_size 200m;
    location / {
        root /usr/local/www/imgsite; #html访问路径  
        index index.html;
    }
}
​```