
# <center>Python for embedded development</center>

### <center>What is an [embedded system](https://www.pcmag.com/encyclopedia/term/42554/embedded-system)?</center>

Any electronic system that uses a computer chip, but that is not a general-purpose workstation, desktop or laptop computer. Such systems use microcontrollers (MCUs) or microprocessors (MPUs), or they may use custom-designed chips. Deployed by the billions each year in myriad applications, the embedded systems market uses the lion's share of electronic components in the world.

Embedded systems are employed in cars, planes, trains, space vehicles, machine tools, cameras, consumer electronics, office appliances, network appliances, cellphones, GPS navigation as well as robots and toys. Low-cost consumer products can use microcontroller chips that cost less than a dollar. See microprocessor and microcontroller.

### [Microcontroller](https://www.pcmag.com/encyclopedia/term/46924/microcontroller)

A single chip that contains the processor (CPU), non-volatile memory (flash memory or ROM) for the program, volatile memory (RAM) for processing the data, a clock and an I/O control unit. Microcontroller units (MCUs) are available in numerous sizes and architectures. See CPU, flash memory, ROM, RAM and clock.

### [System on a Chip](https://www.pcmag.com/encyclopedia/term/51603/soc)

System-On-Chip - Pronounced "S-O-C." An electronic system on a single chip. A system-on-chip (SoC) typically includes a CPU along with graphics and other processing components. For example, a smartphone SoC would include the processor cores, graphics processing unit (GPU), memory caches and a neural processing unit (NPU). In this case, NAND flash storage, RAM, camera, audio, power and numerous small ICs are on the device's motherboard outside the SoC.

### Why Python for embedded development and learning?

- C/C++ bindings
- Speed of development/prototyping
- REPL
- stdlib
- Ecosystem
- Tooling


### [MicroPython](https://micropython.org/)

a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimised to run on microcontrollers and in constrained environments. 

```python
"""Hello World! from MicroPython"""
import time
from pyb import LED

led = LED(1)
led.toggle()

while True:
    led.on()
    time.sleep(1)           # sleep for 1 second
    led.off()
    time.sleep_ms(500)      # sleep for 500 milliseconds
```

### [CircuitPython](https://circuitpython.readthedocs.io/en/latest/docs/index.html)

CircuitPython is a fork of MicroPython with the goal of being beginner friendly and targeted for use on microcontrollers. 

```python
"""Hello World! from CircuitPython"""
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
```

# <center>Demo</center>

## <center>[CircuitPython Getting Started](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython)</center>

### <center>Some of the ins and outs of how we just did that.</center>

### [Bootloader](https://www.pcmag.com/encyclopedia/term/38843/boot-loader)

A small program that calls the operating system into memory (RAM) after the power is turned on. The boot loader may reside in the boot sector of the hard drive (or SSD) or in a chip. In more secure systems, the boot loader may load a second-level boot program, which then loads the operating system. Sometimes, the boot loader and boot manager, which enables one of several operating systems to be selected, are combined in the same program. See boot, boot manager, boot sector and secure boot. [7]

[UF2](https://learn.adafruit.com/installing-circuitpython-on-samd21-boards/installing-the-uf2-bootloader)

### [Firmware](https://www.pcmag.com/encyclopedia/term/43223/firmware)

(FIRM softWARE) Software instructions residing in non-volatile storage that holds its content without power. Firmware is found on computer motherboards to hold hardware settings and boot data (see BIOS) and on myriad consumer electronics devices to hold the operating system. [8]

[CircuitPython](https://circuitpython.org/)

### [Bootsequence](https://www.pcmag.com/encyclopedia/term/56508/first-boot-sequence)

The search sequence of peripheral devices to find the operating system. If the computer cannot locate the OS in the first device, it looks in the second and so on

[CircuitPython Boot Sequence](https://learn.adafruit.com/assets/75708)

### [VM/Interpreter](https://www.pcmag.com/encyclopedia/term/45287/interpreter)

A high-level programming language translator that translates and runs the program at the same time. It converts one program statement into machine language, executes it, and then proceeds to the next statement. This differs from regular executable programs that are presented to the computer as binary-coded instructions. Interpreted programs remain in the source language the programmer wrote in, which is human readable text.

[Circuit/Micro Python](https://circuitpython.readthedocs.io/en/4.x/docs/porting.html)

### Standard Library

CircuitPython comes 'with the kitchen sink' - a lot of the things you know and love about classic Python 3 (sometimes called CPython) already work. There are a few things that don't but we'll try to keep this list updated as we add more capabilities!

[CircuitPython Builtins](https://learn.adafruit.com/circuitpython-essentials/circuitpython-built-ins)

[CircuitPython Modules](https://circuitpython.readthedocs.io/en/latest/shared-bindings/index.html)

## Additional Resources

#### Sites
- [Adafruit](http://adafruit.com/)
- [Hackaday](https://hackaday.com/)
- [Embedded](https://embedded.fm/blog-index)
- [Embedded Artistry](https://embeddedartistry.com/)
- [PC Mag Encyclopedia](https://www.pcmag.com/encyclopedia)

#### Books
- [Make: Electronics](http://shop.oreilly.com/product/9780596153755.do)
- [Making Embedded Systems](http://shop.oreilly.com/product/0636920017776.do)
- [Programming with MicroPython](http://shop.oreilly.com/product/0636920056515.do)

#### Podcast
- [Embedded](https://embedded.fm/)
- [Amp Hour](https://theamphour.com/)
- [Hackaday](https://hackaday.com/category/podcasts/)
- [Adafruit](https://www.youtube.com/adafruit)

#### Social
- [Adafruit Discord](https://discordapp.com/invite/adafruit)
- [Hackaday IO](https://hackaday.io/)

#### Interesting:
- [Evaluation of MicroPython as Application Layer Programming Language on CubeSats](https://ieeexplore.ieee.org/document/7948548)


```python

```
