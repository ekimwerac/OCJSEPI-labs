#! /usr/bin/python
import os
start_time = 0,

########################################################
# TIMER FUNCTIONS
def start_timer():
    """
    The start_timer() function marks the start of 
    a timed interval, to be completed by end_timer().
    This function requires no parameters.
    """
    global start_time
    start_time = os.times()[:2]
    st=os.times()
    return

def end_timer(txt='End time'):
    """
    The end_timer() function completes a timed interval
    started by start_timer.  It prints an optional text
    message (default 'End time') followed by the CPU time
    used in seconds.
    This function has one optional parameter, the text to 
    be displayed.
    """
    et = os.times()
    end_time = et[:2]
    print(type(end_time), end_time, et)
    print(type(start_time), start_time)
    print(os.times())
    print("{0:<12}: {1:10.3f} seconds".format(txt, end_time[0] +  end_time[1] - start_time[0] + start_time[1]))
    return

start_timer()
lines = 0
for row in open("words"):
    lines += 1
    
end_timer()
print ("Number of lines:", lines)
