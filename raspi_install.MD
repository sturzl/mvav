# Random commands/steps

* command to write raspbian image to sd card
   ```bash
    sudo dd bs=4M status=progress if=./2018-06-27-raspbian-stretch.img of=/dev/sdb
    ```
* put empty file named "ssh" on the boot partition

* If running desktop version with a mouse but no keyboard then then add file to desktop with the following
   ```
  ifconfig

  _wifi_password_

  sudo raspi-config

  raspberry

  passwd

  sudo 

  _desired_login_password_

  sudo systemctl enable ssh
  
  sudo systemctl start ssh

  systemctl status sshd

  sudo raspi-config
 
   ```
* Run sudo raspi-config to configure from desktop 
   ```bash
    sudo dd bs=4M status=progress if=./2018-06-27-raspbian-stretch.img of=/dev/sdb
    ```
 
