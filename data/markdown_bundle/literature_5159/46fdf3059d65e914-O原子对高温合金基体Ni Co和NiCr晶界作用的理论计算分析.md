# O原子对高温合金基体Ni Co和NiCr晶界作用的理论计算分析

<!-- source: D:\总文献\O原子对高温合金基体Ni Co和NiCr晶界作用的理论计算分析.pdf -->
<!-- file_sha256: 061d53c0dd29b9d8354f0ea4b04d0bb615b9cb44b977591d7f0eb69a583975fb -->

## Page 1

第 59 卷　第 2 期
2023 年 2 月
V ol . 59 No . 2
Feb . 2023ACTA METALLURGICA SINICA
O 原子对高温合金基体 Ni 、 Co 和 NiCr 晶界
作用的理论计算分析
李 昕 江 河 姚志浩 董建新
( 北京科技大学 材料科学与工程学院 北京 100083 )
摘 要 利用第一性原理计算方法对高温合金基体元素 Ni 进行了不同氧浓度下的晶界理想拉伸实验 ， 并结合理
想分离功和差分电荷图给出了氧弱化 Ni 晶界的内在原因 。 对 Co 和 NiCr 晶界进行了类似的对比分析 ， 给出了
高温合金不同基体晶界氧化弱化的程度差异以及弱化原因 。 结果表明 ， O 原子较大的电负性使得晶界处 Ni —
Ni 金属键因电荷缺失而弱化 ； 在拉伸过程中 ， 当拉伸应变达到 0 . 10 ， 含氧 Ni 晶界应变完全由含氧晶界处的
Ni — Ni 键提供 ， 氧的存在明显加速了 Ni 晶界的断裂失效过程 ； 钴基合金晶界氧化后强度更高 ， 比 Ni 有更好的
抗氧化弱化性能 ， 但断裂应变较小 ； NiCr 基晶界强度最低 ， 但氧化后力学性能较稳定 ； Ni 晶界氧化弱化的原因
在于 O 原子带来的结构畸变 ， 而 Co 和 NiCr 基晶界氧化弱化现象主要来自电荷密度分布的改变 。
关 键 词 高温合金 ， 晶界 ， 氧化 ， 第一性原理
中图分类号 TG 132 . 3 文章编号 0412 - 1961 ( 2023 ) 02 - 0309 - 10
Theoretical Calculation and Analysis of the Effect of Oxygen 
Atom on the Grain Boundary of Superalloy Matrices Ni , 
Co and NiCr
LI Xin , JIANG He , YAO Zhihao , DONG Jianxin
School of Materials Science and Engineering , University of Science and Technology Beijing , Beijing 100083 , China
Correspondent : JIANG He , Tel : 13811910685 , E-mail : jianghe 17 @sina . cn
Supported by National Natural Science Foundation of China ( No . 51771016 )
Manuscript received 2021 - 04 - 30 , i n revised form 2021 - 06 - 03
ABSTRACT As advanced aero engines and heavy-duty gas turbines require high service tempera -
tures , how to maintain better performance and damage tolerance of superalloys at high service tempera -
tures has emerged as a critical issue in the application of superalloys . Previous research has shown that 
temperature rise has no effect on the crack growth rate of alloys placed in a vacuum . However , in air , fa -
tigue crack growth rate is observed to significantly depend on temperature . According to the sample frac -
ture , which is an oxide-covered intergranular fracture , oxygen atoms significantly affect the performance 
of superalloys . As first-principle calculation method has advanced rapidly in recent years , it can eliminate 
the effect of irrelevant impurity atoms on the weakening of grain boundaries and establish a pure grain 
boundary system . Thus , this method is an ideal analysis tool for this research . The ideal tensile test com -
bined with ideal separation work and charge density difference of the grain boundary in nickel-based su -
peralloy under different oxygen concentrations , was performed using the first-principle calculation meth -
od . The internal reason for the weakening of the Ni grain boundary due to oxygen is given . A similar com -
资 助 项 目 国家自然科学基金项目 No . 51771016
收 稿 日 期 2021 - 04 - 30 定稿日期 2021 - 06 - 03
作 者 简 介 李 昕 ， 男 ， 1995 年生 ， 博士生
通 讯 作 者 江 河 ， jianghe 17 @sina . cn ， 主要从事变形高温合金研究
D O I 10 . 11900 / 0412 . 1961 . 2021 . 00176

## Page 2

