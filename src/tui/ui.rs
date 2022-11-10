use crossterm::event::{read, Event, KeyCode, KeyEvent, KeyModifiers};
use crate::core::editor::Editor;
use crate::terminal::screen::Screen;
use crate::tui::components;

pub trait Component {
    fn draw(&self, screen: &mut Screen, editor: &Editor) -> Result<(), ()>;
}

struct Components<'a> {
    bottom: Vec<Box<dyn Component + 'a>>,
    centre: Vec<Box<dyn Component + 'a>>,
}

pub struct Ui<'a> {
    components: Components<'a>,
}

impl<'a> Ui<'a> {
    pub fn new(editor: &'a Editor<'a>) -> Self {
        let status_bar = components::statusbar::StatusBar::new(editor);
        let welcome_msg = components::welcome::WelcomeMessage::new(editor);

        Self {
            components: Components {
                bottom: vec![Box::new(status_bar)],
                centre: vec![Box::new(welcome_msg)],
            },
        }
    }

    pub fn draw(&self, screen: &mut Screen, editor: &Editor) {
        // Dereference the box
        let _ = &*self.components.bottom;

        // Draw all components on the bottom
        for component in &self.components.bottom {
            component.draw(screen, &editor).unwrap();
        };

        // Dereference the box
        let _ = &*self.components.centre;

        // Draw all components in the center
        for component in &self.components.centre {
            component.draw(screen, &editor).unwrap();
        }
    }

    pub fn run(screen: &mut Screen, editor: Editor) {
        loop {
            // Refresh the screen
            screen.refresh().unwrap();

            // Generate all the UI elements
            let components = Ui::new(&editor);

            // Draw all UI elements
            components.draw(screen, &editor);

            // Check for any key presses
            match read().unwrap() {
                Event::Key(KeyEvent {
                    code: KeyCode::Char('q'),
                    modifiers: KeyModifiers::CONTROL,
                    ..
                }) => break,
                Event::Key(KeyEvent {
                    code: KeyCode::Char('c'),
                    modifiers: KeyModifiers::CONTROL,
                    ..
                }) => break,
                _ => (),
            }
        }

        screen.exit();
    }
}
