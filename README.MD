# Shadowsocks-commandline-helper

This is a simple script for making life a little easier when using a subscription of Shadowsocks.

> Only tested on shadowsocks-rust. 

## Installation

```shell
$ git clone https://github.com/itewqq/ss-cmd-helper.git
$ cd ss-cmd-helper
$ pip install -r requirements.txt
```

## Usage

```shell
$ python main.py --help
usage: main.py [-h] [-a URL | -s n | -k | -u | -l]

Shadowsocks subscription commandline helper.

options:
  -h, --help            show this help message and exit
  -a URL, --addurl URL  add your subsciption URL
  -s n, --select n      select node n to use
  -k, --kill            kill sslocal/stop proxy
  -u, --update          update subsciption
  -l, --list            list all nodes
```

## Example

```shell
$ python main.py -a https://yoursubscribe.url?sub=2
[Add] Success! Added https://yoursubscribe.url?sub=2
$ python main.py -u
[Update] Success!
$ python main.py -l
Subscription url is: https://yoursubscribe.url?sub=2

Total: 2

[0]  ss://...
[1]  ss://...
$ python main.py -s 5
[Start] Success!
2022-02-16T20:22:16.462020878+08:00 INFO  shadowsocks local 1.13.2 build 2022-02-16T09:35:29.655779693+00:00
 2022-02-16 20:22:16 [simple-obfs] INFO: obfuscating enabled
 2022-02-16 20:22:16 [simple-obfs] INFO: obfuscation http method: GET
 2022-02-16 20:22:16 [simple-obfs] INFO: obfuscating hostname: 64717e7460736d2833627b7d.sina.cn
 2022-02-16 20:22:16 [simple-obfs] INFO: tcp port reuse enabled
 2022-02-16 20:22:16 [simple-obfs] INFO: listening at 127.0.0.1:35111
2022-02-16T20:22:16.471908290+08:00 INFO  shadowsocks socks TCP listening on 127.0.0.1:1089
$ python main.py -k
[Stop] Success!
```

## Declaration

This script is for educational purposes only, and the author is not responsible for any actions of the user.