from core import utils
import curses


class StatusBar:
    def __init__(self, instance):
        self.mode = instance.mode.upper()
        self.file = instance.buffer.name or "[No Name]"
        self.icon = instance.config["icon"] or "λ"
        self.colors = (7, 5, 13)
        self.components = [self.icon, self.mode, self.file]

    def render(self, instance):
        x = 1
        utils.clear(instance, instance.height - 2, 0)
        for count, component in enumerate(self.components):
            instance.screen.addstr(instance.height - 2, x, component,
                                   curses.color_pair(self.colors[count]) | curses.A_BOLD)
            x += len(component) + 1


class Components:
    def __init__(self, components: dict = None):
        self.components = components or {
            "left": ["  "],
            "bottom": [StatusBar],
        }

    @staticmethod
    def get_component_width(component: list) -> int:
        return sum(len(max(sub_components)) for sub_components in component if max(sub_components))

    def render(self, instance):
        for component in self.components["bottom"]:
            component(instance).render(instance)
