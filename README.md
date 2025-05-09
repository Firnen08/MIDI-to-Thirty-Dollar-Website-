# MIDI to Thirty Dollar Website Converter

## About
Converts MIDI files to TDW Files. 

## Demos
[Demo OG](https://youtu.be/Ipu868-USc8)

[Demo GUI](https://youtu.be/004fRGgsQXw)

## Usage (No GUI)

* Clone This repo: `https://github.com/Firnen08/MIDI-to-Thirty-Dollar-Website-.git`
* Install requirements `pip install -r src\requirements.txt`
* Add MIDI Files to the /in folder (make it if it doesnt exist using)
```
mkdir in && mkdir out
```
![alt text](image-1.png)

Creates both of the folders required
* Run `run.bat`

Output files will show up at /out

![alt text](image.png) 

## Usage (GUI)

![alt text](image-2.png)

A simple Python GUI is now included!
You can select any MIDI file from your computer and convert it with a click.

To run the GUI:
```
python src\main.py --gui
```

or you can run the batch file to easily launch the GUI (from the project root):
```
gui.bat
```

## Running (OG Github Stuff)

~~I highly recommend you download the [Thirty Dollar Website rewrite](https://greasyfork.org/en/scripts/439347-thirty-dollar-rewrite) for a smoother playback, especially when dealing with larger files.~~ TDW has updated their audio system. 

Some MIDI Files also use non-percussion notes on channel 10 - which is reserved for percussion. This screws up the conversion so it is best to just disable percussion in [midi2tdw.py](https://github.com/yangman946/MIDI-to-Thirty-Dollar-Website-/blob/main/midi%20to%2030%20dollar%20website/midi2tdw.py)

## Contributing

This project is a work in progress, If you wish to contribute, submit a pull request and I will look at it ASAP. 

## Credits
All credits and original code goes to https://github.com/yangman946 As he's the one who made MIDI-to-Thirty-Dollar-Website converter

## Limitations

* Haven't fully tested percussion
* Combining and timing bugs

