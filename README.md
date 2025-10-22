# Two-Player Chess Game

A functional chess game built with Python and Pygame featuring a turn-based clock system and forfeit button.

## Features
- Two-player gameplay (same device only)
- Valid move highlighting
- Piece capture tracking
- Check detection with visual alerts for the King pieces
- Turn-based clock system (tracks individual player time and pauses when opponent's turn)
- Game timer (tracks time since current game started)
- Forfeit option

## Requirements
- Python 3.x
- Pygame

## Installation
```bash
pip install pygame
```

## How to Run
```bash
python Chess.py
```

## Controls
- **Mouse**: Left click to select and move pieces
- **Forfeit Button**: Left click to forfeit current player's game
- **Enter**: Press ENTER or RETURN key to restart game after game over

## Future Improvements
- Pawn promotion
- Castling
- En passant
- Checkmate detection
- Stalemate detection
- Move validation (prevent moves that expose king)