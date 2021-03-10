import numpy as np
import matplotlib.pyplot as plt

m = []
x = []
y = []
z = []
vx = []
vy = []
vz = []


######## Masses

# with open('masses.txt',newline='') as f:
#     lines = f.readlines()
#     lines = [line.strip() for line in lines]
#     asciimass = [line.split(',')[0] for line in lines]
#     asciimass.remove('')
#     mass = [float(m) for m in asciimass]
#     mass = [m*np.power(10,10) for m in mass]
#
# # bins = np.linspace(min(mass),max(mass),20)
# logbins = np.logspace(np.log10(min(mass)),np.log10(max(mass)),20)
#
# t = np.linspace(3,60,1000)
# f = 125000*pow(t,-1.3)
#
# plt.plot(t,f,'g',label='Kroupa2001')
#
# plt.hist(mass, logbins)
# plt.xscale('log')
# plt.yscale('log')
# plt.title('Mass distribution(log-log), 143168 stars')
# plt.xlabel('Mass')
# plt.ylabel('Count')
# plt.legend()
# plt.show()

###### Coordinates(don't use this block) ################

# infile = open('coordinates.txt','rt')
# outfile = open('koordinates.txt','wt')
# for line in infile:
#     fout.write(line.replace(',',' '))
# infile.close()
# outfile.close()
#
# with open('koordinates.txt',newline='') as g:
#     lines = g.readlines()
#     lines = [line.strip() for line in lines]
#     asciix = [line.split()[0] for line in lines]
#     x = [float(i) for i in asciix]
#     print(len(x))
#     asciiy = [line.split(', |, |,')[-1] for line in lines]
#     print(asciiy)
    # print(asciiy)
    # asciiz = [line.split(', ')[2] for line in lines]
#     asciix.remove('')
#     asciiy.remove('')
#     asciiz.remove('')
#     x = [float(i) for i in asciix]
#     y = [float(j) for j in asciiy]
#     z = [float(k) for k in asciiz]
#     xx = [i**2 for i in x]
#     yy = [j**2 for j in y]
#     zz = [k**2 for k in z]
#
##########################################################


xmean = sum(x)/len(x)
ymean = sum(y)/len(y)
zmean = sum(z)/len(z)

vxmean = sum(vx)/len(vx)
vymean = sum(vy)/len(vy)
vzmean = sum(vz)/len(vz)

rr = []
for i in range(len(x)):
    rr.append(x[i]**2+y[i]**2+z[i]**2)

r = [np.sqrt(element) for element in rr]


vv = []
for j in range(len(vx)):
    vv.append(vx[j]**2+vy[j]**2+vz[j]**2)

v = [np.sqrt(element) for element in vv]



### r hist
#
# logbins = np.logspace(np.log10(min(r)),np.log10(max(r)),20)
#
# plt.hist(r,logbins)
# plt.title('Spatial distribution(log-log), 143168 stars')
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel('r (kpc)')
# plt.ylabel('Count')
#
# w = np.linspace(4e-5,6e-2,500)
# plummer = 1.4*w*w*w*np.power(0.000009+w**2,-5/2)
#
# plt.plot(w,plummer,'g',label='Plummer')
# plt.legend()
# plt.show()
#

### Is it correctly centered at 0?
# xbins = np.linspace(min(x),max(x),10)
# ybins = np.linspace(min(y),max(y),10)
# zbins = np.linspace(min(z),max(z),10)
#
# fig, axes = plt.subplots(3)
# fig.suptitle('Coordinates, 143168 stars')
# axes[0].hist(x,xbins)
# axes[1].hist(y,ybins)
# axes[2].hist(z,zbins)
# axes[0].set_yscale('log')
# axes[1].set_yscale('log')
# axes[2].set_yscale('log')
# axes[0].set(ylabel='x, mean=%f' %xmean)
# axes[1].set(ylabel='y, mean=%f' %ymean)
# axes[2].set(xlabel='kpc', ylabel='z, mean=%f' %zmean)
# plt.show()


# ## (velocity) Is it correctly centered at 0?
# vxbins = np.linspace(min(vx),max(vx),11)
# vybins = np.linspace(min(vy),max(vy),11)
# vzbins = np.linspace(min(vz),max(vz),11)
#
# fig, axes = plt.subplots(3)
# fig.suptitle('Velocities, 143168 stars')
# axes[0].hist(vx,vxbins)
# axes[1].hist(vy,vybins)
# axes[2].hist(vz,vzbins)
# axes[0].set_yscale('log')
# axes[1].set_yscale('log')
# axes[2].set_yscale('log')
# axes[0].set(ylabel='vx, mean=%f' %vxmean)
# axes[1].set(ylabel='vy, mean=%f' %vymean)
# axes[2].set(xlabel='km/s', ylabel='vz, mean=%f' %vzmean)
# plt.show()

######### r-v plot

plt.scatter(r, v, s=0.01)
plt.title('r-|v| relation, $M_{tot}=10^6 M_S$')
plt.xlabel('r (kpc)')
plt.ylabel('|v| (km/s)')

w = np.linspace(4e-5,6e-2,500)
plummerpotential = 5*np.sqrt(1./np.sqrt(w*w+0.000009))
sigma=plummerpotential/np.sqrt(12)

plt.plot(w,plummerpotential,'g',label='$(1/2)v_{max}^2=\Phi_{Plummer}$')
plt.plot(w,sigma,'r',label='$\sigma(r)$')
plt.legend()


# plt.xscale('log')
# plt.yscale('log')
plt.show()
