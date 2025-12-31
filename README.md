# AI Game Arena (AI 静态游戏竞技场)

**—— Visualizing LLM Coding Capabilities through Games**

- **版本号**: v1.2
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

### 2.1 评测流程 (The Protocol)

每个游戏项目（如“贪吃蛇”）都经历两轮测试：

- **Round 1: One-Shot (一命通关)**
  - **输入**: 统一的标准 Prompt（英文）。
  - **规则**: AI 输出代码后直接运行。
  - **展示**: 无论成败，保留该版本作为“初始能力”证据。
- **Round 2: Optimization (三次修复)**
  - **定义更新**: 不再局限于一次修复，允许进行 **“3轮对话以内的调试”**。
  - **输入**: 将错误信息 (Console Logs) 或视觉描述反馈给 AI。
  - **规则**: 如果在3次对话内修复成功，则视为 Round 2 成功；否则判定为最终失败。
  - **展示**: 展示最后一次生成的代码版本。

------

## 3. 页面详细设计 (Detailed UI) - *[新增]*

### 3.1 首页 (Home - The Showcase)

首页不再罗列所有游戏，而是展示**最具代表性**的内容，吸引用户点击。

- **Hero Section**: 标语 + 随机展示一个“完美运行”的游戏（可交互）。
- **Hall of Fame (红榜)**:
  - 标题：“本周代码之神”
  - 内容：展示 3 个在 Round 1 就完美运行的模型案例（GIF 预览 + 链接）。
- **Wall of Shame (黑榜)**:
  - 标题：“人工智障时刻”
  - 内容：展示逻辑最离谱的失败案例（如：贪吃蛇把自己吃掉、俄罗斯方块只有长条）。
- **Game Index**: 所有已评测游戏入口（Snake, Pong, Tetris...）。

### 3.2 游戏列表页 (games Hub - e.g., /games/snake/)

用户想看“贪吃蛇”这一关，各家模型的表现概览。

- **Prompt Zone (置顶)**:
  - 以代码块形式展示该游戏使用的**完整 Prompt**。
  - *文案*: "Tested with the following prompt stored in `/prompts/snake.md`"
- **Model Grid (卡片墙)**:
  - 每个卡片代表一个 AI 模型。
  - **封面**: 游戏的静态截图（或 GIF）。
  - **标签**:
    - `GPT-4o` (模型名)
    - `🏆 Godlike` / `✨ Redeemed` (评级)
    - `3 Tries` (Round 2 修复次数，如果是 R1通过则不显示)
  - **点击行为**: 跳转到 `/games/snake/gpt4o/`。


 ### 3.3 模板页（模型详情页） (/games/play.html):
    这是一个“空壳”页面，从对应游戏的列表页跳转过来。
    Alpine.js 在初始化时读取 URL 中的 ?game=snake&model=gpt4o。
    然后去 fetch /data/games.json，找到对应的数据。
    最后动态把 <iframe src="..."> 和标题渲染出来。 
    同时这也是这是用户停留时间最长的页面，用于交互体验。
- **Header**:
  - `Title`: GPT-4o's Implementation
- **Control Bar (顶部工具栏)**:
  - **Version Toggle (核心功能)**: 一个类似 iOS 的分段控制器 (Segmented Control)。
    - `[ Round 1 (Initial) ]` -- `[ Round 2 (Fixed) ]`
    - *交互逻辑*: 点击切换，下方的 Iframe `src` 瞬间改变，页面无刷新。
    - *状态*: 如果该模型不需要 Round 2（一次通关），则 R2 按钮置灰并提示“一次过，无需修复”。
- **Main Stage**:
  - `<iframe src="/games/snake/xxx-v1.html" class="w-full h-[600px]"></iframe>`
- **Info Sidebar / Bottom Sheet**:
  - **Prompt Used**: 再次链接到 Prompt 文件。
  - **Modification Logs**: (如果是 Round 2) 简要说明修复了什么，例如 "Fixed syntax error in line 45"。
  - **Download**: "Download HTML" 按钮。


------

## 4. 文件与数据结构 (File System) - *[关键]*

为了支持上述功能，你需要一个清晰的文件命名规范。

### 4.1 目录结构

Plaintext

```
/
  /assets
    /screenshots      # 列表页用的预览图
  /prompts
    snake.md          # 存放贪吃蛇的原始 Prompt
    tetris.md
  /games            # 存放生成的 HTML 产物
    play.html        # template 用于加载对应模型生成的某个游戏页面
    /snake
      index.html      # 游戏列表页  /games/snake/会跳转这里
      gpt4o-r1.html   # Round 1 代码
      gpt4o-r2.html   # Round 2 代码 (如果有)
      deepseek-r1.html
      deepseek-r2.html
    /tetris
      ...
  /data
    games.json        # 核心元数据（驱动列表页生成）
  /
```

### 4.2 元数据设计 (`games.json`)

我们不需要复杂的数据库，用一个 JSON 文件来管理所有页面的生成逻辑（如果你使用静态生成器或通过 JS 渲染）。

JSON

```
{
  "snake": {
    "title": "Retro Snake",
    "prompt_file": "/prompts/snake.md",
    "models": [
      {
        "id": "gpt4o",
        "name": "GPT-4o",
        "status": "Godlike",
        "r1_file": "/games/snake/gpt4o-r1.html",
        "r2_file": null,  // null 代表没有 r2，一次通关
        "notes": "Perfect execution."
      },
      {
        "id": "llama3",
        "name": "Llama 3 70B",
        "status": "Redeemed",
        "r1_file": "/games/snake/llama3-r1.html",
        "r2_file": "/games/snake/llama3-r2.html",
        "notes": "Fixed boundary collision bug after 2 tries."
      }
    ]
  }
}
```

------

## 5. 技术实现细节 (Implementation Notes)

### 5.1 Alpine.js 实现切换逻辑 (详情页)

在详情页中，使用 Alpine.js 实现极简的 R1/R2 切换：

HTML

```
<div x-data="{ version: 'r1' }" class="container mx-auto">

  <div class="flex justify-center space-x-4 my-4">
    <button 
      @click="version = 'r1'" 
      :class="version === 'r1' ? 'bg-blue-600 text-white' : 'bg-gray-200'"
      class="px-4 py-2 rounded">
      Round 1 (Raw)
    </button>
    
    <button 
      @click="version = 'r2'" 
      :class="version === 'r2' ? 'bg-green-600 text-white' : 'bg-gray-200'"
      class="px-4 py-2 rounded">
      Round 2 (Fixed)
    </button>
  </div>

  <div class="border-4 border-gray-800 rounded-lg overflow-hidden">
    <iframe 
      :src="`/games/snake/deepseek-${version}.html`" 
      class="w-full h-[600px] bg-black"
      sandbox="allow-scripts allow-same-origin">
    </iframe>
  </div>

</div>
```

------

## 6. 下一步行动 (Action Items Update)

1. **准备数据**: 创建 `prompts/snake.md`，并将你目前的测试 Prompt 写入。
2. **构建列表页**: 使用 HTML 模板或 JS 读取 `games.json` 渲染“贪吃蛇”下的所有 AI 卡片。
3. **构建详情页**: 制作一个通用模板 `template.html`，可以通过 URL 参数（或静态生成的目录结构）加载不同的 iframe。

