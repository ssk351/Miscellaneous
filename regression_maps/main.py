
import sys
import numpy as np
from scipy import signal
import utils
import figs

if __name__ == "__main__":
    verbose = True

    # load data and create common time axis array
    utils.printmsg("load data ...", verbose)
    dsikkimjastemp, dclimate = utils.load_data()
    sikkim_time = utils.yearly_time_axis(dsikkimjastemp)
    climate_time = utils.common_time_axis(dclimate)
    sikkim_anom = utils.climate_anomaly_y(dsikkimjastemp, sikkim_time)
    climate_anom = utils.climate_anomaly(dclimate, sikkim_time)
    #print(dsikkimjastemp)
    #sys.exit()
    #time = utils.common_time_axis(dismr)
    utils.printmsg("filtered time series ...", verbose)
    sikkim_filt_low = utils.iirfilter(sikkim_anom, N=5, pass_freq=1 / 8)
    #print(sikkim_filt_low) 
    climate_filt_low = utils.iirfilter(climate_anom, N=5, pass_freq=1 / 96)
    sikkim_filt_high = sikkim_anom - sikkim_filt_low
    climate_filt_high = climate_anom - climate_filt_low
    climate_filt_low_reshape = np.reshape(climate_filt_low, (-1,12))
    climate_filt_high_reshape = np.reshape(climate_filt_high, (-1,12))
    climate_filt_low_reshape_year  = np.mean(climate_filt_low_reshape,1)
    climate_filt_high_reshape_year  = np.mean(climate_filt_high_reshape,1)

    np.savetxt('pdo_8yr_lowpass_filt_yearly_1900_2008.txt',climate_filt_low_reshape_year)
    #np.savetxt('nino3_8yr_highpass_filt_yearly_1870_2008.txt',climate_filt_high_reshape_year)
    np.savetxt('sikkim_8yr_lowpass_filt_yearly_1900_2008.txt',sikkim_filt_low)
    #np.savetxt('sikkim_8yr_highpass_filt_yearly_1870_2008.txt',sikkim_filt_high)

    #print(climate_filt_low_reshape)
    #print(climate_filt_low_reshape_year)
    #print(climate_filt_low)
    #print(climate_filt_low_reshape.shape)
    #print(climate_filt_low_reshape_year.shape)

    #print(sikkim_time)
    #print(sikkim_filt_low)
    #print(sikkim_filt_high)
    #sys.exit()
    figs.sikkim_climate_timeseries(sikkim_time, climate_time, sikkim_filt_low, climate_filt_low)
    #figs.input_timeseries(sikkim_time, dsikkimjastemp, sikkim_filt_low, sikkim_filt_high)
    sys.exit()

