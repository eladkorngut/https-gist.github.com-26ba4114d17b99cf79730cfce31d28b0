from ROOT import gROOT,TCanvas,TH1F
import numpy as np


def home_exp(lammda=0.5,x=0):
    if(x>=0):
        return lammda*np.exp(-1*lammda*x)
    else:
       return 0

def draw(n=100,l=0.5):
    vec_num_probexp=[]
    for i in range(n):
        x=np.random.uniform(0, 1, size=None)
        num=0
        num=home_exp(l,x)
        vec_num_probexp.append(num)
    return vec_num_probexp

def create_hist_root_exp(sample_size,l,bin_num):
    min_range=0
    max_range=1
    h=TH1F ('hist','A histogram of 100 numbers, drawen from exponential distrubition lammda=0.5',bin_num,min_range,max_range)
    v=draw(sample_size,l)
    for i in range(sample_size):
        h.Fill(v[i])
    return h

sample_size=100000
l=0.5
bin_num=100
gROOT.Reset()
c=TCanvas('c1','c1')
h=create_hist_root_exp(sample_size,l,bin_num)
h.Draw()
h.GetXaxis().SetTitle("Number")
h.GetYaxis().SetTitle("Counts of times the number was drawn")
c.Update()

print('this is no love song')