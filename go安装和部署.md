# Go的正确安装和部署

- 安装
安装包下载地址为：https://golang.org/dl/。
如果打不开可以使用这个地址：https://golang.google.cn/dl/。
**下载文件参考：go1.13.linux-amd64.tar.gz**

<code>
<pre>
wget https://dl.google.com/go/go1.13.linux-amd64.tar.gz
tar -C /usr/local -xzf go1.13.linux-amd64.tar.gz
</pre>
</code>

- 添加环境变量
<code>
<pre>
mkdir /home/go
mkdir /home/go/src
export PATH=$PATH:/usr/local/go/bin
export GOROOT=/usr/local/go
export GOPATH=/home/go
# 配置代理
export GOPROXY=https://goproxy.io/
</pre>
</code>

- kratos框架安装
<code>
<pre>
go get -u github.com/bilibili/kratos/tool/kratos
cd $GOPATH/src
kratos new gym-food
</pre>
</code>

- Build & Run
<code>
<pre>
cd gym-food/cmd
go build
./cmd -conf ../configs
</pre>
</code>

- 环境变量.bash_profile设置
<code>
<pre>
vi ~/.bash_profile
# 插入以下内容
export GOPATH=/home/go
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOPATH/bin
export GOPROXY=https://goproxy.io   # 代理，这是一条注释
# 修改保存后，执行以下命令让环境变量生效
source .bash_profile
</pre>
</code>