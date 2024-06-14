# Go的正确安装和部署

### 1.安装
安装包下载地址为：https://studygolang.com/dl <br>
> 下载文件参考：go1.13.linux-amd64.tar.gz
```
wget https://dl.google.com/go/go1.13.linux-amd64.tar.gz
tar -C /usr/local -xzf go1.13.linux-amd64.tar.gz
```


### 2.配置环境变量
> 本例子为配置 .bash_profile 文件
```
vi ~/.bash_profile

// 插入以下内容
export GOROOT=/usr/local/go
export PATH=$PATH:$GOROOT/bin
export PATH
export GOPATH=/home/go
export PATH=$PATH:$GOPATH/bin
export PATH
export GO111MODULE=on
export GOPROXY=https://goproxy.io

// 修改保存后，执行以下命令让环境变量生效
source .bash_profile
```
> 修改后，查看环境变量配置列表命令：**export**


### 3.验证是否配置成功
```
go version
// go version go1.15.4 linux/amd64
```

```
// nohup运行
nohup ./aiexton_shell --port=10011 --log_dir=./log --dailyRolling=true
```
