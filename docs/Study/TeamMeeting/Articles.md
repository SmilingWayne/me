# 2024 文献阅读记录

!!! example "Summary"

    > Transportmetrica A ｜ TR part E logistics

    - VRP路线规划 ｜ 货运车辆调度 ｜ 毕设相关
    - Truck and Drones 规划
    - 货车车队platoon
    - 鲁棒优化相关
    - 电动公交车相关
    - 对两本期刊的总结
    
    > 带链接的为相关性较强的

--------

## VRP 路线规划｜货运卡车｜物流相关

1. [Sadati, M. E. H., & Çatay, B. (2021). A hybrid variable neighborhood search approach for the multi-depot green vehicle routing problem. Transportation Research Part E: Logistics and Transportation Review, 149, 102293.](https://www.sciencedirect.com/science/article/pii/S1366554521000673)

- 特征：多Depot、带充电桩、有运量约束，但是没有时间窗约束；

- 数据集：The small-size data set of Erdogan and Miller-Hooks (2012) 

- 启发式方法：Tabu search and Variable Neighbour search

2. [Seyfi, M., Alinaghian, M., Ghorbani, E., Çatay, B., & Sabbagh, M. S. (2022). Multi-mode hybrid electric vehicle routing problem. Transportation Research Part E: Logistics and Transportation Review, 166, 102882.](https://www.sciencedirect.com/science/article/pii/S1366554522002605)

- 特征：混合动力，可以边走边充电；有容量约束也可以使用多种模式；目标是总行驶距离最短，每个车有4种行驶模式（if 路线选中，则需要再选择行驶模式）；
- 数据集：改自TSP 
- 启发式方法：VNS


3. [Chung-Cheng Lu, Ali Diabat, Yi-Ting Li, Yu-Min Yang (2021).  Combined passenger and parcel transportation using a mixed fleet of electric and gasoline vehicles. Transportation Research Part E: Logistics and Transportation Review, 164, 102757.](https://www.sciencedirect.com/science/article/pii/S1366554521003045)

- 特征：混合车队（有新能源和燃油汽车）、集送货和运客一体（combined passenger and parcel transportation problem with a mixed fleet (CPPT-MF).
- Multi-layer 路线网络：一辆车就是一个网络

4. **Yuan, Y., Cattaruzza, D., Ogier, M., Semet, F., & Vigo, D. (2021). A column generation based heuristic for the generalized vehicle routing problem with time windows. Transportation Research Part E: Logistics and Transportation Review, 152, 102391.**

- 列生成方法、广义车辆路径


5. **Dönmez, S., Koç, Ç., & Altıparmak, F. (2022). The mixed fleet vehicle routing problem with partial recharging by multiple chargers: Mathematical model and adaptive large neighborhood search. Transportation Research Part E: Logistics and Transportation Review, 167, 102917.**

- 混合能源车队、在途充电、考虑CO2排放；最小化运行成本；
- ALNS/ solomon +  Schneider et al. (2014)数据集




6.   Chi, J., & He, S. (2023). Pickup capacitated vehicle routing problem with three-dimensional loading constraints: Model and algorithms. Transportation Research Part E: Logistics and Transportation Review, 176, 103208.

- 带三维装载约束的VRP
- 需要考虑货物装卸先后顺序：和卡车先到后到的约束
- 树搜索

7. Pourhejazy, P., Zhang, D., Zhu, Q., Wei, F., & Song, S. (2021). Integrated E-waste transportation using capacitated general routing problem with time-window. Transportation Research Part E: Logistics and Transportation Review, 145, 102169.

- 应用场景：E-waste collection 的VRP
    - 类似论文：11.1 Masmoudi, M. A., Coelho, L. C., & Demir, E. (2022). Plug-in hybrid electric refuse vehicle routing problem for waste collection. Transportation Research Part E: Logistics and Transportation Review, 166, 102875. 
    - 垃圾车一次装满了必须去垃圾场先倒掉，然后再接着走。




8.  [Wang, M., Miao, L., & Zhang, C. (2021). A branch-and-price algorithm for a green location routing problem with multi-type charging infrastructure. Transportation Research Part E: Logistics and Transportation Review, 156, 102529.](https://www.sciencedirect.com/science/article/pii/S136655452100288X):

> 有多类型充电基础设施（GLRP-CI）的绿色基础设施建设问题，旨在确定同时确定仓库位置的决策，有换电（BSI）又有充电设备（FCI）在配电系统中路由电动汽车（EV）。 arc-flow model. 目标是最小化总成本，包括配备BSI或FCI的仓库的每日固定成本、电动汽车的行驶成本、电池的持有成本和充电的电力成本，并从目标函数中减去将能量送回电网的潜在利润。


9.  [Huang, N., Li, J., Zhu, W., & Qin, H. (2021). The multi-trip vehicle routing problem with time windows and unloading queue at depot. Transportation Research Part E: Logistics and Transportation Review, 152, 102370.](https://www.sciencedirect.com/science/article/pii/S1366554521001381)

> - 受城市垃圾回收的影响提出的新的VRP场景，但是卡车在站点有卸货时间：需要等待。> （travelling - waiting - unloading）
> 
> - ==Model： arc-flow model==，最小化旅途成本
> 
> - solomon + Branch and Bound
> 
> - label setting


10. Giménez-Palacios, I., Parreño, F., Álvarez-Valdés, R., Paquay, C., Oliveira, B. B., Carravilla, M. A., & Oliveira, J. F. (2022). First-mile logistics parcel pickup: Vehicle routing with packing constraints under disruption. Transportation Research Part E: Logistics and Transportation Review, 164, 102812.


11. Jia, M., & Chen, F. (2023). Upward scalable vehicle routing problem of automobile inbound logistics with pickup flexibility. Transportation Research Part E: Logistics and Transportation Review, 177, 103253.




12. [Liu, B., Ji, Y., & Cats, O. (2023). Integrating ride-hailing services with public transport: a stochastic user equilibrium model for multimodal transport systems. Transportmetrica A: Transport Science, 1-29.](https://www.tandfonline.com/doi/full/10.1080/23249935.2023.2236240)

> 了解系统中的交通流分布对于该系统的政策决策和服务设计至关重要。我们提出了由私家车、公共交通、网约车组成的多式联运系统的随机用户均衡（SUE）模型。采用多模态图表示方法研究了SUE模型中的出行成本，以捕捉集成系统中不同出行模式的关系。


13. [Malladi, S. S., Christensen, J. M., Ramírez, D., Larsen, A., & Pacino, D. (2022). Stochastic fleet mix optimization: Evaluating electromobility in urban logistics. Transportation Research Part E: Logistics and Transportation Review, 158, 102554.](https://www.sciencedirect.com/science/article/pii/S1366554521003124)

> 研究城市货运物流服务公司拥有的电动和传统混合车队的规模和组合的问题。在战略规划阶段考虑不确定的客户请求。提出了一种新的车辆功耗模型。两阶段随机规划。考虑车辆行驶中的能耗：疫苗投放车的能耗等；
>
> 启发式ALNS

14. 能源相关：Zhang, Q., Qi, J., & Zhen, L. (2023). Optimization of integrated energy system considering multi-energy collaboration in carbon-free hydrogen port. Transportation Research Part E: Logistics and Transportation Review, 180, 103351.
    1.  Unit Commitment：决策何时开机关机、发电水平、多少储能、购能情况；1）表示PIES运行成本的最小化，包括机组的启动和关闭成本、发电成本和购电成本。

15. [Guschinsky, N., Kovalyov, M. Y., Pesch, E., & Rozin, B. (2023). Cost minimizing decisions on equipment and charging schedule for electric buses in a single depot. Transportation Research Part E: Logistics and Transportation Review, 180, 103337.](https://www.sciencedirect.com/science/article/pii/S1366554523003253) :
    - 每次旅行在给定时间在同一个仓库开始和结束，电动巴士在那里为电池充电。问题在于确定电动巴士的电池型号、不同类型的充电器数量和电动巴士的每日循环充电时间表，以便将 （a） 充电设备的每日总成本、电池磨损和消耗的能量，以及 （b） 电动巴士充电中断（切换）的总数降至最低。约束条件包括供电的上限、在第二天为每辆电动巴士执行转移任务之前恢复初始电池能量状态，以及每辆电动巴士在所有电动巴士和访问的每次仓库访问中的最大开关次数的上限。提出了一种双层分解方法，将与详细充电计划和开关次数相关的决策和约束转移到较低级别的问题中。

16. [Lin, N., Akkerman, R., Kanellopoulos, A., Hu, X., Wang, X., & Ruan, J. (2023). Vehicle routing with heterogeneous service types: Optimizing post-harvest preprocessing operations for fruits and vegetables in short food supply chains. Transportation Research Part E: Logistics and Transportation Review, 172, 103084. ](https://www.sciencedirect.com/science/article/pii/S1366554523000728)在问题中，新鲜农产品由移动预处理设施在现场进行预处理，或在集中地点收集进行预处理。对于集中预处理，使用普通卡车收集产品并将其运输到预处理站。对于移动预处理，使用专用预处理车进行现场预处理。我们考虑了使用不同预处理技术的多种类型的预处理车辆的可能性，代表同一过程的不同技术或同一技术的不同版本:旨在为在短食品供应链中进行预加工操作提供一种有效的途径。我们既考虑了移动预处理单元的异构车队，也考虑了拾取产品进行集中预处理的可能性。由此产生的问题是具有时间窗的经典异构车队车辆路径问题 （HFVRPTW） 的变体


17. [Chen, C., Demir, E., Huang, Y., & Qiu, R. (2021). The adoption of self-driving delivery robots in last mile logistics. Transportation research part E: logistics and transportation review, 146, 102214.](https://www.sciencedirect.com/science/article/pii/S1366554520308565#s0015)

- 引入了具有时间窗口和送货机器人的新车辆路径问题：**最后一公里物流**。目标函数：**最小化路线行驶总时间**。有vehicle也有robot，robot负责最后节点的配送，vehicle负责运输到中转，有时间窗口；
- 两阶段数学规划；先对站点做了cluster；数据集是solomon dataset




!!! note "Truck and Drones"

    1. 🌟🌟[Masmoudi, M. A., Mancini, S., Baldacci, R., & Kuo, Y. H. (2022). Vehicle routing problems with drones equipped with multi-package payload compartments. Transportation Research Part E: Logistics and Transportation Review, 164, 102757.](https://www.sciencedirect.com/science/article/pii/S136655452200148X)

    > - VRPD：带无人机的VRP配送，无人机可以在不同truck之间起降，考虑时间窗、负载约束
    >
    > - 无人机和卡车之间的等待、装卸货
    > 
    > - 数据集：
    > 
    > - 启发式方法：模拟退火

    ---------------

    2. **Gao, J., Zhen, L., Laporte, G., & He, X. (2023). Scheduling trucks and drones for cooperative deliveries. Transportation Research Part E: Logistics and Transportation Review, 178, 103267.**

    > 卡车组由一辆卡车和多架无人机组成，这些无人机装载在卡车上。对于每个卡车组，卡车携带无人机，并在道路网络上行驶。无人机可以在路网节点与卡车分离，将货物交付给客户，然后在路网节点返回卡车。在无人机送货的飞行过程中，卡车不需要停下来等待无人机，而是继续行驶.本研究考虑的问题是安排所有卡车组路线，以最大限度地降低总运营成本，包括卡车旅行成本、无人机旅行成本、使用卡车组固定成本以及在客户所在地延迟交付的潜在罚款。

    ----------


    3. [Salama, M. R., & Srinivas, S. (2022). Collaborative truck multi-drone routing and scheduling problem: Package delivery with flexible launch and recovery sites. Transportation Research Part E: Logistics and Transportation Review, 164, 102788.](https://www.sciencedirect.com/science/article/pii/S1366554522001776)

    - 缩短交付时间、货车、无人机协同配送
    - 考虑了三个关键决策——（i） 将每个客户位置分配给车辆，（ii） 卡车和无人机的路线，以及 （iii） 在每个站点安排无人机 LARO 和卡车操作员活动
    - 不局限在用户取货点，而是灵活的车辆位置
    - 模拟退火、大规模邻域搜索

    ---------

    4. [Zhang, G., Zhu, N., Ma, S., & Xia, J. (2021). Humanitarian relief network assessment using collaborative truck-and-drone system. Transportation Research Part E: Logistics and Transportation Review, 152, 102417.](https://www.sciencedirect.com/science/article/pii/S1366554521001848)

    - combined drone orienteering problem (CDOP) 
    - 救灾的大背景下，链路划分：一些路是路运，一些路是空运。使无人机节点和链路获得的利润最大
    - CG ALgo，划分为两个子问题：
    - 分别计算卡车路线和无人机路线

    5. [Kim, D., Seong Ko, C., & Moon, I. (2023). Coordinated logistics with trucks and drones for premium delivery. Transportmetrica A: Transport Science, 1-29.](https://www.tandfonline.com/doi/abs/10.1080/23249935.2023.2282963)
  
    - truck and drones : three-stage heuristic 






!!! note "货车车队platoon"

    1. [Yan, X., Xu, M., & Xie, C. (2023). Local container drayage problem with improved truck platooning operations. Transportation Research Part E: Logistics and Transportation Review, 169, 102992.](https://www.sciencedirect.com/science/article/pii/S1366554522003696)

    > 该公司安排一组司机和一个自动驾驶卡车车队为分布在码头周围当地的一组送货和取货客户提供服务。一辆满载的卡车将从码头出发前往送货客户，并在客户现场等待开箱。拆包工作完成后，空卡车将返回码头或取货客户进行重复使用。

    - 卡车组成车队协同运输、无人车跟随配送
        - 9.1 Barua, L., Zou, B., & Choobchian, P. (2023). Maximizing truck platooning participation with preferences. Transportation Research Part E: Logistics and Transportation Review, 179, 103297.
            - 最大稳定卡车序列长度的设计
        - 9.2 **[Haas, I., & Friedrich, B. (2021). An autonomous connected platoon-based system for city-logistics: development and examination of travel time aspects. Transportmetrica A: Transport Science, 17(1), 151-168.](https://www.tandfonline.com/doi/abs/10.1080/23249935.2018.1494221)**: 重点是与排的大小和数量以及非排车辆数量相关的三个参数。发现的最主要参数是系统中的排数。这个参数有两个相互矛盾的效果：增加这个数字可以减少在排之间切换时的等待时间，但同时会增加交叉点的延迟。
        - 9.3 **Hao, Y., Chen, Z., Jin, J., & Sun, X. (2023). Joint operation planning of drivers and trucks for semi-autonomous truck platooning. Transportmetrica A: Transport Science, 1-37.**： 半自动卡车列队行驶下的驾驶员时间表可能与卡车不完全相同...开发一个数学建模框架....决定要调度的司机数量，以及司机和卡车的行车路线和时间表相互依赖，目的是在满足所有交付需求的同时，将总运营成本降至最低，包括司机的固定调度成本、道路人工成本和能源消耗成本。


------------

## 公交车和交通网络相关

1. **Fan, Y., Ding, J., Liu, H., Wang, Y., & Long, J. (2022). Large-scale multimodal transportation network models and algorithms-Part I: The combined mode split and traffic assignment problem. Transportation Research Part E: Logistics and Transportation Review, 164, 102832.**

- 特征：交通流分配、VI-based、多式连用出行


2. Zeng, Z., Wang, S., & Qu, X. (2022). On the role of battery degradation in en-route charge scheduling for an electric bus system. Transportation Research Part E: Logistics and Transportation Review, 161, 102727.

- 特征：引入入峰均功率比、分时电价和电池磨损公式来解决电网和电池问题、是在途充电（en- route），可以在行驶的站点短暂充电，目的是维持SOC在一个范围内，减少电池老化的影响
- 数据集：瑞典公交车数据，场景特殊



3. [Lee, E., Cen, X., & Lo, H. K. (2021). Zonal-based flexible bus service under elastic stochastic demand. Transportation Research Part E: Logistics and Transportation Review, 152, 102367.](https://www.sciencedirect.com/science/article/pii/S1366554521001356)

- 随机规划、提供门到门服务的灵活公交车，多名乘客共享车辆，从而减少了城市网络的拥堵。根据历史需求特征将灵活公交分配到分区路线。在需求实现后，乘客可以享受定期服务或临时服务，以尽量减少临时服务成本和绕行时间成本的总和。

4. **Zhan, X., Szeto, W. Y., & Chen, X. M. (2022). A simulation–optimization framework for a dynamic electric ride-hailing sharing problem with a novel charging strategy. Transportation Research Part E: Logistics and Transportation Review, 159, 102615.**

> 仿真优化、网约车电动汽车充电策略
> 
> MILP和MINLP的输出更新和跟踪乘客的状态和充电站的充电过程。结果表明，在动态网约车匹配问题中，所提出的充电策略在充电等待时间更短、匹配率更高的情况下优于基准。通过改变初始充电状态（SOC）、REV数量、各充电站充电桩数、充满电时间、充电桩分布等不同场景，检验了所提充电策略的鲁棒性


5. Tran, C. Q., Keyvan-Ekbatani, M., Ngoduy, D., & Watling, D. (2021). Stochasticity and environmental cost inclusion for electric vehicles fast-charging facility deployment. Transportation Research Part E: Logistics and Transportation Review, 154, 102460.

- 为快速充电设施部署双层优化框架 | 考虑随机需求和续航里程下用户路线选择 | 提出了一种基于交叉熵法的算法 | 将资金、网络拥塞和环境成本降至最低。

6. Alvo, M., Angulo, G., & Klapp, M. A. (2021). An exact solution approach for an electric bus dispatch problem. Transportation Research Part E: Logistics and Transportation Review, 156, 102528.

- 混合车队、这个是dispatch，为每个汽车分配路线；两阶段，不是给定时刻表调度，而是设置时刻表。目标是给出一个合理的时间安排和路线（VSP）


7. Huang, D., Wang, Y., Jia, S., Liu, Z., & Wang, S. (2023). A Lagrangian relaxation approach for the electric bus charging scheduling optimisation problem. Transportmetrica A: Transport Science, 19(2), 2023690.

- 拉格朗日松弛框架（同研讨课汇报论文） 


8. [Tran, C. Q., Ngoduy, D., Keyvan-Ekbatani, M., & Watling, D. (2021). A user equilibrium-based fast-charging location model considering heterogeneous vehicles in urban networks. Transportmetrica A: Transport Science, 17(4), 439-461.](https://www.tandfonline.com/doi/abs/10.1080/23249935.2020.1785579)
   
- 快充站点位置设置：在混合汽油和电动汽车的城市网络中，快速充电站在交通平衡流和电动汽车渗透率方面的最佳位置识别问题。提出了一种双层优化框架，其中上层旨在通过最小化总行程时间和充电基础设施的安装成本来定位

9. Thanh, V. V., Su, W., & Wang, B. (2022). Optimal DC microgrid operation with model predictive control-based voltage-dependent demand response and optimal battery dispatch. Energies, 15(6), 2140.

- 。引入自适应充电策略，使电动公交车能够部分灵活地充电。然后，基于考虑连续时间的思想，针对该问题构建了一个混合整数规划模型。还建立了考虑先验贪婪和完全充电策略的两种场景模型进行比较。


10. Tang, C., Xue, H., Ceder, A., & Ge, Y. E. (2023). Optimal variable vehicle scheduling strategy for a network of electric buses with fast opportunity charging. Transportmetrica A: Transport Science, 1-26.

> 我们提出了一种新颖的具有多个站点的公交EB网络的可变车辆调度策略，通过正确改变行程出发时间来应对这一挑战。通过插入一个时间表延迟，可以节省运营成本。


11.  **Guo, H., Wang, Y., Shang, P., Yan, X., & Guan, Y. (2023). Customised bus route design with passenger-to-station assignment optimisation. Transportmetrica A: Transport Science, 1-32.**： 定制公交作为一种新兴....重点关注客到站分配的定制公交路线问题，该文建立了一种时间离散化多商品网络流模型，通过允许分载和混合载荷，共同确定CB路线、时刻表和客到站分配。通过对偶化，将所建立的模型分解为两个可求解的子问题，并提出了一种基于拉格朗日启发式求解算法。

12. Cong, Y., Wang, H., Bie, Y., & Wu, J. (2023). Double-battery configuration method for electric bus operation in cold regions. Transportation Research Part E: Logistics and Transportation Review, 180, 103362:我们提出了一种双电池配置方法，用于在季节之间温度变化很大的寒冷地区运行的 EB。该方法涉及在冬季使用高容量电池，在夏季使用低容量电池。为了确定冬季和夏季的最佳车队规模、电池容量和 EB 调度计划，我们制定了一个整数规划模型，


13. [Cui, S., Gao, K., Yu, B., Ma, Z., & Najafi, A. (2023). Joint optimal vehicle and recharging scheduling for mixed bus fleets under limited chargers. Transportation Research Part E: Logistics and Transportation Review, 180, 103335.](https://www.sciencedirect.com/science/article/pii/S136655452300323X)

- 混合动力公交车队、（也就是两种charge模式：柴油和电、耗时是不一样的）


-----


## 鲁棒优化 and Bayesian


1. Huo, J., Liu, C., Chen, J., Meng, Q., Wang, J., & Liu, Z. (2023). Simulation-based dynamic origin–destination matrix estimation on freeways: A Bayesian optimization approach. Transportation Research Part E: Logistics and Transportation Review, 173, 103108.

- 针对高速公路网络的动态 OD需求估计问题。将该问题表述为双层规划模型，设计了一种计算效率高的贝叶斯优化方法。将物理代理模型嵌入到功能代理模型，提出了一种新的代理模型，使代理模型能够有效地处理高维问题。


2. Duncan, L. C., Watling, D. P., Connors, R. D., Rasmussen, T. K., & Nielsen, O. A. (2023). Choice set robustness and internal consistency in correlation-based logit stochastic user equilibrium models. Transportmetrica A: transport science, 19(3), 2063969.

- SUE and robustness

3. [Wang, D., Yang, K., Yang, L., & Dong, J. (2023). Two-stage distributionally robust optimization for disaster relief logistics under option contract and demand ambiguity. Transportation research part E: logistics and transportation review, 170, 103025.](https://www.sciencedirect.com/science/article/pii/S1366554523000121)

- 需求模糊、救灾背景、两阶段分布式鲁棒

4. [Cao, Y., Zhu, X., & Yan, H. (2022). Data-driven Wasserstein distributionally robust mitigation and recovery against random supply chain disruption. Transportation Research Part E: Logistics and Transportation Review, 163, 102751.](https://www.sciencedirect.com/science/article/pii/S1366554522001429)

- 突发供应链disruption

5. [Xiong, X., Li, Y., Yang, W., & Shen, H. (2022). Data-driven robust dual-sourcing inventory management under purchase price and demand uncertainties. Transportation Research Part E: Logistics and Transportation Review, 160, 102671.](https://www.sciencedirect.com/science/article/pii/S1366554522000667)

- 库存需求的不确定

6. [Li, R., Cui, Z., Kuo, Y. H., & Zhang, L. (2023). Scenario-based Distributionally Robust Optimization for the Stochastic Inventory Routing Problem. Transportation Research Part E: Logistics and Transportation Review, 176, 103193.](https://www.sciencedirect.com/science/article/pii/S1366554523001813)

- 零售店对同质产品的需求是不确定的。供应商需要确定访问零售商的时间、每个零售商的补货数量以及车辆的路线，以尽量减少缺货、持有和运输成本的总和...提出了一个基于场景的分布鲁棒优化框架。将分布鲁棒优化模型转化为混合整数问题...与列生成集成的 Tabu 搜索算法来求解类似集合分区的整数线性规划模型，以便识别更好的路由集。

----

## Review

1. Srinivas, S., Ramachandiran, S., & Rajendran, S. (2022). Autonomous robot-driven deliveries: A review of recent developments and future directions. Transportation research part E: logistics and transportation review, 165, 102834.

- 无人车配送


2. Tan, Z., Liu, F., Chan, H. K., & Gao, H. O. (2022). Transportation systems management considering dynamic wireless charging electric vehicles: Review and prospects. Transportation Research Part E: Logistics and Transportation Review, 163, 102761.

- 无线充电交通系统：电动汽车在行驶时基于感应技术进行无线充电。




-----



!!! note "Some Other topics"
    
    - ride sharing: with Autonomous electric vehicle: 电动无人车的共享交通
    - pedestrian-vehicle flow estimation 行人和车辆流量估计
    - 很少具体涉及能源、电网、V2G？
    
    
    -----

    - transportmetric A:  / reinforcement learning method & framework

    - Guo, Y., Yang, F., Jin, P. J., Liu, H., Ma, S., & Yao, Z. (2022). Vehicle travel path recognition in urban dense road network environments by using mobile phone data. Transportmetrica A: transport science, 18(3), 1496-1516.： 借助手机数据估计车辆行驶路线


    - simulations （Paul, G., Raju, N., Arkatkar, S., & Easa, S. (2021). Can segregating vehicles in mixed-traffic stream improve safety and throughput? implications using simulation. Transportmetrica A: transport science, 17(4), 1002-1026.）
    - 自动驾驶动作规划 / 路径感知与控制调整（Bai, Y., Zhang, Y., Li, X., & Hu, J. (2022). Cooperative weaving for connected and automated vehicles to reduce traffic oscillation. Transportmetrica A: transport science, 18(1), 125-143.）


    ---------

    <!-- 1. Winnipeg network: 交通流量分配
    2. Sioux-Falls 网络 -->
    - post-disaster management
    - 地铁排班调度
    - 事故检测、车祸拥堵检测等
    - data-driven method


---------

Truck–drone hybrid routing problem with time-dependent road travel time


Time-dependent road:

> coordinate trucks and drones, particularly under uncertain traffic conditions

每条路的走行时间不是固定的，而是会随着一天的不同时间而变化。



-------



