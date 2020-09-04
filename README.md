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
    Scroll down and uncoment the line "greeter-session" and then add your greeter
    ```
    
    Example: greeter-session=lightdm-gtk-greeter

Qtile(window manager):

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

