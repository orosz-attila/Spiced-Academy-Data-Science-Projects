## 08. Markov Chain Monte Carlo (MCMC): Predicting and simulating customer behaviour in a supermarket.

<div align="justify">The goal of this project was predicting and visualizing customer behaviour between departments/aisles in a supermarket, applying Markov Chain modeling and Monte-Carlo simulation.</div><br>  

The project involved the following tasks:

1. EDA, Data Wrangling
2. Calculating Transition Probabilities between the aisles
3. Implementing a Customer Class
4. Running MCMC (Markov-Chain Monte-Carlo) simulation for a single class customer 
5. Extending the simulation to multiple customers
6. Animation/Visualization 


### Files for the project steps can be found:

1. notebook/mcmc_transition_matrix.ipynb
2. notebook/mcmc_transition_matrix.ipynb
3. notebook/mcmc_customer_class.ipynb
4. simulation/mcmc_customer_control_keyboard.py
5. simulation/mcmc_simulator.py
6. simulation/mcmc_visualization.py


gif

### To DO:
- Update simulation with dynamic lambda according to the customer database. At the moment, the simulation is running with 2 customer entering per minute. (this is the lambda at the random.Poisson() distbribution)
- Displaying the avatars at the exit location
- Displaing path of the avatars' move between the locations 