59 卷金 属 学 报
parative analysis of Co and NiCr grain boundaries was also performed . Further , the cause of the oxi -
dation and weakening of the grain boundaries is explained . The results demonstrate that the high 
electronegativity of O atoms weakens the Ni — Ni metal bond at the grain boundary due to the lack of 
charge . Further , in the stretching process , when the tensile strain reaches 0 . 10 , the strain of the oxygen-
containing Ni grain boundary is entirely provided by the Ni — Ni bond present at this boundary . The pres -
ence of oxygen significantly accelerates the fracture failure process of the Ni grain boundary . In addition , 
Co-based alloy has higher strength after grain boundary oxidation and has better oxidation resistance 
weakening performance than Ni ; however , the strain of fracture is small . Although the NiCr-based grain 
boundary strength is the weakest , the mechanical properties after oxidation are relatively stable . The rea -
son for the weakening of the Ni grain boundary due to oxidation is attributed to structural distortion 
caused by oxygen atoms , whereas the weakening of Co- and NiCr-based grain boundary due to oxida -
tion is primarily related to changes in the charge density distribution .
K E Y W O R D S superalloy , grain boundary , oxidation , first-principle
镍基高温合金是航空发动机及重型燃气轮机的
关键制造材料 ， 随着先进航空发动机及重型燃气轮
机对更高服役温度的要求 ， 高温合金如何在更高服
役温度下保持较好的使用性能与损伤容限已经成为
高温合金材料应用的核心问题 。 疲劳裂纹扩展实验
作 为 衡 量 材 料 损 伤 容 限 的 重 要 指 标 ， Li 等
[ 1 ]
发 现
RR 1000 合金在 550 ~ 750 ℃ 真空环境下的疲劳裂纹
扩展曲线不同于空气环境的结果 ， 真空中裂纹扩展
速率随温度升高变动较小 。 同样 ， U 720 Li 合金常温
下和 650 ℃ 真空下的疲劳裂纹扩展实验
[ 2 ]
表明 ， 温度
升高并没有明显影响真空中合金的裂纹扩展速率 ，
但在空气环境中的不同温度疲劳实验却明显表现出
裂纹扩展速率的温度相关性 。 近年来的一些工作发
现 ， GH 4738
[ 3 ]
、 FGH 4097
[ 4 ]
等合金均存在疲劳裂纹急
速扩展的拐点温度 ， 并发现在拐点温度处的断裂试
样断口为沿晶断口 ， 其表面存在大量的氧化物覆盖 ，
可见 O 对镍基高温合金晶界性能有极为显著的影
响 。 基于 NiCr 的抗氧化机制已有相关报道
[ 5 ~ 7 ]
， 近些
年来 ， 钴基高温合金发展热度不减 ， 其性能可与镍基
合金相媲美 。
第一性原理计算可以排除无关因素的影响 ， 建
立纯净晶界体系 ， 并排除了其他杂质原子对晶界弱化
的影响 ， 是比较理想的分析工具 。 Chen 和 Dongare
[ 8 ]
研究了 O 和 H 对 Ni 中 Σ 3 ( 111 ) 、 Σ 5 ( 012 ) 、 Σ 5 ( 013 ) 和
Σ 11 ( 113 ) 4 种晶界的偏聚倾向以及致脆程度 ， 发现
Σ 3 晶界上 O 和 H 的偏聚倾向最小 ， 但是低浓度的 O
和 H 对 Σ 3 晶界的断裂以及裂纹萌生的作 用最大 。
Yamaguchi 等
[ 9 , 10 ]
研究了非过渡元素对 Ni Σ 5 ( 012 ) 晶
界的偏聚能和致脆倾向 ， 发现 O 对该晶界的致脆作
用较为明显 。 虽然 O 致脆 Ni 晶界的相关研究
[ 11 , 12 ]
已
经较为完备 ， 但是相关理论并不涉及晶界失效的动
态过程 。 因此 ， 为了进一步揭示和对比分析 Ni 、 Co
和 NiCr 晶界氧化程度对性能的影响 ， 从理论上给出
O 对这些晶界影响的依据 ， 本工作开展了 Ni 的 Σ 5
( 012 ) 晶界在不同 O 浓度下的理想拉伸实验 、 理想分
离功以及差分电荷图的计算与分析 ， 尝试用过程分
析解释 O 弱化晶界的内在原因并为高温合金的氧化
预防提供理论思路 。 在此基础上 ， 还分析了 Co 和
NiCr 基 Σ 5 ( 012 ) 晶界在不同 O 浓度下的失效行为 ， 并
与镍基的数据结果进行了对比分析 。
1 计算方法
使用基于平面波密度泛函理论的 V ASP ( Vien ‐
na Ab-initio Simulation Package ) 软件
[ 13 ]
进行计算 ， 交
换关联泛函采用含有电荷密度梯度信息的广义梯度
近 似 ( generalized gradient approximation ， GGA ) 的
PBE ( Perdew-Burke-Ernzerhof ) 泛函 ， 赝势使用投影
缀加平面波 ( projector augmented-wave ， PAW ) 赝势 ，
截断能的选择为 350 eV 。 因高温合金高温下服役过
程中为顺磁态 ， 为了与实际工况更加贴近并加快计
算速度 ， 故本计算中的晶界模型弛豫与拉伸过程计
算不考虑自旋效应 。 此外 ， 根据第一性原理计算的
特点 ， 本工作仅考虑通过不同 O 含量的计算来讨论
氧的作用程度 。
据报道
[ 14 ]
， 杂质元素在镍基合金晶界的弱化作
用与晶界取向无关 ， 此外 Ni 的 Σ 5 晶界在过去的研
究中被大家广泛使用 ， 因此采用 Σ 5 ( 012 ) 晶界来进行
计算分析 ， Co 和 NiCr 晶界仿照镍基合金的分析手段
进行相关模型的构建和各项测试 。
先 通 过 ICSD ( Inorganic Crystal Structure Data ‐
base )
[ 15 ]
数据库获得 Ni 的实验条件下的 fcc 单胞结
构
[ 16 ]
 ( 点阵常数为 0 . 35276 nm ) ， 进行结构弛豫获得
单胞模型 ( 点阵常数为 0 . 35143 nm ) ， 输入到 Aims ‐
gb
[ 17 ]
中计算获得晶界原始模型 ， 通过将超胞基矢量
转换为正交矢获得晶界的未弛豫模型 ， 经过结构优
310

## Page 3

