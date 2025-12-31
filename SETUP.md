# AI Game Arena - Setup Guide

## Quick Start

### 1. Install Dependencies
```bash
npm install
```

### 2. Compile CSS
**Production Build:**
```bash
npm run build:css
```

**Development Mode (Watch):**
```bash
npm run dev
```

### 3. Local Preview
Serve `index.html` using any static server:
```bash
# Using Node.js
npx http-server -p 8000

# Using Python
python -m http.server 8000
```
Access the site at `http://localhost:8000`.

---

## Content Management Workflow

### Adding a New Game Evaluation
1. **Prepare Prompt**: Create a prompt file in `prompts/[game].md`.
2. **Generate Code**: Run the prompt through the target LLM.
3. **Save Artifacts**: Place the generated HTML in `games/[game]/[model]-r1.html`.
4. **Update Metadata**: Edit `data/games.json` to register the new entry:
   ```json
   {
     "game-id": {
       "title": "Game Title",
       "models": [
         {
           "id": "model-id",
           "name": "Model Name",
           "status": "Pass",
           "r1_file": "/games/[game]/[model]-r1.html",
           "r2_file": null,
           "tries": 1
         }
       ]
     }
   }
   ```

---

## Technical Architecture Notes

### Tailwind CSS v4.0 (CSS-First)
This project utilizes the latest Tailwind v4.0 features:
- **No `tailwind.config.js`**: All configurations are handled within `src/input.css` using the `@theme` block.
- **Direct Imports**: Uses `@import "tailwindcss";`.
- **Custom Variables**: Theme colors (e.g., `--color-accent`) are defined as CSS variables for seamless dark mode transitions.

### Dynamic Loading Logic
The page `games/play.html` acts as a shell. It uses Alpine.js to:
1. Parse the URL (e.g., `?game=snake&model=gpt4o`).
2. Fetch `data/games.json`.
3. Update the `<iframe>` source dynamically to switch between Round 1 (Raw) and Round 2 (Fixed) versions.

---

## Deployment
- **Cloudflare Pages**: Connect your repository. Build command: `npm run build:css`. Output directory: `/` (root).
- **Static Hosting**: Ensure `dist/output.css` is built before uploading.