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
```
go get -u github.com/golang/protobuf/proto
```


### 3.安装goprotobuf插件
```
go get github.com/golang/protobuf/protoc-gen-go
```


### 4.安装gogoprotobuf插件和依赖
```
//gogo
go get github.com/gogo/protobuf/protoc-gen-gogo

//gofast
go get github.com/gogo/protobuf/protoc-gen-gofast

//依赖
go get github.com/gogo/protobuf/proto
go get github.com/gogo/protobuf/gogoproto
```


### 5.安装框架依赖
```
// grpc (或者git clone https://github.com/grpc/grpc-go 然后复制到google.golang.org/grpc)
go get -u google.golang.org/grpc

// genproto (或者git clone https://github.com/google/go-genproto 然后复制到google.golang.org/genproto)
go get google.golang.org/genproto/...
```


### 6.安装kratos tool
~~--proto~~可不要
```
go get -u github.com/go-kratos/kratos/tool/kratos
cd $GOPATH/src
kratos new kratos-demo --proto
```


### 7.运行
```
cd kratos-demo/cmd
go build
./cmd -conf ../configs
```


> 打开浏览器访问：http://localhost:8000/kratos-demo/start
> 你会看到输出了Golang 大法好 ！！！


### 8.kratos tool protoc
```

cd (项目目录)/api

# generate all
kratos tool protoc api.proto
# generate gRPC
kratos tool protoc --grpc api.proto
# generate BM HTTP
kratos tool protoc --bm api.proto
# generate ecode
kratos tool protoc --ecode api.proto
# generate swagger
kratos tool protoc --swagger api.proto

```
