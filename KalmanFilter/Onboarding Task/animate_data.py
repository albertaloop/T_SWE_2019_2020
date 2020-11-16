import pandas as pd
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count

index = count()
time_step = []
estimates = []
states = []

sample_space = 100


def animate(i):
    
    global states, estimates, data

    # Clear the graph after 40 iterations
    x = next(index)
    counter = x

    time_step.append(x)
    if counter > 40:
        time_step.pop(0)
        estimates.pop(0)
        states.pop(0)
        counter = 0
        plt.cla()

    if time_step[-1] < sample_space:
        states.append(data.states[time_step[-1]])
        estimates.append(data.estimates[time_step[-1]])

    plt.plot(states, "b--")
    plt.plot(estimates, "r--")

    '''
    Append to "states" and "estimates" with respective values from pandas dataframe, then
    call the "plot" function
    https://pythonprogramming.net/live-graphs-matplotlib-tutorial/
    https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm
    '''

    ax.legend(["Actual State", "Estimation"])
    ax.set_xlabel("Time Step")
    ax.set_ylabel("Position")
    plt.title('Kalman Filter Estimation')
    time.sleep(.05)  # keep refresh rate of 0.25 seconds


if __name__ == "__main__":
    # * To Do *

    global data

    '''
    Read CSV file.
    '''
    data = pd.read_csv('data.csv')

    # Plot results
    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, animate, frames=sample_space, interval=100, repeat=False)
    print("Done.")

    plt.tight_layout()
    plt.show()
