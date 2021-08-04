# Vue项目构建步骤

### 1.安装Nodejs&npm
```
//安装流程，直接安装Nodejs即可，此处省略...
npm -v

// 使用淘宝镜像
npm install -g cnpm --registry=https://registry.npm.taobao.org

```

### 2.安装vue-cli脚手架构建工具
```
// 使用淘宝镜像安装，这里不建议用cnpm
npm install vue-cli -g --registry=https://registry.npm.taobao.org

```

### 3.使用vue-cli脚手架构建项目
```
// 进入开发目录，打开命令行运行
vue init webpack test-vue
--等待项目安装完成

```

### 4.安装项目依赖资源
```
// 进入test-vue目录
npm install ?? --save

--save 库信息保存在package.json文件中
```

### 5.运行项目
```
npm run dev
```
