~~~
Note: Early development
~~~

# i3asap
## Intro
We all love i3 but it is quite the hassle setting it up everytime you launch a live cd.
What if we could easily configure our live systems based on a amazing collection
 of i3/vimrc/zshrc/fonts/whatever-dotfiles. 
 
Let's stop wasting time installing the same apps over and over and configuring dotfiles
 to get rid of of that awful live cd feeling.
  
Simply wget [insert tiny url link here] or [insert raw github link here] and run. 

## What it does
0. Select config bundle (see screenshots in config folder)
3. download config bundle: 
  - wallpaper, 
  - .i3 config
  - misc dotfiles (e.g. .fonts/, .zshrc, .vimrc, aliases, ..)
  - application install list (e.g. feh, ncdu, htop, alpine, iptraf, mc, irssi, atop, ..)
  - application remove list (e.g. , ..)
1. grep: check if we are in a virtualbox environment 
1. apt-get: install virtualbox guest addons
2. apt-get: uninstall redundant apps of current desktop environment [uninstall list]
3. apt-get: install i3-wm, i3-lock, i3-bar, dwm-tools, suckless-tools and [install list]
4. useradd: create a new user 
5. mv: setup the new user's desktop according to selected bundle
8. logout

Finally login and enjoy your brand new i3 environment
