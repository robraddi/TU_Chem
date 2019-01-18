# IPython log file

get_ipython().magic(u'll')
get_ipython().magic(u'log')
get_ipython().magic(u'dhist')
get_ipython().magic(u'dirs')
get_ipython().magic(u'logstart')
get_ipython().magic(u'hist')
get_ipython().magic(u'history')
get_ipython().magic(u'clear')
help(%clear)
get_ipython().magic(u'clear -help')
get_ipython().magic(u'gui')
get_ipython().magic(u'page')
get_ipython().run_cell_magic(u'bash', u'', u'touch numbers.txt\njob="count"  #the object that you want to toggle\nnum=10\nenu=(zero one two three four five six \\\n     seven eight nine ten)\n\nif [ $job == "count" ]; \nthen\n    for i in $(seq 0 $num);\n    do\n        if [ $i -eq 3 ] || [ $i -eq 7 ] ;\n        then echo ${enu[i]}\n        \n        else\n            echo $i\n        fi\n    done\nelse\n    echo ${enu[$num]}\nfi')
get_ipython().magic(u'page')
import os
path = 'testing.txt'
data = pd.read_csv(path)
data.head()
#data.tail()
import os,
import pandas as pd
path = 'testing.txt'
data = pd.read_csv(path)
data.head()
#data.tail()
import os
import pandas as pd
path = 'testing.txt'
data = pd.read_csv(path)
data.head()
#data.tail()
get_ipython().magic(u'page')
get_ipython().magic(u'cd ./ThinkDSP/code/')
from __future__ import print_function, division
import thinkdsp
import thinkplot
import numpy
import numpy as np
import scipy.fftpack
from scipy.fftpack import fft as fft
from scipy.fftpack import ifft as ifft
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
wave = '/volumes/RDRIVE/Fall2017/Instrumental_Design/Project/dance_of_the_goblins.wav'
response = thinkdsp.read_wave(wave)
start = 2.0
duration = response.duration/65.
response = response.segment(start=start, duration=duration)
response.shift(-start)
response.normalize()
print(duration,'seconds')
response.make_audio()
segment = response.segment(start=start,duration=duration)
segment.normalize()
data = segment.quantize(bound=True,dtype=float)
print('Number of data points = ',len(data))
# Waveform:
total_time = segment.duration+start
x = np.array([total_time/len(data)*i for i in range(0,len(data),1)])
y = [data[i] for i in range(0,len(data),1)]

# Fourier Transform
# Number of sample points
n = len(y) # len = length of a vector
d = 1/response.framerate
print('timestep = ',d)
FT_y = fft(y)
freq = np.fft.fftfreq(n,d)
xf,yf = [],[]
for i in range(0,len(FT_y)):
    if freq[i] > 0 and FT_y[i] >0:
        yf.append(FT_y[i])
        xf.append(freq[i])
        #xf.append(freq[i]*10**(4.))

#fs = np.fft.fftfreq(n, d)
get_ipython().magic(u'pylab inline')
fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111)    # The big subplot
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
# Subplot with linear fitting:
ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

ax1.plot(x,y,'k')
#ax1.plot(x,y,label="_nolegend_")
ax1.set_xlabel('Time,t/(seconds)', fontsize=16)
ax1.set_ylabel('Signal Intensity', fontsize=16)

# Fourier Transform:
ax2.plot(xf,yf,'k')

ax2.set_xlabel('Frequency, $\\nu$ /(Hz)', fontsize=16)
ax2.set_ylabel('', fontsize=16)

ticks = [ax2.xaxis.get_minor_ticks(),ax1.yaxis.get_minor_ticks(),
         ax2.xaxis.get_major_ticks(),ax1.yaxis.get_major_ticks()]
marks = [ax1.get_xticklabels(),ax2.get_xticklabels(),
        ax1.get_yticklabels(),ax2.get_yticklabels()]

for k in range(0,len(ticks)):
    for tick in ticks[k]:
        tick.label.set_fontsize(16)
for k in range(0,len(marks)):
    for mark in marks[k]:
        mark.set_size(fontsize=16)
        mark.set_rotation(s=15)

fig.tight_layout
fig.show()
get_ipython().magic(u'page')
get_ipython().magic(u'clear')
get_ipython().magic(u'who')
get_ipython().magic(u'who_ls')
get_ipython().magic(u'whos x')
get_ipython().magic(u'whos')
get_ipython().magic(u'clear')
get_ipython().magic(u'whos')
get_ipython().magic(u'll')