2 期 李 昕等 ： O 原子对高温合金基体 Ni 、 Co 和 NiCr 晶界作用的理论计算分析
化最终获得弛豫的 80 原子 Ni 晶界模型 ， 如图 1 ， 与
Yamaguchi 等
[ 18 ]
的模型一致 。
单胞结构弛豫采用自旋极化的密度泛函计算 ，
能量收敛标准为 1 × 10
- 6
 eV ， 几何优化力收敛标准
为 0 . 1 eV/nm ， k 点网格采用 9 × 9 × 9 的 Gamma 网
格 。 晶 界 结 构 弛 豫 计 算 的 能 量 收 敛 标 准 为 1 × 
10
- 4
 eV ， 几何优化力收敛标准为 0 . 5 eV/nm ， k 点网格
采用 2 × 2 × 1 的 Monkhorst-Pack 网格 。
根据 Chen 和 Dongare
[ 8 ]
的工作 ， O 原子在 Ni 晶
界中八面体间隙位置形成能要小于四面体间隙 ， 因
此 利 用 VESTA ( Visualization for Electronic and 
Structural Analysis ) 软件
[ 19 ]
在弛豫后的晶界间隙八面
体位置分别添加 1 、 2 、 3 个 O 原子 ( 分别记为 O 1 、 O 2
和 O 3 ) 后再进行结构弛豫 ， 获得结构优化后的含有
杂质 O 原子的晶界模型 ， 如图 2 所示 。 添加杂质原
子后若不进行结构弛豫 ， 则在拉伸过程的开始应力
变为负值
[ 11 ]
， 已有的研究结果认为添加杂质原子后
模型存在压应力 ， 这是因添加杂质原子后未弛豫模
型结构所导致的 。 因此为了确保拉伸结果更符合实
际情况 ， 应先进行结构弛豫 。
本工作借助 Zhang 等
[ 20 ]
的 ideal strength 脚本进
行拉伸实验 。 拉伸计算过程中的结构弛豫计算设置
与晶界结构弛豫的设置相同 。 利用旋转矩阵将拉伸
方向旋转到 [ 100 ] 方向 ， 通过每次增加超胞基矢量 a 、
b 、 c 的 x 值为上一步的 0 . 01 来实现拉伸 ， 每个拉伸点
都进行结构弛豫 ， 可以认为拉伸过程是准静态的 。
应力的获得通过调取 V ASP 软件的 OUTCAR 中应力
张量 xx 值来实现 ， 通过修改 constr_cell_relax . F 文件
实现对晶界模型 x 方向尺寸进行固定 。 该种方法与
实际拉伸过程更为接近 ， 因为不对模型中的原子进
行固定 ， 因此可以对拉伸过程中原子位置移动进行
观察分析 ， 便于进行更为细致的晶界弱化机理研究
工作 。
对于复杂晶界结构的拉伸过程 ， 断裂的瞬间结
构变化较大 ， 使用该脚本一方面需要长时间进行结
构优化以达到该状态的最低能态 ， 另一方面需要占
用较大的计算机内存 ， 因此对晶界模型的实际拉伸
计算过程提出了挑战 ， 本工作通过撰写脚本 mem . sh
和 iosv . sh 来实现对脚本计算过程进行内存控制和结
构优化过程的自动续算
[ 21 ]
， 从而实现使用较少计算
资源便可完成拉伸至断裂的目的 。
此外 ， 还利用 VESTA 来测量原子与原子之间的
距离 ， 分析添加杂质原子后拉伸过程中模型中原子
的间距变化 。 利用差分电荷密度图分析 O 对晶界电
荷密度分布以及成键类型的影响 。
2 计算结果与讨论
2 . 1 Ni 晶界
通过理想拉伸实验 ， 如图 3 所示 ， 发现 Σ 5 晶界
加入 O 原子后材料的强度极限发生明显下降 ， 认为
O 原子对晶界存在明显的弱化作用 ， 并且随着 O 原
子数量增加 ， 材料的强度极限持续下降 ， 该现象与实
际高温疲劳寿命随氧化程度加剧而骤降一致
[ 3 , 4 ]
。
晶界拉伸过程中晶界总宽度与晶界处 Ni-Ni 原
子间距的测量位置如图 4 所示 ， 结果如图 5 所示 。
可以看出 ， 纯净 Ni 晶界和含有一个 O 原子的 Ni 晶
界表现出了明显的差异 。 在 拉伸过程中 ， 晶界模型
被拉长 ， 其长度改变来源于晶界模型中每个 Ni-Ni
原子间距的变大 ， 包含了晶界处的 Ni-Ni 以及非晶
界处的 Ni-Ni 原子间距贡献 ， 但对于含有杂质 O 原
Color online
图 2 氧在晶界平面的放置位置及结构弛豫后的 O 原
子位置
Fig . 2 Position of oxygen atoms in grain boundary 
plane of initial model ( a - c ) and relaxed model 
( d - f )
( a , d ) one oxygen atom ( O 1 ) 
( b , e ) two oxygen atoms ( O 2 ) 
( c , f ) three oxygen atoms ( O 3 )
图 1 Ni 的 ∑ 5 ( 012 ) 晶界模型
Fig . 1 Grain boundary ( GB ) model of Ni ∑ 5 ( 012 )
311

## Page 4

