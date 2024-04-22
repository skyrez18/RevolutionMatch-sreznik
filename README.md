# RevolutionMatch-sreznik

### Overview:
This program intakes a .txt file <sup>1</sup> with data for number of gears, specific gear ratios, differential ratio <sup>2</sup> and tire diameter to create an output (in revolutions per minute) of the engine speeed of the car with the specified specifications. Simplified, this is a digital tachometer.

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

<sup>2</sup> Some cars that have variable differential ratios like the Ford Focus RS. Follow this format of .txt file to use varible differention technology:
```txt
6                                    (Number of gears)
3.23               (Gear ratios for gears 1 through n)
1.95               '                                 '
1.32               '                                 '
1.03               '                                 '
1.13               '                                 '
.94                '_________________________________'
4.063                          (differential ratio #1)
25.1                          (tire diameter (inches))
6800                                         (redline)
2.955                          (differential ratio #2)
2                        (Number of gears that use it)
```

### When in the simulation:
<div style="background-color; border: 1.5px solid #ddd; padding: 10px;">
Use the keys 'a' to accelerate the car and 'd' to decelerate the car. <br>
Use the keys 'UP' to shift to a higher number gear and 'DOWN' to shift to a lower number gear.</div>

## Project #TODO List:
### General Tasks
- [ ] Smooth refresh rate on needle when shifting
- [ ] Shift lights