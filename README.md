# Lacucaracha - Artificial Intelligence and Legos

### Authors
- Tyler Lubbers
- Julian Bracero

## La cucaracha (Task)
Our robot was built to model the basic behaviors of a cockroach. Its primary task is to actively seek a dark hiding spot within the local environment. The robot carries out it's task while avoiding obstacles and reacting to sudden bright lights.

### PEAS Description

- Performance Measure:
    - Given an area with luminescence levels below the threshold exists in the robot's environment, how often can the robot discover said area.
    - Given that a robot discovers an area lit below the light threshold, how much time did the robot take to find it.
- Environment:
    - Partially observable, since the bot will not know the light levels at each area of the room.
    - Single agent
    - Non-deterministic since external agents may effect the environment (e.g. turn on a light) which will change our robot's behavior.
    - Sequential, since the current decision will affect future decisions.
    - Dynamic, light levels may change when the agent runs.
    - Discrete, since the luminescence values are discrete.
    - Unknown the agent may not know how light an area is that it has not visited
- Actuators:
    - Wheels, Two Large Motors, Programmable EV3 Brick, Display
-  Sensors
    - Touch Sensor, Light Sensor, Ultrasonic Sensor

### Incorporated AI
The incorporated AI lies mainly in the random sweep of the state space. The states are simply a position on the ground with some luminosity value. The robot performs a random walk of this space, searching for the goal state, where the goal state is an area of light with a luminescence value that is below a threshold we determined. We are confident the random sweep will eventually find the goal since the space is finite.

### Differences from proposal
There are a number of notable differences between our initial proposal and the final robot.

- Our initial proposal included sudden loud sounds among the stimuli which could invoke a response from the robot. While we did attain a sound sensor, the operating sounds of the robot itself made it difficult to distinguish external sounds, hence the functionality was removed.
- Initially we believed luminescence values would be continuous, however the color sensor provided with the Lego kit returns discrete luminescence values. This affected our PEAS description, but had no consequence to the intended behavior of the robot.
- Our original planned approach to hill-climbing used simulated annealing, however, we quickly realized there was no way to determine a successor state luminescence level. Thus, given the robots position, there was no way to determine which action lead a better state (i.e. a state with a lower luminescence value). Therefore we chose the random walk procedure described above.
