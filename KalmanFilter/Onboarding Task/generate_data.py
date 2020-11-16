from filterpy.kalman import KalmanFilter, predict, update
from filterpy.common.discretization import Q_discrete_white_noise
import numpy as np
from numpy.random import randn
import pandas as pd

sample_space = 100
state = []
measurements = []
estimates = []

'''
Instantiate filter class, and initialize x, F, H, P, R, and Q  https://github.com/rlabbe/filterpy
'''

# Process Noise
Q = 1
# Measurement Noise
R = 5
# Time step
dt = 1

# Instantiation Kalman Filter
kf = KalmanFilter(dim_x=2, dim_z=1)

# Parameterizing the Kalman Filter
# We're using a First Order KF
kf.x = np.zeros(2)
kf.P *= np.array([[100, 0], [0, 1]])
kf.R *= R
kf.Q = Q_discrete_white_noise(2, dt, Q)
kf.F = np.array([[1., dt],
                 [0., 1]])
kf.H = np.array([[1., 0]])


def generate_state():

    global state, dt

    # We will be using a constant Acceleration object
    x = 20.
    v = 0.
    acc = 0.02

    acc_noise_scale = 0.05
    
    for _ in range(sample_space):
        acc += randn() * acc_noise_scale
        v = v + acc * dt
        x = x + v * dt

        state.append((x, v))

    state = np.array(state)

def generate_measurements():

    global state, measurements

    noise = 2

    for s in state:

        # We will only measure the position for now
        measurements.append(s[0] + randn() * noise)

def filter_measurements():

    global kf, measurements, estimates

    for z in measurements:
        kf.predict()
        kf.update(z)

        estimates.append(kf.x)

    estimates = np.array(estimates)

def output_data():

    global state, measurements, estimates

    # Convert the tuples into string for storing them as csv
    # state = [" ".join([str(elem) for elem in x]) for x in state]
    # estimates = [" ".join([str(elem) for elem in x]) for x in estimates]

    out_dict = {
        'states': state[:,0],
        'measurements': measurements,
        'estimates': estimates[:,0]
    }

    df = pd.DataFrame.from_dict(out_dict)
    df.to_csv('data.csv', index=False)


if __name__ == "__main__":
    generate_state()
    generate_measurements()
    filter_measurements()
    output_data()
