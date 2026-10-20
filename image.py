from PIL import Image


def generate_image(maze):
    image = Image.new("RGB", (127, 127), (0, 0, 0))
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            color = (255, 255, 255) if maze[i][j] == 'c' else (0, 0, 0)
            image.putpixel((i, j), color)

    resized_image = image.resize((2048, 2048), resample=Image.NEAREST)
    resized_image.save("resized_image.png")
