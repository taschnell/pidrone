#! /usr/bin/env python3
"""
example  Python gpsd client
run this way: python3 example1.py.txt
"""

import gps               # the gpsd interface module

session = gps.gps(mode=gps.WATCH_ENABLE)

try:
    while 0 == session.read():
        if not (gps.MODE_SET & session.valid):
            # not useful, probably not a TPV message
            continue
        else:
            print('nah')

        print('Mode: %s(%d) Time: ' %
              (("Invalid", "NO_FIX", "2D", "3D")[session.fix.mode],
               session.fix.mode), end="")
        # print time, if we have it
        if gps.TIME_SET & session.valid:
            print(session.fix.time, end="")
        else:
            print('n/a', end="")

        if ((gps.isfinite(session.fix.latitude) and
             gps.isfinite(session.fix.longitude)) and gps.isfinite(session.fix.altMSL) and gps.isfinite(session.fix.altHAE) and gps.isfinite(session.fix.climb) and gps.isfinite(session.fix.speed)):
            print(" Lat %.6f Lon %.6f Speed(m/s) %.6f ",                  (session.fix.latitude, session.fix.longitude, session.fix.speed, session.fix.speed))
        else:
            print(" Lat n/a Lon n/a")

except KeyboardInterrupt:
    # got a ^C.  Say bye, bye
    print('')

# Got ^C, or fell out of the loop.  Cleanup, and leave.
session.close()
exit(0)