59 卷金 属 学 报
子的晶 界拉伸过程 ， 当应变接近 0 . 10 ， 杂质 O 晶界处
Ni-Ni 原子间距曲线发生弯折 ， 斜率变大 ， 其斜率与
含有杂质 O 的晶界模型总长度变化曲线的斜率基本
相等 ， 故应变大于 0 . 10 时 ， 晶界模型总长度变化完全
由晶界处的 Ni-Ni 原子间距贡献 ， 而不是非晶界处
的 Ni — Ni 键 。 因此含 O 晶界在后续拉伸过程中的
应变贡献完全由晶界处的 Ni — Ni 键提供 ， O 的存在
明显促进并加快了 Ni 晶界的断裂失效过程 。 此外 ，
在图 6 中可以明显看到 ， 晶界断裂发生在晶界处的
Ni — Ni 键而不是晶界处 Ni — O 键 ， 因此可以认为是
Ni — O 键 的 存 在 左 右 了 晶 界 处 的 Ni — Ni 键 处 的
断裂 。
根据 Sun 等
[ 22 ]
的工作绘制差分电荷密度 ( Δ ρ ) 图
来反映化学键成键过程电子转移情况 ， 定义如下 ：
Δ ρ = ρ
N i / O
- ρ
N i
- ρ
O
( 1 )
式中 ， ρ
N i / O
代表含有杂质 O 原子的 Ni 晶界电荷密度 ，
ρ
N i
是移除晶界间隙位置 O 原子后计算得到的 Ni 晶
界电荷密度 ， ρ
O
是移除 Ni 晶界后计算得到的间隙 O
原子的电荷密度 。
Ni 晶界的差分电荷密度如图 7 所示 。 可以看
出 ， O 原子周围的 Ni 原子发生了较为明显的电荷转
移情况 ， Ni 原子附近电子密度发生减少而 O 原子附
近发生了电荷密度聚集的现象 ， 形成了离子键特征
的 Ni — O 键 ， 其中 Ni 原子呈现正电性 ， O 原子呈现负
电性 。 此外 ， 由于发生电荷转移 ， 晶界处的 Ni — Ni
金属键中的 Ni 原子电荷发生不均匀分布 ， 金属键成
键电荷减少 ， 因此可以判断晶界处的 Ni — Ni 金属键
相比于无杂质 O 的纯净晶界中的 Ni — Ni 键强度下
降 ， 这与本工作中拉伸实验得到的结构图结果一致 ，
Ni — O 键的形成影响了晶界处 Ni — Ni 键的强度 。
现有实验现象和基于 Rice-Wang 模型
[ 23 , 24 ]
的计
算结果已经显示 O 的存在对晶界起到弱化作用 ， 为
了更深入地研究 O 的存在对结构变化以及电荷分布
的影响并确定主要影响因素 ， 有必要把 O 对晶界的
结构影响和电荷分布影响区分开来研究 。 根据 Lo ‐
zovoi 等
[ 25 ]
的模型 ， 可以把杂质原子对晶界的理想分
离功 ( W
sep
) 的影响划分为因结构畸变引起的结构影
响 ( interstitial structure ， IS ) 和对电荷密度重新分布造
成 的 化 学 影 响 ( chemical and compressed imputity ，
CC ) 。
I S = W
s e p ( C ) - W
s e p
( A ) ( 2 )
C C = W
s e p ( B ) - W
s e p
( C ) ( 3 )
式中 ， W
s e p
( A ) 、 W
s e p ( B ) 、 W
s e p ( C ) 为 A 、 B 、 C 过程的分离
功 ， 其中 A 代表纯净晶界分离功计算 ， B 代表含有杂
质原子的分离功计算 ， C 代表去掉杂质原子的晶界分
离功计算 ， 如图 8 所示 。 若对晶界的结合起削弱作用
则 IS 或 CC 表现为负值 ， 数值越小弱化作用越 明显 。
图 3 Ni 晶界在不同氧化程度下的理想拉伸曲线
Fig . 3 Ideal strength curves of Ni grain boundary under 
different oxidized conditions
Color online
图 4 晶界总长度及 Ni — Ni 原子间距的测量图示
Fig . 4 Schematics of total length of grain boundary and 
spacing of Ni — Ni
( a ) pure grain boundary
( b ) grain boundary with one O atom
图 5 纯净的 Ni 晶界和含有一个 O 原子晶界在拉伸过
程中晶界总宽度及晶界处 Ni — Ni 键长度变化
Fig . 5 Total lengths of grain boundary and spacing of 
Ni — Ni in the process of ideal strength test
312

## Page 5

2 期 李 昕等 ： O 原子对高温合金基体 Ni 、 Co 和 NiCr 晶界作用的理论计算分析
对于分离功的计算可通过下式进行计算 ：
W
s e p
= E
s
- E ( 4 )
式中 ， E 为晶界体系总能量 ； E
s
为晶界分离后体系能
量 。 如果杂质对晶界存在弱化作用则满足下式 ：
Δ = W
s e p ( B ) - W
s e p ( A ) = I S + C C < 0 ( 5 )
其中 ， Δ 值为分离功差值 ， 值越小弱化作用越明显 。
通过计算 Ni 晶界的理想分离功 ， 如图 9 所示 ， 发
现 Δ 值均为负值 ， 因此 O 的存在均对 Ni 􀰑 5 晶界的结
合起到负面作用 ， 这与本次计算得到的理想拉伸数
据是一致的 。 对于单个 O 原子的情况 ， 晶界的弱化
作用主要是由几何结构上的不匹配所引起的 ， 在 2
个以及 3 个 O 原子的情况中 ， 几何和化学影响因素
Color online
图 6 不同 O 含量下的 Ni 晶界理想拉伸实验断裂瞬间的原子分布
Fig . 6 Atom positions in Ni grain boundary when a fracture happens under different oxidized conditions
Color online
图 7 不同 O 含量下的 Ni 晶界差分电荷密度
Fig . 7 Charge density differences of Ni grain boundary under different oxidized conditions
图 8 Lozovoi 模型图示
[ 25 ]
Fig . 8 Lozovoi models of work of separation w
sep
[ 25 ]
 
