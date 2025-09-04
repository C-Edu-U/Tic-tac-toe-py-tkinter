"""
Clase Controller para el juego Tic-Tac-Toe.
Maneja las interacciones del usuario y coordina entre Model y View.
"""

class TicTacToeController:
    """
    Clase Controller que maneja las interacciones del usuario y coordina entre Model y View.
    Sigue el patrón MVC manejando lógica de negocio y entrada del usuario.
    """
    
    def __init__(self, model, view):
        """
        Inicializa el controlador con referencias al modelo y la vista.
        
        Args:
            model: Referencia a la instancia de TicTacToeModel
            view: Referencia a la instancia de TicTacToeView
        """
        self.model = model
        self.view = view
    
    def on_button_click(self, row, col):
        """
        Maneja los eventos de clic en botones desde la vista.
        
        Args:
            row (int): Índice de fila del botón clickeado
            col (int): Índice de columna del botón clickeado
        """
        # Solo permitir movimientos si es el turno del jugador humano y el juego no ha terminado
        if (self.model.current_player == self.model.human_player 
            and not self.model.game_over):
            
            # Intentar hacer el movimiento
            if self.model.make_move(row, col):
                # Actualizar la vista con el movimiento del humano
                self.view.update_button(row, col, self.model.human_player)
                
                # Verificar si el juego terminó después del movimiento del humano
                if self.model.game_over:
                    self.handle_game_over()
                else:
                    # Actualizar estado para el turno de la IA
                    self.view.update_status("La IA está pensando...")
                    # Programar movimiento de la IA después de un breve retraso para mejor UX
                    self.view.root.after(500, self.make_ai_move)
    
    def make_ai_move(self):
        """
        Realiza el movimiento de la IA usando el algoritmo minimax.
        """
        # Obtener el mejor movimiento de la IA
        best_move = self.model.get_best_move()
        
        if best_move:
            row, col = best_move
            # Realizar el movimiento de la IA
            self.model.make_move(row, col)
            # Actualizar la vista con el movimiento de la IA
            self.view.update_button(row, col, self.model.ai_player)
            
            # Verificar si el juego terminó después del movimiento de la IA
            if self.model.game_over:
                self.handle_game_over()
            else:
                # Actualizar estado para el turno del humano
                self.view.update_status("Tu turno (X)")
    
    def handle_game_over(self):
        """
        Maneja el final del juego actualizando la vista y mostrando resultados.
        """
        # Deshabilitar todos los botones
        self.view.disable_all_buttons()
        
        # Actualizar estado basado en el ganador
        if self.model.winner == 'X':
            self.view.update_status("¡Ganaste!")
        elif self.model.winner == 'O':
            self.view.update_status("¡La IA ganó!")
        else:
            self.view.update_status("¡Es un empate!")
        
        # Mostrar mensaje de fin de juego
        self.view.show_game_over_message(self.model.winner)
    
    def on_new_game(self):
        """
        Maneja el clic del botón de nuevo juego reiniciando el estado del juego.
        """
        # Reiniciar el modelo
        self.model.reset_game()
        
        # Reiniciar la vista
        self.view.enable_all_buttons()
        self.view.update_status("Tu turno (X)")
    
    def on_quit(self):
        """
        Maneja el clic del botón de salir cerrando la aplicación.
        """
        self.view.close()
    
    def start_game(self):
        """
        Inicia el juego ejecutando el bucle principal de la vista.
        """
        self.view.run()