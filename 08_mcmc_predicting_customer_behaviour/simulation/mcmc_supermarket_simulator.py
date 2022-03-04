"""
This script simulates customers using a Monte Carlo Markov Chain and produces CSV output.

Run: python mcmc_supermarket_simulator.py
"""

import numpy as np
import pandas as pd
import random


SIMULATE_MINUTES = 60 * 15
NEW_CUSTOMERS_PER_MINUTE = 1.6 # lambda of poisson distribution

locations = ('entrance', 'fruit', 'spices', 'dairy', 'drinks', 'checkout')
prob_matrix = pd.read_csv('mx.csv', index_col=0)


class Customer:
    ''' Customer that moves through the supermarket'''
    
    def __init__(self, id):
        self.id = id
        self.state = 'entrance'


    def next_location(self):
        '''Calculates the next location with the weighted probabilities of the transition matrix'''
        self.state = random.choices(['checkout', 'dairy', 'drinks', 'fruit', 'spices'], list(prob_matrix.loc[self.state]))
        self.state = self.state[0]


    @property    
    def active(self):
        """Returns False if the customer is at the checkout location, and True at all other location"""
        if self.state != 'checkout':
            return True
        else:
            return False


    def __repr__(self):
        return f'<Customer {self.name} in {self.state}>'


    def __repr__(self):
        """formats as CSV"""
        return f"{self.id}, {self.state}"


class Supermarket:
    """Manages list of Customer instances that are currently in the supermarket (customer.active = True)."""

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
            c = Customer(self.last_id)
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


if __name__ == '__main__':

    supermarket = Supermarket("Doodl")

    for i in range(SIMULATE_MINUTES):
        supermarket.next_minute()
        supermarket.add_new_customers()
        supermarket.remove_exited_customers()