# DO NOT RUN THIS IN THE LIVECD !!

import os

# timezone
os.system(" ln -sf /usr/share/zoneinfo/Region/City /etc/localtime ")
os.system("hwclock --systohc ")

# localization
os.system("sed '/en_US.UTF-8 UTF-8/ s/#/ /' /etc/locale.gen")
os.system("locale-gen")

# hostname
os.system("sed -i 's/tux/s' /etc/localtime")
os.system("mkinitcpio -P")

# grub

a = input("name of the drive you want to install on : ")
os.system("grub-install --target=i386-pc  " + a)
os.system("grub-mkconfig -o /boot/grub/grub.cfg")

# setting up my config and the system

os.system("useradd + " input("what do you want to name your user : "))
os.system("sudo pacman -S i3 alacritty lightdm lightdm-gtk-greeter rofi dmenu picom xorg xorg-xinit")