( W
sep
( A ) — work of separation of pure grain 
boundary , W
sep
( B ) — work of separation of grain 
boundary with impurity atom , W
sep
( C ) — work of 
separation of grain boundary without impurity at ‐
om )
313

## Page 6

59 卷金 属 学 报
均对晶界的弱化作用起到了不可忽视的作用 ， 共同
对晶界的弱化起作用 。 综合来看 ， O 的存在都引起
了较大的几何畸变 ， 导致了晶界的弱化 ， 但是随着 O
原子的浓度增加 ， 化学因素方面的影响也逐渐递增 ，
这与 Ni 晶界差分电荷密度图中随 O 原子增加晶界
电子转移程度增加一致 ， O 原子的增加促使了更多
Ni — O 离子键的形成 。
综上所述 ， O 在 Ni 晶界中主要由于 O 的强电负
性形成了离子键成分较高的 Ni — O 键 ， 同时改变了原
有晶界的电荷分布 ， 削弱了晶界处 Ni — Ni 金属键 ， 因
此导致了拉伸过程中的变形不协调现象 ， 使得 Ni 晶
界发生了弱化 。 基于以上研究 ， 为了减弱杂质元素 O
对实际材料服役过程中疲劳失效的影响 ， 势必需要减
轻晶界处 Ni — O 键与 Ni — Ni 键的变形不协调的问
题 ， 根据工程上的便利性 ， 合金化的思路固然是一个
最佳选择 ， 若能避免 O 与 Ni 的直接作用 ( 1 . 形成 Ni —
O 离子键 ， 2 . 弱化晶界处 Ni — Ni 键 ) ， 使得其他合金化
元素优先与 O 结合 ， 应能削弱 O 的弱化作用 。
2 . 2 Co 晶界和 NiCr 晶界
为了对比 Ni 和 Co 晶界氧化后力学行为的差
异 ， 采用类似的方法对 Co 晶界
[ 26 ]
进行分析 ， 得到 Co
晶界在不同 O 含量下的理想拉伸曲线 ， 如图 10 所
示 。 可以看出 ， Co 晶界较 Ni 晶界无论是纯净晶界下
还是不同 O 含量下均保持更高的抗拉极限 ， 但 Co 断
裂应变较 Ni 更小 ， 因此表现出高温氧化脆性 。
Co 晶界断裂时的原子分布如图 11 所示 。 可以
看出 ， 即便在拉伸曲线上已表现为断裂 ， 但是在 2 个
以及 3 个 O 原子的情况下 ， O 原子对晶界依然起到一
定的 “ 缝合 ” 作用 ， Ni 晶界的断裂原子分布则表现为
完全断开 ， 可见 Co — O 键与 Co — Co 键的相对强度
应小于 Ni — O 键与 Ni — Ni 键的相对强度 。
图 1 2 所示为 Co 晶界的理想分离功差值 ， 其主
图 9 不同 O 含量下的 Ni 晶界的理想分离功差值 ( Δ )
Fig . 9 Differences of separation work ( Δ ) of Ni grain 
boundary under different oxidized conditions 
( IS — effect of interstitial structure , CC — effect 
of chemical and compressed imputity )
图 10 不同 O 含量的 Co 晶界理想拉伸曲线
Fig . 10 Ideal strength curves of Co grain boundary un ‐
der different oxidized conditions
Color online
图 11 不同 O 含量的 Co 晶界拉伸断裂瞬间的原子分布
Fig . 11 Atom positions in Co grain boundary when a fracture happens under different oxidized conditions
314

## Page 7

