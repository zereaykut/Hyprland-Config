import subprocess as sp
import os
import json
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.image as mpimg

class KMeansBackend:
    def __init__(self, user, image_path, theme, output_name):
        self.user = user
        self.image_path = image_path
        self.theme = theme
        self.output_name = output_name
        self.image = self.load_image()
        self.color_palette = self.extract_colors()
        self.color_palette_hex = self.convert_palette_to_hex()

    def load_image(self):
        image = mpimg.imread(self.image_path)
        if image.shape[2] == 4:  # Check if the image is in RGBA format and convert to RGB
            image = image[:, :, :3]
        if image.max() <= 1.0:  # Convert the image values to RGB
            image = (image * 255).astype(np.uint8)
        return image

    def extract_colors(self):
        w, h, d = tuple(self.image.shape)
        pixel = np.reshape(self.image, (w * h, d))
        model = KMeans(n_clusters=6, random_state=42).fit(pixel)
        color_palette = np.uint8(model.cluster_centers_)
        sorted_indices = np.argsort(color_palette.sum(axis=1))
        return color_palette[sorted_indices]

    def convert_palette_to_hex(self):
        def rgb_to_hex(rgb):
            return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
        
        return [rgb_to_hex(color)[:7] for color in self.color_palette]

    def save_as_json(self):
        dictionary = {
            "main-bg": self.color_palette_hex[0],
            "main-fg": self.color_palette_hex[5],
            "wb-act-bg": self.color_palette_hex[1],
            "wb-act-fg": self.color_palette_hex[4],
            "wb-hvr-bg": self.color_palette_hex[2],
            "wb-hvr-fg": self.color_palette_hex[3]
        }
        if not os.path.exists(f"/home/{self.user}/.cache/color_schemes"):
            os.mkdir(f"/home/{self.user}/.cache/color_schemes")
        if not os.path.exists(f"/home/{self.user}/.cache/color_schemes/{self.theme}"):
            os.mkdir(f"/home/{self.user}/.cache/color_schemes/{self.theme}")
        with open(f"/home/{self.user}/.cache/color_schemes/{self.theme}/{self.output_name}.json", "w") as f:
            f.write(json.dumps(dictionary, indent=4))

    def execute(self):
        self.save_as_json()

def get_user():
        return sp.run("whoami", shell=True, capture_output=True, text=True).stdout.strip()

def get_images(user):
    """
    returns a list contains info about images:
    images_info : [
                    [ image path, name of theme, name of image]
                ]
    """
    themes = os.listdir(f"/home/{user}/.config/wallpapers")
    images_info = []
    for theme in themes:
        images = os.listdir(f"/home/{user}/.config/wallpapers/{theme}")
        for image in images:
            image_path = f"/home/{user}/.config/wallpapers/{theme}/{image}"
            images_info.append([image_path, theme, image.replace(".png", "").replace(".jpg", "").replace(".gif", "").replace(".jpeg", "")])
    return images_info

if __name__ == "__main__":
    user = get_user()
    images_info = get_images(user)
    
    for image_info in images_info:
        print(image_info[0])
        if os.path.exists(f"/home/{user}/.cache/color_schemes/{image_info[1]}/{image_info[2]}.json"):
            print(f"exists:  /home/{user}/.cache/color_schemes/{image_info[1]}/{image_info[2]}.json")
        else:
            try:
                extractor = KMeansBackend(user, image_info[0], image_info[1], image_info[2])
                extractor.execute()
            except Exception as e:
                with open(f"/home/{user}/.cache/color_schemes/{image_info[1]}/{image_info[2]}.error", "w") as f:
                    f.writelines("Error:\n")
                    f.writelines(f"{e}:\n")
                    f.writelines(f"{image_info[0]}\n")
                    f.writelines(f"{image_info[1]}\n")
                    f.writelines(f"{image_info[2]}\n")
