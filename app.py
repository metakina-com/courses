
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='site', template_folder='site')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    # 确保端口对外可访问
    app.run(host='0.0.0.0', port=5000)
