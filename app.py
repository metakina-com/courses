from flask import Flask, render_template, send_from_directory, redirect, url_for, request
import os
from werkzeug.middleware.proxy_fix import ProxyFix
from datetime import datetime

app = Flask(__name__, static_folder='site', template_folder='site')
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

# 缓存控制
@app.after_request
def add_header(response):
    # 静态资源缓存1周
    if request.path.startswith('/assets/'):
        response.cache_control.max_age = 60 * 60 * 24 * 7  # 7天
    # HTML页面不缓存
    elif response.mimetype == 'text/html':
        response.cache_control.no_cache = True
        response.cache_control.no_store = True
        response.cache_control.must_revalidate = True
    return response

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    # 尝试直接提供静态文件
    static_file_path = os.path.join(app.static_folder, path)
    if path != "" and os.path.exists(static_file_path) and not os.path.isdir(static_file_path):
        return send_from_directory(app.static_folder, path)
    
    # 尝试提供目录的索引文件
    index_path = os.path.join(app.static_folder, path, 'index.html')
    if os.path.exists(index_path):
        return send_from_directory(os.path.join(app.static_folder, path), 'index.html')
    
    # 添加自定义上下文变量
    context = {
        'build_date_utc': datetime.utcnow(),
        'version': '1.0.0',
        'analytics_id': os.environ.get('ANALYTICS_ID', '')
    }
    
    # 尝试渲染主模板
    try:
        return render_template('index.html', **context)
    except Exception as e:
        print(f"模板渲染错误: {e}")
        # 回退到静态主页
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/course-progress')
def course_progress():
    # 这里可以添加用户进度追踪API
    # 在实际应用中，你需要添加用户认证和数据库交互
    return {
        'modules': {
            'module1': {'completed': True, 'progress': 100},
            'module2': {'completed': False, 'progress': 60},
            'module3': {'completed': False, 'progress': 30},
            'module4': {'completed': False, 'progress': 0}
        },
        'total_progress': 47.5
    }

# 添加SEO有利的站点地图路由
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('site', 'sitemap.xml')

# 添加健康检查端点
@app.route('/health')
def health_check():
    return {"status": "ok"}, 200
    
@app.errorhandler(404)
def page_not_found(e):
    # 尝试提供自定义的404页面
    try:
        return send_from_directory(app.static_folder, '404/index.html'), 404
    except:
        return "页面未找到", 404

if __name__ == '__main__':
    # 生产环境配置
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=debug_mode)