# nginx命令帮助文档
<br/>

### 安装

<br/>
### 启动和查看
#### 查看nginx进程
> ps -ef|grep nginx

#### 检测nginx配置文件是否正确
> /usr/local/webserver/nginx/sbin/nginx -t

#### 启动nginx
> /usr/local/webserver/nginx/sbin/nginx

#### 重启nginx
> /usr/local/webserver/nginx/sbin/nginx -s reload

<br/>
### 配置
#### 配置新网站
​```
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