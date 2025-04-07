
# 元话 RWA 课程学习平台 (Yuanhua RWA Course Learning Platform)

## 项目概述 (Project Overview)

这是元话 RWA（Real World Assets）课程学习平台，旨在提供全面的 RWA 知识和学习资源，帮助学员深入了解实物资产代币化及其应用场景。

This is the Yuanhua RWA (Real World Assets) course learning platform, designed to provide comprehensive RWA knowledge and learning resources to help students understand real-world asset tokenization and its application scenarios.

## 功能特点 (Features)

- 模块化课程内容 (Modular course content)
- 互动式学习体验 (Interactive learning experience)
- 集成 Cloudflare 服务的高性能架构 (High-performance architecture integrated with Cloudflare services)
- 响应式设计，支持多设备访问 (Responsive design supporting multiple devices)

## 技术栈 (Tech Stack)

- **前端**: MkDocs, Material for MkDocs
- **后端**: Flask, Python
- **部署**: Cloudflare Pages, Cloudflare Workers
- **CI/CD**: GitHub Actions

## 本地开发 (Local Development)

1. 安装依赖 (Install dependencies):
```bash
pip install mkdocs mkdocs-material flask gunicorn
```

2. 启动开发服务器 (Start development server):
```bash
mkdocs serve
```

3. 构建静态站点 (Build static site):
```bash
mkdocs build
```

## 项目结构 (Project Structure)

```
.
├── docs/               # 课程内容 (Course content)
├── workers-site/       # Cloudflare Workers 配置 (Cloudflare Workers configuration)
├── app.py              # Flask 应用 (Flask application)
├── base_template.html  # 基础模板 (Base template)
├── mkdocs.yml          # MkDocs 配置 (MkDocs configuration)
├── wrangler.toml       # Cloudflare Workers 配置 (Cloudflare Workers configuration)
└── _headers            # Cloudflare Pages 请求头配置 (Cloudflare Pages headers configuration)
```

## 部署 (Deployment)

本项目使用 GitHub Actions 自动部署到 Cloudflare Pages 和 Cloudflare Workers。每次推送到 main 分支都会触发自动部署流程。

This project uses GitHub Actions to automatically deploy to Cloudflare Pages and Cloudflare Workers. Each push to the main branch triggers the automatic deployment process.

## 贡献指南 (Contribution Guidelines)

欢迎对本项目进行贡献！请遵循以下步骤：

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启一个 Pull Request

## 联系方式 (Contact)

如有任何问题或建议，请通过以下方式联系我们：
- 邮箱 (Email): [your-email@example.com]
- 网站 (Website): [your-website.com]

## 许可证 (License)

本项目采用 [选择适当的许可证] 许可证 - 查看 LICENSE 文件了解详情。
