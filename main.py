import argparse
import logging

import keyboard
import pygame

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(console_formatter)

logger.addHandler(console_handler)


def main(sound_press_path, sound_release_path):
    logging.info("Initializing pygame mixer.")
    pygame.mixer.init()

    logging.info(f"Loading sound files: {sound_press_path}, {sound_release_path}")
    sound_press = pygame.mixer.Sound(sound_press_path)
    sound_release = pygame.mixer.Sound(sound_release_path)

    key_states = {}
    logging.info("Starting to listen for key events.")

    def play_sound_on_keystroke():
        def on_key_event(event):
            key = event.name

            if event.event_type == "down":
                if key not in key_states or not key_states[key]:
                    logging.info(f"Key pressed: {key}")
                    sound_press.play()
                    key_states[key] = True

            elif event.event_type == "up":
                if key_states.get(key, False):
                    logging.info(f"Key released: {key}")
                    sound_release.play()
                    key_states[key] = False

        keyboard.hook(on_key_event)
        logging.info("Waiting for key events...")
        keyboard.wait()

    play_sound_on_keystroke()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Play different sounds for key press and release events.")
    parser.add_argument(
        "--sound_press",
        type=str,
        default="press.mp3",
        help="Path to the sound file for key press events (default: press.mp3)",
    )
    parser.add_argument(
        "--sound_release",
        type=str,
        default="release.mp3",
        help="Path to the sound file for key release events (default: release.mp3)",
    )
    args = parser.parse_args()

    logging.info(f"Command line arguments: {args}")
    main(args.sound_press, args.sound_release)
