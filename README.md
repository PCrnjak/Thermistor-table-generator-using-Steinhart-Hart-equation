# Thermistor-table-generator-using-Steinhart-Hart-equation

This code is used to create lookup tables for thermistors or similar semiconductors using Steinhart–Hart equation.
This is useful for 3d printers and other devices that use thermistors but dont want to waste computing power by calculating temperature
from equation shown at bottom. By using lookup table you can just read ADC value and that value is then mapped to correct temperature.

The equation is:

<img src="https://latex.codecogs.com/gif.latex?\frac{1}{T}&space;=&space;A&space;&plus;&space;B&space;*&space;ln(R)&space;&plus;&space;C&space;*&space;(ln(R))^{3}" title="\frac{1}{T} = A + B * ln(R) + C * (ln(R))^{3}" />

Where:
T is the temperature (in kelvins),
R is the resistance at {\displaystyle T}T (in ohms),
A, B, and C are the Steinhart–Hart coefficients, which vary depending on the type and model of thermistor and the temperature range of interest.

Needed modules
------------------

    ./configure
    pip install  matplotlib
     
All other modules should come when you download python

Use
------------------
You need to fill the bottom paramaters in this python script.
R_series is resistor connected in series to your thermistor
Table size is resolution of your ADC. In bottom example it is 10 bit ADC.
Vref is refrence voltage.
T1,T2,T3 are precise temperatures that you will have to mesure and then read the resistances 
Rt1,Rt2,Rt3 with multimeter. We need to mesure these parameters since we dont know A,B,C coeficients 
that are needed to get our thermistor curve that will be used as lookup table.

    ./configure
    R_series = 51000
    table_size = 1024
    Vref = 3.3

    T1 = 10 
    T2 = 36 
    T3 = 100 
    Rt1 = 186000
    Rt2 = 64000
    Rt3 = 7000
    
You will also need to type the location where you will save your table.txt file:
Change the bottom location code to your desired location. 
NOTE: use \\ when typing path

    ./configure
    # Save array witout last element to csv file
    np.savetxt(r'C:\\Users\\USER\\Desktop\\TABLE.txt', T_table, newline = ',',fmt= '%-1.1d')
    # Save last element to csv file (this remove last comma)
    file = open(r'C:\\Users\\USER\\Desktop\\TABLE.txt','a')
    
    
Once you filled those parameters run the script and you should get a curve like this one:

Good temperature mesures
------------------------
Getting good temperatures can be hard but you can get them at home by using bottom values:

* boiling water , should be 100 deg
* Inside of your fridge , usually temperature inside of your fridge is writen on the door (5-10 deg)
* Your body temperature , usually 36 deg can get that by using body thermometar

By using these temperatures you get really nice range of temperatures for the table.

Donate
------------------------

Copyright
------------------------
