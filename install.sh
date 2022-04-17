#!/bin/sh

# Copy lambda to ~/.local/share
mkdir -p ~/.local/share/lambda
cp -rf . ~/.local/share/lambda

# Copy lambda launcher
chmod +x ./lambda
rm -r ~/.local/bin/lambda
ln -s ~/.local/share/lambda/lambda ~/.local/bin/lambda
chmod +x ~/.local/bin/lambda