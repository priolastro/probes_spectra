
import numpy as np
import scipy.constants as sc
from matplotlib import pyplot as plt
from scipy.constants import h, c, e, N_A, electron_mass
from scipy.constants import physical_constants

H_eV=physical_constants['Hartree energy in eV'][0]
Bohrradius=physical_constants['Bohr radius'][0]

esu_Cfactor=2997924579.9996

def nm(wavelength, a=((h*c)/e)*10**9):
    return a/(wavelength)

def plot_spectra_nm(EXC, OS, broadening=0.1, legend=None):
    prefattore=(np.sqrt(sc.pi)*(e*esu_Cfactor)**2*N_A)/(1000*np.log(10)*(c*100)**2*electron_mass)/1000
    x=np.linspace(200, 600, 10000)
    e1 = 0
    for i in range(len(EXC)):
        e1 += prefattore*(OS[i]/(10**7/nm(broadening)))*np.exp(-(((1/x)-(1/EXC[i]))/(1/nm(broadening)))**2)
    plt.plot(x, e1, label=legend)
    return None

def plot_tpaspectra_nm(energie, delta, broadening=0.1, legend=None):
    x = np.linspace(1, 6, 10000)
    k = (((8 * sc.pi ** 2 * sc.fine_structure * Bohrradius ** 5) / sc.speed_of_light) * 100000000) * 10 ** 50
    e1=0
    for i in range(len(energie)):
        e1+= (k*(x/H_eV)**2*delta[i]*broadening/H_eV) / ((2 * (x/H_eV) - (energie[i]/H_eV))**2 + (broadening/H_eV)**2)
    plt.plot(nm(x)*0.5, e1, label=legend)
    return None

def plot_tpaecd_nm(energie, rotatory, broadening=0.3, legend=None, linestyle=None):
    k=4.87555e-5
    e1=0
    x=np.linspace(1,6,1000)
    plt.axhline(linewidth=1, color='black')
    for i in range(len(energie)):
        e1+=(k*x/H_eV**2*rotatory[i]*broadening/H_eV)/((2 * (x/H_eV) - (energie[i]/H_eV))**2 + (broadening/H_eV)**2)
    plt.plot(nm(x)*0.5,e1, label=legend, linestyle=linestyle)
    return None

