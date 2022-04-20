import curses

from core import utils


class StatusBar:
    def __init__(self, instance):
        self.mode = instance.mode.upper()
        self.file = instance.buffer.name or "[No Name]"
        self.icon = instance.config["icon"] or "λ"
        self.theme = "default"
        self.colors = [7, 5, 13]
        self.components = [self.icon, self.mode, self.file]

    def update(self, instance):
        self.mode = instance.mode.upper()
        self.components = [self.icon, self.mode, self.file]

    def render(self, instance):
        # Clear the status bar
        utils.clear_line(instance, instance.height - 2, 0)

        # Update variables
        self.update(instance)

        if self.theme == "inverted":
            # Initialise the x position for each component
            x = 1

            # Render each component
            for count, component in enumerate(self.components):
                instance.screen.addstr(instance.height - 2, x, component,
                                       curses.color_pair(self.colors[count]) | curses.A_BOLD)
                x += len(component) + 1

        else:
            # Initialise temporary colors for inverted theme
            colors = []

            # Add 1 to each color temporarily
            for color in self.colors:
                colors.append(color + 1)

            # Initialise the x position for each component
            x = 0

            # Render each component
            for count, component in enumerate(self.components):
                component = f" {component} "
                instance.screen.addstr(instance.height - 2, x, component,
                                       curses.color_pair(colors[count]) | curses.A_BOLD)
                x += len(component)

            # Add a space at the end of the status bar
            instance.screen.addstr(instance.height - 2, x, " " * (instance.width - x),
                                   curses.color_pair(2))


class Components:
    def __init__(self, instance, components: dict = None):
        self.components = components or {
            "left": ["   "],
            "bottom": [StatusBar(instance)],
        }
        curses.endwin()

    @staticmethod
    def get_component_width(component: list) -> int:
        return len(max(component))

    def render(self, instance):
        for component in self.components["bottom"]:
            component.render(instance)
