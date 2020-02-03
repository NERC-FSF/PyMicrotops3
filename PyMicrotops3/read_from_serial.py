import serial
import os
import sys
import time
import logging

def read_microtops_serial(port, outfile):
    # Open the given serial port
    ser = serial.Serial(port, 4800, timeout=1)
    logging.info("Initiated communication")
    time.sleep(0.5)
    # Input a carriage return and new line to access the menu
    ser.write(b"\r\n")
    logging.info("Reading data")
    # Reads the menu list lines
    menu = ser.readlines()
    # Inputs P, selecting data buffer print option
    ser.write(b"P")
    # Read the data buffer output
    data = ser.readlines()
    # Closes the serial port
    ser.close()
    # We don't want the first two lines of the data
    # (just tells us that it is Microtops data) or the last one (just says END)
    data = data[2:-1]
    #Replaces the carriage return and newline characters
    data = [line.replace(b"\r", b"").replace(b"\n", b"") + b"\n" for line in data]
    
    if os.path.exists(outfile):
        logging.info("File already exists, so appending.")
        # Already has header, so we don't need to write a header again
        # - so remove the first line from the list
        towrite = data[1:]
    else:
        # Doesn't have a header, so write everything
        towrite = data
        
    logging.info("Writing data")
    f = open(outfile, "ab")
    f.writelines(towrite)
    f.close()
    print("Data saved to %s. Exiting" % outfile)
    
def read_microtops_gui():
    print("Microtops II Reading Software")
    print("by Robin Wilson")
    print("adapted to Python 3.6 by NERC Field Spectroscopy Facility")
    print("-----------------------------")
    # Get the parameters either from the command-line or by asking the user

    port = input("Enter the serial port to use (eg. COM8 or /dev/serial):\n")
    outfile = input("Enter the full path to the file to write to:\n")

    print("Reading data...")
    read_microtops_serial(port, outfile)

def main():
    if len(sys.argv) == 3:
        port = sys.argv[1]
        outfile = sys.argv[2]
        read_microtops_serial(port, outfile)
    else:
        read_microtops_gui()


if __name__ == '__main__':
    main()    
    
    

    
    


