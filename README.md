# Tic-Tac-Toe con IA Minimax

Un juego simple de Tic-Tac-Toe implementado en Python usando Tkinter con un oponente de IA imbatible que utiliza el algoritmo minimax.

## Características

- **Arquitectura MVC Limpia**: Separado en componentes Model, View y Controller
- **IA Minimax**: Oponente de IA imbatible que usa el algoritmo minimax
- **GUI Simple**: Interfaz Tkinter limpia e intuitiva
- **Estado del Juego**: Muestra el jugador actual y resultados del juego
- **Nuevo Juego**: Funcionalidad de reinicio fácil

## Cómo Ejecutar

1. Asegúrate de tener Python 3.x instalado
2. Ejecuta la aplicación principal:
   ```bash
   python3 main.py
   ```

## Reglas del Juego

- Tú juegas como 'X' y siempre vas primero
- La IA juega como 'O' y usa el algoritmo minimax
- Haz clic en cualquier celda vacía para hacer tu movimiento
- La IA automáticamente hará su movimiento después del tuyo
- El primero en conseguir 3 en línea (horizontal, vertical o diagonal) gana
- Si todas las celdas se llenan sin ganador, es un empate

## Arquitectura

La aplicación sigue el patrón MVC (Model-View-Controller):

- **Model** (`model.py`): Maneja el estado del juego, lógica y algoritmo minimax
- **View** (`view.py`): Gestiona la presentación de la GUI con Tkinter
- **Controller** (`controller.py`): Coordina entre Model y View, maneja interacciones del usuario
- **Main** (`main.py`): Inicializa e inicia la aplicación

## Archivos

- `main.py` - Punto de entrada principal de la aplicación
- `model.py` - Lógica del juego e implementación de IA minimax
- `view.py` - Interfaz GUI con Tkinter
- `controller.py` - Manejo de interacciones del usuario
- `README.md` - Este archivo

## Requisitos del Sistema

- Python 3.x
- Módulo tkinter (generalmente incluido con Python, pero puede requerir instalación en algunos sistemas Linux)

### Instalación de tkinter en Ubuntu/Debian:
```bash
sudo apt update
sudo apt install python3-tk
```

## Descripción Técnica

Este proyecto implementa un juego de Tic-Tac-Toe completo con las siguientes características técnicas:

- **Algoritmo Minimax**: La IA evalúa todos los movimientos posibles y elige el óptimo
- **Puntuación basada en profundidad**: La IA prefiere victorias más rápidas y derrotas más lentas
- **Estructura de código limpia**: Cada clase tiene una responsabilidad única
- **Experiencia de usuario**: Los movimientos de la IA tienen un pequeño retraso para mejor feedback visual

La IA es imbatible - solo puedes empatar o perder, ¡pero sigue siendo divertido intentarlo!