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
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        # 添加一些自定义的上下文变量
        context = {
            'build_date_utc': datetime.utcnow(),
            'version': '1.0.0',
            'analytics_id': os.environ.get('ANALYTICS_ID', '')
        }
        try:
            return render_template('index.html', **context)
        except:
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

if __name__ == '__main__':
    # 生产环境配置
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)