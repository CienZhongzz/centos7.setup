# kratos项目安装

### 1.安装protoc二进制文件（这一步比较重要）
```
	// 下载地址：https://github.com/protocolbuffers/protobuf/releases/tag/v3.7.1
	//（或者https://github.com/google/protobuf/releases）
	// 选择文件：protoc-3.7.1-linux-x86_64.zip
	mv bin/protoc /usr/local/bin/
	mv include/google /usr/local/include/
```


### 2.安装protobuf库文件
<code><pre>
	go get -u github.com/golang/protobuf/proto
</pre></code>


### 3.安装goprotobuf插件
<code><pre>
	go get github.com/golang/protobuf/protoc-gen-go
</pre></code>


### 4.安装gogoprotobuf插件和依赖
<code><pre>
	//gogo
	go get github.com/gogo/protobuf/protoc-gen-gogo

	//gofast
	go get github.com/gogo/protobuf/protoc-gen-gofast

	//依赖
	go get github.com/gogo/protobuf/proto
	go get github.com/gogo/protobuf/gogoproto
</pre></code>


### 5.安装框架依赖
<code><pre>
	// grpc (或者git clone https://github.com/grpc/grpc-go 然后复制到google.golang.org/grpc)
	go get -u google.golang.org/grpc

	// genproto (或者git clone https://github.com/google/go-genproto 然后复制到google.golang.org/genproto)
	go get google.golang.org/genproto/...
</pre></code>


### 6.安装kratos tool
<code><pre>
	go get -u github.com/go-kratos/kratos/tool/kratos
	cd $GOPATH/src
	kratos new kratos-demo --proto
</pre></code>


### 7.运行
<code><pre>
	cd kratos-demo/cmd
	go build
	./cmd -conf ../configs
</pre></code>


> 打开浏览器访问：http://localhost:8000/kratos-demo/start，你会看到输出了Golang 大法好 ！！！

