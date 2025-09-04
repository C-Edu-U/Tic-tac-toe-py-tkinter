"""
Archivo principal de la aplicación para el juego Tic-Tac-Toe con IA Minimax.
Este archivo inicializa y ejecuta la aplicación MVC completa.
"""

from model import TicTacToeModel
from view import TicTacToeView
from controller import TicTacToeController

def main():
    """
    Función principal que inicializa e inicia el juego Tic-Tac-Toe.
    Crea instancias de Model, View y Controller siguiendo el patrón MVC.
    """
    # Crear instancia del modelo (maneja lógica y estado del juego)
    model = TicTacToeModel()
    
    # Crear instancia del controlador (maneja interacciones del usuario)
    controller = TicTacToeController(model, None)
    
    # Crear instancia de la vista (maneja presentación de la GUI)
    view = TicTacToeView(controller)
    
    # Establecer la referencia de la vista en el controlador
    controller.view = view
    
    # Iniciar el juego
    controller.start_game()

if __name__ == "__main__":
    main()