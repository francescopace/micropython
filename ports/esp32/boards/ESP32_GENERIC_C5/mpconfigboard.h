// This configuration is for a generic ESP32C5 board with 4MiB (or more) of flash.

#ifndef MICROPY_HW_BOARD_NAME
#define MICROPY_HW_BOARD_NAME               "ESP32C5 module"
#endif
#define MICROPY_HW_MCU_NAME                 "ESP32-C5"

#define MICROPY_PY_MACHINE_I2S              (0)
#define MICROPY_HW_ENABLE_UART_REPL         (1)
