"""
Read and write to the shift register of the LT3Maps_P1 chip.

Hardware: LT3Maps_P1 chip, USBpix Multi-IO board, FE-I4 adapter card.
Software: pyBAR

"""


class Chip(object):
    """
    The LT3Maps_P1 chip.

    Control the chip's shift registers. Syntax for reading and writing
    is to use lists of Chip.HIGH and Chip.LOWs.

    """

    HIGH = 1
    """
    Represents a HIGH level in input or output.
    
    """
    LOW = 0
    """
    Represents a LOW level in input or output.

    """

    def __init__(self):
        """
        Connect to the chip.

        """
        self.num_columns = 16
        self._current_column = 0

    def clock_in_bits(self, input_bits):
        """
        Write the current column's shift register and return the output.

        Give the bits as a list of Chip.HIGH and Chip.LOWs.
        Shift in the first bit of the list first. Returns a list with the first
        output bit first (i.e. the order the bits are shifted out).
        To change columns, use set_column().

        """
        output_bits = []
        for bit in input_bits:
            self._set_input(bit)
            output_bits.append(self._advance_clock())
        return output_bits

    def set_column(self, column_number):
        """
        Set the (double-) column number read/write.

        Assuming the columns start at number 0.

        """
        # Note: the order is reversed since the first bit to go in corresponds to
        # the highest-numbered column.
        self._set_column_register_input(Chip.LOW)
        self._advance_column_register_clock(self.num_columns-column_number-1)
        self._set_column_register_input(Chip.HIGH)
        self._advance_column_register_clock(1)
        self._set_column_register_input(Chip.LOW)
        self._advance_column_register_clock(column_number)

    def get_column(self):
        """
        Get the (double-) column number to read/write.

        """
        return self._current_column

    def _advance_clock(self, num_clocks=1):
        """
        Send num_clocks clock signals to the column data register and return the output.

        """
        pass

    def _set_input(self, level):
        """
        Set the input level to send to the column data register.

        """
        pass

    def _advance_column_register_clock(self, num_clocks=1):
        """
        Send num_clocks clock signals to the column selector register and return the output.

        """
        pass

    def _set_column_register_input(self, level):
        """
        Set the column shift register input level.

        Level could be Chip.HIGH or Chip.LOW

        """
        pass
