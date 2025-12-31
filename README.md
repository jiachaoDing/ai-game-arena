# AI Game Arena (AI 静态游戏竞技场)

**—— Visualizing LLM Coding Capabilities through Games**

- **版本号**: v1.0
- **项目代号**: `static-arena`
- **核心理念**: 拒绝枯燥跑分，用游戏直观展示 AI 编程能力。拒绝人工修饰，展示最真实的代码现场。

------

## 1. 项目背景与愿景 (Executive Summary)

### 1.1 痛点分析

- 目前的 AI 编程榜单（如 HumanEval, SweetBench）只有冷冰冰的分数，普通用户无法感知 "85分" 和 "90分" 的区别。
- 现有的代码生成演示往往经过人为修改（Cherry-picking），掩盖了模型真实的“幻觉”和 bug。
- 用户缺乏一个“所见即所得”的游乐场，直接体验 AI 生成的游戏。

### 1.2 核心价值

- **可视化 (Visual)**: 通过“贪吃蛇”、“俄罗斯方块”等经典游戏，一眼看出模型逻辑能力的差异。
- **真实性 (Authentic)**: 严格执行“无人工干预”原则，通过 **Round 1 (初生成)** 和 **Round 2 (自修复)** 的对比，展示模型的真实水平。
- **极速体验 (Static)**: 基于 Cloudflare Pages 的纯静态架构，秒开，无需等待生成。

------

## 2. 核心玩法与规则 (Core Mechanics)

这是本项目的灵魂，必须严格遵守标准化的评测流程 (SOP)。

### 2.1 评测流程 (The Protocol)

每个游戏项目（如“贪吃蛇”）都经历两轮测试：

- **Round 1: One-Shot (一命通关)**
  - **输入**: 统一的标准 Prompt（英文）。
  - **规则**: 直接保存生成的 HTML。如果跑不起来，就展示黑屏或报错界面。
  - **目的**: 测试模型的“一次性交付能力”。
- **Round 2: Self-Correction (自我救赎)**
  - **触发条件**: 仅当 Round 1 存在 Bug 或无法运行时进行。
  - **输入**: 将浏览器的 Console Error 或简短的视觉反馈（如“蛇不会动”）喂回给同一个 AI。
  - **规则**: 允许 AI 进行一次自我修复。
  - **目的**: 测试模型的“反思与Debug能力”。

### 2.2 评测等级 (The Ranking System)

在页面上为每个模型打上标签：

| **等级标签**       | **颜色** | **描述**                                               |
| ------------------ | -------- | ------------------------------------------------------ |
| **🏆 Godlike**      | 金色     | Round 1 完美运行，无需修复。                           |
| **✨ Redeemed**     | 蓝色     | Round 1 失败，但 Round 2 修复成功（浪子回头）。        |
| **🤡 Hallucinated** | 黄色     | 虽然能跑，但逻辑诡异（如贪吃蛇会穿墙，球会飞出屏幕）。 |
| **💀 Dead**         | 红色     | Round 2 依然无法运行，彻底失败。                       |

------

## 3. 功能架构与页面设计 (Feature & UI)

### 3.1 网站结构图 (Sitemap)

Plaintext

```
/ (首页)
  ├── Hero Section (Slogan + 热门对决)
  ├── Game Gallery (游戏列表：贪吃蛇, 俄罗斯方块, 粒子效果...)
  └── About (评测标准说明)

/games/snake (贪吃蛇详情页 - 核心战场)
  ├── Prompt Zone (展示使用的提示词)
  ├── Control Panel (模型筛选器)
  └── Battle Grid (游戏展示网格)
```

### 3.2 核心页面交互设计

#### A. 详情页 (The Battle Arena)

这是最复杂的页面，建议采用 **“模型卡片” (Model Card)** 设计。

