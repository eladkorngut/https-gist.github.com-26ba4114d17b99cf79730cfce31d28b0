#In this program we are trying to answer question 2. which mainly involve creating a exponential distrubition then
#"messing" it up by adding to it a number of uniform disturbition numbers. We will test when the exponential fit will no
#longer be a valid approximation with the chi sqaure function.

from ROOT import gROOT,TCanvas,TH1F  #The follwing modules are form ROOT (a program developed by cern)
import numpy as np
from scipy import integrate


def qauntile(lammda=0.5,x=0):
    #the qauntelie as was developed in class
        return (-1/lammda)*np.log((1-x))

def exp_dist(x=0,l=0.5):
    #the pdf of an exponetial distubtion
    return l*np.exp(-1*l*x)

def draw(n=100,l=0.5):
    #In here we are to recreate the process of picking a number from exp distubtion. and puting it in an array
    vec_num_probexp=[]
    for i in range(n):
        x=np.random.uniform(0, 1, size=None) #selecting a random number from a uniform distubtion
        num=qauntile(l,x) #The unifrom random is placed in the qauntile function
        vec_num_probexp.append(num)
    return vec_num_probexp

def pk(min_range,max_range,l=0.5):
    #The integral over an exp distrubtion over the range from min_range to max_range
    return np.exp(-1*l*min_range)-np.exp(-1*l*max_range)

def create_hist_root_exp(sample_size,l,bin_num,v):
    #A function that involve creating the histogram in ROOT (by cern)
    min_range=0; max_range=1
    h=TH1F ('Data','Histogram of numbers drawen from exponential distrubition lammda=0.5',bin_num,min_range,max_range)
    for i in range(sample_size):
        h.Fill(v[i])
    return h

def chi_sq(v=[],E=[],bin_num=0):
    #The chi sqaured (for a single bin) function with v as the number
    #of sample observables and E as the expected value
    sum=0
    for i in range(bin_num):
            sum+=((v[i]-E[i])**2/E[i])
    return sum

def create_experimental(bin_num,sample_size,l):
    #the summation over the different bins to obtain chi-sq
    E=[]
    for i in range(bin_num):
        min_range = float(i) / float(bin_num);
        max_range = float(i + 1) / float(bin_num)
        E.append(sample_size * pk(min_range, max_range, l))
    return E

def add_two_uniform_num(org_sample=[]):
    #adding a two uniform distubtion numbers to our sample vector
    two_rand = np.random.uniform(0, 1, size=2)
    return org_sample.extend(two_rand)

def add_n_more(c,org_sample=[],runs=1,bin_num=10,l=0.5,):
    #Adding a number of 2 uniform distributed numbers to our sample vector
    for i in range(runs):
        add_two_uniform_num(org_sample)
    E=create_experimental(bin_num, np.size(org_sample), l)
    h=create_hist_root_exp(np.size(org_sample), l, bin_num, org_sample)
    return (h,chi_sq(org_sample, E, bin_num))

#The start of the program
sample_size=100; l=0.5; bin_num=50
v=draw(sample_size,l)
E=create_experimental(bin_num,sample_size,l)
chi_sum=chi_sq(v,E,bin_num)
#some function to run ROOT ploting tools
gROOT.Reset()
c=TCanvas('c1','Exp distubition question')
c.Divide(3)
h=create_hist_root_exp(sample_size,l,bin_num,v)
c.cd(1)
h.Draw()
h.GetXaxis().SetTitle("Number")
h.GetYaxis().SetTitle("Counts of times the number was drawn")
h.SetTitle("A histogram of numbers drawen from exponential distrubition chi_sqr=%d" %chi_sum)
print(chi_sum)

#Above the end of the ploting using root and below test our sample vector

runs=1
hist_two=add_n_more(c,v,runs,bin_num,l)
c.cd(2)
hist_two[0].Draw()
hist_two[0].GetXaxis().SetTitle("Number")
hist_two[0].GetYaxis().SetTitle("Counts of times the number was drawn")
hist_two[0].SetTitle("A histogram of numbers drawen from exponential distrubition and two form uniform chi_sqr=%d" %hist_two[1])
runs=30
hist_alot=add_n_more(c,v,runs,bin_num,l)
print(hist_two[1])

c.cd(3)
hist_alot[0].Draw()
hist_alot[0].GetXaxis().SetTitle("Number")
hist_alot[0].GetYaxis().SetTitle("Counts of times the number was drawn")
hist_alot[0].SetTitle("A histogram of numbers drawen from exponential distrubition and a lot more form uniform chi_sqr=%d" %hist_alot[1])
print(hist_alot[1])

print(chi_sum)