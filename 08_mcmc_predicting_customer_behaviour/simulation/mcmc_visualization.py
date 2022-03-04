"""
Visualization of a MCMC simulation of a supermarket.

Run: python mcmc_visualization.py
"""

import numpy as np
import pandas as pd
import cv2
import random
import time

SIMULATE_MINUTES = 60 * 15
NEW_CUSTOMERS_PER_MINUTE = 1.6 # lambda of poisson distribution
LOCATIONS = ['fruit', 'spices', 'dairy', 'drinks', 'checkout']
PROBABILITIES = pd.read_csv('mx.csv', index_col=0)

# size of a tile (32*32 pixels = 1 tile)
TILE_SIZE = 32               

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
##CC....CC.......#
##CC....CC.......#
##...............#
###X....X##E....E#
""".strip()


class TilesMap:
    """Constructor for the map, visualizes the supermarket layout(MARKET) with extracting the icons from the tiles"""

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

    def __init__(self, id, map, avatar):
        """
        supermarket: A SuperMarketMap object
        avatar : a numpy array containing a 32x32 tile image
        row: the starting row
        col: the starting column
        """
        self.id = id
        self.location = 'entrance'
        self.map =map
        self.avatar = avatar

    def draw(self, frame):
        '''# places the customer-object onto the map'''
        x = 11 * TILE_SIZE
        y = random.randint(12,15) * TILE_SIZE
        frame[x:x+TILE_SIZE, y:y+TILE_SIZE] = self.avatar

    def next_location(self):
        '''Calculates the next location with the weighted probabilities of the transition matrix'''
        ''' places the customer-object onto the map'''
        self.location = random.choices(LOCATIONS, list(PROBABILITIES.loc[self.location]))[0]

        if self.location == 'fruit':
            x = TILE_SIZE * random.randint(2,6)
            y = TILE_SIZE * random.randint(14,15)
        elif self.location == 'spices':
            x = TILE_SIZE * random.randint(2,6)
            y = TILE_SIZE * random.randint(10,11) 
        elif self.location == 'dairy':
            x = TILE_SIZE * random.randint(2,6)
            y = TILE_SIZE * random.randint(6,7)
        elif self.location == 'drinks':
            x = TILE_SIZE * random.randint(2,6)
            y = TILE_SIZE * random.randint(2,3)
        else:
            x = TILE_SIZE * random.randint(8,9)
            y = TILE_SIZE * random.randint(4,7)
        frame[x:x+TILE_SIZE, y:y+TILE_SIZE] = self.avatar

    @property    
    def active(self):
        """Returns False if the customer is at the checkout location, and True at all other location"""
        if self.location != 'checkout':
            return True
        else:
            return False

    def __repr__(self):
        """formats as CSV"""
        return f"{self.id}, {self.location}"


class Supermarket:
    """This class controls the list of Customer instances that are currently in the supermarket (customer.active = True)."""

    def __init__(self, name):        
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.last_id = 0
        self.name = name

    @property
    def time(self):
        '''Current time in HH:MM format'''
        hour = 7  + self.minutes // 60
        min = self.minutes % 60
        return f"{hour:02}:{min:02}:00"

    @property
    def n_customers(self):
        '''Returns the number of customers in the supermarket'''
        return len(self.customers)


    def next_minute(self):
        """It sets one minute and moves all customers to the next location"""
        self.minutes += 1
        for c in self.customers:
            c.next_location()
            self.print_row(c)

    def add_new_customers(self):
        """New customer added in every minute calulated with the lamda=1.6"""
        n = np.random.poisson(NEW_CUSTOMERS_PER_MINUTE)
        for i in range(n):
            self.last_id += 1
            c = Customer(self.last_id, map, avatar)
            c.draw(frame)
            self.customers.append(c)
            self.print_row(c)

    def remove_exited_customers(self):
        """
        Recreates customers list from active customer (who are not at the checkout), 
        in this way, it removes customers that are at the checkout
        """
        self.customers = [c for c in self.customers if c.active]

    def print_row(self, customer):
        """Prints one row of CSV"""
        row = str(self) + ', ' + str(customer)
        print(row)

    def __repr__(self):
        """formats as CSV"""
        return f"{self.time}, {self.name}, {self.n_customers}"


if __name__ == "__main__":

    background = np.zeros((500, 700, 3), np.uint8)
    tiles = cv2.imread("tiles.png")
    
    # Instantiating a TilesMap object 
    map = TilesMap(LAYOUT, tiles)

    avatar = tiles[3*TILE_SIZE:4*TILE_SIZE,1*TILE_SIZE:2*TILE_SIZE] # this one gives a pacman
     
    # Instantiating a Customer and Supermarket object 
    supermarket = Supermarket("Doodl") 

    for i in range(SIMULATE_MINUTES):
        frame = background.copy()
        map.draw(frame) 


        supermarket.next_minute()
        supermarket.add_new_customers()
        supermarket.remove_exited_customers()
        time.sleep(0.5)


        # https://www.ascii-code.com/
        key = cv2.waitKey(1)
        if key == 113: # 'q' key
            break
    
        cv2.imshow("frame", frame)

    cv2.destroyAllWindows()

#    market.write_image("supermarket.png")