- **布局**: 响应式网格（桌面端一行 3 个，移动端一行 1 个）。
- **单张卡片结构**:
  - **Header**: 模型名称 (e.g., DeepSeek V3) + 厂商 Logo。
  - **Viewport (iFrame)**: 这是一个 `iframe` 窗口，直接加载静态 HTML 文件。
    - *默认加载*: `snake-deepseek-v1.html`
  - **Footer (控制器)**:
    - **状态标签**: 显示 🏆 Godlike 或 💀 Dead。
    - **Toggle Switch (切换开关)**: `[ v1.0 Original ]` <--> `[ v2.0 Fixed ]`
      - *交互*: 点击切换时，iframe 的 `src` 发生变化，让用户直观看到修复前后的对比。
    - **Action**: "View Code" (点击弹窗显示源码/下载)。

#### B. 首页 (Showcase)

- **特色栏目**: "Fail of the Week" (本周最佳翻车)。
  - 展示一个 Llama 3 把贪吃蛇写成直线的截图，增加趣味性和传播度。

------

## 4. 技术架构 (Technical Stack)

为了符合你的“纯前端”和“低成本”需求：

- **基础设施**: Cloudflare Pages (免费、无限流量、全球 CDN)。

- **前端框架**: **Alpine.js** + **Tailwind CSS** + **HTML5**。

  - *理由*: Alpine.js 非常轻量，足够处理“点击切换 v1/v2”这种简单的交互，不需要引入 React/Vue 的构建复杂度。

- 文件存储结构 (关键):

  你需要设计一个清晰的目录结构来管理成百上千个 HTML 文件。

  Plaintext

  ```
  /public
    /battles
      /snake
        /gpt4o-v1.html
        /gpt4o-v2.html
        /deepseek-v1.html
        /deepseek-v2.html
      /tetris
        /...
    /index.html
    /snake.html (主评测页)
  ```

- 沙箱隔离 (Sandbox):

  所有的游戏必须运行在 <iframe> 中，并且加上 sandbox="allow-scripts" 属性。

  - *防止*: AI 生成的恶意代码（如死循环）卡死你的主网站。CSS 样式也不会互相污染。

------

## 5. 内容生产 SOP (Content Production)

这是你作为“站长”的日常工作流程。

1. **选题**: 确定本期题目（如：Flappy Bird）。
2. **定 Prompt**: "Write a Flappy Bird game in a single HTML file..."
3. **批量生成**:
   - 打开 5 个浏览器窗口：ChatGPT, Claude, Gemini, DeepSeek, Meta.ai。
   - 同时发送 Prompt。
4. **保存 v1**:
   - 将代码复制到 VS Code，保存为 `flappy-gpt4-v1.html` 等。
   - 本地打开测试。
5. **生成 v2 (如果需要)**:
   - 如果有 Bug，把报错贴回给 AI。
   - 保存修复后的代码为 `flappy-gpt4-v2.html`。
6. **部署**: `git push` 到 Cloudflare。

------

## 6. 推广文案示例 (Marketing)

- **标题**: "全网首个 AI 惨案现场：DeepSeek 写的贪吃蛇把自己吃掉了？"
- **副标题**: "我们测试了 7 个顶尖模型，只有 2 个一次通关。点击查看它们生成的真实代码。"
- **Twitter/X 内容**: 放一个 GIF 动图，左边是 GPT-4 流畅运行，右边是 Llama 3 疯狂报错闪屏。配文："Expectation vs Reality. #AI #Coding"

------

## 7. 下一步行动 (Action Items)

1. **Day 1**: 搭建基础 HTML 框架，配置 Tailwind 和 Alpine.js。
2. **Day 2**: 完成第一期内容 "Snake (贪吃蛇)" 的生成和文件整理（包含 v1 和 v2）。
3. **Day 3**: 编写首页和详情页代码，实现 iframe 的切换逻辑。
4. **Day 4**: 上线 Cloudflare Pages，在 V2EX 或 Twitter 发布。