
from flask import Flask, render_template, redirect, url_for, request, send_from_directory
import os
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

# Serve MkDocs static files
@app.route('/')
@app.route('/<path:path>')
def serve_docs(path=''):
    if path == '':
        return send_from_directory('site', 'index.html')
    return send_from_directory('site', path)

# Add Cloudflare Web Analytics
@app.context_processor
def inject_cf_analytics():
    return {
        'cf_analytics_token': os.environ.get('CF_ANALYTICS_TOKEN', '')
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
