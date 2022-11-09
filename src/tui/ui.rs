use crossterm::event::{read, Event, KeyCode, KeyEvent, KeyModifiers};
use crate::core::editor::Editor;
use crate::terminal::screen::Screen;
use crate::tui::components;

pub trait Component {
    fn draw(&self, screen: &mut Screen, editor: &Editor) -> Result<(), ()>;
}

struct Components {
    bottom: Vec<Box<dyn Component>>,
}

pub struct Ui {
    components: Components,
}

impl Ui {
    pub fn new<'a>(editor: &'a Editor<'a>) -> Self {
        let status_bar = components::statusbar::StatusBar::new(editor);

        Self {
            components: Components { bottom: vec![Box::new(status_bar)]},
        }
    }

    pub fn draw(&self) {

    }

    pub fn run(screen: &mut Screen, editor: Editor) {
        loop {
            // Refresh the screen
            screen.refresh().unwrap();

            // Generate all the UI elements
            let components = Ui::new(&editor);

            // Draw all UI elements
            components.draw();

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
