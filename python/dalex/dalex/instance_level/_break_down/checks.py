import numpy as np
import pandas as pd


def check_new_observation(new_observation, explainer):
    if isinstance(new_observation, (pd.Series, list)):
        new_observation = np.array(new_observation)
        if new_observation.ndim == 1:
            # make 1D array 2D
            new_observation = new_observation.reshape((1, -1))

        new_observation = pd.DataFrame(new_observation, columns=explainer.data.columns)
    elif isinstance(new_observation, pd.DataFrame):
        new_observation.columns = explainer.data.columns
    else:
        raise TypeError("new_observation must be a numpy.ndarray or pandas.Series or pandas.DataFrame")

    return new_observation


def check_order(order):
    if order is not None and not isinstance(order, (list, np.ndarray)):
        raise TypeError('Wrong order type')

    if order is not None:
        return np.array(order)
    else:
        return None
