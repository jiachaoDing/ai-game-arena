# 📂 Project Structure - After Template System Implementation

## 🌳 Directory Tree

```
ai-game-arena/
│
├── 📁 assets/                      # Static assets
│   ├── logo/                       # AI model logos
│   │   ├── chatgpt.svg
│   │   ├── claude.svg
│   │   ├── deepseek.svg
│   │   ├── gemini.svg
│   │   ├── grok.svg
│   │   ├── kimi.svg
│   │   ├── qingyan.svg
│   │   └── qwen.svg
│   └── screenshots/                # Project screenshots
│
├── 📁 data/                        # ⭐ Configuration data
│   └── games.json                  # All game metadata & models (ENHANCED)
│
├── 📁 dist/                        # Build output
│   └── output.css                  # Compiled Tailwind CSS
│
├── 📁 games/                       # ⭐ Game implementations
│   │
│   ├── game-template.html          # 🆕 Base template (reference)
│   ├── TEMPLATE_USAGE.md           # 🆕 Template usage guide (EN)
│   │
│   ├── 📁 snake/                   # Snake game
│   │   ├── index.html              # 🔄 Updated to use template
│   │   ├── deepseek-v3.2-r1.html   # Model implementations
│   │   ├── glm-4.7-r1.html
│   │   ├── gpt-5.2-r1.html
│   │   ├── grok-code-fast-v1-r1.html
│   │   ├── kimi-k2-r1.html
│   │   ├── qwen3-Max-r1.html
│   │   ├── qwen3-Max-r2.html
│   │   └── sonnet-4.5-r1.html
│   │
│   └── play.html                   # Game player page
│
├── 📁 node_modules/                # NPM dependencies
│
├── 📁 prompts/                     # AI prompts
│   └── snake.md                    # Snake game prompt
│
├── 📁 src/                         # Source files
│   └── input.css                   # Tailwind input CSS
│
├── 📄 create_files.py              # 🔄 Auto-add models (UPDATED)
├── 📄 update_json.py               # 🔄 Update models (UPDATED)
│
├── 📄 index.html                   # Main landing page
├── 📄 package.json                 # NPM config
├── 📄 package-lock.json            # NPM lock file
│
├── 📄 EvaluationParticipant.md     # Evaluation guide
├── 📄 LICENSE                      # License file
├── 📄 README.md                    # Main README
├── 📄 SETUP.md                     # Setup instructions
└── 📄 PROJECT_STRUCTURE.md         # 🆕 This file
```


## 🔄 Workflow

### Adding a New Game

```
1. Edit data/games.json
   └─> Add game configuration
       
2. Create directory
   └─> mkdir games/your-game
       
3. Copy template
   └─> cp games/snake/index.html games/your-game/
       
4. Add model files
   └─> games/your-game/model-r1.html
       
5. Run script
   └─> python create_files.py
       
6. Done!
   └─> Access at /games/your-game/
```

### Adding a New Model

```
1. Add HTML file
   └─> games/game-name/model-name-r1.html
       
2. Edit create_files.py
   └─> GAME_ID = "game-name"
       
3. Run script
   └─> python create_files.py
       
4. Done!
   └─> Model appears on game page
```

### Adding Your First Game
```bash
# 1. Edit data/games.json
# 2. Create directory
mkdir games/my-game

# 3. Copy template
cp games/snake/index.html games/my-game/

# 4. Add your model files
# (place HTML files in games/my-game/)

# 5. Run script
# (edit create_files.py: GAME_ID = "my-game")
python create_files.py

# 6. Visit
http://localhost:8000/games/my-game/
```