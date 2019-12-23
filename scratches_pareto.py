from ROOT import gROOT,TCanvas,TH1F
import numpy as np
import matplotlib.pyplot as plt


def create_hist_root(bin_num,min_range,max_range,v):
    h=TH1F('Data','The pareto Distubtion function',bin_num,min_range,max_range)
    for i in range(np.size(v)):
        h.Fill(v[i])
    return h

def chi_sq_k(d,N,pk):
    return ((d-N*pk)**2)/(N*pk)

def chi_sq(d,N,p,B):
    sum=0
    for k in range(B):
        sum+=chi_sq_k(d[k],N,p[k])
    return sum

def pk(min,max,alpha,xm):
    return xm/(min**alpha)-xm/(max**alpha)

def p(new_pareto,alpha,xm):
    vec_of_p=[]
    for i in range(np.size(new_pareto)-1):
        vec_of_p.append(pk(i+xm,i+xm+1,alpha,xm))
    return vec_of_p

def create_pareto(a,m):
    return (np.random.pareto(a, 1000) + 1) * m

a, m = 3., 2.
d = (np.random.pareto(a, 1000) + 1)*m
B=20; max_check=26; c=[]
N=np.size(d)
alpha_vec=[]
for i in range(10,max_check):
    new_alpha=(i+0.1)/10
    alpha_vec.append((new_alpha))
    new_pareto=create_pareto(new_alpha,m)
    pk_vec=p(new_pareto,new_alpha,m)
    c.append(chi_sq(d,N,pk_vec,B))

fig=plt.gcf()
plt.plot(alpha_vec,c)
plt.xlabel('Alpha')
plt.ylabel('Chi squared')
plt.title('The chi sqaure value as a function of alpha')
plt.show()
fig.savefig('/home/elad/Pareto.png',dpi=100)