2 期 李 昕等 ： O 原子对高温合金基体 Ni 、 Co 和 NiCr 晶界作用的理论计算分析
要由电荷密度重新分布造成的化学影响组成 ， 对晶
界的断裂起到促进作用 ， 而结构畸变引起的结构影
响占比较小但对晶界断裂起到抑制作用 ， 与 Ni 晶界
的结构畸变主导的理想分离功不同 ， 因此 Ni 晶界与
Co 晶界在不同 O 含量下的断裂行为应是不同机制 。
Co 晶界在不同氧化程度的差分电荷密度如图 13
所示 。 Co 晶界引入杂质 O 原子后均出现了较为明显
的正负电子转移情况 ， 相比 Ni 晶界转移电子数量更
多 ， 因此可以判断 Co 晶界中形成了比 Ni 晶界更多的
离子键 。 由于离子键是脆性键 ， 晶界处离子键越多则
表现出的脆性越大 ， 因此相比 Ni 晶界 ， Co 晶界虽然
强度可能高 ， 但断裂应变要明显小于 Ni 晶界 ， 此结论
与 Co 晶界理想拉伸的低断裂应变结果一致 。
仿照 Ni 和 Co 晶界的研究方法 ， 选取 Ni
0 . 6
Cr
0 . 4
单
胞
[ 27 ]
生成 NiCr ∑ 5 ( 012 ) 晶界模型 ， 其中 Ni 原子占据
fcc 单胞的 6 个面心位置 ， Cr 原子占据单胞的 8 个顶
点位置 ， 含 O 晶界模型 O 原子放在晶界八面体间隙
位置
[ 28 ]
。 NiCr 晶界在不同 O 含量下的理想拉伸曲线
如图 14 所示 。 可以看出 ， 较 Ni 晶界而言 ， 虽然 NiCr
晶界无论是纯净晶界还是氧化后晶界 ， 其晶界强度
均小于 Ni 晶界 ， 但是 NiCr 晶界在不同 O 含量氛围下
性能较为稳定 ， 基本不随 O 含量的增加而发生较为
明显的衰减 。
NiCr 晶界断裂时刻的原子分布如图 15 所示 。
可以看出 ， 晶界断裂并不完全 ， 其中 2 个 O 原子情况
下断裂发生在无杂质 O 的晶界处 ， 说明该情况下 O
的存在对晶界弱化起到抑制作用 ， 断裂发生在无杂
质 O 的晶界处 。
NiCr 晶界的理想分离功差值如图 16 所示 。 可
以看出 ， NiCr 晶界理想分离功差值主要由电荷分布
改变带来的化学影响组成 ， 但随氧化程度的加剧 ， 化
学影响的改变不是特别明显 。 结构影响组成较小但
对晶界断裂起到抑制作用 ， 由于晶界电荷密度分布
变化引起的弱化作用占主要地位 ， 因此从总的效果
上该晶界依旧表现为晶界弱化现象 。
Color online
图 13 不同 O 含量下的 Co 晶界差分电荷密度
Fig . 13 Charge density differences of Co grain boundary under different oxidized conditions
图 12 计算得到的不同 O 含量下 Co 晶界的理想分离
功差值
Fig . 12 Differences of work of separation of Co grain 
boundary under different oxidized conditions
315

## Page 8

59 卷金 属 学 报
与 Ni 和 Co 晶界的差分电荷密度计算方法相
同 ， 计算得到的 NiCr 晶界不同氧化程度的差分电荷
密度如图 17 所示 。 可以看出 ， 3 种氧化程度的晶界
差分电荷密度图差异不是很大 ， 这与 NiCr 晶界理想
分离功差值在 3 种氧化程度下计算得到的结果差异
性不大的结论一致 ， 因此不能简单认为 NiCr- 2 O 情
况下断裂发生在不含 O 晶界处是由于电荷密度分布
发生改变所致 。 根据目前的计算 ， 从差分电荷密度
结果看出 NiCr 晶界 1 个和 2 个 O 原子情况下不含 O
晶界处的原子结合更加紧密 ， 3 个 O 原子的不含 O 晶
界与前 2 种情况明显不同 ， 因此可能是 O 原子的引
入引起了不含 O 晶界的强弱变化 ， 即含 O 晶界与不
含 O 晶界均发生了强度变化 。
2 . 3 3 种晶界氧化影响对比
综合 Ni 、 Co 以及 NiCr 3 种晶界的理想拉伸实验
结果 ， 如表 1 所示 ， 3 种晶界随氧化程度的加剧 ， 均表
现为较为明显的晶界抗拉强度下降 ， 其中 Ni 晶界力
学性能受氧化影响最为显著 ， 抗拉强度从纯净晶界
的 31 . 59 GPa 到 3 个 O 原子作用下的 17 . 43 GPa ， 强度
下降比例达到 44 . 8 % ， 断裂应变下降比例为 70 % ， 受
氧化作用影响最为显著 。 纯净 Co 晶界及不同氧化
程度晶界的抗拉强度均为 3 种晶界中最大 ( 24 . 71 ~
34 . 89 GPa ) ， 但 断 裂 应 变 为 3 种 晶 界 中 最 小 ( 0 . 10 ~
0 . 21 ) ， 可见钴基合金能够在氧化程度较高的情况下
保持较为出色的强度 ， 但是需要注意 Co 晶界在低应
变下的断裂现象 。 对于 NiCr 晶界 ， 虽然纯净晶界的
强度在 3 种晶界中最低 ( 26 . 25 GPa ) ， 但其氧化后的
抗拉强度均保持在较小的下降范围 ( 19 . 9 %~ 25 . 1 % ) ，
可以认为 NiCr 晶界性能最为稳定 ， 晶界氧化弱化得
到了控制 ， 这一点也说明高温合金中添加 Cr 的合
理性 。
3 种晶界的理想分离功差值数据如表 2 所示 。
对比可以看出 ， O 原子对 3 种晶界均表现为弱化作
用 ， 这与理想拉伸实验结果一致 。 从弱化来源来看 ，
Ni 晶界弱化表现为结构畸变和电荷密度重新分布
共同作用的晶界弱化 ， 并随氧化程度的加剧 ， 结构影
响占比逐渐下降 ( 86 . 0 %~ 60 . 4 % ) 。 Co 晶界弱化原因
主要为电荷密度重新分布带来的化学影响 ， 其中随
着氧化程度的加剧 ， 化学影响逐渐增加 ( 由 - 2 . 26 eV
至 - 8 . 05 eV ) ， 结构畸变对 Co 晶界弱化随氧化程度
加 剧 先 起 促 进 作 用 ( - 0 . 39 eV ) 后 转 为 抑 制 作 用
( 2 . 66 eV ) ， 但净影响依然表现为晶界弱化 。 根据理
想分离功计算方法 ， 结构影响起到抑制作用反映的
图 14 不同 O 含量的 NiCr 晶界理想拉伸曲线
Fig . 14 Ideal strength curves of NiCr grain boundary 
under different oxidized conditions
Color online
图 15 不同 O 含量的 NiCr 晶界拉伸断裂瞬间的原子分布
Fig . 15 Atom positions in NiCr grain boundary when a fracture happens under different oxidized conditions
316

