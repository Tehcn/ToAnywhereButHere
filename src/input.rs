use bevy::{
    input::{
        mouse::{MouseButtonInput, MouseMotion, MouseWheel},
        keyboard::KeyboardInput
    },
    prelude::*,
    window::CursorMoved,
};

pub struct InputSystem;

impl Plugin for InputSystem {
    fn build(&self, app: &mut App) {
        app.add_system(keyboard_event_system)
            .add_system(mouse_events_system);
    }
}

fn keyboard_event_system(mut keyboard_input_events: EventReader<KeyboardInput>) {
    for event in keyboard_input_events.iter() {
        info!("{:?}", event);
    }
}

fn mouse_events_system(
    mut mouse_button_input_events: EventReader<MouseButtonInput>,
    mut mouse_motion_events: EventReader<MouseMotion>,
    mut cursor_moved_events: EventReader<CursorMoved>,
    mut mouse_wheel_events: EventReader<MouseWheel>,
) {
    for event in mouse_button_input_events.iter() {
        info!("{:?}", event);
    }

    for event in mouse_motion_events.iter() {
        info!("{:?}", event);
    }

    for event in cursor_moved_events.iter() {
        info!("{:?}", event);
    }

    for event in mouse_wheel_events.iter() {
        info!("{:?}", event);
    }
}