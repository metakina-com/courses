
from flask import Flask, render_template, send_from_directory, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__, static_folder='site', template_folder='site')

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

if __name__ == '__main__':
    # 确保端口对外可访问
    app.run(host='0.0.0.0', port=5000, debug=True)