## Page 9

2 期 李 昕等 ： O 原子对高温合金基体 Ni 、 Co 和 NiCr 晶界作用的理论计算分析
是相比原始纯净晶界 ， 含有杂质原子的晶界在分离
过 程 中 需 要 的 能 量 更 大 ， 因 此 表 现 为 抑 制 作 用 。
NiCr 晶界表现为因电荷密度重新分布造成的晶界
弱化 ， 结构畸变反而对晶界弱化起到一定的抑制作
用 ， 但不是特别明显 ， 占比仅为 0 . 2 %~ 3 . 2 % 。 综合来
看 ， Ni 晶界氧化弱化原因与 Co 和 NiCr 晶界不同 ， Ni
晶界弱化原因为 O 原子带来的结构畸变和电荷密度
重新分布共同作用 ， 而 Co 和 NiCr 晶界弱化主要由 O
原子带来的电荷密度重新分布的化学影响产生 ， 但
随着氧化程度加剧 ， 3 种晶界均表现出结构影响占
比下降 ， 化学影响占比上升的趋势 。
表 2 3 种晶界理想分离功差值计算结果
T a b l e 2 Differences of separation work of three kinds of grain bound aries
( eV ) 
System
Ni
Co
NiCr
IS
O 1
- 11 . 75
- 0 . 39
2 . 52
O 2
- 7 . 67 
 2 . 66
 0 . 66
O 3
- 9 . 00
2 . 06
0 . 13
CC
O 1
- 1 . 85
- 2 . 26
- 81 . 35
O 2
- 5 . 46
- 5 . 99
- 81 . 39
O 3
- 5 . 93
- 8 . 05
- 86 . 77
Δ
O 1
- 13 . 60
- 2 . 65
- 78 . 83
O 2
- 13 . 13
- 3 . 33
- 80 . 73
O 3
- 14 . 93
- 5 . 99
- 86 . 64
图 16 计算得到的不同 O 含量下 NiCr 晶界的理想分
离功差值
Fig . 16 Differences of separation work of NiCr grain 
boundary under different oxidized conditions
Color online
图 17 不同 O 含量下的 NiCr 晶界差分电荷密度
Fig . 17 Charge density differences of NiCr grain boundary under different oxidized conditions
表 1 3 种晶界理想拉伸实验结果
T a b l e 1 Ideal strength test results of three kinds of grain boundaries
System
Ni
Co
NiCr
Tensile strength / GPa
Pure
31 . 59
34 . 89
26 . 25
O 1
24 . 73
28 . 69
19 . 66
O 2
22 . 75
24 . 71
20 . 36
O 3
17 . 43
25 . 57
21 . 03
Fracture strain
Pure
0 . 30
0 . 21
0 . 16
O 1
0 . 22
0 . 14
0 . 16
O 2
0 . 28
0 . 13
0 . 17
O 3
0 . 09
0 . 10
0 . 18
317

## Page 10

