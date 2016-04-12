# -*- mode: ruby -*-
# vi: set ft=ruby :

# Requirements:
#
# pip install ansible
# vagrant plugin install vai
# 
# Optional:
# vagrant plugin install vagrant-hostsupdater
#

NAME="mariadb"
IP="192.168.33.160"

Vagrant.configure("2") do |config|
  config.vm.define NAME do |machine|
    machine.vm.box     = "debian/jessie64"
    machine.vm.guest   = :debian
    machine.vm.provider "virtualbox" do |vbox|
      vbox.gui    = false
    end

    machine.vm.hostname = NAME
    machine.vm.network :private_network, ip: IP
  end
  
  config.vm.provision "vai" do |ansible|
    ansible.inventory_dir      = "ansible/inventory"
    ansible.inventory_filename = "hosts"
  end

end
