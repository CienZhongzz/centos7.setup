# 通用签名方法
<br/>

### 1.格式
签名**sign**的格式是**MD5**加密串，大写，32位<br/>
在http header传入，需同时传入key、时间戳**timestamp**(秒)和签名**sign**字段.<br/>

### 2.语法
key：key是用户唯一的令牌，登录时返回给应用;<br/>
timestamp：应用当前时间戳，与API服务器的时间戳误差控制在上下10分钟内;<br/>
sign：key和时间戳拼合字符串的加密串转成大写，如下:<br/>
```
...
sign = MD5(key + timestamp).toUpperCase();
...
```
<br/>

### 3.补充注意点
> *key有一定的生命周期，如果签名失败了就说明key失效了，需要重新登录获取最新的key值。*
<br/>