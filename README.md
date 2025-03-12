With this program, you will be able to extract the data from the sensor, read this data in another file and convert it into your graph.
So, how do we do this? First of all, I will tell you the materials I have: \n
1 Raspery pi zero 2w \n
1 zmpt101b \n
4 female to female cable\n
The arrangement of the cables will be as follows: zmpt gnd to zero gnd,\n
zmpt gnd to zero gnd, zmpt out to zero any gpio, zmpt vcc to zero will be plugged into 5v pin or 3.3 v pin.\n
Then we will throw the codes we wrote into our zero and run the terminal, but of course, first of all, \n
replace the pin value in the data_writing file with the pin you installed yourself (the place we call zero's any gpio) and save it,\n
then make the connections, you are done electronically, all you have to do is plug the ends of the place where you want to measure \n
the volts with zmpty, but let me tell you something like this: zmpt returns an adc value, but zero 2w cannot get this value on its own,\n
so tell us It will return 1 or 0. If you want to return a different value, find a tool that converts the analog current to digital \n
current and put it between the two, but this code does not work for them. After setting the voltage location, run your Raspery Zero 2w,\n
enter the terminal and write the location of the files of the code I wrote into the terminal, how "python3 home/pi/veri/veri_write.py" \n
(write without quotes, write first, then read) and Our program is completed.
