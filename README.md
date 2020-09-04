# config_files

I've copied most of my dotfiles from **[antoniosarosi](https://github.com/antoniosarosi)**

# Qtile installation

***Prerequisites***

Before installing Qtile you need to install **[xorg](https://wiki.archlinux.org/index.php/Xorg)** to enable graphical interface:

```bash
sudo pacman -S xorg
```

***Installation***

Now you can install Qtile and the basic software that you will need:

*Lightdm and lightdm-gtk greeter (Display Maneger):*
```bash
sudo pacman -S lightdm lightdm-gtk-greeter
```
    
Now enable the greeter by editing
```bash
/etc/lightdm/lightdm.config
```
Scroll down and uncoment the line "greeter-session" and then add your greeter

Example: greeter-session=lightdm-gtk-greeter

*Qtile(window manager):*

```bash
sudo pacman -S Qtile    
```
Firefox(Web Browser):

```bash
sudo pacman -S firefox
```    

Alacritty (Terminal Emulator):
```bash
sudo pacman -S alacritty
```

Nautilus (File Maneger):
```bash
sudo pacman -S nautilus
```

# Qtile Configuration

***First steps***

*Keyboard*

The default keyboard layout in Qtile is US layout. To change it you shuld use setxkbmap. I've changed to spanish layout:
```bash
setxkbmap es
```

*AUR(Arch User Repository)*

AUR is a package manager driven by the Arch community. We'll install some tools from there, so its important to install it.

To install AUR first you have to install git:
```bash
sudo pacman -S git
```
You need to install binutils too
Then clone "https://aur.archlinux.org/yay-git.git" on /opt/ with the command:

```bash
git clone /opt/https://aur.archlinux.org/yay-git.git
```

Then go to /opt/yay-git:

```bash
cd /opt/yay-git
*Audio*

To enable the audio you can use pulseaudio. You can install pavucontrol if you want to have a graphical volume interface:
```bash
pacman -S pulseaudio pavucontrol
```

Install volumeicon using yay to have a 
At this point probably you have to reboot.