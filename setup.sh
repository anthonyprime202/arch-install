#!/bin/bash

ln -sf /usr/share/zoneinfo/Asia/Kolkata /etc/localtime
hwclock --systohc

locale-gen
echo "LANG=en_US.UTF-8" > /etc/locale.conf

echo "archlinux" > /etc/hostname

mkinitcpio -P 
grub-install --target="x86_64-efi" --bootloader-id="Arch Linux"
grub-mkconfig -o /boot/grub/grub.cfg

mkdir /etc/X11/xorg.conf.d
mv ./30-touchpad.conf /etc/X11/xorg.conf.d/

passwd
useradd -mg users -G wheel -s /usr/bin/zsh anthonyprime
passwd anthonyprime

su anthonyprime

exit
