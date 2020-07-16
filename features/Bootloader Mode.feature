Feature: Bootloader Mode

    Scenario: Bootloader mode is entered due to an absent firmware image
        Given an unpowered STM32F412G discovery kit connected via USART
        And no firmware image is flashed on the kit
        When the kit is powered on
        Then bootloader mode is entered
        And the WELCOME BOOTLOADER message is printed to the CLI

    Scenario: Bootloader mode is entered due to an invalid firmware image
        Given an unpowered STM32F412G discovery kit connected via USART
        And an invalid (HOW!?) firmware image has been flashed on the kit
        When the kit is powered on
        Then bootloader mode is entered
        And the WELCOME BOOTLOADER message is printed to the CLI

    Scenario: Bootloader mode is entered via METHOD
        Given an unpowered STM32F412G discovery kit connected via USART
        And ENTRY METHOD
        When the kit is powered on
        Then bootloader mode is entered
        And the BOOTLOADER WELCOME message is printed to the CLI
