import os
import json

IMAGE_FOLDER = "images"
JS_FILE = "images.js"


def get_image_paths():
    return [
        os.path.join(IMAGE_FOLDER, filename).replace("\\", "/")
        for filename in sorted(os.listdir(IMAGE_FOLDER))
        if filename.lower().endswith(
            (".png", ".jpg", ".jpeg", ".gif", ".webp", ".heic")
        )
    ]


def update_js():
    images = get_image_paths()
    js_content = f"const images = {json.dumps(images, indent=2)};"

    with open(JS_FILE, "w", encoding="utf-8") as f:
        f.write(js_content)

    print(f"{JS_FILE} updated with {len(images)} images.")


if __name__ == "__main__":
    update_js()
