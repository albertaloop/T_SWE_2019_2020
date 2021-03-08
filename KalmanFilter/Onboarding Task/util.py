from matplotlib.patches import Ellipse
import numpy as np
import matplotlib.pyplot as plt
from filterpy.stats import covariance_ellipse

"""
WARNING: The functions are not tested rigorously,

It would work best with dimensions
    Measurements, zs: (N,) [Only the position dimension]
    State vector, x: (N,d) [d = 2 or 3]
"""

def plot_confidence(x, P):
    """
    This function plots the confidence ellipses

    Parameters:
        - x: the state vector of the kf
        - P: the covariance matrix of the kf associated with the state vector
    """

    label_mappings = {
        'p': 'Position',
        'v': 'Velocity',
        'a': 'Acceleration'
    }
    
    # [x x']
    if x.shape[0] == 2:
        fig, axes = plt.subplots(1,1)
        axes = (axes,)
        covs = (P,)
        means = (x,)
        labels = (['p','v'], )
    
    # [x x' x'']
    elif x.shape[0] == 3:
        # [x x'], [x,x'']
        fig, axes = plt.subplots(1,2)
        covs = (P[0:2, 0:2], P[[[0],[2]], [[0,2]]])
        means = (x[:2],x[1:])
        labels = (['p', 'v'], ['p', 'a'])

    # TODO: Generalize for higher order terms
    # However, for our case, order upto acceleration should be sufficient

    # Plot the ellipses
    for label, mean, ax, cov in zip(labels, means, axes, covs):
        # Get the arguments for plotting an ellipse, check the `covariance_ellipse` function
        # in filterpy.stats for more information
        ellipse = covariance_ellipse(cov)

        # Unpack the arguments
        angle = np.degrees(ellipse[0])
        width = ellipse[1] * 2.
        height = ellipse[2] * 2.

        # Set standard deviation (Generalize later)
        sd = 1

        # Create an ellipse patch
        e = Ellipse(xy=mean, width=sd*width, height=sd*height, angle=angle,
                    facecolor='g',
                    edgecolor='g',
                    alpha=0.4,
                    lw=2, ls='solid')

        ax.add_patch(e)

        label = list(map(lambda x: label_mappings[x], label))

        ax.set_xlabel(label[0])
        ax.set_ylabel(label[1])

        ax.set_title(f'{label[0]} vs {label[1]}')

        x, y = mean
        # Plot the mid point
        ax.scatter(x, y, marker='+', color='k')


def plot_all_residuals(zs, data):
    """
    Plots all the residual graphs, currently it plots
        - position residuals
        - velocity residuals

    ** This will be generalized to all the available order of position. (Based on measurement order)

    Parameter:
        - zs: the measurements
        - data: object returned by the Saver class
    """

    fig, axes = plt.subplots(1, 1 if len(zs.shape) == 1 else zs.shape[1])

    for col, axis in enumerate(axes if isinstance(axes, list) else [axes]):
        # For generalizing later, change the label to <n>-th order residual
        plot_residuals(axis, zs, data, col, 'First Order Position Residuals(1$\sigma$)', 'meters')


def plot_residuals(ax, zs, data, col, title, y_label, std=1):
    """
    Plots an individual residual graph on the specified axis

    Parameter:
        - ax: Axes class of matplotlib
        - zs: measurements
        - data: output of the Saver class
        - col: the column of the state vector
        - title: <str>
        - y_label: <str>
        - std: <int>, pick one of 1, 2 and 3.
    """

    # Calculate the residuals
    res = (m := np.matmul(data.x_prior, np.transpose(data.H[0][0])) - zs) if col == 0 else m[col]

    ax.set_title(title)
    ax.set_xlabel('time (sec)')
    ax.set_ylabel(y_label)

    ax.plot(res)
    plot_residual_limits(ax, data.P[:, col, col], std)


def plot_residual_limits(ax, Ps, std=1.):
    """ 
    Plots standand deviation given in Ps as a yellow shaded region. One std
    by default, use std for a different choice (e.g. std=3 for 3 standard
    deviations.
    """

    std = np.sqrt(Ps) * std

    ax.plot(-std, color='k', ls=':', lw=2)
    ax.plot(std, color='k', ls=':', lw=2)
    ax.fill_between(range(len(std)), -std, std, facecolor='#ffff00', alpha=0.3)


def plot_measurement(xs, ys=None, dt=1, color='k', label='measurement'):
    """
    Plots the measurements

    - This just functions just defines some options for plotting,
      apart from that this does the same thing as plt.scatter

    Returns: None
    """

    # Plot a single axis
    if ys is None:
        ys = xs
        xs = np.arange(0, len(ys) * dt, dt)

    # lw/linewidth = borderwidth
    plt.scatter(xs, ys, edgecolor=color, facecolor='none', lw=2, label=label)
