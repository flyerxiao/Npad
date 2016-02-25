# 简陋的留言板

---

## 练手项目

### 界面

    Bootstrap 和 wtf 渲染界面,SQLAlchemy提供分页

- 导航条

    引入基础模版,自定义模版
 
- 留言框

    留言表单

- 留言列表

    查询和循环 实现 显示全部留言列表

- 留言分页

    分页宏 实现 留言列表分页

- 页面分离

    修改首页,添加留言页面,微调模版

- 添加错误处理页面

    增加处理404,500页面

- 用户登陆

    登陆表单,login页面

- 用户注册

    注册表单,register页面

- 用户页面,留言页面

    用户页面显示自己的留言列表,留言页面改为登陆后显示

### 功能

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

- 页面分离

    增加留言路由,修改首页路由

- 错误处理

    增加404,500路由

- 用户登陆

    Flask-Login提供主要功能,Flask-wtf登陆表单,修改User模型引入密码设置和验证,增加登陆路由

- 用户注册

    Flask-wtf注册表单,增加注册路由

- 用户页面,留言页面

    用户页面,增加用户路由,修改留言路由判断是否登陆


未解决:用户页分页问题