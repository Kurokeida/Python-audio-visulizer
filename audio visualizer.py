
import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
from matplotlib.figure import Figure

CHUNK = 1024*2
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 90100
window = tk.Tk()

#%matplotlib tk
p = pyaudio.PyAudio()
stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer=CHUNK
)

fig, ax = plt.subplots()

x = np.arange(2, 10*CHUNK,10)
line, = ax.plot(x,np.random.rand(CHUNK),color="red")
ax.set_ylim(430, 1000)
ax.set_xlim(0, CHUNK)

while True:
    data = stream.read(CHUNK, exception_on_overflow=False)
    
    data_int = np.array(struct.unpack(str(2*CHUNK) +'B', data), dtype='b')[::2] + 500

    line.set_ydata(data_int)
    if data_int[0] < 500:
        line.set_color("red")
    if data_int[0] > 600:
        line.set_color("yellow")
    
    fig.canvas.draw()
    fig.canvas.flush_events()
