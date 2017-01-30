# script4MW300R
using QPython3 script on Android device to control WIFI Router

主要操作就是：扫描要中继的WIFI信道，然后修改到路由器上。

起因：分析路由器管理页面的js库文件的时候，发现身份验证采用的是cookie，所以密码不变，cookie就可以一直使用。

在笔记本上用python开发环境debug成功后上传到手机上就直接可以用了。

原本打算用这个绕过校园网的windows客户端的，账号密码运算部分直接用openkeeper的代码，然后写成py脚本交给安卓手机去运行，接下来再由脚本控制路由器正常拨号。

快毕业了，也许没时间去捣鼓这个东西。


