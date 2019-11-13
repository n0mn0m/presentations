import board
import busio
import digitalio
import adafruit_rfm9x
import time

class OpenInterface:
    def __init__(self, tx_pin, rx_pin, brc_pin, baud_rate=115200):
        self._board = busio.UART(tx_pin, rx_pin, baudrate=baud_rate)
        self._tx_pin = tx_pin
        self._rx_pin = rx_pin
        self._brc_pin = brc_pin
        self._baud_rate = baud_rate
        self._operating_mode = "off"

        self._brc_pin.direction = digitalio.Direction.OUTPUT

    @property
    def operating_mode(self):
        return self._operating_mode

    @operating_mode.setter
    def operating_mode(self, new_mode):
        self._operating_mode = new_mode

    def command(self, new_command):
        self._board.write(new_command)

    def wake_up(self):
        for i in range(3):
            self._brc_pin.value = False
            time.sleep(0.5)
            self._brc_pin.value = True
            time.sleep(0.5)
            self._brc_pin.value = False
            time.sleep(0.5)

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

cs = digitalio.DigitalInOut(board.RFM9X_CS)
reset = digitalio.DigitalInOut(board.RFM9X_RST)

rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 433.0)

bot = OpenInterface(board.TX, board.RX, digitalio.DigitalInOut(board.A1))

bot.wake_up()

while True:
    packet = rfm9x.receive(3)  # Wait for a packet to be received (up to 0.5 seconds)
    if packet is not None:
        print('Starting')
        bot.command(b'\x80')
        bot.command(b'\x83')
        bot.command(b'\x87')
        time.sleep(5)
    else:
        bot.command(b'\x85')
        bot.command(b'\xAD')
        print('Stopping')
