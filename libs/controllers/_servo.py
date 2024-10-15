import time

import RPi.GPIO as GPIO

from libs.controllers.volume import VolumeController


class ServoVolumeController(VolumeController):
    def __init__(self) -> None:

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        pwm_gpio = 12
        frequence = 50
        GPIO.setup(pwm_gpio, GPIO.OUT)
        self.pwm = GPIO.PWM(pwm_gpio, frequence)

        self.pwm.start(self._angle_to_percent(0))

    @staticmethod
    def _angle_to_percent(angle):
        if angle > 180 or angle < 0 :
            return False

        start = 3
        end = 13.5
        ratio = (end - start) / 180

        angle_as_percent = angle * ratio

        return start + angle_as_percent

    def close_connection(self):
        self.pwm.stop()
        GPIO.cleanup()

    def set_volume(self, volume: int):
        converted_angle = self._angle_to_percent(volume)
        self.pwm.ChangeDutyCycle(converted_angle)
        self.pwm.ChangeDutyCycle(0)


