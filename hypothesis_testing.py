import numpy as np
from scipy import stats as scs



def hypothesis_func1(confidence_level, null_data, new_data, two_tails=True):
    null_mean = np.mean(null_data)
    new_mean = np.mean(new_data)
    data_se = np.std(null_data) / np.sqrt(len(null_data))

    if two_tails:
        t_multiple = scs.t.ppf((confidence_level+ (1-confidence_level)*0.5), len(null_data)-1)
        reject_low = null_mean - t_multiple * data_se
        reject_high = null_mean + t_multiple * data_se
    else:
        t_multiple = scs.t.ppf(confidence_level, len(null_data) - 1)
        reject_low = null_mean - t_multiple * data_se
        reject_high = null_mean + t_multiple * data_se

    if new_mean < reject_low or new_mean > reject_high:
        print('null mean:', null_mean)
        print('new mean:', new_mean)
        print('reject_high:', reject_high)
        print('reject_low:', reject_low)

        print('Alternative Hypothesis stands')
    else:
        print('null mean:', null_mean)
        print('new mean:', new_mean)
        print('reject_high:', reject_high)
        print('reject_low:', reject_low)
        print('Null Hypothesis Stands')
