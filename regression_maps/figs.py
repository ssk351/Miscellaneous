#! /usr/local/opt/python/libexec/bin/python
"""
Functions used to plot the output figures
=========================================


"""
# Created: Thu Nov 16, 2017  02:05PM
# Last modified: Fri Nov 17, 2017  09:02AM
# Copyright: Bedartha Goswami <goswami@pik-potsdam.de>


import numpy as np
import datetime as dt
from scipy import signal
import matplotlib.pyplot as pl
import matplotlib.dates as mdates


def input_timeseries(sikkim_time, dsikkimjastemp, sikkim_filt_low, sikkim_filt_high):
    """
    Plots input time series, filtered time series, and phase space plots.
    """
        # set up figure
    fig = pl.figure(figsize=[8.5, 8.5])
    axlabfs, tiklabfs, splabfs = 11, 9, 13

    # set up first axis and plot the NINO index
    ax1 = fig.add_axes([0.10, 0.325, 0.85, 0.510])
    ax1.bar(sikkim_time, dsikkimjastemp)
    ax1.plot(sikkim_time, sikkim_filt_low,
             c="Tomato",
             label="8 yr low pass filtered")
    ax1.plot(sikkim_time, sikkim_filt_high, c='y',label="8 yr high pass filtered")
    # prettify ax1 and ax2
    xlo, xhi = dt.datetime(1705, 1, 1), dt.datetime(2008, 12, 31)
    for ax in [ax1]:
        ax.set_xlim(xlo, xhi)
        XMajorLocator = mdates.YearLocator(base=40, month=6, day=15)
        XMinorLocator = mdates.YearLocator(base=4, month=6, day=15)
        # XMinorLocator = mdates.MonthLocator(bymonthday=15, interval=3)
        XMajorFormatter = mdates.DateFormatter("%Y")
        ax.xaxis.set_major_locator(XMajorLocator)
        ax.xaxis.set_minor_locator(XMinorLocator)
        ax.xaxis.set_major_formatter(XMajorFormatter)
        ax.set_ylim(-3.0, 3.0)
        ax.set_yticks(np.arange(-2.0, 2.01, 1.0))
        ax.grid(which="both")
        ax.tick_params(which="major", axis="both", size=8, direction="out")
        ax.tick_params(which="minor", axis="both", size=5, direction="out")
        ax.tick_params(axis="both", labelsize=tiklabfs)
    leg = ax1.legend(loc="upper right")
    for txt in leg.get_texts():
        txt.set_size(tiklabfs)
    ax1.set_ylim(-4., 4.)
    #ax1.tick_params(bottom="off", top="on", which="both",
     #               labelbottom="off", labeltop="on")
    ax1.set_xlabel("Time", fontsize=axlabfs)
    # save figure

    figname = "01_input_timeseries.png"
    pl.savefig(figname)
    print("figure saved to: %s" % figname)

    return None
def sikkim_climate_timeseries(sikkim_time, climate_time, sikkim_filt_low, climate_filt_low):
    """
    Plots input time series, filtered time series, and phase space plots.
    """
        # set up figure
    fig = pl.figure(figsize=[12.5, 8.5])
    axlabfs, tiklabfs, splabfs = 11, 9, 13

    # set up first axis and plot the NINO index
    ax1 = fig.add_axes([0.10, 0.325, 0.85, 0.510])
    print(sikkim_filt_low)
    ax1.plot(sikkim_time, sikkim_filt_low, 
             c="SteelBlue", label="8 yr low pass filtered Sikkim JAS temp")
    ax1.plot(climate_time, climate_filt_low,
             c="Tomato",
             label="8 yr low pass filtered PDO index")
    # prettify ax1 and ax2
    xlo, xhi = dt.datetime(1900, 1, 1), dt.datetime(2008, 12, 31)
    for ax in [ax1]:
        ax.set_xlim(xlo, xhi)
        XMajorLocator = mdates.YearLocator(base=20, month=6, day=15)
        XMinorLocator = mdates.YearLocator(base=2, month=6, day=15)
        # XMinorLocator = mdates.MonthLocator(bymonthday=15, interval=3)
        XMajorFormatter = mdates.DateFormatter("%Y")
        ax.xaxis.set_major_locator(XMajorLocator)
        ax.xaxis.set_minor_locator(XMinorLocator)
        ax.xaxis.set_major_formatter(XMajorFormatter)
        #ax.set_ylim(-3.0, 3.0)
        ax.set_yticks(np.arange(-2.0, 2.01, 1.0))
        ax.grid(which="both")
        ax.tick_params(which="major", axis="both", size=8, direction="out")
        ax.tick_params(which="minor", axis="both", size=5, direction="out")
        ax.tick_params(axis="both", labelsize=tiklabfs)
    leg = ax1.legend(loc="upper right")
    for txt in leg.get_texts():
        txt.set_size(tiklabfs)
    #ax1.set_ylim(-4., 4.)
    #ax1.tick_params(bottom="off", top="on", which="both",
     #               labelbottom="off", labeltop="on")
    ax1.set_xlabel("Time", fontsize=axlabfs)
    # save figure

    figname = "sikkim_climate.png"
    pl.savefig(figname)
    print("figure saved to: %s" % figname)

    return None


