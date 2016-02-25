# 简陋的留言板

### Flask框架练手项目

    Web框架: Flask
    模版: Flask-Bootstrap
    表单: Flask-WTF
    数据库: SQLite
    ORM: Flask-SQLAlchemy

### 练习要点

Flask: 普通路由,渲染模版,错误处理路由,带变量的路由,路由到模版的变量传递

Flask-Bootstrap: 模版继承,HTML基础标签用法,嵌入if,for语句,宏,导入wtf,宏,css

Flask-WTF: 创建,提交,验证表单,表单提示

Flask-SQLAlchemy: 数据库概念,设计数据模型,设置1对多表间关系,取值,查询,过滤

Flask-Script: 命令行管理工具,集成命令行命令,管理运行,单元测试,数据库调试

Flask-Migrate: 数据库迁移工具,检测数据库变化并更新

重构到大型项目的结构: 各组件间的相互导入,工厂函数和蓝本的引入,单元测试的用法

## 功能

* 用户登陆,用户注册
* 首页显示留言列表
* 登陆后可以添加留言
* 用户页面可以查看自己的留言

