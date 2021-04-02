# 功能
指定不同程序使用不同的网卡
使用场景：通过有线网卡连公司内网，通过无线网卡访问外网
# 图片预览
![]()
# 使用说明
1. 点击“Guid”获取网卡Guid
2. 选择ForceBindIP64.exe路径
3. 选择要启动的程序的路径
4. 输入网卡Guid
5. 点击“start” 启动程序

# 其它
**1、网络连接优先级**
![]()

无线网和有线网同时使用时，通过修改接口跃点数能改变网络连接的优先级。

**2、[ForceBindIP](https://r1ch.net/projects/forcebindip "ForceBindIP")**
Bind any Windows application to a specific interface or IP address

**3、语言**
程序是用pyinstaller打包的，体积有点大。

**4、更简便使用方法**
cmd执行如下命令：
ForceBindIP64绝对路径 网卡Guid 指定程序绝对路径
```
"C:\ForceBindIP-1.32\ForceBindIP64.exe" {F8xxxF66-2E45-xxxx-xxxx-9CE6xxxC2A32} "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
```
网卡guid也可以用网卡对应的ip替换，如：
```
"C:\ForceBindIP-1.32\ForceBindIP64.exe" 192.168.0.11 "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
```
