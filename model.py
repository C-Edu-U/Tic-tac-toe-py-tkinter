"""
Clase Model para el juego Tic-Tac-Toe.
Maneja el estado del juego, lógica y algoritmo de IA minimax.
"""

class TicTacToeModel:
    """
    Clase Model que maneja el estado del juego y la lógica.
    Sigue el patrón MVC separando datos y lógica de negocio de la presentación.
    """
    
    def __init__(self):
        """
        Inicializa el modelo del juego con tablero vacío y jugador inicial.
        """
        # Tablero 3x3 representado como lista de listas
        # Las celdas vacías se representan con None
        self.board = [[None for _ in range(3)] for _ in range(3)]
        # El jugador humano es 'X', el jugador IA es 'O'
        self.human_player = 'X'
        self.ai_player = 'O'
        # El jugador actual comienza con el humano
        self.current_player = self.human_player
        # Seguimiento del estado del juego
        self.game_over = False
        self.winner = None
    
    def make_move(self, row, col):
        """
        Realiza un movimiento en el tablero para el jugador actual.
        
        Args:
            row (int): Índice de fila (0-2)
            col (int): Índice de columna (0-2)
            
        Returns:
            bool: True si el movimiento fue exitoso, False si es inválido
        """
        # Verificar si el movimiento es válido
        if not self.is_valid_move(row, col):
            return False
        
        # Realizar el movimiento
        self.board[row][col] = self.current_player
        
        # Verificar si el juego terminó después de este movimiento
        self.check_game_over()
        
        # Cambiar jugadores si el juego no ha terminado
        if not self.game_over:
            self.switch_player()
        
        return True
    
    def is_valid_move(self, row, col):
        """
        Verifica si un movimiento es válido (dentro de los límites y la celda está vacía).
        
        Args:
            row (int): Índice de fila
            col (int): Índice de columna
            
        Returns:
            bool: True si el movimiento es válido, False en caso contrario
        """
        # Verificar límites
        if row < 0 or row >= 3 or col < 0 or col >= 3:
            return False
        
        # Verificar si la celda está vacía
        return self.board[row][col] is None
    
    def switch_player(self):
        """
        Cambia el jugador actual entre humano e IA.
        """
        if self.current_player == self.human_player:
            self.current_player = self.ai_player
        else:
            self.current_player = self.human_player
    
    def check_game_over(self):
        """
        Verifica si el juego ha terminado y determina el ganador.
        Establece los atributos game_over y winner en consecuencia.
        """
        # Verificar ganador
        winner = self.get_winner()
        if winner:
            self.winner = winner
            self.game_over = True
        # Verificar empate (tablero lleno y sin ganador)
        elif self.is_board_full():
            self.game_over = True
            self.winner = None  # Empate
    
    def get_winner(self):
        """
        Verifica si hay un ganador en el tablero.
        
        Returns:
            str or None: El jugador ganador ('X' o 'O') o None si no hay ganador
        """
        # Verificar filas
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return row[0]
        
        # Verificar columnas
        for col in range(3):
            if (self.board[0][col] == self.board[1][col] == self.board[2][col] 
                and self.board[0][col] is not None):
                return self.board[0][col]
        
        # Verificar diagonales
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] 
            and self.board[0][0] is not None):
            return self.board[0][0]
        
        if (self.board[0][2] == self.board[1][1] == self.board[2][0] 
            and self.board[0][2] is not None):
            return self.board[0][2]
        
        return None
    
    def is_board_full(self):
        """
        Verifica si el tablero está completamente lleno.
        
        Returns:
            bool: True si el tablero está lleno, False en caso contrario
        """
        for row in self.board:
            for cell in row:
                if cell is None:
                    return False
        return True
    
    def get_available_moves(self):
        """
        Obtiene todos los movimientos disponibles en el tablero.
        
        Returns:
            list: Lista de tuplas (row, col) que representan movimientos disponibles
        """
        moves = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] is None:
                    moves.append((row, col))
        return moves
    
    def reset_game(self):
        """
        Reinicia el juego al estado inicial.
        """
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = self.human_player
        self.game_over = False
        self.winner = None
    
    def minimax(self, depth, is_maximizing):
        """
        Algoritmo minimax para la toma de decisiones de la IA.
        
        Args:
            depth (int): Profundidad actual en el árbol del juego
            is_maximizing (bool): True si es jugador maximizador (IA), False si es minimizador (humano)
            
        Returns:
            int: Puntuación para el estado actual del tablero
        """
        # Verificar estados terminales
        winner = self.get_winner()
        if winner == self.ai_player:
            return 10 - depth  # IA gana (prefiere victorias más rápidas)
        elif winner == self.human_player:
            return depth - 10  # Humano gana (prefiere derrotas más lentas)
        elif self.is_board_full():
            return 0  # Empate
        
        if is_maximizing:
            # Turno de la IA - maximizar puntuación
            best_score = float('-inf')
            for row, col in self.get_available_moves():
                # Realizar movimiento
                self.board[row][col] = self.ai_player
                # Evaluar recursivamente
                score = self.minimax(depth + 1, False)
                # Deshacer movimiento
                self.board[row][col] = None
                best_score = max(score, best_score)
            return best_score
        else:
            # Turno del humano - minimizar puntuación
            best_score = float('inf')
            for row, col in self.get_available_moves():
                # Realizar movimiento
                self.board[row][col] = self.human_player
                # Evaluar recursivamente
                score = self.minimax(depth + 1, True)
                # Deshacer movimiento
                self.board[row][col] = None
                best_score = min(score, best_score)
            return best_score
    
    def get_best_move(self):
        """
        Obtiene el mejor movimiento para la IA usando el algoritmo minimax.
        
        Returns:
            tuple: (row, col) del mejor movimiento, o None si no hay movimientos disponibles
        """
        best_score = float('-inf')
        best_move = None
        
        for row, col in self.get_available_moves():
            # Realizar movimiento
            self.board[row][col] = self.ai_player
            # Evaluar movimiento
            score = self.minimax(0, False)
            # Deshacer movimiento
            self.board[row][col] = None
            
            if score > best_score:
                best_score = score
                best_move = (row, col)
        
        return best_move