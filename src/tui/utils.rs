// Surrounds a &str with spaces
pub fn with_spaces(text: &str) -> String {
    format!(" {} ", text)
}

// Calculates the starting x coordinate for centred text
pub fn calc_centred_x(screen_width: usize, item_length: usize) -> usize {
    (screen_width / 2) - (item_length / 2)
}

// Returns the longest element in a vector
pub fn longest_element_in_vec(elements: Vec<&str>) -> usize {
    elements.iter().max_by_key(|x: &&&str| x.len()).unwrap().len()
}
