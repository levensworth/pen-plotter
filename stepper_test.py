from machine import Pin
from time import sleep

pins = [
    Pin(2, Pin.OUT),  # IN1
    Pin(3, Pin.OUT),  # IN2
    Pin(4, Pin.OUT),  # IN3
    Pin(5, Pin.OUT),  # IN4
]

FULL_STEP_SEQUENCE = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
]

HALF_STEP_SEQUENCE = [
    [1, 0, 0, 0],
    [1, 1, 0, 0], 
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],

]


# smoothness

SUPER_SLOW = 0.1
SLOW = 0.02
FAST = 0.002
SUPER_FAST = 0.0002


class StepperMotor:
    
    def __init__(self, pin_config: list[Pin], step_sequence: list[list[int]]):
        self._pin_config_map = pin_config
        self._step_sequence = step_sequence
        self._last_sequence_state = 0

    def move(self, step_count: int, smoothness: float ) -> None:
        for _ in range(step_count):
            self.take_step()
            sleep(smoothness)


    def take_step(self,) -> None:
        sequence_length = len(self._step_sequence)
        current_sequence = self._step_sequence[self._last_sequence_state]
        for pin, value in zip(self._pin_config_map, current_sequence):
            pin.value(value)

        # you move in the sequence
        self._last_sequence_state =  (self._last_sequence_state + 1) % sequence_length


            




motor1 = StepperMotor(
    pin_config=[
        Pin(2, Pin.OUT),  # IN1
        Pin(3, Pin.OUT),  # IN2
        Pin(4, Pin.OUT),  # IN3
        Pin(5, Pin.OUT),  # IN4
    ], 
    step_sequence=HALF_STEP_SEQUENCE)

motor2 = StepperMotor(
    pin_config=[
        Pin(10, Pin.OUT),  # IN1
        Pin(11, Pin.OUT),  # IN2
        Pin(12, Pin.OUT),  # IN3
        Pin(13, Pin.OUT),  # IN4
    ], 
    step_sequence=HALF_STEP_SEQUENCE)

motor3 = StepperMotor(
    pin_config=[
        Pin(18, Pin.OUT),  # IN1
        Pin(19, Pin.OUT),  # IN2
        Pin(20, Pin.OUT),  # IN3
        Pin(21, Pin.OUT),  # IN4
    ], 
    step_sequence=HALF_STEP_SEQUENCE)

motor1.move(2048, FAST)
motor2.move(2048, FAST)
motor3.move(2048, FAST)

