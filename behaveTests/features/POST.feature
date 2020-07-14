Feature: POST

   Scenario: LED is on during POST
       Given a powered STM32F412G discovery kit
       When the systemis restarted
       Then LD2 is on during POST

   Scenario: Success message is displayed when POST completes
       Given a powered STM32F412G discovery kit connected via USART
       And the system is restarted
       When POST is completed (LD2turns off)
       Then "[POST]: Flash ID verification and RWR cycle passed" is received via USART

   Scenario: Success message is displayed when POST completes
       Given a powered STM32F412G discovery kit connected via USART
       And the system is restarted
       When POST completes (LD2 turns off)
       Then "Mcu flash ID verification and RWR cycle passed" is sent via USART
