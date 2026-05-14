#!/usr/bin/env python3
"""Generate American English MP3 pronunciations for all word cards via edge-tts."""
import asyncio
import os

from edge_tts import Communicate

WORDS = [
    "Sun", "Star", "Apple", "Banana", "Grape", "Berry", "Carrot",
    "Cat", "Dog", "Fish", "Frog", "Lion", "Monkey", "Panda", "Rabbit",
    "Turtle", "Bee", "Butterfly", "Elephant", "Book", "Pencil", "Bag",
    "Color", "House", "Door", "Window", "Bed", "Chair", "Toy", "Tree",
    "Flower", "Rain", "Snow", "Fire", "Water", "Rainbow", "Car", "Bus",
    "Bike", "Train", "Plane", "Rocket", "Boat", "Moon", "Ball", "Music",
    "Happy", "Love", "Hello", "Bird",
]

VOICE = "en-US-JennyNeural"
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "audio")


async def gen(word: str) -> None:
    path = os.path.join(OUT_DIR, f"{word.lower()}.mp3")
    if os.path.exists(path):
        print(f"  skip  {word.lower()}.mp3")
        return
    await Communicate(word, VOICE).save(path)
    print(f"  ok    {word.lower()}.mp3")


async def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    await asyncio.gather(*[gen(w) for w in WORDS])
    print(f"\nDone — {len(WORDS)} files in audio/")


asyncio.run(main())
