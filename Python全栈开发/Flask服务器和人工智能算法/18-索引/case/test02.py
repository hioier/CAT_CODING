import config

# 若没有初始化数据库，则初始化，若已初始化，则什么都不做
config.init_db()
# 获取数据库
db = config.get_db()

# 在下方写你的代码：在字段sno上创建唯一索引，降序
db.student.create_index([('sno', -1)], unique=True)

# 已知集合中存在学号 050306007990 的文档
stu = {'name': '乔布斯', 'gender': 'male', 'school': '北京市第二实验小学', 'grade': '3年级', 'class': '3班', 'age': 9,
       'sno': '050306007990'}
# 在下方写你的代码：再插入相同学号的文档，观察结果
db.student.insert_one(stu)
