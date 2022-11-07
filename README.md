# λ Lambda
A next-generation hackable incredibly performant rust text editor for nerds.
> ⚠️ Lambda is in *very* early stages at the moment. Lambda's goals are still being decided and features may completely change.

## Overview
Lambda is a similar text editor to `vim` or `kakoune`, taking some ideas from `xi`.
The main goal is to build the best text editor possible by taking ideas from existing text editors and implementing them in the best possible way.

- Lambda is written in Rust, so it's incredibly fast and logical
  - It's also full of comments, so anyone can try and learn what it's doing
- Lambda is very modular and extensible, so features can be easily added through a variety of methods
  - Need to run a set of keybinds in order? Create a macro
  - Need to create a completely new feature? Just fork it and write it in Rust
- Lambda is separated between the core and the standard terminal implementation
  - This means that anyone can implement their own keybinds, ui, themes, styling, etc.
  - This also means that there is one standard way for managing the text itself - inside of the lambda core
- Lambda is a modal text editor and uses ideas from kakoune, and is designed for the select -> action structure
  - Since anyone can implement their own keybinds, it's possible to make a vim implementation that uses the action -> select structure
- Lambda follows the unix philosophy of "do one thing and do it well"
  - It has no bloated features like splits or tabs
  - It contains the bare necessities and provides a few extra modules
- Lambda has much better default keybindings than other text editors

## Getting started
You'll need `cargo` (ideally from `rustup`) and an up to date version of `rust`.
```bash
git clone https://github.com/SpyHoodle/lambda.git # Clone the repositiory
cargo run # Build and run lambda!
```
