Role: Expert Frontend Developer
Task: Create a fully functional "Snake Game" in a SINGLE HTML file.

Requirements:
1. Technical Stack: 
   - Use HTML5, CSS3, and Vanilla JavaScript.
   - No external libraries or frameworks (no Bootstrap, no Tailwind CDN).
   - All code (CSS, JS) must be embedded within the HTML file.

2. Visual Style (Cyberpunk/Dark Theme):
   - Background: Dark gray or black (#1a1a1a).
   - Game Board: Visible border with a subtle glow effect.
   - Snake: Neon green or bright accent color.
   - Food: Red or a distinct bright color (circular shape).
   - Typography: Use a monospaced font (like 'Courier New' or similar) for the score.

3. Core Gameplay Mechanics:
   - Movement: Control the snake using Arrow Keys.
   - Logic: 
     - Snake grows when eating food.
     - Score increases by 10 points per food.
     - Game speed increases slightly as the score gets higher (progressive difficulty).
     - Collision detection: Game over if snake hits the wall or its own tail.
   - **Crucial Logic Constraint**: Prevent the snake from reversing direction immediately (e.g., if moving Up, pressing Down should be ignored to prevent instant death).

4. UI Components:
   - Start Screen: A "Start Game" button overlay before the game begins.
   - Scoreboard: Display current score at the top.
   - Game Over Screen: An overlay showing the Final Score and a "Restart" button.

5. Code Structure:
   - Clean, commented, and modular JavaScript code.
   - Ensure the game loop is smooth (use requestAnimationFrame).