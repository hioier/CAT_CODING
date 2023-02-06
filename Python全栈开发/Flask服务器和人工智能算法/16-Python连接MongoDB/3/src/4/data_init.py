import pymongo


def data_init():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client['mydb12']
    if not db.video.find_one({}):
        db.video.insert_many(
            [
                {'name': '新版哆啦A梦', 'part': 565, 'plot': '新版哆啦A梦 重温儿时的梦想！体验新一代哆啦A梦的神奇法宝！……', 'picture': '新版哆啦A梦.jpg'},
                {'name': '火影忍者', 'part': 720, 'plot': '十多年前一只拥有巨大威力的妖兽“九尾妖狐”袭击了木叶忍者村，当时的第四代火影拼尽全力，以自己的生……',
                 'picture': '火影忍者.jpg'},
                {'name': '银河护卫队第三季', 'part': 26, 'plot': '2014年北美最卖座电影《银河护卫队》正式宣布了启动动画剧集版《Marvel’s Guardians……',
                 'picture': '银河护卫队第三季.jpg'},
                {'name': '小黄人和萌友', 'part': 19, 'plot': '童心未眠，小黄人携萌友爆笑回归。由环球携手打造，照明娱乐呈献的40支小黄人官方宣传动画“小黄人和萌友……',
                 'picture': '小黄人和萌友.jpg'},
                {'name': '泰迦奥特曼国语', 'part': 1, 'plot': '第一个奥特曼，泰罗之子，泰伽登场！ 地球上住着很多偷偷隐居在此的宇宙人。只有很少一部分的人知道这……',
                 'picture': '泰迦奥特曼国语.jpg'},
                {'name': '泰迦奥特曼日语版', 'part': 1, 'plot': '地球上住着很多偷偷隐居在此的宇宙人。只有很少一部分的人知道这个真相，一般民众并不知情。在……',
                 'picture': '泰迦奥特曼日语版.jpg'},
                {'name': '女武神的餐桌', 'part': 2, 'plot': '《崩坏3》官方首部原创连载动画。这是回到宿舍的女武神们，发生在她们身上的和食物有关的故事。女武神们做……',
                 'picture': '女武神的餐桌.jpg'},
                {'name': '假面骑士时王', 'part': 42, 'plot': '《假面骑士Zi-O》（日语：仮面ライダージオウ）是2018年播出的日本特摄电视剧，也是“平成假面骑士……',
                 'picture': '假面骑士时王.jpg'},
                {'name': '倒数七天', 'part': 13, 'plot': '死亡通知，这个实验性计划，将会经过好几轮的测试，每一轮的测试，都会挑出几个即将过世的特定人选，观察他……',
                 'picture': '倒数七天.jpg'}, {'name': '霹雳靖玄录', 'part': 6, 'plot': '随着虚无的力量扩散，神秘的南域亦受影响，能人辈出各显风采。神秘的浩劫，隐藏着武林未知的暗潮。……', 'picture': '霹雳靖玄录.jpg'},
                {'name': '太空终界第二季', 'part': 2, 'plot': '一位名叫加里的宇航员和他的星球毁灭伙伴“月饼”开始了一系列的太空旅行，以解开宇宙到底在哪里结束以及是……',
                 'picture': '太空终界第二季.jpg'},
                {'name': '鬼灭之刃', 'part': 14, 'plot': '电视动画《鬼灭之刃》改编自吾峠呼世晴创作的同名漫画，于2018年6月4日在《周刊少年JUMP》201……',
                 'picture': '鬼灭之刃.jpg'},
                {'name': '妖精的尾巴', 'part': 316, 'plot': '男主角纳兹“Natsu”这个名字的日文原意为“夏天”。 故事叙述在一个充满魔法的世界——阿斯……',
                 'picture': '妖精的尾巴.jpg'},
                {'name': '裤袜视界', 'part': 9, 'plot': '4月。下雨的早晨。开始凋零的樱花被雨滴打落，漂浮在积水之上。学生们撑着五颜六色的雨伞，穿过高中的校门……',
                 'picture': '裤袜视界.jpg'},
                {'name': '变形金刚：领袖之证第一季', 'part': 9, 'plot': '故事讲述两派来到地球后，因为发生了一些“事件”，导致双方外形大变（也解释了两系列风格不同的原因）。也……',
                 'picture': '变形金刚：领袖之证第一季.jpg'},
                {'name': 'GATE奇幻自卫队炎龙篇', 'part': 12, 'plot': '故事描绘了20XX年，突如其来的“通往异世界的门”在东京银座出现，从中涌出来了大量怪物和军队。而……',
                 'picture': 'GATE奇幻自卫队炎龙篇.jpg'},
                {'name': '灵域第五季', 'part': 12, 'plot': '少年秦烈与同伴在秘境中力挫各方势力的青年才俊，秦烈不但成功收服了木、火、雷、冰四灵兽和封魔碑，还在秘……',
                 'picture': '灵域第五季.jpg'},
                {'name': '灵域第四季', 'part': 12, 'plot': '秦烈和同伴们继续在秘境神葬场中进行着残酷的试炼。神葬场中危机四伏，秦烈从巫虫的控制中救下洛尘之后，却……',
                 'picture': '灵域第四季.jpg'},
                {'name': '灵域第三季', 'part': 12, 'plot': '秦烈拔起十二根灵纹柱，邪族和人族的战争一触即发。然而就在危机关头，天剑山的李牧出现阻止了一切往最坏的……',
                 'picture': '灵域第三季.jpg'},
                {'name': 'GATE奇幻自卫队炎龙篇', 'part': 12, 'plot': '故事描绘了20XX年，突如其来的“通往异世界的门”在东京银座出现，从中涌出来了大量怪物和军队。而……',
                 'picture': 'GATE奇幻自卫队炎龙篇.jpg'},
                {'name': '灵域第五季', 'part': 12, 'plot': '少年秦烈与同伴在秘境中力挫各方势力的青年才俊，秦烈不但成功收服了木、火、雷、冰四灵兽和封魔碑，还在秘……',
                 'picture': '灵域第五季.jpg'},
                {'name': '灵域第四季', 'part': 12, 'plot': '秦烈和同伴们继续在秘境神葬场中进行着残酷的试炼。神葬场中危机四伏，秦烈从巫虫的控制中救下洛尘之后，却……',
                 'picture': '灵域第四季.jpg'},
                {'name': '灵域第三季', 'part': 12, 'plot': '秦烈拔起十二根灵纹柱，邪族和人族的战争一触即发。然而就在危机关头，天剑山的李牧出现阻止了一切往最坏的……',
                 'picture': '灵域第三季.jpg'},
                {'name': '灵域第二季', 'part': 10, 'plot': '少年秦烈为守护唐思琪，不顾境界相差悬殊和梁少扬对战，同时他体内沉睡的力量开始慢慢觉醒。器具宗在玄天盟……',
                 'picture': '灵域第二季.jpg'},
                {'name': '少年正义联盟第三季', 'part': 16, 'plot': '华纳正式宣布DC良心动画《少年正义联盟》要拍第3季。目前已经开始制作，主创Greg Weisman和……',
                 'picture': '少年正义联盟第三季.jpg'},
                {'name': 'JOJO的奇妙冒险黄金之风', 'part': 37, 'plot': '住在意大利那不勒斯的青年乔鲁诺·乔巴拿，是继承了乔斯达家宿敌·DIO之血脉的儿子。幼年时遭受迫害而自……',
                 'picture': 'JOJO的奇妙冒险黄金之风.jpg'},
                {'name': '炎炎消防队', 'part': 1, 'plot': '全人类为之恐惧——。 没有任何异常的人类突然燃烧，化作操纵火焰的怪物“焰人”，并极尽破坏之能事的“人……',
                 'picture': '炎炎消防队.jpg'},
                {'name': '新石纪', 'part': 1, 'plot': '全人类因谜般的现象而在一瞬间石化，之后过了数千年——。拥有超越人类的头脑，天生的科学……', 'picture': '新石纪.jpg'},
                {'name': '万界神主', 'part': 46, 'plot': '身为古神的叶辰从神境世界陨落到了苍蓝世界，这里百州千国林立，豪强争霸，叶辰在这个苍蓝世界呆了数百年，……',
                 'picture': '万界神主.jpg'},
                {'name': '水果篮子', 'part': 14, 'plot': '高中生本田透自从唯一的亲人——母亲去世之后，就开始一个人在帐篷中生活。但她设置帐篷的地方正是历史悠久……',
                 'picture': '水果篮子.jpg'},
                {'name': '骚动时节的少女们啊', 'part': 1, 'plot': '小野寺和纱等5名女生，从属于高中的文艺部。 某天，她们正在谈论“死前想要做的事情”这一话题，此时部员……',
                 'picture': '骚动时节的少女们啊.jpg'},
                {'name': '没出息的阴阳师一家', 'part': 11, 'plot': '即使Boss永远刷不过、即使对战永远打不赢、即使SSR永远抽不到、即使组队永远组翻车、即使是倒霉的人……',
                 'picture': '没出息的阴阳师一家.jpg'},
                {'name': '斗罗大陆第一季', 'part': 59, 'plot': '唐门外门弟子唐三，因偷学内门绝学为唐门所不容，跳崖明志时却发现没有死，反而以另外一个身份来到了另一个……',
                 'picture': '斗罗大陆第一季.jpg'},
                {'name': '倒数七天', 'part': 13, 'plot': '死亡通知，这个实验性计划，将会经过好几轮的测试，每一轮的测试，都会挑出几个即将过世的特定人选，观察他……',
                 'picture': '倒数七天.jpg'},
                {'name': '喜羊羊与灰太狼之羊村守护者', 'part': 60, 'plot': '习惯了“狼捉羊”的“套路”，可曾想象过狼与羊和平相处的温馨画面？据原创动力副总经理蔡瑞琼在发布会介绍……',
                 'picture': '喜羊羊与灰太狼之羊村守护者.jpg'},
                {'name': '一拳超人第二季', 'part': 13, 'plot': '因兴趣而开始做英雄的男人，埼玉。他通过3年的特训获得了无敌的力量，成为仅凭一击就能打倒任何敌人的英……',
                 'picture': '一拳超人第二季.jpg'},
                {'name': '画江湖之不良人第三季', 'part': 26, 'plot': '《画江湖之不良人》第三季侠影归来，再现唐末乱世风云！乾陵被毁、龙泉宝藏下落不明，前朝皇子李星云欲归隐……',
                 'picture': '画江湖之不良人第三季.jpg'},
                {'name': '为了女儿，我说不定连魔王都能干掉', 'part': 1, 'plot': '年纪轻轻就崭露头角，在附近一带小有名气的精干冒险者青年迪尔。他因某件委托而踏足进入深邃森林，遇到了……',
                 'picture': '为了女儿，我说不定连魔王都能干掉.jpg'},
                {'name': '系统逼我做皇后', 'part': 16, 'plot': '游戏手残莫小西，莫名其妙的穿越到自己玩的一款游戏当中，还被系统逼着成为一代帝后……',
                 'picture': '系统逼我做皇后.jpg'},
                {'name': '交锋联盟之机巧一族', 'part': 21, 'plot': '讲述了有着不同技能的5个种族:十八番街、动物健将、机巧一族、恐怖玩具、审判专家之间相互战斗的故事。这……',
                 'picture': '交锋联盟之机巧一族.jpg'},
                {'name': '偶像活动Friends～闪耀的宝石～', 'part': 14, 'plot': '电视动画《偶像活动Friends!～闪耀的宝石～》是《偶像活动》系列的新作将于2019年4月开播  ……',
                 'picture': '偶像活动Friends～闪耀的宝石～.jpg'},
                {'name': '女武神的餐桌', 'part': 2, 'plot': '《崩坏3》官方首部原创连载动画。这是回到宿舍的女武神们，发生在她们身上的和食物有关的故事。女武神们做……',
                 'picture': '女武神的餐桌.jpg'},
                {'name': '精灵宝可梦太阳月亮', 'part': 128, 'plot': '与宠物小精灵们冒险的小智，这一次将开始从未体验过的校园生活。……', 'picture': '精灵宝可梦太阳月亮.jpg'},
                {'name': '荒野的寿飞行队外传：天空的春风飞行队', 'part': 4, 'plot': '荒野的世界生存ひよっこ飞行部队的上会日常短篇动画乐趣!……',
                 'picture': '荒野的寿飞行队外传：天空的春风飞行队.jpg'},
                {'name': '灵剑尊', 'part': 42, 'plot': '大梦一场，落魄少年立志要改变现状奋发图强创造一片新天地。珍奇异宝，功法武决，遗失的强者洞府，在这个天……',
                 'picture': '灵剑尊.jpg'},
                {'name': '香蕉怪大叔呐呐~呐第二季', 'part': 13, 'plot': '本作以东京电视台吉祥物呐呐呐为原型，登场角色的香蕉形象由其衍生而来。本质则是一档吐槽东京电视台历代番……',
                 'picture': '香蕉怪大叔呐呐~呐第二季.jpg'},
                {'name': '宇宙战舰大和号2202', 'part': 21, 'plot': '《宇宙战舰大和号2202 爱的战士们》由小说《亡国舰队》、《魔女潜舰》的作者福井晴敏担任编剧，《苍穹……',
                 'picture': '宇宙战舰大和号2202.jpg'},
                {'name': '钢之炼金术师FA', 'part': 64, 'plot': '爱德华和他的弟弟阿尔方斯因为太思念去世的母亲，触犯了将私人复活这一炼金术最大的禁忌，进行了人体炼成。……',
                 'picture': '钢之炼金术师FA.jpg'},
                {'name': '钢之炼金术师', 'part': 51, 'plot': '年幼的爱力克兄弟十分思念去世的母亲，不惜触犯炼金术中最大的禁忌，进行了人体炼成。可是炼成失败了，哥哥……',
                 'picture': '钢之炼金术师.jpg'},
                {'name': '彼方的阿斯特拉', 'part': 1, 'plot': '在宇宙之行变的理所当然的近未来。高中生卡纳特，阿莉艾斯等9人踏上了“行星之旅”的征程。从来没有体验过……',
                 'picture': '彼方的阿斯特拉.jpg'},
                {'name': '彼方的阿斯特拉', 'part': 1, 'plot': '在宇宙之行变的理所当然的近未来。高中生卡纳特，阿莉艾斯等9人踏上了“行星之旅”的征程。从来没有体验过……',
                 'picture': '彼方的阿斯特拉.jpg'},
                {'name': '流汗吧！健身少女', 'part': 1, 'plot': '“响……你又胖了吧？”朋友毫不留情的一句话，刺入爱吃的女高中生·纱仓响心中。她想着暑假之前绝对要瘦下……',
                 'picture': '流汗吧！健身少女.jpg'},
                {'name': '雄兵连之诸天降临', 'part': 25, 'plot': '《雄兵连》系列是国内首部3D战争科幻类动漫作品，《雄兵连II诸天降临》为该系列故事最新续作，描述了在……',
                 'picture': '雄兵连之诸天降临.jpg'},
                {'name': '万界仙踪第二季', 'part': 23, 'plot': '家族大会之后，炎绝在逃亡路上被叶星云设局击毙，炎武一族实力骤减。玄冥世家蠢蠢欲动，绑架叶雪云想借机与……',
                 'picture': '万界仙踪第二季.jpg'},
                {'name': '甲铁城的卡巴内瑞：海门决战', 'part': 3, 'plot': '全世界被产业革命的波澜推动，自近世变迁至近代之时，不死的怪物突然出现。被钢铁的皮膜包覆，只要心脏不被……',
                 'picture': '甲铁城的卡巴内瑞：海门决战.jpg'},
                {'name': '甲铁城的卡巴内瑞', 'part': 12, 'plot': '本作是一部以蒸汽机发达的岛国“日之本”为舞台的蒸汽朋克生存动作剧，作品主要描写了拥有钢铁心脏的僵尸=……',
                 'picture': '甲铁城的卡巴内瑞.jpg'},
                {'name': '猫和老鼠四川方言版', 'part': 124, 'plot': '《猫和老鼠》从1940年问世以来，一直是全世界最受欢迎的卡通之一，Tom和jerry这一对搞笑活宝，……',
                 'picture': '猫和老鼠四川方言版.jpg'},
                {'name': '非人哉', 'part': 48, 'plot': '中国古典神话传说中的“著名”精怪是如何在现代社会生存下去，他们成为了我们身边有着神仙特色的宅女、暖男……',
                 'picture': '非人哉.jpg'},
                {'name': '大王不高兴', 'part': 11, 'plot': '地府新任大BOSS阎王竟然是个少女，更要命的是这位少女超级怕鬼！为了成为合格接班人、守护千百年来阎王……',
                 'picture': '大王不高兴.jpg'},
                {'name': '反叛的鲁路修R2', 'part': 25, 'plot': '“东京决战”一年后，布里塔尼亚少年鲁路修在11区（原日本国）过着平凡的学生生活。但是，鲁路修与弟弟罗……',
                 'picture': '反叛的鲁路修R2.jpg'},
                {'name': '猫和老鼠', 'part': 185, 'plot': 'TOM是一只可爱的猫，十分喜爱恶作剧，JERRY是和TOM生活在一起的小老鼠，他们在生活中相互为伴，……',
                 'picture': '猫和老鼠.jpg'},
                {'name': '蜂蜜与四叶草2', 'part': 12, 'plot': '美术大学五人组的故事仍在继续。竹本（神谷浩史 配音）结束了寻找自我的单车之旅，在盛放烟火的晚上对阿久……',
                 'picture': '蜂蜜与四叶草2.jpg'},
                {'name': '蜂蜜与四叶草', 'part': 24, 'plot': '美术大学学生竹本和学长真山以及多次留级的森田一起生活在单身公寓里，大家的生活风清云淡却也乐趣无穷。 ……',
                 'picture': '蜂蜜与四叶草.jpg'},
                {'name': '三国演义3D动画版', 'part': 52, 'plot': '东汉末年，朝廷腐败，连年灾荒，爆发黄巾起义。涿郡城刘备遇张飞、关羽，三人志同道合，桃园三结义。立军功……',
                 'picture': '三国演义3D动画版.jpg'},
                {'name': '灵域第一季', 'part': 10, 'plot': '在这片名为灵域的天地间，有一片赤澜大陆，大陆上的武者和灵器有着明确的等级划分，家族，宗派势力也有着严……',
                 'picture': '灵域第一季.jpg'},
                {'name': '在世界尽头咏唱恋曲的少女YU-NO', 'part': 14, 'plot': '主人公有马在幼年时期就失去了母亲，身为历史学家的父亲也在两个月前因事故去世了。所有一切都失去活力的高……',
                 'picture': '在世界尽头咏唱恋曲的少女YU-NO.jpg'},
                {'name': '在世界尽头咏唱恋曲的少女YU-NO', 'part': 14, 'plot': '主人公有马在幼年时期就失去了母亲，身为历史学家的父亲也在两个月前因事故去世了。所有一切都失去活力的高……',
                 'picture': '在世界尽头咏唱恋曲的少女YU-NO.jpg'},
                {'name': '战斗吧歌姬！第二季', 'part': 13, 'plot': '5位想要成为“Swan”的少女，已经做好了“战斗”的准备。迎接她们的，是地狱般的训练……而更残酷的，……',
                 'picture': '战斗吧歌姬！第二季.jpg'},
                {'name': '时之歌 暮日醒觉诗 谍影篇', 'part': 8, 'plot': '遥远银河彼端，闪耀着一颗孕育魔法神力的星球——维尔哈伦。大陆上存在着四个迥然各异的国家。……',
                 'picture': '时之歌 暮日醒觉诗 谍影篇.jpg'},
                {'name': '斗破苍穹之大主宰', 'part': 20, 'plot': '"这是一个灵气为王的世界，谁拥有吞天噬月的灵力，谁就是大主宰！ 大千世界，万道争锋。主宰之……',
                 'picture': '斗破苍穹之大主宰.jpg'},
                {'name': '我家大师兄脑子有坑 特别篇', 'part': 37, 'plot': '逍遥门大师兄东方纤云，风流倜傥，玉树临风。作为一个穿越者，他凭借自己的聪慧在第一时间确认了自己的设定……',
                 'picture': '我家大师兄脑子有坑 特别篇.jpg'},
                {'name': '英雄时代', 'part': 26, 'plot': '遥远的，遥远的，时空的彼方。宇宙里有一群自称为“黄金一族”的人……', 'picture': '英雄时代.jpg'},
                {'name': '魔法禁书目录2', 'part': 24, 'plot': '由日本著名轻小说家镰池和马创作的「魔法禁书目录」，小说以及之后推出的漫画版都大受欢迎。继2008年1……',
                 'picture': '魔法禁书目录2.jpg'},
                {'name': '魔法禁书目录', 'part': 24, 'plot': '自己的阳台栏杆上出现了像被单一样挂在上面的少女，这种非现实的情节出现在了上条当麻的眼前。虽然在这个城……',
                 'picture': '魔法禁书目录.jpg'},
                {'name': '反叛的鲁路修', 'part': 25, 'plot': '鲁路修本是帝国的王子，在母后遇害后，和失明的妹妹一起被流放到11区（原日本国）作为人质。在那里他们结……',
                 'picture': '反叛的鲁路修.jpg'},
                {'name': '反叛的鲁路修', 'part': 25, 'plot': '鲁路修本是帝国的王子，在母后遇害后，和失明的妹妹一起被流放到11区（原日本国）作为人质。在那里他们结……',
                 'picture': '反叛的鲁路修.jpg'},
                {'name': '圣痕的凯撒2', 'part': 12, 'plot': '吉野弘幸原作、佐藤健悦绘图的校园格斗漫画《圣痕鍊金士》（长鸿代理），故事里就读圣米海洛夫学园的少女「……',
                 'picture': '圣痕的凯撒2.jpg'},
                {'name': '圣痕炼金士2', 'part': 12, 'plot': '某一天，就读圣米海洛夫学园的织部真冬见到了男主角亚历山大·尼古拉叶维奇赫尔（昵称沙夏），他是一个俄国……',
                 'picture': '圣痕炼金士2.jpg'},
                {'name': '圣痕炼金士', 'part': 24, 'plot': '某一天，就读圣米海洛夫学园的织部真冬捡到了[shuangtv.net]男主角亚历山大·尼古拉叶维奇赫……',
                 'picture': '圣痕炼金士.jpg'},
                {'name': '妖精的旋律', 'part': 14, 'plot': '一次突发事故，二觭人露西杀死警卫，逃出了研究所，并丧失了记忆，后被主角耕太和其表亲由香所收养。研究所……',
                 'picture': '妖精的旋律.jpg'},
                {'name': '血色苍穹', 'part': 26, 'plot': '李鸣洋原本是一个平凡上班族，因为扫了一个二维码后，被卷入一个巨大空旷的奇怪城市——“血色苍穹”世界。……',
                 'picture': '血色苍穹.jpg'},
                {'name': '奇幻沼泽第一季', 'part': 8, 'plot': '一个13岁的女孩神奇地被送到了两栖动物的世界。……', 'picture': '奇幻沼泽第一季.jpg'},
                {'name': '少年泰坦出击第五季', 'part': 38, 'plot': 'The Titans try to remember how to be superheroes i……',
                 'picture': '少年泰坦出击第五季.jpg'},
                {'name': '少年泰坦出击第五季', 'part': 38, 'plot': 'The Titans try to remember how to be superheroes i……',
                 'picture': '少年泰坦出击第五季.jpg'},
                {'name': '闪电十一人猎户座的刻印', 'part': 36, 'plot': '闪电十一人猎户座的刻印……', 'picture': '闪电十一人猎户座的刻印.jpg'},
                {'name': '假面骑士时王国语', 'part': 41, 'plot': '《假面骑士Zi-O》（日语：仮面ライダージオウ）是2018年播出的日本特摄电视剧，也是“平成假面骑士……',
                 'picture': '假面骑士时王国语.jpg'},
                {'name': '斗罗大陆2绝世唐门荣耀篇动态漫画', 'part': 33, 'plot': '曾经叱咤斗罗大陆的唐三成神之后，唐门日渐式微，一天他发现一名叫做霍雨浩的少年，因母亲被自己同父异母的……',
                 'picture': '斗罗大陆2绝世唐门荣耀篇动态漫画.jpg'},
                {'name': '智龙迷城', 'part': 65, 'plot': '简介: 本作不同于智龙迷城X，讲述的是以现代为舞台，热血小学生明石大河以职业游戏玩家世界的第一名为目……',
                 'picture': '智龙迷城.jpg'},
                {'name': '高校星歌剧第三季', 'part': 1, 'plot': '“放弃梦想的方法，我不知道——” 终于与“憧憬的高中生”凤树实现共演的星谷悠太， 以下一个梦想为目标……',
                 'picture': '高校星歌剧第三季.jpg'},
                {'name': '欢迎来到加帕里公园第二季', 'part': 5, 'plot': '坐落在这个世界的某个角落的超大型综合动物园「加帕里公园」，依靠着那里的神秘物质「砂之星」的力量，动物……',
                 'picture': '欢迎来到加帕里公园第二季.jpg'},
                {'name': '高校星歌剧第三季', 'part': 1, 'plot': '“放弃梦想的方法，我不知道——”                                  ……',
                 'picture': '高校星歌剧第三季.jpg'},
                {'name': '降妖贱师', 'part': 16, 'plot': '这是一个中二少年与另类妖怪相爱相杀的热血故事。少年，就是不断的去战斗，然后胜利。不管你是……',
                 'picture': '降妖贱师.jpg'},
                {'name': '高校星歌剧OVA', 'part': 2, 'plot': '高校星歌剧OVA动画全集共分为2卷，第1卷2016年7月发售，第2卷9月发售。高校星歌剧故事讲述了在……',
                 'picture': '高校星歌剧OVA.jpg'},
                {'name': '房东妹子青春期', 'part': 12, 'plot': '导演: 小川优树编剧: 水瀬るるう主演: 久保由利香 / 木户衣吹 / 山崎惠理类型: 动画制片国家……',
                 'picture': '房东妹子青春期.jpg'},
                {'name': '队长小翼日语版', 'part': 52, 'plot': '《足球小将》宣布复活！将于2018年4月播出。这部动画主要是描绘以大空翼为中心的一群年轻有为的足球小……',
                 'picture': '队长小翼日语版.jpg'},
                {'name': '队长小翼国语版', 'part': 52, 'plot': '《足球小将》宣布复活！将于2018年4月播出。这部动画主要是描绘以大空翼为中心的一群年轻有为的足球小……',
                 'picture': '队长小翼国语版.jpg'},
                {'name': '足球小将翼国语版', 'part': 52, 'plot': '《足球小将》宣布复活！将于2018年4月播出。这部动画主要是描绘以大空翼为中心的一群年轻有为的足球小……',
                 'picture': '足球小将翼国语版.jpg'},
                {'name': '足球小将翼日语版', 'part': 52, 'plot': '《足球小将》宣布复活！将于2018年4月播出。这部动画主要是描绘以大空翼为中心的一群年轻有为的足球小……',
                 'picture': '足球小将翼日语版.jpg'},
                {'name': 'GATE奇幻自卫队', 'part': 24, 'plot': '故事描绘了20XX年，突如其来的“通往异世界的门”在东京银座出现，从中涌出来了大量怪物和军队。而陆上……',
                 'picture': 'GATE奇幻自卫队.jpg'},
                {'name': '魔法禁书目录3', 'part': 26, 'plot': '位于东京西部的巨大“学园都市”。在总人口达230万人，其中约8成是学生的这座都市中，实施着超能力开发……',
                 'picture': '魔法禁书目录3.jpg'},
                {'name': 'Q弟侦探因幡', 'part': 12, 'plot': '以前是秘密警察犬（杜伯曼犬）的主人公因幡洋是通过人工授精出生的狼男。为了寻找行踪不明的弟弟・遥而成为……',
                 'picture': 'Q弟侦探因幡.jpg'},
                {'name': '你遭难了吗', 'part': 1, 'plot': '没有家，没有食物，也没有水…… 女高中生4人组，在不知何处的无人岛上陷入遭难的大危机！ 原本是这样的……',
                 'picture': '你遭难了吗.jpg'},
                {'name': '魔术学姐', 'part': 1, 'plot': '“我和她相遇了……，和虽然可爱却很‘奇怪’的学姐！” 非常喜欢变戏法，却因为怯场而导致失败率100%……',
                 'picture': '魔术学姐.jpg'},
                {'name': '进击的巨人第三季Part.2', 'part': 10, 'plot': '为了赢得真正的胜利，调查军团决定执行夺回玛利亚之墙的作战。作战内容是利用艾伦的硬质化能力将位于玛利亚……',
                 'picture': '进击的巨人第三季Part.2.jpg'},
                {'name': '八月的棒球甜心', 'part': 11, 'plot': '又名:八月的灰姑娘棒球队 / Hachigatsu no Cinderella Nine……',
                 'picture': '八月的棒球甜心.jpg'}, {'name': '火影忍者：博人传之次世代继承者', 'part': 113, 'plot': '讲述原作的故事完结后漩涡鸣人之子漩涡博人的冒险故事……',
                                             'picture': '火影忍者：博人传之次世代继承者.jpg'},
                {'name': '弦色清音第一季邂逅乐章', 'part': 19, 'plot': '好不容易进入了大学，想要好好学习出人头地的“完美”男生李清吉，刚一入学就莫名被拐入了一个三流摇滚乐队……',
                 'picture': '弦色清音第一季邂逅乐章.jpg'},
                {'name': '恶作剧之吻', 'part': 25, 'plot': '《恶作剧之吻》是90年代少女漫画界的不巧名作，这么久的作品突然拿出来动画化，不免让人有“炒冷饭”的怀……',
                 'picture': '恶作剧之吻.jpg'},
                {'name': '亚人OAD', 'part': 3, 'plot': 'OAD动画内容为单行本第二卷收录的File:00「中村慎也事件」。《File：00 中村慎也事件》的……',
                 'picture': '亚人OAD.jpg'},
                {'name': '亚人第二季', 'part': 13, 'plot': '亚人第二季动画改编自樱井画门原作的同名漫画，讲述高中生永井圭在被卡车撞死之后却奇怪地复活了。由此，他……',
                 'picture': '亚人第二季.jpg'},
                {'name': '亚人', 'part': 13, 'plot': '导演: 濑下宽之 / 安藤裕章编剧: 濑古浩司 / 樱井画门(原作)主演: 宫野真守 / 细谷佳正 ……',
                 'picture': '亚人.jpg'},
                {'name': '复仇者集结 第二季', 'part': 7, 'plot': '惊奇漫画公司给予的标题是世上最强英雄组合原创的复仇者成员为蚁人（ant man），黄蜂侠，雷神索尔（……',
                 'picture': '复仇者集结 第二季.jpg'},
                {'name': '一弦定音', 'part': 13, 'plot': '即将废社的时濑高中筝曲社。来到只身一人的社长面前的是不良少年和他的朋友们，以及古筝的天才少女。各自各……',
                 'picture': '一弦定音.jpg'}]

        )
    return db


db = data_init()
