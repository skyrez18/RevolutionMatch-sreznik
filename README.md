# RevolutionMatch-sreznik

### Overview:
This program intakes a .txt file <sup>1</sup> with data for number of gears, specific gear ratios, differential ratios <sup>2</sup> and tire diameter to create an output (in revolutions per minute) of the engine speeed of the car with the specified specifications. Simplified, this is a digital tachometer.

<sup>1</sup> .txt file format should be as follows:
```txt
5                                    (Number of gears)
3.07               (Gear ratios for gears 1 through n)
1.77               '                                 '
1.19               '                                 '
0.87               '                                 '
0.70               '_________________________________'
4.40                              (differential ratio)
25.7                          (tire diameter (inches))
6000                                         (redline)
```

<sup>2</sup> Unfortunatley there are some cars that have variable differential ratios like the Ford Focus RS, currently the program is not set up to deal with more than 1 differential ratio. This may cahange in the future.

### When in the simulation:
<div style="background-color; border: 1.5px solid #ddd; padding: 10px;">
Use the keys 'a' to accelerate the car and 'd' to decelerate the car. <br>
Use the keys 'UP' to shift to a higher number gear and 'DOWN' to shift to a lower number gear.<br>
A 'money shift' will terminate the program.</div>

## Project #TODO List:
### General Tasks
- [ ] Money shift (1000 over redline) kills program
- [ ] Agressive downshift will rev down to red line (shifting within 1000 rpm of redline)
- [ ] Implement a good way to be less than 1000 rpm (currently hardcoded)
- [ ] Create project timeline
- [ ] Identify stakeholders
- [ ] Stall ? low rpms
### Beauty Improvements
- [ ] Smooth refresh rate on needle when shifting