def amplitude_timeseries(ct, ampl, nino_grad, nino_hilbert ):
	"""
	Plots the amplitude, smoothed derivative of nino 3 time series and hilbert transform
	"""
	fig = pl.figure(figsize=[16.5, 4.5])
	axlabfs, ticklabfs, splabfs = 12, 10, 14
	ax = fig.add_axes([0.15, 0.15, 0.7, 0.7])
	ax.plot(ct, ampl*12,'b', ct, nino_grad*12,'r--', ct, nino_hilbert*12, 'g--', ct, -ampl*12, c='b' )
	# prettify ax
	xlo, xhi = dt.datetime(1900, 1, 1), dt.datetime(1930, 12, 31)
	ax.set_xlim(xlo, xhi)
	XMajorLocator = mdates.YearLocator(base=5, month=6, day=15)
	XMinorLocator = mdates.YearLocator(base=5, month=6, day=15)
	XMajorFormatter = mdates.DateFormatter("%Y")
	ax.xaxis.set_major_locator(XMajorLocator)
	ax.xaxis.set_minor_locator(XMinorLocator)
	ax.set_xlabel("Time[years]", fontsize=axlabfs)
	ax.set_ylabel("derivative [K/year]", fontsize=axlabfs)
	# save figure
	figname = "../plots/04_amplitude_timeseries.png"
	pl.savefig(figname)
	print("figure saved to: %s" % figname)
	return None


def delphi_timeseries(ct, del_phi, te, volc_time, dvolc):
    """
    Plots the instantaneous phase diff with periods of phase sync highlighted.
    """
    # set up figure
    fig = pl.figure(figsize=[12, 6])
    axlabfs, tiklabfs, splabfs = 9, 10, 14

    # set up ax1 and plot delPhi and event series there
    ax1 = fig.add_axes([0.1, 0.38, 0.85, 0.4])
    ax1.plot(ct, -del_phi/6.28,
             c="Maroon", zorder=5,
             )
    ylo, yhi = ax1.get_ylim()
    ax1.bar(left = te,
            width = 31 * np.ones(len(te)),
            height = (yhi - ylo) * np.ones(len(te)),
            bottom = ylo * np.ones(len(te)),
            edgecolor="none", facecolor="Turquoise",
            zorder=1,
            )
    # set up second ax2 and plot the volcanic radiative forcing 
    ax2 = fig.add_axes([0.1, 0.28, 0.85, 0.1])
    ax2.plot(volc_time, dvolc, c="Gray", zorder=5)
    # prettify ax1
    xlo, xhi = dt.datetime(850, 1, 1), dt.datetime(1850, 12, 31)
    ax1.set_xlim(xlo, xhi)
    XMajorLocator = mdates.YearLocator(base=100, month=6, day=15)
    XMinorLocator = mdates.YearLocator(base=20, month=6, day=15)
    XMajorFormatter = mdates.DateFormatter("%Y")
    ax1.xaxis.set_major_locator(XMajorLocator)
    ax1.xaxis.set_minor_locator(XMinorLocator)
    ax1.xaxis.set_major_formatter(XMajorFormatter)
    ax1.set_ylim(ylo, yhi)
    #ax1.set_ylim(-12,12 )
    ax1.grid(which="both")
    ax1.tick_params(which="major", size=8, direction="out")
    ax1.tick_params(which="minor", size=5, direction="out")
    ax1.tick_params(axis="both", labelsize=tiklabfs)
    ax1.set_xlabel("Time", fontsize=axlabfs)
    ax1.set_ylabel(r"$\Delta\phi = \phi_{ISMR} - \phi_{NINO}[2\pi]$",
                   fontsize=axlabfs)
		# prettify ax2
    xlo, xhi = dt.datetime(850, 1, 1), dt.datetime(1850, 12, 31)
    ax2.set_xlim(xlo, xhi)
    XMajorLocator = mdates.YearLocator(base=100, month=6, day=15)
    XMinorLocator = mdates.YearLocator(base=20, month=6, day=15)
    XMajorFormatter = mdates.DateFormatter("%Y")
    ax2.xaxis.set_major_locator(XMajorLocator)
    ax2.xaxis.set_minor_locator(XMinorLocator)
    ax2.xaxis.set_major_formatter(XMajorFormatter)
    ylo, yhi = ax2.get_ylim()
    ax2.set_ylim(ylo, yhi)
    ax2.grid(which="both")
    ax2.set_xlabel("Time", fontsize=12)
    ax2.set_ylabel("VRF (W/$m^2$)", fontsize=axlabfs)

    # save figure
    figname = "../plots/02_delphi_timeseries.png"
    pl.savefig(figname)
    print("figure saved to: %s" % figname)
    return None


def delphi_histogram(del_phi_dot, lothres, hithres):
    """
    Plots the histogram of instantaneous phase differences.
    """
    # set up figure
    fig = pl.figure(figsize=[6.5, 6.5])
    axlabfs, tiklabfs, splabfs = 6, 10, 14

    # plot histogram of derivative of del_phi
    ax1 = fig.add_axes([0.12, 0.12, 0.85, 0.85])
    h, be = np.histogram(del_phi_dot, bins="fd")
    bc = 0.5 * (be[1:] + be[:-1])
    ax1.fill_between(bc, h,
                     color="Maroon",
                     )
    ax1.fill_between(bc, h,
                     color="Turquoise",
                     where=(bc >= lothres) * (bc <= hithres),
                     )

    # show vertical lines to indicate the interval we choose for del_phi ~ 0
    ax1.axvline(lothres, color="k", linestyle="--")
    ax1.axvline(hithres, color="k", linestyle="--")

    # prettify ax1
    ax1.grid()
    ax1.set_xlabel(r"$\frac{\Delta\phi}{\mathrm{d}t}$",
                   fontsize=axlabfs)
    ax1.set_ylabel("Histogram counts", fontsize=axlabfs)
    ax1.tick_params(axis="both", labelsize=tiklabfs)
    _, yhi = ax1.get_ylim()
    ax1.set_ylim(0., yhi)

    # save figure
    figname = "../plots/03_delphi_histogram.png"
    pl.savefig(figname)
    print("figure saved to: %s" % figname)

    return None



