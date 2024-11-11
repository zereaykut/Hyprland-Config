import subprocess as sp

from color_schemes import ColorSchemeGenerator


class ColorSchemeGeneratorOW(ColorSchemeGenerator):
    def process_images(self):
        """
        Process each image and generate color schemes.
        Overwrite existing color schemess.
        """
        images_info = self.get_images()

        for image_info in images_info:
            print(image_info[0])

            try:
                self.get_color_scheme(image_info[0], image_info[1], image_info[2])
            except Exception as e:
                error_path = f"{self.base_dir}/{image_info[1]}/{image_info[2]}.error"
                with open(error_path, "w") as f:
                    f.writelines("Error:\n")
                    f.writelines(f"{e}:\n")
                    f.writelines(f"{image_info[0]}\n")
                    f.writelines(f"{image_info[1]}\n")
                    f.writelines(f"{image_info[2]}\n")


if __name__ == "__main__":
    generator = ColorSchemeGeneratorOW()
    generator.process_images()

