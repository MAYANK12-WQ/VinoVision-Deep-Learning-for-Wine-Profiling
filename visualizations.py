# visualizations.py
import matplotlib.pyplot as plt

def alcohol_distribution(data):
    red = data[data['type'] == 1]
    white = data[data['type'] == 0]

    fig, ax = plt.subplots(1, 2)
    ax[0].hist(red['alcohol'], color='red', alpha=0.5, label='Red Wine')
    ax[1].hist(white['alcohol'], color='white', edgecolor='black', alpha=0.5, label='White Wine')
    ax[0].set_title("Red Wine Alcohol")
    ax[1].set_title("White Wine Alcohol")
    plt.show()
