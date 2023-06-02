
mv ./dotfiles/.zprofile ~
mkdir -p .cache/zsh

mkdir /home/anthonyprime/.config/ 
mv ./dotfiles/* /home/anthonyprime/.config/

mkdir -p ~/downloads/repos
cd ~/downloads/repos
git clone https://aur.archlinux.org/paru.git 
cd paru 
makepkg -si

sudo pacman -Syu qtile sddm alacritty discord firefox nemo lxsession lxappearance qt5ct qt6ct rofi dunst neofetch blueman network-manager-applet kdeconnect cbatticon maim neovim nitrogen
paru -S qtile-extras-git picom-git kdeconnect-indicator-git 

sudo systemctl enable NetworkManger 
sudo systemctl enable bluetooth
sudo systemctl enable sddm

exit




