# λ lambda

Next generation hackable text editor for nerds.

### Let it be known!

Lambda is in *very* early stages at the moment. Features may change completely, or even be removed.<br>
Don't expect lambda to stay the way it is. Updates are pushed often.

### Overview

Lambda is a similar text editor to `vim` or `kakoune`.<br>
However, it takes a different approach to most of the features seen in other editors.

- Lambda is written in Python, so it is easy to hack and learn.
    - It also has a good amount of comments!
- Lambda is incredibly modular, so you can easily add new features.
- Lambda follows the unix philosophy of "do one thing and do it well."
    - It has no bloated features, like splits or tabs
    - It contains the bare necessities and provides a few extra modules
- Lambda isn't limited to modes or keybindings.
    - Keybindings and modes can be easily changed
    - Other modes can be used by holding down keybindings (i.e. `ctrl-x` inside of `insert` mode)
- Lambda is extremely fast and makes use of efficient memory management.
    - Neovim is slow, and actually requires [a plugin to speed it up](https://github.com/lewis6991/impatient.nvim).
- Lambda has much better default keybindings than other text editors.

### Getting started

```bash
git clone https://github.com/SpyHoodle/lambda.git # Clone the repository
cd lambda # Enter lambda directory
chmod +x install.sh # Make the install script executable
./install.sh # Run the install script
```