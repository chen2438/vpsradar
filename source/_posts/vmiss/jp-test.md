---
title: 【NodeQuality】VMISS 日本 VPS 测试
date: 2026-02-18
updated: 
categories:
- vmiss
cover: /img/vmiss.png
tags:
- 日本VPS
- 评测
description: 
copyright: false
---

## [NodeQuality] VMISS JP.TKY.TRI.Basic 测试

官网：https://app.vmiss.com/aff.php?aff=4367

数据来源：https://www.nodeseek.com/post-620924-1

```
########################################################################
                  bash <(curl -sL https://run.NodeQuality.com)
                   https://github.com/LloydAsp/NodeQuality
        报告时间：2026-02-15 18:55:56 CST  脚本版本：v0.0.1
        频道: https://t.me/nodeselect 网站：https://NodeQuality.com
########################################################################


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                          硬件质量体检报告：154.36.*.*
                    https://github.com/xykt/HardwareQuality
                    bash <(curl -sL https://Check.Place) -H
            报告时间：2026-02-15 18:56:08 CST  脚本版本：v2026-02-10
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
一、操作系统信息
容器/虚拟化：          KVM 虚拟机
架构：                 x86_64
操作系统/内核：        Debian GNU/Linux 12 (bookworm) 6.1.0-42-cloud-amd64
运行时间：             0 天 0 小时 10 分钟
负载：                 0.31, 0.10, 0.03
进程：                 3 用户，79 进程，12/120 活跃/总服务
区域设置：             C, UTF-8, Etc/UTC UTC +0000
二、主板信息
BIOS：    SeaBIOS, 版本1.16.0-1.module_el8.7.0+1140+ff0772f9
芯片组：  Intel 82371SB PIIX3 ISA [Natoma/Triton II]
          Intel 440FX - 82441FX PMC [Natoma]
网卡：    Red Hat, Inc. Virtio network device
三、CPU测评
CPU：     AMD EPYC-Milan Processor 步进1 (25代) 32/64-bit
           ╚═ 1核心, 1线程, 2645.030MHz, 利用率4%        
缓存：    L1d 32 KiB, L1i 32 KiB, L2 512 KiB, L3 32 MiB
指令集：   ✘ VT-x/AMD-V    ✔ AES-NI    ✔ AVX2    ✔ BMI1/2    ✘ EPT/NPT 
Sysbench：单线程 3856.87     
GB5基准： J1900 N5105 N100 6700K 9900K 5900X 12900K 14900K 7713 7995WX
GB5单核：      |1250
GB5多核：      |1217
详细结果：https://browser.geekbench.com/v5/cpu/24114367
五、内存测评
内存：    总容量 973 MB,  已用 214 MB(22%),  可用 759 MB(78%)
超开指标： ✔ 气球回收     ✘ KSM 复用 
Sysbench：读取 50693.7 MB/s    写入 31228.2 MB/s    延迟 146 ns
六、硬盘测评
硬盘：    数量 1,  总容量 9.7G,  已用容量 2.0G(20%),  可用容量 7.3G(80%)
测试设备：vda1(/r**t) -> DISK
Fio测试： RND4K/Q1    IOPS||RND4K/Q32   IOPS||SEQ1M/Q1    IOPS||SEQ1M/Q8    IOPS
读取：    74.4MB/s     19k||423MB/s     108k||3621MB/s    3.6k||18586MB/s    19k
写入：    65.4MB/s     17k||274MB/s      70k||2504MB/s    2.5k||4808MB/s    4.8k
七、HQ硬件加权评分
项目：      总 分          CPU           GPU          内 存         硬 盘  
分数：      29243    =    17054    +     N/A     +    10119    +    2070   
排名：      3.6%          12.7%          N/A          4.9%          6.3%   
================================================================================
今日硬件检测量：126；总检测量：3632。感谢使用xy系列脚本！ 
报告链接：https://Report.Check.Place/hardware/36ZN40VR4.svg

########################################################################
                       IP质量体检报告：154.36.*.*
                   https://github.com/xykt/IPQuality
                bash <(curl -sL https://Check.Place) -I
        报告时间：2026-02-15 18:59:40 CST  脚本版本：v2026-02-08
########################################################################
一、基础信息（Maxmind 数据库）
自治系统号：            AS979
组织：                  NetLab Global
坐标：                  97°49′19″W, 37°45′4″N
地图：                  https://check.place/37.751,-97.822,13,cn
城市：                  N/A
使用地：                [JP]日本, [NA]北美洲
注册地：                [US]美国
时区：                  America/Chicago
IP类型：                 广播IP 
二、IP类型属性
数据库：      IPinfo    ipregistry    ipapi    IP2Location   AbuseIPDB 
使用类型：     商业        商业        机房        机房        商业    
公司类型：     家宽        机房        家宽        机房    
三、风险评分
风险等级：      极低         低       中等       高         极高
IP2Location：   3|低风险
Scamalytics：   2|低风险
ipapi：    0.04%|极低风险
AbuseIPDB：    0|低风险
IPQS：                        75|可疑IP
DB-IP：         |低风险
四、风险因子
库： IP2Location ipapi ipregistry IPQS Scamalytics ipdata IPinfo IPWHOIS
地区：    [JP]    [JP]    [JP]    [JP]    [JP]    [JP]    [JP]    [JP]
代理：     否      否      否      是      否      否      否      否 
Tor：      否      否      否      否      否      否      否      否 
VPN：      否      否      否      是      否      无      是      否 
服务器：   是      否      是      无      否      否      否      是 
滥用：     否      否      否      否      否      否      无      无 
机器人：   否      否      无      否      否      无      无      无 
五、流媒体及AI服务解锁检测
服务商：  TikTok   Disney+  Netflix Youtube  AmazonPV  Reddit   ChatGPT 
状态：     解锁     解锁     解锁     解锁     解锁     解锁     解锁   
地区：     [JP]     [JP]     [JP]     [JP]     [JP]     [JP]     [JP]   
方式：     原生     原生     原生     原生     原生     原生     原生   
六、邮局连通性及黑名单检测
本地25端口出站：阻断
通信：远端25端口不可达​
IP地址黑名单数据库：  有效 439   正常 414   已标记 23   黑名单 2
========================================================================
今日IP检测量：1027；总检测量：1013066。感谢使用xy系列脚本！ 
报告链接：https://Report.Check.Place/ip/3K5IPDLRM.svg

********************************************************************************
                          网络质量体检报告：154.36.*.*
                       https://github.com/xykt/NetQuality
                    bash <(curl -sL https://Check.Place) -N
            报告时间：2026-02-15 19:01:18 CST  脚本版本：v2026-01-25
********************************************************************************
一、BGP信息（BGP.TOOLS & HE.NET）
注册信息：          ARIN, Cogent Communications, LLC (COGC), Prefix/16
注册/修改日期：     1992-02-05 / 2025-09-23
地区：              [US]United States of America, Northern America, Americas
地址：              2450 N Street NW
活跃邻居：          Subnet/24  195 / 256     Prefix/16  23131 / 65536 
二、本地策略
NAT类型：         开放网络无NAT 
TCP拥塞控制算法：bbr          TCP接收缓冲区（rmem）：4096 131072 6291456
队列调度算法：   fq           TCP发送缓冲区（wmem）：4096 16384 4194304
三、接入信息（*=Tier1 *=非Tier1 *=上游）
互联网交换点接入数：-         上游数量：-         对等互联数量：-
四、三网TCP大包延迟（依次为电信|联通|移动 Step=80ms） 京⣀⣀⣀⣀⣀74 ⣀⣀⣀⣀⣀60 ⣀⣀⣀⣀⣤75 
津⣀⣤⣤⣄⣠80 ⣀⣀⣀⣀⣀57 ⣀⣀⣀⣀⣀71  冀⣀⣀⣀⣄⣠77 ⣀⣀⣀⣀⣀69 ⣤⣤⣤⣠⣠88  晋⡆⠀⠀⠀⠀177⢀⣧⠀⣤⣤207⡄⠀⠀⠀⠀85 
蒙⣄⣠⣀⣤⣤83 ⣀⣀⣀⣀⣀64 ⣠⣤⣀⣀⣤79  辽⣤⣤⣤⣤⣤87 ⣀⣀⣀⣀⣀73 ⣤⣤⣤⣤⣤90  吉⣤⣤⣤⣤⣤94 ⣀⣀⣀⣀⣀71 ⣤⣤⣤⣤⣤89 
黑⣤⣤⣤⣤⣤95 ⣤⣤⣤⣤⣤82 ⣤⣤⣤⣤⣤90  沪⢀⣀⣀⣀⣀53 ⡀⣀⢀⣀⣀61 ⣀⠀⣀⣀⢀68  苏⣀⣀⣀⣀⣀59 ⣀⣀⣀⣀⣀63 ⣀⣀⣀⣀⣀65 
浙⣀⣀⣀⣀⣀62 ⣀⣀⣀⣀⣀65 ⣀⣀⣀⣀⣀59  皖⣀⣀⣀⣀⣀64 ⣀⣀⣀⣀⣀60 ⣤⣤⣤⣤⣤101 闽⣠⣀⣀⣀⣠67 ⣀⣀⣀⣀⣀73 ⣠⣀⣀⣀⣀73 
赣⣀⣀⣀⣀⣀73 ⣀⣀⣀⣀⣀62 ⣶⣶⣶⣶⣶182 鲁⣀⣄⣀⣀⣀76 ⣀⣀⣀⣀⣀64 ⢠⣤⣤⣤⣤85  豫⣀⢀⣄⣀⣀71 ⣀⣀⣀⣀⣀59 ⣤⢠⣤⣤⣤93 
鄂⣆⢀⣀⣀⣆93 ⡀⣠⣤⣤⣀102⢰⡆⠀⠀⢰204 湘⢀⣀⣀⣀⣀67 ⣀⣀⣀⣀⣀66 ⣀⣀⣀⣀⣀62  粤⣀⣀⣀⣀⣀57 ⣤⣤⣀⣀⣤79 ⣀⣀⣀⣀⣀70 
桂⣀⣀⣀⣀⣀62 ⣤⣠⣤⣤⣤86 ⣀⣀⣀⣀⣀71  琼⣀⣀⣀⣀⣀62 ⣤⣤⣤⣤⣤89 ⣀⣀⣀⣀⣀70  渝⢰⣀⣀⣀⣄84 ⣀⣦⡄⡄⡄135⡆⢠⢠⣦⣦126
川⣤⣄⣠⣠⣤80 ⡄⣤⣤⣤⣤82 ⣿⣿⡇⣿⣿281 贵⣇⣀⣀⣀⣀97 ⣀⣀⣀⣀⣀74 ⣀⣀⣀⣀⣀72  云⣄⣄⣄⣀⣀78 ⣤⣤⡄⠀⠀85 ⣤⣤⣤⣤⣤86 
藏⣤⣤⣤⣤⣤86 ⣤⣤⣤⣤⣤101⣤⣤⣤⣤⣤146 陕⣤⣠⣤⣤⣠83 ⣀⣀⣀⣀⣀69 ⣤⣤⣤⣤⣤89  甘⣄⣤⣤⣤⣤86 ⣀⣀⣀⣀⣀71 ⣤⣤⣤⣤⣤95 
青⣤⣤⣤⣤⣤96 ⣀⣀⣀⣀⣀75 ⣠⣄⣄⣄⣄89  宁⣤⣤⣤⣤⣤85 ⣀⣀⣀⣀⣀69 ⣤⣤⣤⣤⣤100 新⣤⣤⣤⣤⣤115⣤⣤⣤⣤⣤104⣤⣤⣤⣤⣤120
五、三网回程路由（线路可能随网络负载动态变化）
北京TCP：电信    AS979->CTGGIA || 联通    AS979->10099  || 移动    AS979->CMI   
北京UDP：电信    AS979->CTGGIA || 联通    AS979->10099  || 移动    AS979->CMI   
上海TCP：电信    AS979->CTGGIA || 联通    AS979->10099  || 移动    AS979->CMI   
上海UDP：电信    AS979->CTGGIA || 联通    AS979->10099  || 移动    AS979->CMI   
广州TCP：电信    AS979->CTGGIA || 联通    AS979->10099  || 移动    AS979->CMI   
广州UDP：电信    AS979->CTGGIA || 联通    AS979->10099  || 移动    AS979->CMI   
六、国内测速   发送  延迟    接收  延迟||单位：Mbps ms  发送  延迟    接收  延迟
苏州电信         96   103      91   102||杭州电信         96    96      96    83
上海联通          ERROR         ERROR  ||香港联通          ERROR         ERROR  
苏州移动         93   447       0   429||深圳移动          ERROR         ERROR  
七、国际互连   延迟 发送 重传 接收 重传||单位：ms Mbps  延迟 发送 重传 接收 重传
香港      ⣀⣀⣀⣀⣀⣀ 44    91  30    91 838||东京      ⣀⣀⣀⣀⣀⣀  0    95   0    95 169
新加坡    ⣀⣀⣀⣀⣀⣀ 78    88 165    90   0||悉尼      ⣤⣤⣤⣤⣤⣤132    81   0    83   0
洛杉矶    ⣤⣤⣤⣤⣤⣤100    84   0    86   0||纽约      ⣤⣤⣤⣤⣤⣤153    76   1    79   0
法兰克福  ⣶⣶⣶⣶⣶⣶216    63   9    59   0||伦敦      ⣶⣶⣶⣶⣶⣶229    67   0    71   0
阿姆斯特丹⣶⣶⣶⣶⣶⣶218    60   0    68   0||圣保罗    ⣿⣿⣿⣿⣿⣿320    39   0    34   0
================================================================================
今日网络检测量：510；总检测量：413715。感谢使用xy系列脚本！ 
报告链接：https://Report.Check.Place/net/1QWVPNM1I.svg

********************************************************************************
                          网络质量体检报告：154.36.*.*
                       https://github.com/xykt/NetQuality
                    bash <(curl -sL https://Check.Place) -N
            报告时间：2026-02-15 19:08:13 CST  脚本版本：v2026-01-25
********************************************************************************
五、三网回程路由（线路可能随网络负载动态变化）
  北京 电信    AS979 -> CTGGIA  
地理路径：日本 -> 香港 -> 北京    自治系统路径：AS979 -> AS23764 -> AS4809 -> AS4134 -> AS4847 
 1       0.90ms  154.36.*.*   AS979                       日本 东京都 户越 as979.net
 2       0.44ms  10.81.*.*                                * RFC1918
 4-5     1.55ms  203.128.*.*  AS23764                     日本 东京都 东京 chinatelecomglobal.com 电信
 6      44.28ms  203.22.*.*             [CTG-CN]          * 中国 香港 电信
 7      49.45ms  69.194.*.*   AS23764                     * 中国 香港 电信/CTGNet
 9-10  165.74ms  59.43.*.*    AS4809    [CN2-BackBone]    * 中国 北京 chinatelecom.cn 电信
11      66.33ms  202.97.*.*   AS4134    [CHINANET-BB]     中国 香港 chinatelecom.com.cn 电信
13-15   71.21ms  219.141.*.*  AS4847    [CHINATELECOM-BJ] 中国 北京 bj.189.cn
16      74.34ms  106.37.*.*   AS4847    [CHINANET-HN]     中国 北京 bj.189.cn
  北京 联通    AS979 -> 10099  
地理路径：日本 -> 上海 -> 广东 -> 北京    自治系统路径：AS979 -> AS10099 -> AS4837 -> AS4808 
 1       1.03ms  154.36.*.*   AS979                       日本 东京都 户越 as979.net
 2       0.45ms  10.81.*.*                                * RFC1918
 5-8     0.93ms  203.160.*.*  AS10099   [CUG-BACKBONE]    日本 东京都 东京 chinaunicomglobal.com
 9-10   56.71ms  219.158.*.*  AS4837    [CU169-BACKBONE]  中国 上海 X-I chinaunicom.cn 联通
11      60.17ms  219.158.*.*  AS4837    [CU169-BACKBONE]  中国 广东省 广州市 chinaunicom.cn
12      56.28ms  219.158.*.*  AS4837    [CU169-BACKBONE]  中国 北京 chinaunicom.cn 联通
13      61.71ms  124.65.*.*   AS4808    [UNICOM-BJ]       中国 北京 www.bbn.com.cn 联通
14-15   63.22ms  61.148.*.*   AS4808    [UNICOM-CN]       中国 北京 www.bbn.com.cn
18      63.53ms  221.222.*.*  AS4808    [UNICOM-BJ]       中国 北京 海淀 www.bbn.com.cn
  北京 移动    AS979 -> CMI  
地理路径：日本 -> 北京    自治系统路径：AS979 -> AS58453 -> AS9808 -> AS56048 
 1       0.89ms  154.36.*.*   AS979                       日本 东京都 户越 as979.net
 2       0.82ms  10.81.*.*                                * RFC1918
 4       0.65ms  223.118.*.*  AS58453   [CMI-INT]         中国 香港 cmi.chinamobile.com 移动
 5-6     0.44ms  223.119.*.*  AS58453   [CMI-INT]         日本 东京都 东京 cmi.chinamobile.com 移动
 7      52.57ms  223.120.*.*  AS58453   [CMI-INT]         中国 北京 cmi.chinamobile.com 移动
 8-9    52.56ms  221.183.*.*  AS9808    [CMNET]           中国 北京 X-I chinamobileltd.com 移动
19      55.85ms  211.136.*.*  AS56048   [CMNET]           中国 北京 bj.10086.cn 移动
  上海 电信    AS979 -> CTGGIA  
地理路径：日本 -> 香港 -> 上海    自治系统路径：AS979 -> AS23764 -> AS4809 -> AS4812 
 1       0.86ms  154.36.*.*   AS979                       日本 东京都 户越 as979.net
 2       0.40ms  10.81.*.*                                * RFC1918
 4-5     1.66ms  203.128.*.*  AS23764                     日本 东京都 东京 chinatelecomglobal.com 电信
 6      44.01ms  203.22.*.*             [CTG-CN]          * 中国 香港 电信
 7      46.00ms  69.194.*.*   AS23764                     * 中国 香港 电信/CTGNet
 9     147.74ms  59.43.*.*    AS4809    [CN2-Global]      * 中国 上海 chinatelecom.cn 电信
10-11  151.12ms  59.43.*.*    AS4809    [CN2-BackBone]    * 中国 上海 I-C chinatelecom.cn 电信
18      54.11ms  101.226.*.*  AS4812    [CHINANET-SH]     中国 上海市 chinatelecom.cn 电信
  上海 联通    AS979 -> 10099  
地理路径：日本 -> 上海    自治系统路径：AS979 -> AS10099 -> AS4837 -> AS140979 
 1      19.67ms  154.36.*.*   AS979                       日本 东京都 户越 as979.net
 2      12.83ms  10.81.*.*                                * RFC1918
 5-8     0.94ms  203.160.*.*  AS10099   [CUG-BACKBONE]    日本 东京都 东京 chinaunicomglobal.com
 9-10   58.98ms  219.158.*.*  AS4837    [CU169-BACKBONE]  中国 上海 X-I chinaunicom.cn 联通
18      61.42ms  58.246.*.*   AS140979                    中国 上海市 chinaunicom.cn 联通
  上海 移动    AS979 -> CMI  
地理路径：日本 -> 上海    自治系统路径：AS979 -> AS58453 -> AS9808 
 1       1.23ms  154.36.*.*   AS979                       日本 东京都 户越 as979.net
 2       0.99ms  10.81.*.*                                * RFC1918
 4       0.66ms  223.118.*.*  AS58453   [CMI-INT]         中国 香港 cmi.chinamobile.com 移动
 5-6     0.59ms  223.119.*.*  AS58453   [CMI-INT]         日本 东京都 东京 cmi.chinamobile.com 移动
 7      53.65ms  223.120.*.*  AS58453   [CMI-INT]         中国 上海 cmi.chinamobile.com
 8-10   31.99ms  221.183.*.*  AS9808    [CMNET]           中国 上海 X-I chinamobileltd.com 移动
14      58.98ms  117.185.*.*  AS9808    [CMNET]           中国 上海市 chinamobileltd.com 移动
  广东 电信    AS979 -> CTGGIA  
地理路径：日本 -> 香港 -> 广东    自治系统路径：AS979 -> AS23764 -> AS4809 -> AS4134 
 1       0.95ms  154.36.*.*   AS979                       日本 东京都 户越 as979.net
 2       0.83ms  10.81.*.*                                * RFC1918
 4-5     1.62ms  203.128.*.*  AS23764                     日本 东京都 东京 chinatelecomglobal.com 电信
 6      44.11ms  203.22.*.*             [CTG-CN]          * 中国 香港 电信
 7      49.18ms  69.194.*.*   AS23764                     * 中国 香港 电信/CTGNet
10     158.92ms  59.43.*.*    AS4809    [CN2-BackBone]    * 中国 广东 广州 chinatelecom.cn 电信
11      65.11ms  202.97.*.*   AS4134    [CHINANET-BB]     中国 广东 广州 chinatelecom.com.cn 电信
18      57.84ms  183.47.*.*   AS4134    [APNIC-AP]        中国 广东省 广州市 chinatelecom.com.cn 电信
  广东 联通    AS979 -> 10099  
地理路径：日本 -> 上海 -> 广东    自治系统路径：AS979 -> AS10099 -> AS4837 -> AS17816 -> AS136958 
 1       1.02ms  154.36.*.*   AS979                       日本 东京都 户越 as979.net
 2       0.65ms  10.81.*.*                                * RFC1918
 5-8     1.62ms  203.160.*.*  AS10099   [CUG-BACKBONE]    日本 东京都 东京 chinaunicomglobal.com
 9-11   58.97ms  219.158.*.*  AS4837    [CU169-BACKBONE]  中国 上海 X-I chinaunicom.cn 联通
13      82.75ms  120.81.*.*   AS17816   [APNIC-AP]        中国 广东 广州 China Unicom IP network China169 Guangdong province
19      78.33ms  157.148.*.*  AS136958  [UNICOM-GD]       中国 广东省 广州市 chinaunicom.cn 联通
  广东 移动    AS979 -> CMI  
地理路径：日本 -> 广东    自治系统路径：AS979 -> AS58453 -> AS9808 -> AS56040 
 1       1.00ms  154.36.*.*   AS979                       日本 东京都 户越 as979.net
 2       0.52ms  10.81.*.*                                * RFC1918
 4       0.67ms  223.118.*.*  AS58453   [CMI-INT]         中国 香港 cmi.chinamobile.com 移动
 5-6     0.53ms  223.119.*.*  AS58453   [CMI-INT]         日本 东京都 东京 cmi.chinamobile.com 移动
 7      59.12ms  223.120.*.*  AS58453   [CMI-INT]         中国 广东 广州 cmi.chinamobile.com
 8-10   60.34ms  221.183.*.*  AS9808    [CMNET]           中国 广东 广州 X-I chinamobileltd.com 移动
12      67.62ms  211.136.*.*  AS56040   [CMNET]           中国 广东 广州 gd.10086.cn 移动
13-15   70.23ms  120.198.*.*  AS56040   [APNIC-AP]        中国 广东 广州 gd.10086.cn 移动
19      74.87ms  211.139.*.*  AS56040   [CMNET]           中国 广东 广州 gd.10086.cn 移动
================================================================================
今日网络检测量：521；总检测量：413726。感谢使用xy系列脚本！ 
报告链接：https://Report.Check.Place/net/5PCI0S5J6.svg

[NodeQuality链接](https://nodequality.com/r/Qr4YGohBjr9mtgJV00N12zxs01wuA8Kg)

```
