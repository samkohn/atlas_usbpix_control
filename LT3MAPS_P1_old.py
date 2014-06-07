"""
Hardware-specific implementation of Chip class to control the LT3Maps_P1 chip.

"""

from shiftregister import Chip
import visa

class ChipWithInstruments(Chip):
    """
    Control the LT3Maps_P1 chip using data generator, signal generator, and counter.

    """

    def __init__(self):
        """
        Connect to the function and data generators and to the counter.

        """
        self.function_generator = visa.GpibInstrument("GPIB::5",board_number=0)
        self.data_generator = visa.GpibInstrument("GPIB::3", board_number=0)
        self.counter = visa.GpibInstrument("GPIB::10", board_number=0)

    def test_connections(self):
        # Sets the voltage on the function generator to 0.2V
        self.function_generator.write("VOLT 0.2")
        
        # Print the display of the data generator
        print self.data_generator.ask("DISP?")
        
        # Presets the counter to default and selects the positive trigger slope
        self.counter.write("*RST");
        self.counter.write(":CONF:TOT:CONT")

if __name__ == "__main__":
    myChip = ChipWithInstruments()
    print "testing connections"
    myChip.test_connections()