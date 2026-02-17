---
title: 【NodeQuality】Skyline Connect 新加坡 VPS 测试
date: 2026-02-18
updated: 
categories:
- skylineconnect
cover: /img/skylineconnect.png
tags:
- 新加坡VPS
- 评测
description: 
copyright: false
---

## [NodeQuality] Skyline - SG 新加坡Ⅰ型 测试

官网：https://www.skylineconnect.io/signup?aff=QNUQO4OT

测试数据来源：https://www.nodeseek.com/post-620989-1

```
########################################################################
                  bash <(curl -sL https://run.NodeQuality.com)
                   https://github.com/LloydAsp/NodeQuality
        报告时间：2026-02-18 05:44:41 CST  脚本版本：v0.0.1
        频道: https://t.me/nodeselect 网站：https://NodeQuality.com
########################################################################


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                         硬件质量体检报告：195.172.*.*
                    https://github.com/xykt/HardwareQuality
                    bash <(curl -sL https://Check.Place) -H
            报告时间：2026-02-18 05:44:58 CST  脚本版本：v2026-02-17
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
一、操作系统信息
容器/虚拟化：          KVM 虚拟机
架构：                 x86_64
操作系统/内核：        Debian GNU/Linux 12 (bookworm) 6.12.63+deb13-cloud-amd64
运行时间：             0 天 0 小时 36 分钟
负载：                 1.30, 0.65, 0.27
进程：                 3 用户，107 进程，11/147 活跃/总服务
区域设置：             C, UTF-8, Etc/UTC UTC +0000
二、主板信息
BIOS：    SeaBIOS, 版本1.16.2-debian-1.16.2-1
芯片组：  Intel 82371SB PIIX3 ISA [Natoma/Triton II]
          Intel 440FX - 82441FX PMC [Natoma]
网卡：    Red Hat, Inc. Virtio network device
三、CPU测评
CPU：     AMD EPYC 7542 32-Core Processor 步进0 (23代) 32/64-bit
           ╚═ 1核心, 1线程, 2894.562MHz, 利用率19%              
缓存：    L1d 32 KiB, L1i 32 KiB, L2 512 KiB, L3 128 MiB
指令集：   ✔ VT-x/AMD-V    ✔ AES-NI    ✔ AVX2    ✔ BMI1/2    ✔ EPT/NPT 
Sysbench：单线程 1521.64     
GB5基准： J1900 N5105 N100 6700K 9900K 5900X 12900K 14900K 7713 7995WX
GB5单核：    |881
GB5多核：     |929
Crypto Score              732    Single-Core Score||   1318     Multi-Core Score
Floating Point Score     1085    Single-Core Score||   1104     Multi-Core Score
Integer Score             799    Single-Core Score||    819     Multi-Core Score
AES-XTS                   732          1.25 GB/sec||   1318          2.25 GB/sec
Camera                   1007      11.7 images/sec||    996      11.5 images/sec
Clang                     855      6.66 Klines/sec||    783      6.10 Klines/sec
Face Detection           1051      8.09 images/sec||   1029      7.93 images/sec
Gaussian Blur             977     53.7 Mpixels/sec||   1130     62.1 Mpixels/sec
HDR                      1983     27.0 Mpixels/sec||   1834     25.0 Mpixels/sec
HTML5                     798  936.7 KElements/sec||    792  929.5 KElements/sec
Horizon Detection         903     22.3 Mpixels/sec||    915     22.6 Mpixels/sec
Image Compression         858     40.6 Mpixels/sec||    847     40.1 Mpixels/sec
Image Inpainting         1931     94.7 Mpixels/sec||   1917     94.1 Mpixels/sec
Machine Learning          806      31.2 images/sec||    794      30.7 images/sec
N-Body Physics            942      1.18 Mpairs/sec||   1106      1.38 Mpairs/sec
Navigation                796         2.24 MTE/sec||    778         2.19 MTE/sec
PDF Rendering             804     43.7 Mpixels/sec||    847     45.9 Mpixels/sec
Ray Tracing              1282     1.03 Mpixels/sec||   1327     1.07 Mpixels/sec
Rigid Body Physics        962           5962.6 FPS||    949           5878.4 FPS
SQLite                    635      199.0 Krows/sec||    778      243.6 Krows/sec
Speech Recognition        887       28.4 Words/sec||    847       27.1 Words/sec
Structure from Motion     835     7.48 Kpixels/sec||    850     7.62 Kpixels/sec
Text Compression          783          3.96 MB/sec||    846          4.28 MB/sec
Text Rendering            711         226.5 KB/sec||    732         233.2 KB/sec
详细结果：https://browser.geekbench.com/v5/cpu/24119504
五、内存测评
内存：    总容量 930 MB,  已用 266 MB(29%),  可用 664 MB(71%)
超开指标： ✔ 气球回收     ✘ KSM 复用 
Sysbench：读取 44138.1 MB/s    写入 20043.5 MB/s    延迟 167 ns
六、硬盘测评
硬盘：    数量 2,  总容量 7.8G,  已用容量 2.1G(26%),  可用容量 5.4G(74%)
测试设备：vda1(/r**t) -> DISK
Crystal： RND4K/Q1    IOPS||RND4K/Q32   IOPS||SEQ1M/Q1    IOPS||SEQ1M/Q8    IOPS
读取：    688KB/s      172||6.26MB/s    1.6k||293MB/s      293||306MB/s      305
写入：    612KB/s      153||5.31MB/s    1.4k||82.2MB/s      82||259MB/s      258
ATTO：    READ                          IOPS||WRITE                         IOPS
512B      10.2MB/s                       21k||82KB/s                         165
1K        21.0MB/s                       21k||155KB/s                        155
2K        40.6MB/s                       21k||353KB/s                        176
4K        67.4MB/s                       17k||1.91MB/s                       489
8K        107MB/s                        14k||4.37MB/s                       559
16K       162MB/s                        10k||10.9MB/s                       695
32K       238MB/s                       7.6k||22.2MB/s                       709
64K       325MB/s                       5.2k||27.7MB/s                       442
128K      326MB/s                       2.6k||55.8MB/s                       446
256K      329MB/s                       1.3k||113MB/s                        451
512K      321MB/s                        642||171MB/s                        341
1M        328MB/s                        328||233MB/s                        232
2M        316MB/s                        157||286MB/s                        143
4M        327MB/s                         81||306MB/s                         76
8M        382MB/s                         47||300MB/s                         37
16M       388MB/s                         24||272MB/s                         17
32M       361MB/s                         11||268MB/s                          8
64M       293MB/s                          4||246MB/s                          3
七、HQ硬件加权评分
项目：      总 分          CPU           GPU          内 存         硬 盘  
分数：      22333    =    13667    +     N/A     +    8089     +     577   
排名：      1.6%          8.0%           N/A          2.8%          0.2%   
================================================================================
今日硬件检测量：690；总检测量：5247。感谢使用xy系列脚本！ 
报告链接：https://Report.Check.Place/hardware/2LVVV1RQF.svg

########################################################################
                      IP质量体检报告：195.172.*.*
                   https://github.com/xykt/IPQuality
                bash <(curl -sL https://Check.Place) -I
        报告时间：2026-02-18 05:56:09 CST  脚本版本：v2026-02-08
########################################################################
一、基础信息（Maxmind 数据库）
自治系统号：            AS216211
组织：                  Cyberverse LLC
坐标：                  °7′21″W, 51°29′47″N
地图：                  https://check.place/51.4964,-0.1224,15,cn
城市：                  N/A
使用地：                [GB]英国, [EU]欧洲
注册地：                [GB]英国
时区：                  Europe/London
IP类型：                 原生IP 
二、IP类型属性
数据库：      IPinfo    ipregistry    ipapi    IP2Location   AbuseIPDB 
使用类型：     家宽        家宽        商业        机房        家宽    
公司类型：     家宽        商业        商业        机房    
三、风险评分
风险等级：      极低         低       中等       高         极高
IP2Location：                                                99|高风险
Scamalytics：  0|低风险
ipapi：    0.00%|极低风险
AbuseIPDB：    0|低风险
IPQS：                        75|可疑IP
DB-IP：         |低风险
四、风险因子
库： IP2Location ipapi ipregistry IPQS Scamalytics ipdata IPinfo IPWHOIS
地区：    [JP]    [JP]    [JP]    [US]    [GB]    [GB]    [SG]     无 
代理：     是      否      否      是      否      否      否      无 
Tor：      否      否      否      否      否      否      否      无 
VPN：      是      否      是      是      否      无      否      无 
服务器：   是      否      否      无      否      是      否      无 
滥用：     否      否      否      否      否      否      无      无 
机器人：   否      否      无      否      否      无      无      无 
五、流媒体及AI服务解锁检测
服务商：  TikTok   Disney+  Netflix Youtube  AmazonPV  Reddit   ChatGPT 
状态：     解锁     解锁     解锁     解锁     解锁     解锁     解锁   
地区：     [GB]     [SG]     [SG]     [JP]     [JP]     [SG]     [SG]   
方式：     原生     原生     原生     原生     原生     原生     原生   
六、邮局连通性及黑名单检测
本地25端口出站：阻断
通信：远端25端口不可达​
IP地址黑名单数据库：  有效 439   正常 411   已标记 28   黑名单 0
========================================================================
今日IP检测量：2563；总检测量：1019207。感谢使用xy系列脚本！ 
报告链接：https://Report.Check.Place/ip/3KLI8H88M.svg

########################################################################
                 IP质量体检报告：2a13:edc0:1:*:*:*:*:*
                   https://github.com/xykt/IPQuality
                bash <(curl -sL https://Check.Place) -I
        报告时间：2026-02-18 05:56:09 CST  脚本版本：v2026-02-08
########################################################################
一、基础信息（Maxmind 数据库）
自治系统号：            AS216211
组织：                  Cyberverse LLC
坐标：                  103°47′9″E, 1°18′9″N
地图：                  https://check.place/1.3024,103.7857,15,cn
城市：                  N/A, 新加坡, 13
使用地：                [SG]新加坡, [AS]亚洲
注册地：                [SG]新加坡
时区：                  Asia/Singapore
IP类型：                 原生IP 
二、IP类型属性
数据库：      IPinfo    ipregistry    ipapi    IP2Location   AbuseIPDB 
使用类型：     家宽        家宽        商业        机房        家宽    
公司类型：     商业        商业        商业        机房    
三、风险评分
风险等级：      极低         低       中等       高         极高
IP2Location：   3|低风险
Scamalytics：  0|低风险
ipapi：    0.00%|极低风险
AbuseIPDB：    0|低风险
IPQS：                        75|可疑IP
DB-IP：         |低风险
四、风险因子
库： IP2Location ipapi ipregistry IPQS Scamalytics ipdata IPinfo IPWHOIS
地区：    [SG]    [SG]    [SG]    [SG]    [SG]    [SG]    [SG]     无 
代理：     否      否      否      是      否      否      否      无 
Tor：      否      否      否      否      否      否      否      无 
VPN：      否      否      否      是      否      无      否      无 
服务器：   是      是      否      无      否      是      否      无 
滥用：     否      否      否      否      否      否      无      无 
机器人：   否      否      无      否      否      无      无      无 
五、流媒体及AI服务解锁检测
服务商：  TikTok   Disney+  Netflix Youtube  AmazonPV  Reddit   ChatGPT 
状态：     失败     解锁     解锁     解锁     屏蔽     解锁     解锁   
地区：              [SG]     [SG]     [SG]              [SG]     [SG]   
方式：              原生     原生     原生              原生     原生   
六、邮局连通性及黑名单检测
本地25端口出站：阻断
通信：远端25端口不可达​
========================================================================
今日IP检测量：2565；总检测量：1019209。感谢使用xy系列脚本！ 
报告链接：https://Report.Check.Place/ip/36B2P2T1O.svg

********************************************************************************
                         网络质量体检报告：195.172.*.*
                       https://github.com/xykt/NetQuality
                    bash <(curl -sL https://Check.Place) -N
            报告时间：2026-02-18 05:58:38 CST  脚本版本：v2026-01-25
********************************************************************************
一、BGP信息（BGP.TOOLS & HE.NET）
注册信息：          RIPE, AS216211 CYBERVERSE LLC, Prefix/24
注册/修改日期：     2026-01-02 / 2026-01-02
地区：              [SG]Singapore, South-eastern Asia, Asia
地址：              16192 Coastal Hwy, 19958, Lewes, US
地理数据供给：      https://cyberverse-assets.s3.ap-northeast-1.amazonaws.com/geofeed.csv
活跃邻居：          Prefix/24  73 / 256 
二、本地策略
NAT类型：         开放网络无NAT 
TCP拥塞控制算法：cubic        TCP接收缓冲区（rmem）：4096 131072 6291456
队列调度算法：   fq_codel     TCP发送缓冲区（wmem）：4096 16384 4194304
三、接入信息（*=Tier1 *=非Tier1 *=上游）
互联网交换点接入数：0         上游数量：3         对等互联数量：60
AS174  AS3356 AS3491 
Cogent  Lumen  PCCW  
四、三网TCP大包延迟（依次为电信|联通|移动 Step=80ms） 京⣿⣿⣿⣿⣿286⣤⣤⣤⣤⣤95 ⣤⣤⣤⣤⣤95 
津⣿⣿⣿⣿⣿286⣤⣤⣤⣤⣤95 ⣤⣤⣤⣤⣤100 冀⣿⣿⣿⣿⣿291⣤⣤⣤⣤⣤100⣤⣤⣤⣤⣤115 晋⣿⣿⡇⠀⠀440⢰⠀⣴⢰⣦176⡇⠀⠀⠀⠀242
蒙⣿⣿⣿⣿⣿295⣤⣤⣤⣤⣤102⣤⣤⣤⣤⣤120 辽⣿⣿⣿⣿⣿243⣤⣤⣤⣤⣤122⣤⣤⣤⣤⣤132 吉⣿⣿⣿⣿⣿310⣤⣤⣤⣤⣤121⣤⣤⣤⣤⣤117
黑⣿⣿⣿⣿⣿320⣤⣤⣤⣤⣤132⣤⣤⣤⣤⣤111 沪⣿⣿⣿⣿⣿271⣤⣤⢠⣤⣤109⣀⢀⣄⣀⣀63  苏⣶⣶⣶⣶⣶231⣤⣤⣤⣤⣤97 ⣀⣀⣀⣀⣀70 
浙⣶⣶⣶⣶⣶217⣤⣤⣤⣤⣤86 ⣀⣀⣀⣀⣀62  皖⣿⣿⣿⣿⣿274⣤⣤⣤⣤⣤89 ⣄⣀⣀⣀⣠78  闽⣿⣿⣿⣿⣿311⣤⣤⣤⣤⣤96 ⣀⣀⣀⣀⣀58 
赣⣿⣿⣿⣿⣿309⣤⣤⣤⣤⣤82 ⣀⣀⣀⣀⣀64  鲁⣿⣿⣿⣿⣿290⢠⣤⣤⣤⣤116⣤⣤⣤⣤⣤108 豫⣿⣿⣿⣿⣿255⣤⣤⣤⣤⣤88 ⣤⣤⣤⣤⣤122
鄂⣷⣶⣶⣶⣶257⢰⢰⡆⢰⣶211⡄⣦⣶⣶⢰188 湘⣿⣿⣿⣿⣿304⣤⣤⣤⣤⣤85 ⣀⣀⣀⣀⣀57  粤⣿⣷⣷⣷⣿251⣤⣤⣤⣤⣤100⣀⣠⣤⣤⣤91 
桂⣿⣿⣿⣿⣿260⣤⣤⣤⣤⣤101⣀⣀⣀⣀⣀51  琼⣿⣿⣿⣿⣿304⣤⣤⣤⣤⣤98 ⣀⣀⣀⣀⣀54  渝⣿⣿⣿⣿⣿303⣶⢰⣶⣦⣴175⡄⡀⣄⣀⣄98 
川⣿⠀⠀⠀⣿323⣤⣤⣤⣤⢠109⣤⣤⣤⣤⣤100 贵⣿⣿⣿⣿⣿302⣤⣤⣤⣤⣤93 ⣀⣀⣀⣀⣀60  云⣿⣿⣿⣿⣿282⣤⣤⣤⣤⣤109⣀⣠⣀⣀⣀74 
藏⣿⣿⣿⣿⣿301⣤⣤⣤⣤⣤135⣤⣤⣤⣤⣤149 陕⣿⣿⣿⣿⣿286⣤⣤⣤⣤⣤105⣤⣤⣤⣤⣤101 甘⣿⣿⣿⣿⣿304⣤⣤⣤⣤⣤117⣤⣤⣤⣤⣤149
青⣿⣿⣿⣿⣿313⣤⣤⣤⣤⣤119⣤⣤⣤⣤⣤127 宁⣿⣿⣿⣿⣿303⣤⣤⣤⣤⣤113⣤⣤⣤⣤⣤116 新⣿⣿⣿⣿⣿279⣤⣤⣤⣤⣤130⣤⣤⣤⣤⣤139
五、三网回程路由（线路可能随网络负载动态变化）
北京TCP：电信 AS216211->NoData || 联通 AS216211->NoData || 移动 AS216211->NoData
北京UDP：电信   NoData->NoData || 联通   NoData->NoData || 移动   NoData->NoData
上海TCP：电信 AS216211->NoData || 联通 AS216211->NoData || 移动 AS216211->CMI   
上海UDP：电信   NoData->NoData || 联通   NoData->NoData || 移动   NoData->NoData
广州TCP：电信 AS216211->163    || 联通 AS216211->NoData || 移动 AS216211->NoData
广州UDP：电信   NoData->NoData || 联通   NoData->NoData || 移动   NoData->NoData
六、国内测速   发送  延迟    接收  延迟||单位：Mbps ms  发送  延迟    接收  延迟
苏州电信        415   396    2395   360||杭州电信        247   415    1090   388
上海联通        313   504    2601   495||香港联通          ERROR         ERROR  
苏州移动        867   186       1   179||深圳移动          ERROR         ERROR  
七、国际互连   延迟 发送 重传 接收 重传||单位：ms Mbps  延迟 发送 重传 接收 重传
香港      ⣀⣀⣀⣀⣀⣀ 38   759   0   706  18||东京      ⣀⣀⣀⣀⣀⣀ 67   417   0   454   0
新加坡    ⣀⣀⣀⣀⣀⣀  0  6478   7  3319  1k||悉尼      ⣤⣤⣤⣤⣤⣤ 97    81 540   234   0
洛杉矶    ⣶⣶⣶⣶⣶⣶165   134 285   138   0||纽约      ⣶⣶⣶⣶⣶⣶224    78   0   102   0
法兰克福  ⣤⣤⣤⣤⣤⣤154   124   0   159  59||伦敦      ⣤⣤⣤⣤⣤⣴159   156   0   169   0
阿姆斯特丹⣤⣤⣤⣤⣤⣤157   155   0   157   0||圣保罗    ⣿⣿⣿⣿⣿⣿318    53   0    47   0
================================================================================
今日网络检测量：1672；总检测量：417513。感谢使用xy系列脚本！ 
报告链接：https://Report.Check.Place/net/2MROS0AZN.svg

********************************************************************************
                    网络质量体检报告：2a13:edc0:1:*:*:*:*:*
                       https://github.com/xykt/NetQuality
                    bash <(curl -sL https://Check.Place) -N
            报告时间：2026-02-18 05:58:38 CST  脚本版本：v2026-01-25
********************************************************************************
一、BGP信息（BGP.TOOLS & HE.NET）
注册信息：          RIPE, AS216211 CYBERVERSE LLC, Prefix/48
注册/修改日期：     2024-03-27 / 2025-01-21
地区：              [SG]Singapore, South-eastern Asia, Asia
地址：              16192 Coastal Highway Lewes, DE 19958
地理数据供给：      https://cyberverse-assets.s3.ap-northeast-1.amazonaws.com/geofeed.csv
二、本地策略
TCP拥塞控制算法：cubic        TCP接收缓冲区（rmem）：4096 131072 6291456
队列调度算法：   fq_codel     TCP发送缓冲区（wmem）：4096 16384 4194304
三、接入信息（*=Tier1 *=非Tier1 *=上游）
互联网交换点接入数：99+       上游数量：8         对等互联数量：36
AS174  AS1299  AS2914 AS3257 AS3320 AS3356 AS3491 AS5511 AS6453 AS6461 AS6762  
Cogent Arelion   NTT    GTT   DTAG   Lumen  PCCW  Orange  TATA   Zayo  Sparkle 
AS6830   AS6939   AS7018 AS12956  AS30058   
Liberty Hurricane  AT&T  Telxius FDCServers 
四、三网TCP大包延迟（依次为电信|联通|移动 Step=80ms） 京⣿⣿⣿⣿⣿321⣿⣿⣿⣿⣿353⣤⣤⣤⣤⣤83 
津⣿⣿⣿⣿⣿328⣿⢸⣿⣿⣿343⣀⣀⣀⣀⣀77  冀⣿⣿⣿⣿⣿357⢸⣿⣿⣿⣿343⣤⣤⣤⣤⣤91  晋⣿⣿⣿⣿⣿334⢸⣿⣿⢸⣿355⣤⣤⣤⣤⣤88 
蒙⣿⣿⣿⣿⣿321⡇⡇⢸⢸⣿349⣤⣤⣤⣤⣤88  辽⣿⣿⣿⣿⣿334⣿⣿⣿⣿⣿377⣤⣤⣤⣤⣤98  吉⣿⣿⣿⣿⣿339⠀⣿⣿⢸⣿364⣤⣤⣤⣤⣤95 
黑⣿⣿⣿⣿⣿331⣿⣿⠀⣿⣿371⣤⣤⣤⣤⣤91  沪⣿⣿⣿⣿⣿318⣿⣿⣿⣿⣿360⣀⣀⣀⣀⣀65  苏⣿⣿⣿⣿⣿327⣿⠀⣿⣿⣿364⣀⣀⣀⣀⣀67 
浙⣿⣿⣿⣿⣿327⣿⣿⣿⡇⡇355⣀⣀⣀⣀⣀69  皖⣿⣿⣿⣿⣿327⠀⠀⠀⠀⠀0  ⣀⣠⣄⣀⣀78  闽⣿⣿⣿⣿⣿330⢸⣿⣿⣿⣿384⣀⣀⣀⣀⣀65 
赣⣿⣿⣿⣿⣿332⣿⡇⣿⣿⣿374⣀⣀⣀⣀⣀67  鲁⣿⣿⣿⣿⣿335⣿⣿⣿⣿⣿345⣠⣤⣤⣤⣤81  豫⣿⣿⣿⣿⣿332⣿⣿⣿⢸⣿355⣤⣤⣤⣤⣤85 
鄂⣿⣿⣿⣿⣿336⣿⣿⡇⣿⣿366⣄⣤⣤⣠⣤82  湘⣿⣿⣿⣿⣿340⣿⡇⢸⣿⣿369⣀⣀⣀⣀⣀61  粤⣿⣿⣿⣿⣿356⣿⣿⣿⠀⣿367⣀⣀⣀⣀⣀48 
桂⣿⣿⣿⣿⣿342⠀⡇⣿⣿⡇390⣤⣤⣠⣄⣄80  琼⣿⣿⣿⣿⣿347⣿⣿⣿⣿⣿337⣀⣀⣀⣀⣀58  渝⣿⣿⣿⣿⣿347⡇⣿⣿⡇⣿369⣠⣀⣀⣀⣀73 
川⣿⣿⣿⣿⣿352⢸⣿⣿⣿⡇371⣄⣀⣀⣠⣀76  贵⣿⣿⣿⣿⣿339⣿⣿⣿⣿⢸391⣀⣀⣀⣀⣀65  云⣿⣿⣿⣿⣿356⣿⢸⣿⡇⣿380⣀⣀⣄⣀⣀74 
藏⣿⣿⣿⣿⣿367⣿⢸⣿⣿⡇408⣤⣤⣤⣤⣤131 陕⣿⣿⣿⣿⣿324⣿⡇⣿⣿⣿336⣤⣤⣤⣤⣤87  甘⣿⣿⣿⣿⣿332⣿⡇⣿⡇⣿357⣤⣤⣤⣤⣤97 
青⣿⣿⣿⣿⣿365⣿⣿⢸⡇⣿374⣤⣤⣤⣤⣤103 宁⣿⣿⣿⣿⣿339⣿⣿⣿⣿⣿353⣤⣤⣤⣤⣤97  新⣿⣿⣿⣿⣿362⡇⣿⣿⢸⡇383⣠⣠⣀⣄⣠81 
五、三网回程路由（线路可能随网络负载动态变化）
北京TCP：电信   Cogent->163    || 联通   Cogent->4837   || 移动   Level3->CMI   
北京UDP：电信   Cogent->163    || 联通   Cogent->4837   || 移动   Level3->CMI   
上海TCP：电信   Cogent->163    || 联通   Cogent->4837   || 移动   Level3->CMI   
上海UDP：电信   Cogent->163    || 联通   Cogent->4837   || 移动   Level3->CMI   
广州TCP：电信   Cogent->163    || 联通   Cogent->4837   || 移动   Level3->CMI   
广州UDP：电信   Cogent->163    || 联通   Cogent->4837   || 移动   Level3->CMI   
七、国际互连   延迟 发送 重传 接收 重传||单位：ms Mbps  延迟 发送 重传 接收 重传
香港      ⣀⣀⣀⣀⣀⣀ 33   927 223   709 234||东京      ⣀⣀⣀⣀⣀⣀ 70   406   3   431   0
新加坡    ⣀⣀⣀⣀⣀⣀  0  6799   5  3007  1k||悉尼      ⣿⣿⣿⣿⣿⣿242    33 743    94   0
洛杉矶    ⣶⣶⣶⣶⣶⣶181   136   0   135   0||纽约      ⣶⣶⣶⣶⣶⣶212     ERROR   101 122
法兰克福  ⣤⣤⣤⣤⣤⣤150   119   1   163   0||伦敦      ⣶⣶⣴⣶⣦⣶161   151   0   162   0
阿姆斯特丹⣤⣤⣤⣤⣤⣤156   153   0   170   0||圣保罗    ⣿⣿⣿⣿⣿⣿325    53   0    59  30
================================================================================
今日网络检测量：1676；总检测量：417517。感谢使用xy系列脚本！ 
报告链接：https://Report.Check.Place/net/JD33CUV5C.svg

********************************************************************************
                         网络质量体检报告：195.172.*.*
                       https://github.com/xykt/NetQuality
                    bash <(curl -sL https://Check.Place) -N
            报告时间：2026-02-18 06:12:35 CST  脚本版本：v2026-01-25
********************************************************************************
五、三网回程路由（线路可能随网络负载动态变化）
  北京 电信    AS216211 -> NoData  
地理路径：法国 -> 北京    自治系统路径：AS216211 -> AS4847 
 1       0.39ms  80.249.*.*   AS216211                    法国 法兰西岛大区 巴黎 cyberverseservice.com
15     291.49ms  106.37.*.*   AS4847    [CHINANET-HN]     中国 北京 bj.189.cn
  北京 联通    AS216211 -> NoData  
地理路径：法国 -> 北京    自治系统路径：AS216211 -> AS4808 
 1       0.62ms  80.249.*.*   AS216211                    法国 法兰西岛大区 巴黎 cyberverseservice.com
15      95.91ms  221.222.*.*  AS4808    [UNICOM-BJ]       中国 北京 海淀 www.bbn.com.cn
  北京 移动    AS216211 -> NoData  
地理路径：法国 -> 北京    自治系统路径：AS216211 -> AS56048 
 1       0.32ms  80.249.*.*   AS216211                    法国 法兰西岛大区 巴黎 cyberverseservice.com
15     111.79ms  211.136.*.*  AS56048   [CMNET]           中国 北京 bj.10086.cn 移动
  上海 电信    AS216211 -> NoData  
地理路径：法国 -> 上海    自治系统路径：AS216211 -> AS4812 
 1       0.30ms  80.249.*.*   AS216211                    法国 法兰西岛大区 巴黎 cyberverseservice.com
16     279.27ms  101.226.*.*  AS4812    [CHINANET-SH]     中国 上海市 chinatelecom.cn 电信
  上海 联通    AS216211 -> NoData  
地理路径：法国 -> 上海    自治系统路径：AS216211 -> AS140979 
 1       0.60ms  80.249.*.*   AS216211                    法国 法兰西岛大区 巴黎 cyberverseservice.com
17     100.51ms  112.64.*.*   AS140979  [APNIC-AP]        中国 上海市 闵行 chinaunicom.cn 联通
  上海 移动    AS216211 -> CMI  
地理路径：法国 -> 上海    自治系统路径：AS216211 -> AS9808 
 1       0.44ms  80.249.*.*   AS216211                    法国 法兰西岛大区 巴黎 cyberverseservice.com
12      60.08ms  117.185.*.*  AS9808    [CMNET]           中国 上海市 chinamobileltd.com 移动
  广东 电信    AS216211 -> 163  
地理路径：法国 -> 广东    自治系统路径：AS216211 -> AS4134 
 1       0.47ms  80.249.*.*   AS216211                    法国 法兰西岛大区 巴黎 cyberverseservice.com
19     233.50ms  183.47.*.*   AS4134    [APNIC-AP]        中国 广东省 广州市 chinatelecom.com.cn 电信
  广东 联通    AS216211 -> NoData  
地理路径：法国 -> 广东    自治系统路径：AS216211 -> AS136958 
 1       0.62ms  80.249.*.*   AS216211                    法国 法兰西岛大区 巴黎 cyberverseservice.com
17     105.59ms  157.148.*.*  AS136958  [UNICOM-GD]       中国 广东省 广州市 chinaunicom.cn 联通
  广东 移动    AS216211 -> NoData  
地理路径：法国 -> 广东    自治系统路径：AS216211 -> AS56040 
 1       0.44ms  80.249.*.*   AS216211                    法国 法兰西岛大区 巴黎 cyberverseservice.com
16      60.23ms  211.139.*.*  AS56040   [CMNET]           中国 广东 广州 gd.10086.cn 移动
================================================================================
今日网络检测量：1678；总检测量：417519。感谢使用xy系列脚本！ 
报告链接：https://Report.Check.Place/net/18L94XDKD.svg

********************************************************************************
                    网络质量体检报告：2a13:edc0:1:*:*:*:*:*
                       https://github.com/xykt/NetQuality
                    bash <(curl -sL https://Check.Place) -N
            报告时间：2026-02-18 06:12:35 CST  脚本版本：v2026-01-25
********************************************************************************
五、三网回程路由（线路可能随网络负载动态变化）
  北京 电信    Cogent -> 163  
地理路径：新加坡 -> 法国 -> 德国 -> 北京    自治系统路径：AS216211 -> AS174 -> AS4134 -> AS23724 
 1       0.32ms  2a13:edc0:1:*:*:*:*:*      AS216211  新加坡 cyberverseservice.com
 2       0.98ms  2402:4480:2:*:*:*:*:*      AS174     中国 香港 cogentco.com
 3       2.69ms  2001:550:0:*:*:*:*:*       AS174     新加坡 cogentco.com
 4     159.83ms  2001:550:0:*:*:*:*:*       AS174     法国 普罗旺斯-阿尔卑斯-蓝色海岸大区 马赛 cogentco.com
 5     157.72ms  2001:550:0:*:*:*:*:*       AS174     法国 法兰西岛大区 巴黎 cogentco.com
 6     157.62ms  2001:550:0:*:*:*:*:*       AS174     德国 黑森 美因河畔法兰克福 cogentco.com
 9     307.09ms  240e:0:a:*:*:*:*:*         AS4134    中国 chinatelecom.com.cn 电信
10-11  308.47ms  240e:0:a:*:*:*:*:*         AS4134    中国 北京 chinatelecom.com.cn 电信
12-14  309.27ms  240e:0:9000:*:*:*:*:*      AS23724   中国 北京 bjtelecom.net 电信
15     309.89ms  240e:904:800:*:*:*:*:*     AS23724   中国 北京市 bjtelecom.net 电信
  北京 联通    Cogent -> 4837  
地理路径：新加坡 -> 香港 -> 日本 -> 北京    自治系统路径：AS216211 -> AS174 -> AS4837 -> AS4808 
 1       0.36ms  2a13:edc0:1:*:*:*:*:*      AS216211  新加坡 cyberverseservice.com
 2       0.87ms  2402:4480:2:*:*:*:*:*      AS174     中国 香港 cogentco.com
 3      43.80ms  2001:550:0:*:*:*:*:*       AS174     新加坡 cogentco.com
 5     194.00ms  2001:550:0:*:*:*:*:*       AS174     日本 东京都 东京 cogentco.com
 6     343.11ms  2408:8000:2:*:*:*:*:*      AS4837    中国 chinaunicom.cn 联通
 7     348.50ms  2408:8000:2:*:*:*:*:*      AS4837    中国 北京 chinaunicom.cn 联通
10-11  344.69ms  2408:8000:1f10:*:*:*:*:*   AS4808    中国 北京 www.bbn.com.cn 联通
12     346.78ms  2408:8706:0:*:*:*:*:*      AS4808    中国 北京市 www.bbn.com.cn 联通
  北京 移动    Level3 -> CMI  
地理路径：新加坡 -> 香港 -> 上海 -> 河南    自治系统路径：AS216211 -> AS3356 -> AS58453 -> AS9808 -> AS24445 -> AS137687 -> AS9808 
 1       0.35ms  2a13:edc0:1:*:*:*:*:*      AS216211  新加坡 cyberverseservice.com
 2-3     1.60ms  2001:1900:2100:*:*:*:*:*   AS3356    新加坡 lumen.com
 4-6     0.60ms  2402:4f00:100:*:*:*:*:*    AS58453   中国 香港 cmi.chinamobile.com 移动
 7      61.57ms  2402:4f00:100:*:*:*:*:*    AS58453   中国 上海 cmi.chinamobile.com
 8-10   61.28ms  2409:8080:0:*:*:*:*:*      AS9808    中国 上海 chinamobileltd.com 移动
11-12   81.19ms  2409:8080:0:*:*:*:*:*      AS9808    中国 河南 郑州市 chinamobileltd.com 移动
13      84.15ms  2409:8088:3000:*:*:*:*:*   AS24445   中国 河南省 ha.10086.cn 移动
14     210.08ms  240e:b:f004:*:*:*:*:*      AS137687  中国 河南省 郑州市 chinatelecom.cn 电信
15     206.16ms  fdbd:dc00:46:*:*:*:*:*               * RFC4193
16      86.01ms  2409:8c44:2:*:*:*:*:*      AS9808    中国 河南省 郑州市 chinamobileltd.com 移动
  上海 电信    Cogent -> 163  
地理路径：新加坡 -> 法国 -> 德国 -> 上海    自治系统路径：AS216211 -> AS174 -> AS4134 -> AS4812 -> AS4811 
 1       0.51ms  2a13:edc0:1:*:*:*:*:*      AS216211  新加坡 cyberverseservice.com
 2       0.86ms  2402:4480:2:*:*:*:*:*      AS174     中国 香港 cogentco.com
 3       0.90ms  2001:550:0:*:*:*:*:*       AS174     新加坡 cogentco.com
 4     160.52ms  2001:550:0:*:*:*:*:*       AS174     法国 普罗旺斯-阿尔卑斯-蓝色海岸大区 马赛 cogentco.com
 5     159.18ms  2001:550:0:*:*:*:*:*       AS174     法国 法兰西岛大区 巴黎 cogentco.com
 6     159.07ms  2001:550:0:*:*:*:*:*       AS174     德国 黑森 美因河畔法兰克福 cogentco.com
 9     312.52ms  240e:0:a:*:*:*:*:*         AS4134    中国 chinatelecom.com.cn 电信
10-11  309.89ms  240e:2:a:*:*:*:*:*         AS4134    中国 上海 chinatelecom.com.cn 电信
12-13  315.53ms  240e:18:10:*:*:*:*:*       AS4812    中国 上海 chinatelecom.cn
15     314.33ms  240e:96c:1100:*:*:*:*:*    AS4811    中国 上海市 chinatelecom.cn 电信
  上海 联通    Cogent -> 4837  
地理路径：新加坡 -> 香港 -> 日本 -> 北京 -> 江苏    自治系统路径：AS216211 -> AS174 -> AS4837 
 1       0.38ms  2a13:edc0:1:*:*:*:*:*      AS216211  新加坡 cyberverseservice.com
 3       2.40ms  2001:550:0:*:*:*:*:*       AS174     新加坡 cogentco.com
 4     183.61ms  2001:550:0:*:*:*:*:*       AS174     中国 香港 cogentco.com
 5     186.52ms  2001:550:0:*:*:*:*:*       AS174     日本 东京都 东京 cogentco.com
 6-9   348.74ms  2408:8000:2:*:*:*:*:*      AS4837    中国 北京 chinaunicom.cn 联通
10-12  372.19ms  2408:8000:a009:*:*:*:*:*   AS4837    中国 江苏省 泰州市 chinaunicom.cn 联通
13     351.92ms  2408:8000:a009:*:*:*:*:*   AS4837    中国 江苏省 泰州市 chinaunicom.cn 联通
  上海 移动    Level3 -> CMI  
地理路径：新加坡 -> 香港 -> 上海    自治系统路径：AS216211 -> AS3356 -> AS58453 -> AS9808 
 1       0.48ms  2a13:edc0:1:*:*:*:*:*      AS216211  新加坡 cyberverseservice.com
 2-3     4.40ms  2001:1900:2100:*:*:*:*:*   AS3356    新加坡 lumen.com
 4-6     0.81ms  2402:4f00:100:*:*:*:*:*    AS58453   中国 香港 cmi.chinamobile.com 移动
 7      59.82ms  2402:4f00:100:*:*:*:*:*    AS58453   中国 上海 cmi.chinamobile.com 移动
 8-12   62.18ms  2409:8080:0:*:*:*:*:*      AS9808    中国 上海 chinamobileltd.com 移动
14      64.87ms  2409:8c1e:75b0:*:*:*:*:*   AS9808    中国 上海 上海 chinamobileltd.com
  广东 电信    Cogent -> 163  
地理路径：新加坡 -> 法国 -> 德国 -> 广东    自治系统路径：AS216211 -> AS174 -> AS4134 -> AS4816 
 1       0.45ms  2a13:edc0:1:*:*:*:*:*      AS216211  新加坡 cyberverseservice.com
 2       1.07ms  2402:4480:2:*:*:*:*:*      AS174     中国 香港 cogentco.com
 3      46.98ms  2001:550:0:*:*:*:*:*       AS174     新加坡 cogentco.com
 4     159.94ms  2001:550:0:*:*:*:*:*       AS174     法国 普罗旺斯-阿尔卑斯-蓝色海岸大区 马赛 cogentco.com
 5     157.98ms  2001:550:0:*:*:*:*:*       AS174     法国 法兰西岛大区 巴黎 cogentco.com
 6     157.75ms  2001:550:0:*:*:*:*:*       AS174     德国 黑森 美因河畔法兰克福 cogentco.com
 9     333.12ms  240e:0:a:*:*:*:*:*         AS4134    中国 chinatelecom.com.cn 电信
10-11  332.90ms  240e:0:a:*:*:*:*:*         AS4134    中国 广东 广州 chinatelecom.com.cn 电信
12-13  336.80ms  240e:1f:6000:*:*:*:*:*     AS4816    中国 广东 深圳 电信
15     330.03ms  240e:97c:4040:*:*:*:*:*    AS4816    中国 广东省 深圳市 电信
  广东 联通    Cogent -> 4837  
地理路径：新加坡 -> 香港 -> 日本 -> 北京 -> 广东    自治系统路径：AS216211 -> AS174 -> AS4837 -> AS17816 
 1       0.53ms  2a13:edc0:1:*:*:*:*:*      AS216211  新加坡 cyberverseservice.com
 2       1.09ms  2402:4480:2:*:*:*:*:*      AS174     中国 香港 cogentco.com
 3       1.92ms  2001:550:0:*:*:*:*:*       AS174     新加坡 cogentco.com
 5     189.64ms  2001:550:0:*:*:*:*:*       AS174     日本 东京都 东京 cogentco.com
 6-9   355.48ms  2408:8000:2:*:*:*:*:*      AS4837    中国 北京 chinaunicom.cn 联通
10-13  365.38ms  2408:8001:3101:*:*:*:*:*   AS17816   中国 广东 潮州市 联通
14     366.43ms  2408:8001:3101:*:*:*:*:*   AS17816   中国 广东 潮州 China Unicom IP network China169 Guangdong province
  广东 移动    Level3 -> CMI  
地理路径：新加坡 -> 香港 -> 广东    自治系统路径：AS216211 -> AS3356 -> AS58453 -> AS9808 
 1       0.46ms  2a13:edc0:1:*:*:*:*:*      AS216211  新加坡 cyberverseservice.com
 2-3     1.13ms  2001:1900:2100:*:*:*:*:*   AS3356    新加坡 lumen.com
 4-7     0.78ms  2402:4f00:100:*:*:*:*:*    AS58453   中国 香港 cmi.chinamobile.com 移动
 8-10   41.38ms  2409:8080:0:*:*:*:*:*      AS9808    中国 广东 广州 chinamobileltd.com 移动
16      45.61ms  2409:8c54:2010:*:*:*:*:*   AS9808    中国 广东省 chinamobileltd.com 移动
================================================================================
今日网络检测量：1679；总检测量：417520。感谢使用xy系列脚本！ 
报告链接：https://Report.Check.Place/net/3IS59AFBO.svg

[NodeQuality链接](https://nodequality.com/r/xBpqgFYbYxuXPkbWx6pJ4M5pIw8lLbpb)
```
