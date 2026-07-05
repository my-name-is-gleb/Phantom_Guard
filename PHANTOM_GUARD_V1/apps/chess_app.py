import pygame
import chess
import os
import sys

# --- НАСТРОЙКИ И КОНСТАНТЫ ---
WIDTH, HEIGHT = 600, 600
SQ_SIZE = WIDTH // 8
FPS = 30

# Цвета
COLOR_LIGHT = (240, 240, 210)
COLOR_DARK = (120, 150, 90)
COLOR_GREEN = (0, 255, 0, 100) # Прозрачный зеленый (движение)
COLOR_BLUE = (0, 100, 255, 150) # Прозрачный синий (атака)
COLOR_OVERLAY = (0, 0, 0, 180)  # Фон финала

# Пути
BASE_PATH = os.path.dirname(__file__)
ASSETS_PATH = os.path.join(BASE_PATH, "chess_image")

IMAGES = {}

def load_images():
    """Загрузка изображений с защитой от ошибок."""
    piece_map = {
        'wK': 'Chess_klt60.png', 'wQ': 'Chess_qlt60.png', 'wR': 'Chess_rlt60.png',
        'wB': 'Chess_blt60.png', 'wN': 'Chess_nlt60.png', 'wP': 'Chess_plt60.png',
        'bK': 'Chess_kdt60.png', 'bQ': 'Chess_qdt60.png', 'bR': 'Chess_rdt60.png',
        'bB': 'Chess_bdt60.png', 'bN': 'Chess_ndt60.png', 'bP': 'Chess_pdt60.png'
    }
    try:
        for p_code, file_name in piece_map.items():
            path = os.path.join(ASSETS_PATH, file_name)
            img = pygame.image.load(path).convert_alpha()
            IMAGES[p_code] = pygame.transform.smoothscale(img, (SQ_SIZE, SQ_SIZE))
    except Exception as e:
        print(f"[!] КРИТИЧЕСКАЯ ОШИБКА РЕСУРСОВ: {e}")
        pygame.quit()
        sys.exit()

def draw_board(screen):
    for row in range(8):
        for col in range(8):
            color = COLOR_LIGHT if (row + col) % 2 == 0 else COLOR_DARK
            pygame.draw.rect(screen, color, (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, board):
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            col = chess.square_file(square)
            row = 7 - chess.square_rank(square)
            color_prefix = "w" if piece.color == chess.WHITE else "b"
            p_type = piece.symbol().upper()
            screen.blit(IMAGES[color_prefix + p_type], (col * SQ_SIZE, row * SQ_SIZE))

def draw_highlights(screen, board, selected_sq):
    if selected_sq is not None:
        # Рисуем кружки для доступных ходов
        for move in board.legal_moves:
            if move.from_square == selected_sq:
                to_sq = move.to_square
                col = chess.square_file(to_sq)
                row = 7 - chess.square_rank(to_sq)
                center = (col * SQ_SIZE + SQ_SIZE // 2, row * SQ_SIZE + SQ_SIZE // 2)
                
                # ЛОГИКА СИНЕЙ КЛЕТКИ: Если на клетке враг - рисуем синим
                color = COLOR_BLUE if board.is_capture(move) else COLOR_GREEN
                pygame.draw.circle(screen, color, center, 15)

def draw_game_over(screen, result_text):
    """Окно завершения игры."""
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill(COLOR_OVERLAY)
    screen.blit(overlay, (0, 0))
    
    font = pygame.font.SysFont("Impact", 50)
    btn_font = pygame.font.SysFont("Arial", 30)
    
    text = font.render(result_text, True, (255, 255, 255))
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - 100))
    
    # Кнопка RESTART
    restart_btn = pygame.Rect(WIDTH//2 - 100, HEIGHT//2, 200, 50)
    pygame.draw.rect(screen, (50, 200, 50), restart_btn)
    btn_text = btn_font.render("ИГРАТЬ СНОВА", True, (0, 0, 0))
    screen.blit(btn_text, (restart_btn.x + 10, restart_btn.y + 10))
    return restart_btn

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("PHANTOM CHESS - Secure Module")
        clock = pygame.time.Clock()
        load_images()
        
        board = chess.Board()
        selected_sq = None
        game_over = False
        result_msg = ""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
                    col = event.pos[0] // SQ_SIZE
                    row = 7 - (event.pos[1] // SQ_SIZE)
                    square = chess.square(col, row)
                    
                    move = chess.Move(selected_sq, square) if selected_sq is not None else None
                    
                    if move in board.legal_moves:
                        board.push(move)
                        selected_sq = None
                    else:
                        # Выбираем только фигуры текущего цвета
                        piece = board.piece_at(square)
                        if piece and piece.color == board.turn:
                            selected_sq = square
                        else:
                            selected_sq = None

                elif game_over and event.type == pygame.MOUSEBUTTONDOWN:
                    # Проверка клика по кнопке Restart
                    if restart_btn.collidepoint(event.pos):
                        board.reset()
                        game_over = False
                        selected_sq = None

            # Проверка состояния игры
            if not game_over:
                if board.is_checkmate():
                    game_over = True
                    winner = "ЧЕРНЫЕ" if board.turn == chess.WHITE else "БЕЛЫЕ"
                    result_msg = f"МАТ! ПОБЕДА: {winner}"
                elif board.is_stalemate() or board.is_insufficient_material():
                    game_over = True
                    result_msg = "НИЧЬЯ / ПАТ"

            # ОТРИСОВКА
            draw_board(screen)
            draw_highlights(screen, board, selected_sq)
            draw_pieces(screen, board)
            
            if game_over:
                restart_btn = draw_game_over(screen, result_msg)

            pygame.display.flip()
            clock.tick(FPS)

    except Exception as fatal_error:
        print(f"[!] КРИТИЧЕСКИЙ СБОЙ ПРИЛОЖЕНИЯ: {fatal_error}")
        # В реальном PHANTOM GUARD здесь была бы отправка лога админу

if __name__ == "__main__":
    main()