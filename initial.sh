#!/bin/bash

timedatectl set-ntp true
mkfs.btrfs -f /dev/nvme0n1p2
mkfs.fat -F32 /dev/nvme0n1p1
mkswap /dev/nvme0n1p3

mount /dev/nvme0n1p2 /mnt 
btrfs subvolume create /mnt/@
btrfs subvolume create /mnt/@home
umount /mnt 

mount -o noatime,compress=lzo,space_cache=v2,subvol=@ /dev/nvme0n1p2 /mnt
mount --mkdir -o noatime,compress=lzo,space_cache=v2,subvol=@home /dev/nvme0n1p2 /mnt/home
mount --mkdir /dev/nvme0n1p1 /mnt/boot/efi
swapon /dev/nvme0n1p3

pacstrap -K /mnt base base-devel linux-zen linux-zen-headers linux-zen-docs linux-firmware vim vi sudo mesa amd-ucode xf86-video-amdgpu xf86-input-libinput xorg-xinput zsh man-db man-pages texinfo btrfs-progs git grub efibootmgr os-prober plymouth networkmanager bluez bluez-utils 

genfstab -U /mnt >> /mnt/etc/fstab

arch-chroot

