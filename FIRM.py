import pyaudio
import wave
import struct

CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 4
RATE = 16000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index = 2)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    count = len(data)/2
    format = "<%dh"%(count)
    x = struct.unpack(format,data)
    for i in range(len(x)):
        if(x[i] > x[i+1]+40 and x[i] > x[i+2]+40 and x[i] > x[i+3]+40):
            print "left side"
        
'''        
frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
'''
