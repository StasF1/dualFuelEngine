'''----------------------------------------------------------------------------
       ___       |
     _|˚_ |_     |   Language: Python
    /  ___| \    |   Version:  3.x
    \_| ____/    |   Website:  https://github.com/StasF1/dualFuelEngine
      |__˚|      |
----------------------------------------------------------------------------'''

from math import pi

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

tmpFolder          = 'tmp*' # path to Diesel-RK results folder


terminalOutput     = 'true' # true or false

saveFormat         = 'txt' # None, csv or txt (coordinates is writen in the .csv, velocities in the .txt)

cylParPlot         = 'false' # true or false

inOutParPlot       = 'false' # true or false

movingPartsPlot    = 'false' # true or false

inletInjectionPlot = 'false' # true or false

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

n                  = 92 # RPM

S                  = 2.7 # m


IPO                = 42 # ˚CA before BDC

IPC                = IPO # ˚CA after BDC

EVO                = 85 # ˚CA before BDC

EVC                = 46 # ˚CA after BDC

inletArea          = 1.092e-03 # m^2


injG_max           = 1 # kg/s, q_injGas = 95 (g), t_injGas = 0.0815 (s)

injCA2Max          = 10 # ˚CA

injArea            = pi*pow(3.75e-03, 2)/4*2 # m^2, area which equals of the two injector orifices d = 3.75 (mm)

injT               = 380 # K (estimated)

injP               = 150e+05 # Pa (estimated)

injR               = 518.3 # J/mol/K specific gas constant


# *****************************************************************************
