from enum import Enum, unique


@unique
class VolumeControllerType(Enum):
    MOCK = 0
    SERVO = 1

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class VolumeController:
    def set_volume(self, volume: int):
        raise Exception("method not implemented")


class VolumeControllerFactory:
    def create(type: VolumeControllerType):
        if type == VolumeControllerType.MOCK:
            from ._mock import MockVolumeController
            return MockVolumeController()
        if type == VolumeControllerType.SERVO:
            from ._servo import ServoVolumeController
            return ServoVolumeController()
        raise Exception("invalid connector type")
    