## rsacry
> 这是一个用来加密密码等小数据的小应用。使用rsa算法，会产生一个公钥和私钥。
> 其中公钥用来加密数据，私钥用来解密数据。

### 由来
> &emsp;&emsp;之所以会写这个小程序，原因是上午
> 登陆网银的时候，竟然发现网银的密码和人人的密码是一样的。这怎么能行，于是乎
> 更改了网银密码，但是又怕自己忘了。于是想到可以把密码放到某个网络云存储上。
> 但是又想到，这岂不是脱光了衣服跑别人屋子里么，钥匙还在别人手上。这可不安全。
> 虽然有类似的网络管理密码的应用，但是还是自己加密来的放心。

### 依赖
* python 2
* rsa module in python2

> rsa 安装方法
>
> `pip install rsa`
>
> 或    
>
> `easy_install rsa`

### 执行方法
* 使用`python rsacry.py -h`可查看帮助

* 把 `python`放入`PATH`变量，在脚本的第一行加入`#!/bin/env python` (現以加入)

* 比如`python`在目录`~/bin`中，在脚本的第一行加入`#!~/bin/python` (或绝对路径)

### 使用方法

* `rsacry.py --genkey`用来产生公钥和私钥

* `rsacry.py --encry origin_data`用来产生加密数据,数据需要用`'`括起来

* `rsacry.py --decry encrypted_data`用来还原原始数据

### 获取方法

* 直接下载脚本

* 用 `git clone https://github.com/zhaozq/rsaencrypt_self_data.git`

