Feature: Application Mode

   Scenario: Firmware image is automatically loaded
       Given an unpowered STM32F412G connected via USART
       And the kit is loaded withvalid BLANK firmware
       When the kit is powered on
       Then the BLANK firmware is loaded
       And bootloader mode is not entered
       And the BOOTLOADER WELCOME MESSAGE is not printed to the CLI
