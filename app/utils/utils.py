import random

PRESETS = {
    "default": "abcdefghijklmnopqrstuvwxyz0123456789",
    "emoji": "💀🥶☠️😈😭😢🥺😡🤬❤️🥵👿😔😎😂😤😨🤓🗣️👍❌"
}

def generate_id(preset="default", length=12):
    pool = list(PRESETS.get(preset, PRESETS["default"]))
    return ''.join(random.choice(pool) for _ in range(length))