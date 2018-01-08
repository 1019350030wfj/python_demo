# -*-coding:utf-8-*-

'''

==============http://flask.pocoo.org/docs/0.12/quickstart/#quickstart================
# 调试模式

    1、app.run（）方法启动一个本地开发服务器，但是每次修改源码
    2、app.run(debug=True) 打开调试模式，那么服务器会在修改应用之后重启

   ## 注意：
    绝对不能在生成环境中使用调试器

# 路由

    @ap.route('/')
    def index():
        return 'Index Page'

    route（）装饰器用于把一个函数绑定到一个URL

# 变量规则

    通过把URL的一部分标记为<variable_name>就可以在URL中添加变量。
    @app.route('/user/<username>')
    def show_user_profile(username):
        return 'User %s' % username

    使用<converter:variable_name>,加上一个转换器
    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        return 'Post %d' % post_id

    现有的转换器有：
    int 接受整数
    float 接受浮点数
    path 和缺省情况相同，但也接受斜杠

# 唯一的URL / 重定向行为：

    @app.route('/project/')
        这是路径末尾有斜杠， 当你访问的时候没有写末尾斜杠，/project。flask会帮你自动填上
    @app.route('/about')
        这是路径末尾没有斜杠的， 当你访问的时候/about/，则服务器会返回 Not Found 404错误


# 构建URL

    通过url_for()函数，把函数名称作为它的第一个参数。没有使用硬编码来构建url。好处有三点：
        1、当url有变化的时候，我们只需要改一个地方
        2、url_for()可以帮我们处理特殊字符的转义和Unicode编码数据
        3、当我们应用放在/application 而不是/，url_for()会帮我们处理它

# http 方法

    默认route（）只响应GET请求。 可以通过 @app.route('/login',methods=['GET','POST'])

# 静态文件

    通常在我们项目的模块下面新建一个static。访问静态文件：
    url_for('static', filename='style.css')


# 渲染模版

    flask使用Jinja2模版引擎。为了渲染一个模版，可以使用render_template()方法来渲染模版
    flask会在templates文件夹下寻找模版


==============http://flask.pocoo.org/docs/0.12/quickstart/#quickstart================

'''