# 简陋的留言簿

---

## 练手项目

### 1.	界面

    Bootstrap 和 wtf 渲染界面

- 导航条

    Flask-Bootstrap 实现
 
- 留言框

    Flask-wtf 实现
 
- 留言框

    wtf 实现 文本框，提交按钮

- 留言列表

    list和循环 实现 显示全部留言列表

- 留言分页

    分页宏 实现 留言列表分页

### 2.	功能

       SQLAlchemy 储存 文章

- 初始化数据库

    Flask-SQLalchemy

- 定义数据模型

    Message 模型

- 创建数据库

    导入Script 用 shell 命令实现

- 视图操作数据库

    用 if 判断是否存在相同后,用 db.session.add() 添加记录

- 留言列表

    用 query.order_by().all() 查询并传入模版渲染

- 留言分页显示

    用 query.order_by().paginate() 实现分页