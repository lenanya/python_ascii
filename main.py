from PIL import Image
from math import floor
from sys import argv


class AsciiConverter:
    ASCII_TABLE: str = " .,:;I!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"[::1]
    IMG_WIDTH: int = 77
    IMG_HEIGHT: int = floor(IMG_WIDTH / 3)
    pixel_grid: list[list[int]]
    
    def convert_image_to_ascii(self, image_path: str) -> str:
        original_image = Image.open(image_path).convert("L")
        resized_image = original_image.resize((self.IMG_WIDTH, self.IMG_HEIGHT))

        resized_image.save("resized_image.png")
        
        self.pixel_grid = []
        for y in range(self.IMG_HEIGHT):
            self.pixel_grid.append([])
            for x in range(self.IMG_WIDTH):
                six_bit_color: int = floor(resized_image.getpixel((x, y)) / 256 * 64)
                self.pixel_grid[y].append(six_bit_color)
                

        result: str = ""
        for row in self.pixel_grid:
            current: str = ""
            for pixel in row:
                current += self.ASCII_TABLE[pixel]
            result += current + "\n"

        return result


if __name__ == "__main__":
    
    if len(argv) < 2:
        raise ValueError("Please provide an image file path as an argument.")
    
    path = argv[1]
       
    text = AsciiConverter().convert_image_to_ascii(path)
    with open("result.txt", "w") as f:
        f.write("`" + text + "`")
