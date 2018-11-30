将下载好的破解文件放到一个不会改动的文件夹中。我放在如下目录（macOS系统）：
 /Library/JetbrainsLicense (**笔者存放的 Library 文件夹是系统根目录下的, 需要读写权限的, 所以没有读写权限的朋友不要放在这里, 常规文件夹如‘文档’、‘下载’等等都可以，否则会出现 ‘Key is invalid’的提示**)

打开PyCharm的安装目录，macOS版去**应用程序/Applications**中找到对应程序**显示包内容**如下：

/Applications/PyCharm.app/Contents/bin/pycharm.vmoptions

打开pycharm.vmoptions，笔者用的是atom打开的，在最后一行加上-javaagent:步骤2中破解文件放置的位置，**保存**，笔者的如下

{"licenseId":"1337", "licenseeName":"Your Name", "assigneeName":"", "assigneeEmail":"", "licenseRestriction":"Unlimited license till end of the century.", "checkConcurrentUse":false, "products":[ {"code":"II","paidUpTo":"2099-12-31"}, {"code":"DM","paidUpTo":"2099-12-31"}, {"code":"AC","paidUpTo":"2099-12-31"}, {"code":"RS0","paidUpTo":"2099-12-31"}, {"code":"WS","paidUpTo":"2099-12-31"}, {"code":"DPN","paidUpTo":"2099-12-31"}, {"code":"RC","paidUpTo":"2099-12-31"}, {"code":"PS","paidUpTo":"2099-12-31"}, {"code":"DC","paidUpTo":"2099-12-31"}, {"code":"RM","paidUpTo":"2099-12-31"}, {"code":"CL","paidUpTo":"2099-12-31"}, {"code":"PC","paidUpTo":"2099-12-31"}, {"code":"DB","paidUpTo":"2099-12-31"}, {"code":"GO","paidUpTo":"2099-12-31"}, {"code":"RD","paidUpTo":"2099-12-31"} ], "hash":"2911276/0", "gracePeriodDays":7, "autoProlongated":false}

启动，它会弹出授权的提示框，选择

Activaction code

，复制刚才粘贴的一整段，激活，done！！

## 一些常见的问题

### 1. 关于 Key  is invalid 的解决办法

> 出现该问题的朋友貌似都是使用 Mac 的朋友, 至少向我求助的都是使用 Mac 的朋友, 我想 Window 出现该问题解决方法是一样的。

拿 PyCharm为例, 去 /Users/用户名/Library/Preferences 目录下, 

画圈部分为你曾经安装过的旧版本的配置信息, 只保留最新的, 其余删除, 重新破解, 一切正常



