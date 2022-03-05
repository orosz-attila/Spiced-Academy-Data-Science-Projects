## 08. Markov Chain Monte Carlo (MCMC): Predicting and simulating customer behaviour in a supermarket.

![animation](https://raw.githubusercontent.com/orosz-attila/Spiced-Academy-Data-Science-Projects/master/08_mcmc_predicting_customer_behaviour/images/mcmc_simulation.gif)<br>


<div align="justify">The goal of this project was predicting and visualizing customer behaviour between departments/aisles in a supermarket, applying Markov Chain modeling and Monte-Carlo simulation.</div><br>  

The project involved the following tasks:

### 1. Data Analysis

See the notebook/[mcmc_data_analysis.ipynb](link).

### 2. Calculating Transition Probabilities between the aisles  (5x5 crosstab)

See the notebook/[mcmc_transition_matrix.ipynb](link).

### 3. Creating a Customer Class

See the notebook/[mcmc_customer_class.ipynb](link).

### 4. Running MCMC (Markov-Chain Monte-Carlo) simulation for a single class customer 

See the simulation/[mcmc_customer_control_keyboard.py](link).

### 5. Extending the simulation to multiple customers

See the simulation/[mcmc_simulator.py](link).

### 6. Visualization of the supermarket layout and the simulation of the customer behaviour based on the transition probabilities.

See the simulation/[mcmc_visualization.py](link).


### To Do:
- Update simulation with dynamic lambda according to the customer data. At the moment, the simulation is running with 2 customer entering per minute. (this is the lambda at the random.Poisson() distbribution)
- Displaying the avatars at the exit location
- Displaing path of the avatars' move between the locations 