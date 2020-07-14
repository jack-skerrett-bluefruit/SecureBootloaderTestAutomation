Feature: CLI

   Scenario: "flash" command allows firmware to be sent via serial
       Given an STM32F412G discovery kit connected via USART
       And the kit is in bootloader mode with the ">" command prompt displayed
       When "flash 500" is entered
       Then the message "BLANK" is printed to the CLI

   Scenario: "help" command displays a list of all current commands
       Given an STM32F412G discovery kit connected via USART
       And the kit is in bootloader mode with the ">" command prompt displayed
       When the "help" command is sent
       Then a list of all current commands is returned (SEE REFERENCE)

   Scenario: An erroneous command is ignored by the bootloader
       Given an STM32F412G discovery kit connected via USART
       And the kit is in bootloader mode with the ">" command prompt displayed
       When [command] is entered
       Then "Not recognised" is printed to the CLI
       
       [command] "123456789", "@#][acsv", "dowhatisay", "halp"

   Scenario: Firmware image data is sent via USART
       Given an STM32F412G discovery kit connected via USART
       And "flash 500" has been entered
       When 500 bytes is entered
       Then "BLANK" is printed to the CLI

   Scenario: The command prompt ">" is printed to the CLI after every command input
       Given a STM32F412G discovery board connected via USART
       And the kit is in bootloader mode
       When [command] is entered
       Then the line awaiting the next command input is prefixed with a ">"
       
       [command] "help", "flash 500", "nonsense"

   Scenario: The command prompt ">" is printed to the CLI on start up
       Given an unpowered STM32F412G discovery kit
       When the kit is powered on
       And the bootloader welcome message is displayed
       Then the nextline is prefixed with a ">", awaiting a command input

   Scenario: Welcome message is sent when the system powers on
       Given an unpowered STM32F412G discovery kit connected via USART
       When the kit is powered on
       And the kit enters the "bootloader" mode
       Then "" is printed to the CLI
