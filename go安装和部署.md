# Go的正确安装和部署

- 安装
安装包下载地址为：https://studygolang.com/dl
**下载文件参考：go1.13.linux-amd64.tar.gz**

<code>
<pre>
wget https://dl.google.com/go/go1.13.linux-amd64.tar.gz
tar -C /usr/local -xzf go1.13.linux-amd64.tar.gz
</pre>
</code>

- 配置环境变量.bash_profile
<code><pre>
	vi ~/.bash_profile

	# 插入以下内容
	export GOROOT=/usr/local/go
	export PATH=$PATH:$GOROOT/bin
	export PATH
	export GOPATH=/home/go
	export PATH=$PATH:$GOPATH/bin
	export PATH
	export GO111MODULE=on
	export GOPROXY=https://goproxy.io

	# 修改保存后，执行以下命令让环境变量生效
	source .bash_profile
</pre></code>

- 验证是否配置成功
<code><pre>
	go version
	# go version go1.15.4 linux/amd64
</pre></code>

