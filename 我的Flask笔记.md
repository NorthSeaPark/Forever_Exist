# 我的Flask笔记

1. 1 搭建环境

   （1）创造一个文件夹

   （2）在文件夹内，创建一个运行环境，py -m venv env

   （3）使用command: env\Scripts\activate

     (4) 在这个环境内安装Flask

   （5）cls 可以清除终端所有烦人的代码

   （6）在你搭建的环境上，set FLASK_APP = app.py

   ​		set FLASK_APP = 你的主程序名称

   （7）flask run，启动服务器

   

   1.2 路由的交互

   （1）用户在浏览器输入URL

   （2）Flask接受请求并分析请求的URL

   （3）为这个URL找到对应的处理函数

   （4）执行函数并生成相应，返回给浏览器

   （5）浏览器接受并解析相应，将信息显示在页面中

   

   1.3 URL

   ​	（1）“/“ 对应的是根地址

   ​	（2）app.route() 是把地址和函数绑定在一起

   ​	（3）改变端口到8000 ：flask run --port=8000

   ​	（4）Debug模式： set FLASK_ENV=development

   

   



