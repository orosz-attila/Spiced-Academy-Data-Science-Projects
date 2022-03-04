"""
This script visualizes the layout of the supermarket, and places one customer avatar in it. 
The w,a,s,d keys can control the direction of the next move of customer avatar.

Run: python customer_keyboard_control.py
"""

import numpy as np
import cv2
import random


# size of a tile (32*32 pixels = 1 tile)
TILE_SIZE = 32

# the black area around the supermarket picture (OFFSET)
OFS = 50                    

# represantation of the market with one symbol '#', '.', 'b' or similar for each tile on the png-file
LAYOUT = """
##################
##..............##
#D..DS..SB..BV..V#
#D..DS..SB..BV..V#
#D..DS..SB..BV..V#
#D..DS..SB..BV..V#
#D..DS..SB..BV..V#
##...............#
##..CC..CC..CC...#
##..CC..CC..CC...#
##...............#
##XX##########EE##
""".strip()


class TilesMap:
    """Constructor for the map, Visualizes the supermarket layout(MARKET) with extracting the icons from the tiles"""

    def __init__(self, layout, tiles):
        """
        layout : a string with each character representing a tile
        tiles   : a numpy array containing all the tile images
        """
        self.tiles = tiles
        # split the layout string into a two dimensional matrix
        self.contents = [list(row) for row in layout.split("\n")]
        self.ncols = len(self.contents[0])
        self.nrows = len(self.contents)
        self.image = np.zeros(
            (self.nrows*TILE_SIZE, self.ncols*TILE_SIZE, 3), dtype=np.uint8
        )
        self.prepare_map()

    def extract_tile(self, row, col):
        """extract a tile array from the tiles image"""
        y = row*TILE_SIZE
        x = col*TILE_SIZE
        return self.tiles[y:y+TILE_SIZE, x:x+TILE_SIZE]

    def get_tile(self, char):
        """returns the array for a given tile character"""
        if char == "#":
            return self.extract_tile(0, 0)
        elif char == "B":
            return self.extract_tile(0, 4)
        elif char == "C":
            return self.extract_tile(5, 3)
        elif char == "D":
            return self.extract_tile(6, 13)
        elif char == "E":
            return self.extract_tile(7, 3)
        elif char == "S":
            return self.extract_tile(5, 8)     
        elif char == "V":
            return self.extract_tile(1, 11)        
        elif char == "X":
            return self.extract_tile(6, 10)
        else:
            return self.extract_tile(1, 2)
        
    def prepare_map(self):
        """prepares the entire image as a big numpy array"""
        for row, line in enumerate(self.contents):
            for col, char in enumerate(line):
                bm = self.get_tile(char)
                y = row*TILE_SIZE
                x = col*TILE_SIZE
                self.image[y:y+TILE_SIZE, x:x+TILE_SIZE] = bm

    def draw(self, frame):
        """
        draws the image into a frame
        """
        frame[0:self.image.shape[0], 0:self.image.shape[1]] = self.image

    def write_image(self, filename):
        """writes the image into a file"""
        cv2.imwrite(filename, self.image)


class Customer: 
    """
    Customer class that models the customer behavior in a supermarket.
    """

    def __init__(self, map, avatar, row, col):
        """
        supermarket: A SuperMarketMap object
        avatar : a numpy array containing a 32x32 tile image
        row: the starting row
        col: the starting column
        """
        # self.name = "whatever"
        self.map =map
        self.avatar = avatar
        self.row = row
        self.col = col

    def draw(self, frame):
        '''# places the customer-object onto the map'''
        x = self.row * TILE_SIZE
        y = self.col * TILE_SIZE
        frame[x:x+TILE_SIZE, y:y+TILE_SIZE] = self.avatar

    def move(self, direction):
        new_row = self.row
        new_col = self.col

        if direction == 'up':
            new_row -= 1

        if direction == 'down':
            new_row += 1

        if direction == 'right':
            new_col += 1

        if direction == 'left':
            new_col -= 1

        if self.map.contents[new_row][new_col] == '.':
            self.col = new_col
            self.row = new_row

    def __repr__(self):
        '''returns where the customer is drawn, if no errors occur'''
        return f"customer at {self.row}/{self.col}"
        

if __name__ == "__main__":

    background = np.zeros((500, 700, 3), np.uint8)
    tiles = cv2.imread("tiles.png")
    
    # Instantiating a SupermarketMap object 
    map = TilesMap(LAYOUT, tiles)

    # this one gives a pacman from tiles.png, it loads the icon at (3,1)
    avatar = tiles[3*TILE_SIZE:4*TILE_SIZE,1*TILE_SIZE:2*TILE_SIZE]

     # Instantiating a Customer object 
    customer = Customer(map, avatar, 10, 15)

    while True:
        frame = background.copy()
        map.draw(frame)
        customer.draw(frame) 

        # https://www.ascii-code.com/
        key = cv2.waitKey(1)
       
        # 119 is the 'w' key
        if key == 119:
            customer.move('up')

        if key == 115:
            customer.move('down')

        if key == 100:
            customer.move('right')

        if key == 97:
            customer.move('left')

        if key == 113: # 'q' key
            break
    
        cv2.imshow("frame", frame)


    cv2.destroyAllWindows()

    map.write_image("supermarket.png")
