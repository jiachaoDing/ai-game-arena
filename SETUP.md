# AI Game Arena - 项目设置指南

## 快速开始

### 1. 安装依赖

```bash
npm install
```

### 2. 编译 CSS

**一次性编译：**
```bash
npm run build:css
```

**开发模式（自动监听）：**
```bash
npm run dev
```

### 3. 预览网站

使用任何静态服务器打开 `index.html`，例如：

```bash
# 使用 Python
python -m http.server 8000

# 使用 Node.js (需要安装 http-server)
npx http-server -p 8000

# 使用 VS Code Live Server 扩展
# 右键 index.html -> Open with Live Server
```

然后在浏览器中访问 `http://localhost:8000`

---

## 项目结构

```
ai-game-arena/
├── assets/
│   └── screenshots/          # 游戏截图
├── battles/                  # AI 生成的游戏 HTML
│   └── snake/
│       ├── gpt4o-r1.html
│       ├── deepseek-v3-r1.html
│       ├── deepseek-v3-r2.html
│       └── claude-3-opus-r1.html
├── data/
│   └── games.json           # 游戏元数据
├── dist/
│   └── output.css           # 编译后的 Tailwind CSS（自动生成）
├── prompts/
│   └── snake.md             # 标准 Prompt
├── src/
│   └── input.css            # Tailwind v4.0 CSS-First 配置
├── index.html               # 首页
├── detail-template.html     # 详情页模板
└── package.json
```

---

## 技术栈

- **CSS 框架**: Tailwind CSS v4.0 (CSS-First Setup)
- **JavaScript 库**: Alpine.js (CDN)
- **部署**: Cloudflare Pages / GitHub Pages / Netlify

---

## 添加新游戏

### 1. 准备文件

1. 在 `prompts/` 下创建新的 Prompt 文件（如 `tetris.md`）
2. 在 `battles/` 下创建游戏目录（如 `battles/tetris/`）
3. 添加 AI 生成的 HTML 文件

### 2. 更新元数据

编辑 `data/games.json`，添加新游戏条目：

```json
{
  "tetris": {
    "title": "Tetris",
    "prompt_file": "/prompts/tetris.md",
    "description": "The classic block-stacking game.",
    "icon": "🧱",
    "models": [
      {
        "id": "gpt4o",
        "name": "GPT-4o",
        "status": "Godlike",
        "r1_file": "/battles/tetris/gpt4o-r1.html",
        "r2_file": null,
        "notes": "Perfect implementation.",
        "tries": 1
      }
    ]
  }
}
```

### 3. 刷新页面

重新打开 `index.html`，新游戏会自动显示在首页。

---

## 设计原则

### 极简主义 (Minimalist)
- 大量留白和内边距
- 避免视觉杂乱

### 优雅 (Elegant)
- 深色调色板（Deep Slate/Navy）
- 高质量排版（Inter + JetBrains Mono）

### 现代 (Modern)
- 玻璃态效果和柔和渐变
- 避免硬边框

---

## Tailwind CSS v4.0 注意事项

本项目使用 Tailwind v4.0 的 **CSS-First Setup**：

- ✅ 使用 `@import "tailwindcss";`
- ✅ 使用 `@theme` 指令配置主题
- ✅ 使用 Standard CLI 编译
- ❌ **不使用** `tailwind.config.js`
- ❌ **不使用** 旧的 `@tailwind` 指令

### 自定义主题变量

所有主题配置都在 `src/input.css` 的 `@theme` 块中：

```css
@theme {
  --color-bg-main: #0f172a;
  --color-accent: #38bdf8;
  --font-sans: "Inter", system-ui, sans-serif;
}
```

---

## 部署

### Cloudflare Pages

1. 连接 GitHub 仓库
2. 构建命令：`npm run build:css`
3. 输出目录：`/`（根目录）

### GitHub Pages

```bash
npm run build:css
git add .
git commit -m "Build CSS"
git push origin main
```

在仓库设置中启用 GitHub Pages，选择 `main` 分支的根目录。

---

## 常见问题

### Q: CSS 没有生效？
A: 确保运行了 `npm run build:css`，并且 `dist/output.css` 文件已生成。

### Q: Alpine.js 不工作？
A: 检查浏览器控制台是否有错误，确保 CDN 链接正常加载。

### Q: 如何修改颜色主题？
A: 编辑 `src/input.css` 中的 `@theme` 块，然后重新编译 CSS。

---

## License

MIT

