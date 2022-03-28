import os

os.system("loadkeys us")

# asking info about the drive
a = input("what partition is the root partition on your system : ")

b = input("now please input the boot partition on your system : ")

c = input("do you have a swap partition : ")




# using said info we will format the partitions

os.system("mkfs.ext4 " + a)
os.system("mkfs.vfat " + b)

# checking for a swap partition

if c == "y" or c == "Y":
    e = input("whats the location of the SWAP partition : ")
    os.system("mkswap " + e)

else:
    pass

# now the mounting part 

print("now we will mount said filesystems")

os.system("mount " + a + " /mnt ")
os.system("mkdir /mnt/boot")
os.system("mount " + b + " /mnt/boot")
os.system("swapon " + e)


# now the pacstrap

os.system("pacstrap /mnt linux linux-firmware base vim neofetch picom grub networkmanager")

# fstab

os.system("genfstab -U  /mnt >> /mnt/etc/fstab ")

# now we will move the script to /mnt so that you can use it
# i now it isnt in the best place but its usable

os.system("mv ~/dominus_config /mnt")
os.system("arch-chroot /mnt")





