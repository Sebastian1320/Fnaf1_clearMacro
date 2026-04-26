# 🎮 FNAF1 Bot — Automatic Gameplay Script

> Inspired by the original idea from (https://www.youtube.com/watch?v=BaX71RpF7rI)

A Python automation bot that plays **Five Nights at Freddy's 1** automatically using screen color detection and mouse simulation. It navigates menus, survives nights, and progresses through the game on its own.

---

## 📋 Requirements

- Python 3.14.3
- [pyautogui](https://pypi.org/project/pyautogui/)
- [pynput](https://pypi.org/project/pynput/)

Install dependencies:
```bash
pip install pyautogui pynput
```

---

## ▶️ How to use

1. Open **Five Nights at Freddy's 1** and place it on your screen.
2. Run the script:
```bash
python Fnaf.py
```
3. Use the keyboard controls below.

---

## ⌨️ Controls

| Key | Action |
|-----|--------|
| `M` | Start the bot |
| `P` | Print current mouse coordinates and pixel color (If you want to test another pixel or something) |

---

## 🤖 What the bot does

- Detects how many stars are unlocked on the main menu using pixel color matching.
- **0 stars** — starts a new game or continues from where it left off.
- **1 star** — navigates to Night 6.
- **2 stars** — goes to Custom Night and sets animatronics to max difficulty (20/20/20/20).
- **3 stars** — stops, the game is fully completed.

During each night it:
- Checks the left door for Bonnie using pixel detection.
- Checks the right door for Chica using pixel detection.
- Opens/closes doors as needed to survive.
- Monitors camera 4B to stun Freddy.
- Opens cameras between light checks to stun Foxy.
- Detects when the night ends to return to the main menu or continues in the next night.

---

## ⚠️ Notes

- The coordinates in the script are stored as **screen ratios** (0.0 to 1.0), so they adapt to any resolution automatically.
- The game window must be **visible and not minimized** while the bot runs.
- If you want to stop the script, close the game and drag the mouse to one of your main screen corners(Not recommended for laptop users without mouse).
- The README was AI generated.

---

## 👥 Credits

| Role | User |
|------|------|
| Developer | [@Sebastian1320](https://github.com/Sebastian1320) |
| Developer | [@Sebasgcs](https://github.com/Sebasgcs) |
| Original idea | [YouTube video](https://www.youtube.com/watch?v=BaX71RpF7rI) |

---
---

# 🎮 FNAF1 Bot — Script de Juego Automático

> Inspirado en la idea original de (https://www.youtube.com/watch?v=BaX71RpF7rI)

Un bot de automatización en Python que juega **Five Nights at Freddy's 1** automáticamente usando detección de colores en pantalla y simulación del mouse. Navega menús, sobrevive las noches y progresa en el juego por su cuenta.

---

## 📋 Requisitos

- Python 3.14.3
- [pyautogui](https://pypi.org/project/pyautogui/)
- [pynput](https://pypi.org/project/pynput/)

Instalar dependencias:
```bash
pip install pyautogui pynput
```

---

## ▶️ Cómo usar

1. Abre **Five Nights at Freddy's 1** y déjalo visible en pantalla.
2. Ejecuta el script:
```bash
python Fnaf.py
```
3. Usa los controles de teclado descritos abajo.

---

## ⌨️ Controles

| Tecla | Acción |
|-------|--------|
| `M` | Iniciar el bot |
| `P` | Mostrar coordenadas del mouse y color del píxel (Por si quieren probar sacar más píxeles en un futuro) |

---

## 🤖 Qué hace el bot

- Detecta cuántas estrellas están desbloqueadas en el menú principal usando detección de color de píxeles.
- **0 estrellas** — inicia una partida nueva o continúa donde se quedó.
- **1 estrella** — navega a la Noche 6.
- **2 estrellas** — va a la Noche Personalizada y pone los animatrónicos en dificultad máxima (20/20/20/20).
- **3 estrellas** — se detiene, el juego está completado.

Durante cada noche:
- Revisa la puerta izquierda buscando a Bonnie con detección de píxeles.
- Revisa la puerta derecha buscando a Chica con detección de píxeles.
- Abre y cierra puertas según sea necesario para sobrevivir.
- Monitorea la cámara 4B para aturdir a Freddy.
- Abre la cámara entre chequeos de las puertas para aturdir a Foxy.
- Detecta cuando termina la noche para volver al menú principal o continúa en la próxima noche.

---

## ⚠️ Notas

- Las coordenadas del script están guardadas como **proporciones de pantalla** (0.0 a 1.0), por lo que se adaptan automáticamente a cualquier resolución.
- La ventana del juego debe estar **visible y no minimizada** mientras el bot corre.
- Si se desea terminar el script, cierre el juego y arrastre el cursor a alguna de las esquinas de su monitor principal (No recomendado para usuarios de laptop sin mouse)
- El README fue generado con IA.

---

## 👥 Créditos

| Rol | Usuario |
|-----|---------|
| Desarrollador | [@Sebastian1320](https://github.com/Sebastian1320) |
| Desarrollador | [@Sebasgcs](https://github.com/Sebasgcs) |
| Idea original | [Video de YouTube](https://www.youtube.com/watch?v=BaX71RpF7rI) |

---
