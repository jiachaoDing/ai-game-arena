# Game Template Usage Guide

This document explains how to add new games to the AI Game Benchmark using the standardized template.

## Overview

The game benchmark system now uses a **template-based approach** where:
- All game-specific information is stored in `data/games.json`
- Each game uses the same HTML template (`game-template.html`)
- The template dynamically loads game configuration and displays it

## Adding a New Game

### Step 1: Add Game Configuration to `data/games.json`

Add a new entry in `data/games.json` with the following structure:

```json
{
  "your-game-id": {
    "title": "Your Game Name",
    "emoji": "🎮",
    "description": "A brief description of your game for SEO and display",
    "keywords": "keyword1, keyword2, keyword3",
    "controls": [
      {
        "keys": ["W", "A", "S", "D"],
        "description": "Movement keys"
      },
      {
        "description": "Other control instructions (no keys needed)"
      }
    ],
    "requirements": [
      {
        "title": "Technical Challenge 1",
        "description": "Description of the first technical requirement"
      },
      {
        "title": "Technical Challenge 2",
        "description": "Description of the second technical requirement"
      }
    ],
    "models": [
      {
        "id": "model-id",
        "name": "MODEL NAME",
        "type": "standard",
        "status": "Pass",
        "r1_file": "/games/your-game-id/model-id-r1.html",
        "r2_file": null,
        "notes": "Any notes about this model's implementation",
        "tries": 1
      }
    ]
  }
}
```

### Step 2: Create Game Directory

Create a new directory under `games/`:

```
games/
  your-game-id/
    index.html          # Copy from game-template.html (adjust paths)
    model-id-r1.html    # Model implementation files
    model-id-r2.html    # (if needed)
```

### Step 3: Copy and Adjust Template

Copy `games/game-template.html` to `games/your-game-id/index.html` and update the relative paths:

**For games at `games/GAME_NAME/index.html`:**
- CSS: `href="../dist/output.css"` → `href="../../dist/output.css"`
- Home link: `href="../"` → `href="../../"`
- Games data: `fetch('../data/games.json')` → `fetch('../../data/games.json')`
- Footer links: Update accordingly

Or simply **copy** the existing `games/snake/index.html` which already has the correct paths!

### Step 4: Add Model Implementation Files

Place your HTML game implementation files in the game directory:
- `your-game-id/model-id-r1.html` - First attempt
- `your-game-id/model-id-r2.html` - Second attempt (if needed)

## Configuration Reference

### Game Object Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes | Display name of the game |
| `emoji` | string | Yes | Emoji icon for the game |
| `description` | string | Yes | SEO description and overview |
| `keywords` | string | No | SEO keywords |
| `controls` | array | No | Game control instructions |
| `requirements` | array | No | Technical challenge descriptions |
| `models` | array | Yes | List of model implementations |

### Model Object Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier (kebab-case) |
| `name` | string | Yes | Display name |
| `type` | string | No | Model type (e.g., "standard", "reasoning") |
| `status` | string | Yes | "Pass", "Fixed", or "Failed" |
| `r1_file` | string | Yes | Path to Round 1 implementation |
| `r2_file` | string | No | Path to Round 2 implementation |
| `notes` | string | No | Implementation notes |
| `tries` | number | Yes | Number of attempts |

### Control Object Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `keys` | array | No | List of keyboard keys (if applicable) |
| `description` | string | Yes | Control instruction text |

### Requirement Object Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes | Requirement title |
| `description` | string | Yes | Detailed description |

## Example: Adding a Tetris Game

### 1. Update `data/games.json`:

```json
{
  "snake": { ... },
  "tetris": {
    "title": "Tetris Benchmark",
    "emoji": "🧱",
    "description": "Test AI models with the classic Tetris puzzle game",
    "keywords": "Tetris, puzzle game, AI coding, block game",
    "controls": [
      {
        "keys": ["←", "→"],
        "description": "Move piece left/right"
      },
      {
        "keys": ["↓"],
        "description": "Soft drop"
      },
      {
        "keys": ["↑", "Space"],
        "description": "Rotate piece"
      }
    ],
    "requirements": [
      {
        "title": "Piece Rotation",
        "description": "Implement proper rotation matrix for all 7 tetromino shapes"
      },
      {
        "title": "Line Clearing",
        "description": "Detect and remove completed rows, shift blocks down"
      }
    ],
    "models": [
      {
        "id": "gpt-5",
        "name": "GPT-5",
        "type": "standard",
        "status": "Pass",
        "r1_file": "/games/tetris/gpt-5-r1.html",
        "r2_file": null,
        "notes": "Perfect first attempt",
        "tries": 1
      }
    ]
  }
}
```

### 2. Create directory structure:

```
games/
  tetris/
    index.html               # Copy from games/snake/index.html
    gpt-5-r1.html           # Implementation file
```

### 3. That's it!

The template will automatically:
- Extract "tetris" from the URL path
- Load game configuration from `games.json`
- Display all models and their implementations
- Generate navigation between games
- Update SEO meta tags

## Benefits of This Approach

✅ **No Code Duplication** - Single template for all games  
✅ **Easy Maintenance** - Update template once, affects all games  
✅ **Data-Driven** - All game info in one JSON file  
✅ **Automatic Navigation** - Previous/Next game links generated automatically  
✅ **Consistent UI** - All games look and behave the same  
✅ **Quick Setup** - Add new games in minutes  

## Troubleshooting

### Game not loading?
- Check that game ID in URL matches key in `games.json`
- Verify JSON syntax is valid
- Check browser console for errors

### Wrong paths?
- Ensure relative paths are correct for your directory depth
- Use `games/snake/index.html` as reference

### Styles not loading?
- Verify CSS path points to `../../dist/output.css` for games in subdirectories
- Check that Tailwind output file exists

## Questions?

Refer to the existing `games/snake/` implementation as a working example!

