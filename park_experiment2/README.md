## Plane to see: Experiment 3, going 2D


In this experiment,  two reflectors are used seperated by a distance of 20m.  The initiator then connects to each in turn (because I couldn't get two reflectors sounding at the same time, see my [devzone ticket](https://devzone.nordicsemi.com/f/nordic-q-a/124351/channel-sounding-using-multiple-reflectors)), gets raw data and does some math to estimate position on the plane.


The [serial log dump](./serial_20250915_143537.txt) contains a bunch of logging, quick summaries for me to be able to see what's up out in the field, etc.  The lines used for processing are the "Resfull" which look like


```
Resfull,1,3.571,6.155,3.779,21.373,21.018,21.229,-1.102,3.358,-0.097,6.138,-0.910,3.635,-1.102,3.358,-0.097,6.138,-0.910,3.635
```

These lines are

  * "Resfull" line identifier
  * datetime
  * prefix
  * curcon
  * c0_fft
  * c0_phase
  * c0_rtt
  * c1_fft
  * c1_phase
  * c1_rtt
  * fft_x
  * fft_y
  * phase_x
  * phase_y
  * rtt_x
  * rtt_y
  
With the "cN" items being raw estimations for connection N, and the various `_x` and `_y` being the calculated position based on related pairs of distance estimates.


The code actually crashed a couple of times while I was logging, need to work on that code.  It basically picked up where it left off, but that would cause a huge jump on the first reported values every time.

