from pprint import pprint
from numpy.random import randn
import matplotlib.pyplot as plt
import numpy as np
from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise, Saver
from util import *

class ConstantVelocityObject(object):
    def __init__(self, x0=0, vel=1., noise_scale=0.06):
        self.x = x0
        self.vel = vel
        self.noise_scale = noise_scale

    def update(self):
        self.vel += randn() * self.noise_scale
        self.x += self.vel
        return (self.x, self.vel)

def sense(x, noise_scale=1.):
    return x[0] + randn()*noise_scale

def SecondOrderKF(R_std, Q, dt, P=100):
    """ Create second order Kalman filter. 
    Specify R and Q as floats."""
    
    kf = KalmanFilter(dim_x=3, dim_z=1)
    kf.x = np.zeros(3)
    kf.P[0, 0] = P
    kf.P[1, 1] = 1
    kf.P[2, 2] = 1
    kf.R *= R_std**2
    kf.Q = Q_discrete_white_noise(3, dt, Q)
    kf.F = np.array([[1., dt, .5*dt*dt],
                     [0., 1.,       dt],
                     [0., 0.,       1.]])
    kf.H = np.array([[1., 0., 0.]])
    return kf

def filter_data(kf, zs):
    """
    Runs the Kalman Filter in batch

    Parameter:
        - kf: a KalmanFilter object
        - zs: measurements
    """

    s = Saver(kf)
    kf.batch_filter(zs, saver=s)
    s.to_array()
    return s

def simulate_system(Q, count):
    """
    This function gets the real and sensor data.
    """
    
    obj = ConstantVelocityObject(x0=.0, vel=0.5, noise_scale=Q)
    xs, zs = [], []
    for i in range(count):
        x = obj.update()
        z = sense(x)
        xs.append(x) # x = [position, velocity]
        zs.append(z)
    return np.array(xs), np.array(zs)


def main():
    R, Q = 1, 0.03
    xs, zs = simulate_system(Q=Q, count=100)

    kf = SecondOrderKF(R, Q, dt=1)
    data = filter_data(kf, zs)

    # Plot the filter
    plt.plot(xs[:,0], linestyle='--', color='k', label='Track')
    plot_measurement(zs) # Position vs Time
    plt.plot(data.x[:,0], label='Filter')

    # Plot the residuals
    plot_all_residuals(zs, data)
    #print(covariance_ellipse(data.P[-1]))

    # Plot confidence interval
    plot_confidence(data.x[-1,:], data.P[-1,:])

    plt.show()


main()