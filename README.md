# Keystroke Sound Player

## Overview

The Keystroke Sound Player is a Python script that plays different sound files for key press and release events. It uses the `pygame` library to handle sound playback and the `keyboard` library to capture keystrokes. The script is configured to log activities to the console for real-time monitoring.

## Features

- Play custom sound files for key press and key release events.
- Real-time console logging for debugging and monitoring.
- Easy to run and configure with command-line arguments.

## Requirements

- Python 3.x
- `pygame` library
- `keyboard` library

## Installation

1. **Install Required Libraries**:

   You need to install `pygame` and `keyboard`. Run the following command:

   ```bash
   pip install pygame keyboard
   ```

2. **Download the Script**:

   Save the provided Python script to a file, for example, `main.py`.

## Usage

To run the script, use the following command:

```bash
python main.py --sound_press path/to/press.mp3 --sound_release path/to/release.mp3
```

### Command-Line Arguments

- `--sound_press`: Path to the sound file to be played for key press events. Default: `press.mp3`
- `--sound_release`: Path to the sound file to be played for key release events. Default: `release.mp3`

If you do not specify the paths, the script will use `press.mp3` and `release.mp3` located in the same directory as the script.

## Example

Run the script with default sound files:

```bash
python main.py
```

Run the script with custom sound files:

```bash
python main.py --sound_press custom_press.mp3 --sound_release custom_release.mp3
```

## Console Output

The script prints log messages to the console, including:

- Initialization messages
- Loaded sound files
- Key press and release events

## Converting to Executable

To convert this script into a standalone executable, use [PyInstaller](https://www.pyinstaller.org/). Follow these steps:

1. **Install PyInstaller**:

   ```bash
   pip install pyinstaller
   ```

2. **Create the Executable**:

   Run PyInstaller with the following command:

   ```bash
   pyinstaller --onefile main.py
   ```

   This will generate an executable in the `dist` directory.

3. **Run the Executable**:

   Navigate to the `dist` directory and run the executable. The application will behave the same way as the script, with console logging enabled.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to modify the README according to any additional details or preferences you might have.
