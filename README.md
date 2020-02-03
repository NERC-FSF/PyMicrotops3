# PyMicrotops3
A module which allows for the reading and processing of data from a Microtops II sun photometer. The package communicates with a Microtops II sun photometer, reads the data buffer from the instrument, and writes that data to a .csv file. The module also allows the user to process the data from the instrument. 

This module was originally developed by Dr. Robin Wilson as PyMicrotops. This version updates the software so that it can be used within environments using Python 3. The original module can be found at https://github.com/robintw/PyMicrotops

**Installation**

The module can be installed through the git package -- 
```
pip install git+https://github.com/NERC-FieldSpectroscopyFacility/PyMicrotops3.git
```

**Reading data from Microtops II sun photometer**
1. Connect the Microtops II sun photometer via RS-232 or a serial-to-USB connection
2. Identify the COM port in use (e.g. on Windows, "COM6", or on Linux distributions, "/dev/ttyS0")
3. 
```python
from PyMicrotops3 import read_from_serial
```
3. Run ```read_from_serial.read_microtops_gui()``` 
4. Input the COM port and name of the file to save data to

**Processing data from the Microtops II sun photometer**

The following code example demonstrates the processing functions of the package -- 

```python
from PyMicrotops import Microtops
m = Microtops('microtopsfile.csv')
# Plot all of the AOT data
m.plot()
# Plot for a specific time period
m.plot('2014-07-10','2014-07-19')
# Get AOT at a specific wavelength - interpolating if needed
m.aot(550)
```

