import io

from typing import Optional

from libs.controllers.volume import VolumeController, VolumeControllerFactory, VolumeControllerType


class _APIInfra:

    def __init__(self):
        self._volume_controller: Optional[VolumeController] = None

    @staticmethod
    def _is_raspberrypi():
        try:
            with io.open('/sys/firmware/devicetree/base/model', 'r') as m:
                if 'raspberry pi' in m.read().lower():
                    return True
        except Exception:
            pass
        return False

    @property
    def volume_controller(self) -> VolumeController:
        if not self._volume_controller:
            if not self._is_raspberrypi():
                self._volume_controller = VolumeControllerFactory.create(VolumeControllerType.MOCK)
            else:
                self._volume_controller = VolumeControllerFactory.create(VolumeControllerType.SERVO)
        return self._volume_controller


APIInfra = _APIInfra()
