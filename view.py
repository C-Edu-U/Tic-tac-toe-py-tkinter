"""
Clase View para el juego Tic-Tac-Toe.
Maneja la presentación de la GUI usando Tkinter.
"""

import tkinter as tk
from tkinter import messagebox

class TicTacToeView:
    """
    Clase View que maneja la presentación de la GUI.
    Sigue el patrón MVC manejando solo aspectos visuales.
    """
    
    def __init__(self, controller):
        """
        Inicializa la vista con una referencia al controlador.
        
        Args:
            controller: Referencia al controlador para manejar interacciones del usuario
        """
        self.controller = controller
        self.root = tk.Tk()
        self.buttons = []
        self.status_label = None
        
        self.setup_gui()
    
    def setup_gui(self):
        """
        Configura los componentes principales de la GUI incluyendo ventana, botones y etiquetas.
        """
        # Configurar ventana principal
        self.root.title("Tic-Tac-Toe - IA Minimax")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Crear marco principal
        main_frame = tk.Frame(self.root, bg='lightgray')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Etiqueta de título
        title_label = tk.Label(
            main_frame, 
            text="Tic-Tac-Toe", 
            font=("Arial", 24, "bold"),
            bg='lightgray',
            fg='darkblue'
        )
        title_label.pack(pady=(0, 20))
        
        # Etiqueta de estado para mostrar jugador actual o resultado del juego
        self.status_label = tk.Label(
            main_frame,
            text="Tu turno (X)",
            font=("Arial", 14),
            bg='lightgray',
            fg='darkgreen'
        )
        self.status_label.pack(pady=(0, 20))
        
        # Marco del tablero de juego
        board_frame = tk.Frame(main_frame, bg='lightgray')
        board_frame.pack(pady=(0, 20))
        
        # Crear cuadrícula 3x3 de botones
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(
                    board_frame,
                    text="",
                    font=("Arial", 24, "bold"),
                    width=4,
                    height=2,
                    bg='white',
                    fg='black',
                    relief='raised',
                    bd=2,
                    command=lambda r=row, c=col: self.controller.on_button_click(r, c)
                )
                button.grid(row=row, column=col, padx=2, pady=2)
                button_row.append(button)
            self.buttons.append(button_row)
        
        # Marco de botones de control
        control_frame = tk.Frame(main_frame, bg='lightgray')
        control_frame.pack(pady=(0, 10))
        
        # Botón de nuevo juego
        new_game_button = tk.Button(
            control_frame,
            text="Nuevo Juego",
            font=("Arial", 12),
            bg='lightblue',
            fg='darkblue',
            relief='raised',
            bd=2,
            command=self.controller.on_new_game
        )
        new_game_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # Botón de salir
        quit_button = tk.Button(
            control_frame,
            text="Salir",
            font=("Arial", 12),
            bg='lightcoral',
            fg='darkred',
            relief='raised',
            bd=2,
            command=self.controller.on_quit
        )
        quit_button.pack(side=tk.LEFT)
    
    def update_button(self, row, col, symbol):
        """
        Actualiza un botón específico con el símbolo dado.
        
        Args:
            row (int): Índice de fila del botón
            col (int): Índice de columna del botón
            symbol (str): Símbolo a mostrar ('X' o 'O')
        """
        if 0 <= row < 3 and 0 <= col < 3:
            self.buttons[row][col].config(text=symbol)
            # Deshabilitar el botón después de usarlo
            self.buttons[row][col].config(state='disabled')
    
    def update_status(self, message):
        """
        Actualiza la etiqueta de estado con el mensaje dado.
        
        Args:
            message (str): Mensaje a mostrar en la etiqueta de estado
        """
        self.status_label.config(text=message)
    
    def disable_all_buttons(self):
        """
        Deshabilita todos los botones del juego (usado cuando el juego termina).
        """
        for row in self.buttons:
            for button in row:
                button.config(state='disabled')
    
    def enable_all_buttons(self):
        """
        Habilita todos los botones del juego y limpia su texto (usado para nuevo juego).
        """
        for row in self.buttons:
            for button in row:
                button.config(text="", state='normal')
    
    def show_game_over_message(self, winner):
        """
        Muestra un cuadro de mensaje cuando el juego termina.
        
        Args:
            winner (str or None): El ganador ('X', 'O') o None para empate
        """
        if winner == 'X':
            message = "¡Felicidades! ¡Ganaste!"
            title = "¡Ganaste!"
        elif winner == 'O':
            message = "¡La IA gana! ¡Mejor suerte la próxima vez!"
            title = "¡La IA Gana!"
        else:
            message = "¡Es un empate!"
            title = "¡Empate!"
        
        messagebox.showinfo(title, message)
    
    def run(self):
        """
        Inicia el bucle principal de la GUI.
        """
        self.root.mainloop()
    
    def close(self):
        """
        Cierra la ventana de la GUI.
        """
        self.root.destroy()