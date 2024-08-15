class SceneManager:
    def __init__(self, screen):
        self.screen = screen
        self.scenes = {}
        self.current_sceen = None

    def add_scene(self, scene_name, scene_class):
        self.scenes[scene_name] = scene_class(self)

    def change_scene(self, scene_name):
        if scene_name in self.scenes:
            self.current_sceen = self.scenes[scene_name]
        else:
            print(f"Scene {scene_name} not found in available scenes.")

    def handle_events(self, events):
        if self.current_sceen:
            self.current_sceen.handle_events(events)

    def update(self):
        if self.current_sceen:
            self.current_sceen.update()

    def draw(self):
        if self.current_sceen:
            self.current_sceen.draw(self.screen)
