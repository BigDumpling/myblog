# myblog
1. 新建项目
django-admin startproject myblog

2. 新建app
python3 manage.py startapp blog

3. 虚拟环境
virtualenv venv -p python3

4. 启用虚拟环境
source venv/bin/activate

5. 生成迁移文件：
python manage.py makemigrations appname

6. 同步到数据库中：
python manage.py migrate appname filename

7. 数据库逆向到Model:
python manage.py inspectdb