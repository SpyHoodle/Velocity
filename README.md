# λ Lambda
A next-generation hackable incredibly performant rust text editor for nerds.
> ⚠️ Lambda is in *very* early stages at the moment. Lambda's goals are still being decided and features may completely change.

## Overview
Lambda is a similar text editor to `vim` or `kakoune`, taking some ideas from `xi`.
The main goal is to build the best text editor possible by taking ideas from existing text editors and implementing them in the best possible way.

- Lambda is written in Rust, so it's incredibly fast and logical
  - It's also full of comments, so anyone can try and learn what it's doing
- Lambda is very modular, so features can be easily added
- Lambda follows the unix philosophy of "do one thing and do it well"
  - It has no bloated features like splits or tabs
  - It contains the bare necessities and provides a few extra modules
- Lambda has much better default keybindings than other text editors

## Getting started
You'll need `cargo` (ideally from `rustup`) and an up to date version of `rust`.
```
git clone https://github.com/SpyHoodle/lambda.git # Clone the repositiory
cargo run # Build and run lambda!
```
