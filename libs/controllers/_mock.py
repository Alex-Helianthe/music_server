from libs.controllers.volume import VolumeController


class MockVolumeController(VolumeController):

    def set_volume(self, volume: int):
        print(f"Mock volume set to {volume}")
