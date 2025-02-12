With this program, you will be able to extract the data from the sensor, read this data in another file and convert it into your graph.
So, how do we do this? First of all, I will tell you the materials I have: 
1 Raspery pi zero 2w
1 zmpt101b 
4 female to female cable
The arrangement of the cables will be as follows: zmpt gnd to zero gnd,
zmpt gnd to zero gnd, zmpt out to zero any gpio, zmpt vcc to zero will be plugged into 5v pin or 3.3 v pin.
Then we will throw the codes we wrote into our zero and run the terminal, but of course, first of all, 
replace the pin value in the data_writing file with the pin you installed yourself (the place we call zero's any gpio) and save it,
then make the connections, you are done electronically, all you have to do is plug the ends of the place where you want to measure 
the volts with zmpty, but let me tell you something like this: zmpt returns an adc value, but zero 2w cannot get this value on its own,
so tell us It will return 1 or 0. If you want to return a different value, find a tool that converts the analog current to digital 
current and put it between the two, but this code does not work for them. After setting the voltage location, run your Raspery Zero 2w,
enter the terminal and write the location of the files of the code I wrote into the terminal, how "python3 home/pi/veri/veri_write.py" 
(write without quotes, write first, then read) and Our program is completed.
