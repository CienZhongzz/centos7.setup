
# Python 3.x 安装部署指引

### 1.准备安装环境
```
yum install openssl-devel -y

yum install libffi-devel -y

yum install -y unzip zip

yum install openssl-devel libffi-devel unzip zip -y

yum install gcc -y
```

### 2.下载安装包
前往官网手动下载：https://www.python.org/downloads/source/
```
wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz
(https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz)
```

### 3.解压、编译安装
```
// 解压
tar -zxvf Python-3.8.5.tgz

cd Python-3.8.5

// 编译
./configure --prefix=/opt/Python
(./configure --prefix=/opt/Python --enable-shared --enable-loadable-sqlite-extensions)

// 安装
make
make install
```

### 4.配置软连接
```
ln -s /opt/Python/bin/python3 /usr/bin/python3
```

### 5.安装setuptools工具
```
wget https://files.pythonhosted.org/packages/1d/64/a18a487b4391a05b9c7f938b94a16d80305bf0369c6b0b9509e86165e1d3/setuptools-41.0.1.zip

unzip setuptools-41.0.1.zip

cd setuptools-41.0.1

python3 setup.py build

python3 setup.py install
```

### 6.安装pip
```
wget https://files.pythonhosted.org/packages/93/ab/f86b61bef7ab14909bd7ec3cd2178feb0a1c86d451bc9bccd5a1aedcde5f/pip-19.1.1.tar.gz

tar -zxvf pip-19.1.1.tar.gz

cd pip-19.1.1

python3 setup.py build

python3 setup.py install

// 配置pip3软连接
ln -s /opt/Python/bin/pip3 /usr/bin/pip3
```

### 7.安装python程序运行必要的库
```
pip3 install requests BeautifulSoup4 Click Flask uWSGI dns-batch-resolver fake-useragent Flask-Script

pip3 install asyncio aiohttp pymysql DBUtils yaml-config redis logging3

// pip 更新库
(pip3 install --upgrade 库名)

```
