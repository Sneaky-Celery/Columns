from PIL import Image, ImageDraw
import numpy as np
import random

def generate_colors():
    # Size, RGBA outter color, RGBA inner color
    green = ((25,35), (25,70,0),(150,190,50))
    red = ((25, 35), (150, 25, 10), (250, 180, 50))
    blue = ((25, 35), (25, 25, 150), (140, 180, 250))
    yellow = ((25, 35), (234, 239, 44), (250, 250, 205))
    orange = ((25, 35), (220, 100, 34), (252, 252, 180))
    purple = ((25, 35), (90, 34, 139), (241, 231, 254))

    return list([green, red, blue, yellow, orange, purple])

class Gems:
    def __init__(self, color, triplet, x_pos=3, y_pos=0, rotation = 0):
        self._color = color
        self._triplet = triplet
        self._rotation = rotation
        self._position = np.array([x_pos,y_pos])

        def generate_triplet():
            triplet_positions = np.array([[1,0],[1,1],[1,2], np.int32])
            first_gem = create_gem(random.choice(generate_colors()))

            def get_biased_color(previous_color):
                # Create a weighted list with a 20% higher chance of selecting the previous color
                weight_factor = 1.2 
                weighted_colors = generate_colors().copy() 
                weighted_colors.append(previous_color) 

                # Generate probabilities
                probabilities = [
                    (weight_factor if color == previous_color else 1) for color in weighted_colors
                ]

                # Normalize the probabilities
                total = sum(probabilities)
                normalized_probabilities = [p / total for p in probabilities]

                # Select a color based on the new probabilities
                return random.choices(weighted_colors, weights=normalized_probabilities, k=1)[0]
            
            triplet = [first_gem]
            triplet.append(get_biased_color(triplet[0]))
            triplet.append(get_biased_color(triplet[0]))

            gems = [Gems(color) for color in triplet]
            return gems, triplet_positions

        def create_gem(size, color_center, color_edge):
            gem = Image.new('RGBA', size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(gem)

            # Create radial gradient
            for i in range(size[0]//2, 0, -1):
                # Calculate the color for each circle
                ratio = i / (size[0] // 2)
                color = (
                    int(color_center[0] * ratio + color_edge[0] * (1 - ratio)),
                    int(color_center[1] * ratio + color_edge[1] * (1 - ratio)),
                    int(color_center[2] * ratio + color_edge[2] * (1 - ratio)),
                    255
                )
                # Draw circle with calculated color
                draw.ellipse(
                    [
                        (size[0] // 2 - i, size[1] // 2 - i),
                        (size[0] // 2 + i, size[1] // 2 + i)
                    ],
                    fill=color
                )
            
            return gem
