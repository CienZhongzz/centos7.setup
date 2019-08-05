# Linux使用mount命令挂载Windows共享文件夹
> 因项目中数据经常需要从windows共享文件下个获取，为了方便读取，就直接在将windows的共享文件夹挂载到了linux服务器上，而没有使用SmbFile读取，在这里简单记录一下之前的挂载过程。

- 1.在windows上创建共享目录/code1
- 2.在linux上创建一个要挂载到的文件目录;
<code><pre>
    // 创建的文件夹目录：/test1
    mkdir /test1
</pre></code>
- 3.使用mount 命令进行挂载
<code><pre>
mount -t cifs -o username=Administrator,password=cienwins  //10.124.120.60/code1 /test1
</pre></code>
- 4. 查看挂载结果，命令：
<code><pre>
    df -h
</pre></code>
*当出现挂载的目录时，说明windows共享文件夹已挂载成功，在linux服务器上部署的项目就可以直接使用File来进行文件的读取操作了。*