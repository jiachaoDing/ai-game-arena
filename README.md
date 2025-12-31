# AI Game Arena
**Visualizing LLM Coding Capabilities through Classic Games**

AI Game Arena is a benchmarking platform designed to move beyond abstract scores. It showcases the real-world coding proficiency of Large Language Models (LLMs) by having them generate fully functional, static games (e.g., Snake, Tetris) without human intervention.

---

## 1. Core Philosophy
- **Visual over Metrics**: Instead of "85 vs 90" points on a leaderboard, we use playable games to demonstrate logic and UI capabilities.
- **Authenticity (No Cherry-picking)**: We display the raw output of models, including their bugs and hallucinations, to provide a transparent look at AI performance.
- **Static & Fast**: Built on a pure static architecture (Cloudflare Pages) for instant loading and zero-latency exploration.

## 2. The Evaluation Protocol
Each model undergoes a two-stage evaluation to test both initial generation and debugging capabilities:

### Round 1: One-Shot Generation
- **Input**: A standardized system prompt (English).
- **Rule**: The model must generate the entire game in a single response.
- **Outcome**: The code is run immediately. This version is preserved as the "Initial Capability" baseline.

### Round 2: Self-Correction (Optimization)
- **Constraint**: Maximum of **3 debugging turns**.
- **Input**: Feedback is provided via console logs or visual descriptions of bugs.
- **Success Criteria**: If the game becomes functional within 3 turns, it is marked as `Fixed`. Otherwise, it is marked as `Failed`.

---

## 3. System Architecture & UI
### 3.1 Tech Stack
- **Styling**: Tailwind CSS v4.0 (CSS-first setup).
- **Interactivity**: Alpine.js (Lightweight state management).
- **Metadata**: Driven by a central `data/games.json` file.

### 3.2 Key Pages
- **Home**: Showcases the "Hall of Fame" (Perfect One-Shots) and "Wall of Shame" (Logical Failures).
- **Game Hub**: Displays all models tested for a specific game, including their status (`Pass`, `Fixed`, or `Failed`).
- **Playroom (Detail Page)**: A dynamic template (`play.html`) that uses URL parameters to load specific model versions in an `<iframe>`. Includes a version toggle to switch between Round 1 and Round 2 code.

---

## 4. Project Structure
```text
/
├── data/games.json       # Central metadata (Model status, file paths)
├── prompts/              # Standardized prompts for each game
├── games/                # Generated HTML artifacts
│   ├── play.html         # Universal detail page template
│   └── [game-name]/      # index.html (List) + gpt4o-r1.html, etc.
├── src/input.css         # Tailwind v4 theme configurations
└── dist/output.css       # Compiled production CSS
```

## 5. Design System
The project follows a **Minimalist & Modern** aesthetic:
- **Rating System**: 
  - `Pass` (Green): Perfect One-shot.
  - `Fixed` (Yellow): Resolved within Round 2.
  - `Failed` (Red): Non-functional after 3 tries.
- **Dark Mode**: Fully supported via Tailwind v4 CSS variables and Alpine.js persistence.
