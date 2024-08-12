from PIL import Image
from math import floor
from sys import argv

# comments are so even beginners can sorta understand maybe?



class AsciiConverter:
    ASCII_TABLE: str = " .,:;I!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"[::1]
    IMG_WIDTH: int = 77 # dont ask these fit perfectly on discord 
    IMG_HEIGHT: int = floor(IMG_WIDTH / 3) # /3 seems to just work sorta
    pixel_grid: list[list[int]] # grid of "pixels" 
    
    def convert_image_to_ascii(self, image_path: str) -> str:
        original_image = Image.open(image_path).convert("L") # grayscale
        resized_image = original_image.resize((self.IMG_WIDTH, self.IMG_HEIGHT)) # resize to smol

        # resized_image.save("resized_image.png") # forgor
        
        # standard iterating shit bla bla
        self.pixel_grid = []
        for y in range(self.IMG_HEIGHT):
            self.pixel_grid.append([])
            for x in range(self.IMG_WIDTH):
                # convert to six bit color cuz only 64 characters not 256
                six_bit_color: int = floor(resized_image.getpixel((x, y)) / 256 * 64) # isnt this just /4 
                self.pixel_grid[y].append(six_bit_color)
                

        result: str = ""
        for row in self.pixel_grid: # whats itertools lmao
            current: str = ""
            for pixel in row:
                current += self.ASCII_TABLE[pixel]
            result += current + "\n"

        return result # return as string to save to file :3


if __name__ == "__main__": # you can technically import this n use the class lol
    
    if len(argv) < 2: # if no file go away >:(
        raise ValueError("Please provide an image file path as an argument.")
    
    path = argv[1]
       
    text = AsciiConverter().convert_image_to_ascii(path)
    with open("result.txt", "w") as f:
        f.write("`" + text + "`")
