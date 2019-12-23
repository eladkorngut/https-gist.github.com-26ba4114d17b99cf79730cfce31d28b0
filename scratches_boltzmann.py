from ROOT import gROOT,TCanvas,TH1D
import ROOT
import numpy as np
from  scipy.constants import Boltzmann
from fractions import Fraction


def energy(max_energy):
    x = np.random.uniform(0, max_energy, size=None)

def maxboltzman(x,a):
    return (np.sqrt(2/np.pi)/(np.power(a,3)))*((x**2)*np.exp((-1*x**2)/(2*a**2)))351


def rejection_sampling(a,max_energy,rand_boltz):
    x = np.random.uniform(0, max_energy, size=None)
    mb_max=a
    y=np.random.uniform(0,mb_max)
    mb=maxboltzman(x,a)
    if(y<=mb):
        rand_boltz.append(x)
    return rand_boltz


def n_rej_samp(max_energy,a,it=100000,rand_boltz=[]):
    while(np.size(rand_boltz)<it):
        rejection_sampling(a,max_energy,rand_boltz)
    return rand_boltz

def create_hist_root(bin_num,min_range,max_range,v):
    h=TH1D ('Data','Histogram for the rejection method T=300, max energy 1E-19',bin_num,min_range,max_range)
    for i in range(np.size(v)):
        h.Fill(v[i])
    return h

def inv_m(r,a):
    frac=Fraction('1/3')
    return ((3*np.sqrt(np.pi/2)*r)**frac)*a

def m(x,a):
    return np.sqrt(2/np.pi)*(x**2)/(a**3)

def imp_samp(x,a,rand_boltz):
    r2 = np.random.uniform(0, 1, size=None)
    if(r2*m(x,a)<np.exp(-1*(x**2)/(a**2))):
        return rand_boltz.append(x)
    return rand_boltz

def pick_m_x(a):
    r1 = np.random.uniform(0, 1, size=None)
    return inv_m(r1,a)

def n_m_samp(a,it=100000,rand_boltz=[]):
    while(np.size(rand_boltz)<it):
        x=pick_m_x(a)
        rand_boltz=imp_samp(x,a,rand_boltz)
    return rand_boltz

T=300.0; it=100; max_energy=1E-19; bin_num=100;
a=Boltzmann*T

it_m=100
m_boltz=[]
m_boltz=n_m_samp(a,it_m,m_boltz)
hist_m=create_hist_root(bin_num,0,max_energy,m_boltz)

c=TCanvas('c1','Boltzmann distubition question')
c.Divide(2)
c.cd(2)
hist_m.Draw()

rej_boltz=[]
rej_boltz=n_rej_samp(max_energy,a,it,rej_boltz)
hist_rej=create_hist_root(bin_num,0,max_energy,rej_boltz)
c.cd(1)
hist_rej.Draw()