59 卷金 属 学 报
3 结论
( 1 ) 当拉伸应变达到 0 . 10 后 ， 含氧 Ni 晶界的应
变完全由含氧晶界处的 Ni — Ni 键提供 ， O 的存在明
显加速了 Ni 晶界的断裂失效过程 。
( 2 ) Co 晶界相比较于 Ni 及 NiCr 晶界氧化后强
度更高 ， Co 比 Ni 有更好的抗晶界氧弱化性能 ， 但断
裂应变较小 。 NiCr 晶界强度最低 ， 但相较于 Ni 和
Co 晶界氧化后力学性能较稳定 。
( 3 ) Ni 晶界氧化弱化的原因在于 O 原子带来的
结构畸变 ， 而 Co 和 NiCr 晶界氧化弱化原因主要来
自电荷密度分布的改变 。 无论是 Ni 、 Co 还是 NiCr
晶界 ， 随着氧化程度加剧 ， 电荷密度分布的改变带来
的晶界弱化作用都发生了增加 。
参 考 文 献
[ 1 ] Li H Y , Sun J F , Hardy M C , et al . Effects of microstructure on 
high temperature dwell fatigue crack growth in a coarse grain PM 
nickel based superalloy [ J ]. Acta Mater ., 2015 , 90 : 355
[ 2 ] Tong J , Dalby S , Byrne J , et al . Creep , fatigue and oxidation in 
crack growth in advanced nickel base superalloys [ J ]. Int . J . Fa ‐
tigue , 2001 , 23 : 897
[ 3 ] Xu C , Nai Q L , Yao Z H , et al . Grain boundary oxidation effect of 
GH 4738 superalloy on fatigue crack growth [ J ]. Acta Metall . Sin ., 
2017 , 53 : 1453
( 徐 超 , 佴启亮 , 姚志浩等 . 晶界氧化对 GH 4738 高温合金疲劳裂
纹扩展的作用 [ J ]. 金属学报 , 2017 , 53 : 1453 )
[ 4 ] Xu C , Yao Z H , Dong J X . The sharp drop in fatigue crack growth 
life at a critical elevated temperature for a PM Ni-based superalloy 
FGH 97 [ J ]. Mater . Sci . Eng ., 2019 , A 761 : 138038
[ 5 ] Ghonem H , Zheng D . Oxidation-assisted fatigue crack growth be ‐
havior in alloy 718 -part I . Quantitative modeling [ J ]. Fatigue 
Fract . Eng . Mater . Struct ., 1991 , 14 : 749
[ 6 ] Thomas L E , Bruemmer S M . High-resolution characterization of 
intergranular attack and stress corrosion cracking of alloy 600 in 
high-temperature primary water [ J ]. Corrosion , 2000 , 56 : 572
[ 7 ] Was G S , Lian K . Role of carbides in stress corrosion cracking re ‐
sistance of alloy 600 and controlled-purity Ni - 16 % Cr - 9 % Fe in 
primary water at 360
o
C [ J ]. Corrosion , 1998 , 54 : 675
[ 8 ] Chen J , Dongare A M . Role of grain boundary character on oxygen 
and hydrogen segregation-induced embrittlement in polycrystal ‐
line Ni [ J ]. J . Mater . Sci ., 2017 , 52 : 30
[ 9 ] Yamaguchi M . First-principles study on the grain boundary embrit ‐
tlement of metals by solute segregation : Part I . Iron ( Fe ) - solute 
( B , C , P , and S ) systems [ J ]. Metall . Mater . Trans ., 2011 , 42 A : 319
[ 10 ] Yamaguchi M , Shiga M , Kaburaki H . Energetics of segregation 
and embrittling potency for non-transition elements in the Ni 
Σ 5 ( 012 ) symmetrical tilt grain boundary : A first-principles study 
[ J ]. J . Phys .: Condens . Matter , 2004 , 16 : 3933
[ 11 ] Wang L G , Wang C Y . First-principles calculations of energies of 
impurities and doping effects at grain boundaries in nickel [ J ]. Ma ‐
ter . Sci . Eng ., 1997 , A 234 - 236 : 521
[ 12 ] Lefkaier I K , Bentria E T . The effect of impurities in nickel grain 
boundary : density functional theory study [ A ]. Study of Grain 
Boundary Character [ M ]. Rijeka : InTech , 2016 : 1
[ 13 ] Vargas-Hernández R A . Bayesian optimization for calibrating and 
selecting hybrid-density functional models [ J ]. J . Phys . Chem ., 
2020 , 124 A : 4053
[ 14 ] Liu W G , Ren C L , Han H , et al . First-principles study of the effect 
of phosphorus on nickel grain boundary [ J ]. J . Appl . Phys ., 2014 , 
115 : 043706
[ 15 ] Rühl S . The inorganic crystal structure database ( ICSD ): A tool for 
materials sciences [ A ]. Materials Informatics : Methods , Tools and 
Applications [ M ]. Weinheim : Wiley-VCH , 2019 : 41
[ 16 ] Rouquette J , Haines J , Fraysse G , et al . High-pressure structural 
and vibrational study of PbZr
0 . 40
Ti
0 . 60
O
3
 [ J ]. Inorg . Chem ., 2008 , 
47 : 9898
[ 17 ] Cheng J L , Jian L , Yang K S . Aimsgb : An algorithm and open-
source python library to generate periodic grain boundary struc ‐
tures [ J ]. Comput . Mater . Sci ., 2018 , 155 : 92
[ 18 ] Yamaguchi M , Shiga M , Kaburaki H . Grain boundary decohesion 
by impurity segregation in a nickel - sulfur system [ J ]. Science , 
2005 , 307 : 393
[ 19 ] Momma K , Izumi F . VESTA 3 for three‐dimensional visualization 
of crystal , volumetric and morphology data [ J ]. J . Appl . Cryst ., 
2011 , 44 : 1272
[ 20 ] Zhang M , Liu H Y , Li Q , et al . Superhard BC
3
 in cubic diamond 
structure [ J ]. Phys . Rev . Lett ., 2015 , 114 : 015502
[ 21 ] Li X . ArticleAttachment , 2023 , https : //github . com/lixin 555 /Article ‐
Attachment
[ 22 ] Sun S N , Kioussis N , Lim S P , et al . Impurity effects on atomic 
bonding in Ni
3
Al [ J ]. Phys . Rev ., 1995 , 52 B : 14421
[ 23 ] Rice J R , Wang J S . Embrittlement of interfaces by solute segrega ‐
tion [ J ]. Mater . Sci . Eng ., 1989 , A 107 : 23
[ 24 ] Razumovskiy V I , Lozovoi A Y , Razumovskii I M . First-principles-
aided design of a new Ni-base superalloy : Influence of transition 
metal alloying elements on grain boundary and bulk cohesion [ J ]. 
Acta Mater ., 2015 , 82 : 369
[ 25 ] Lozovoi A Y , Paxton A T , Finnis M W . Structural and chemical em ‐
brittlement of grain boundaries by impurities : A general theory and 
first-principles calculations for copper [ J ]. Phys . Rev ., 2006 , 74 B : 
155416
[ 26 ] Häglund J , Guillermet A F , Grimvall G , et al . Theory of bonding in 
transition-metal carbides and nitrides [ J ]. Phys . Rev ., 1993 , 48 B : 
11685
[ 27 ] Abe F , Tanabe T . Change in lattice spacing of nickel by dissolved 
chromium and tungsten [ J ]. Int . J . Mater . Res ., 1985 , 76 : 420
[ 28 ] Kim J J , Shin S H , Jung J A , et al . First-principles study of intersti ‐
tial diffusion of oxygen in nickel chromium binary alloy [ J ]. Appl . 
Phys . Lett ., 2012 , 100 : 131904
( 责任编辑 : 李海兰 )
318
