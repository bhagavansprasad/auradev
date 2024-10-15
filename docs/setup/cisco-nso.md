c#Cisco NSO setup and running

### Source

https://rayka-co.com/lesson/cisco-nso-netsim-to-add-devices-in-nso-lab/

#### Source the configuration

```sh
source ~/nso-6.3/ncsrc
```

#### Create nso instance folder

```sh
ncs-setup --package ~/nso-6.3/packages/neds/cisco-iosxr-cli-3.5 \
--package ~/nso-6.3/packages/neds/cisco-asa-cli-6.6 \
--package ~/nso-6.3/packages/neds/cisco-ios-cli-3.8 \
--package ~/nso-6.3/packages/neds/cisco-nx-cli-3.0 \
--package ~/nso-6.3/packages/neds/juniper-junos-nc-3.0 \
--dest ~/nso-instance
```

#### Start nso

```sh
cd ~/nso-instance
ncs
```

#### Check nso status

```sh
ncs --status | grep status
```

#### Browse nso

http://localhost:8080/login.html
admin/admin

#### connect to NSO CLI

```sh
ncs_cli -C -u admin # cisco style
ncs_cli -J -u admin # juniper style
```

#### NSO commands

```sh
show ncs-state version
show packages package package-version
```

# add devices using "netsim"

```sh
cd ~/nso-instance/
ncs-netsim delete-network # if already exist
ncs-netsim create-network packages/cisco-ios-cli-6.88 3 ios
ncs-netsim add-to-network packages/cisco-asa-cli-6.16 1 asa
ncs-netsim add-to-network packages/cisco-iosxr-cli-7.43 1 iosxr
ncs-netsim add-to-network packages/cisco-nx-cli-5.23 1 nxos
ncs-netsim add-to-network packages/juniper-junos-nc-3.0 1 junos
ncs-netsim start
```

# Enter into configuration mode

```sh
config terminal
```

# Configure device

```sh
devices authgroups group AURA
default-map remote-name aura
default-map remote-password jnjnuh
default-map remote-secondary-password jnjnuh

# add a device
devices device R1
address 192.168.2.91
authgroup AURA
ssh host-key-verification none
device-type cli ned-id cisco-ios-cli-6.88
device-type cli protocol ssh
state admin-state unlocked
commit
connect
end
```

show running-config devices global-settings ssh-algorithms public-key | details

docker run -itd --platform=linux/amd64 -p 2222:22 -p 443:443 -p 8181:80 --name nso-dev1 cisco-nso-base:6.3-bhagavan

docker run -itd --name nso cisco-nso-base:6.3-bhagavan

docker run -itd --name nso --rm -p 80:80 cisco-nso-base:6.3-bhagavan
docker run -itd --name nso --rm 
    -p 80:80
    -p 4443:443
    -p 222:22
    -e ADMIN_USERNAME=admin
    -e ADMIN_PASSWORD=admin
    -e ENABLE_ADMIN_USER=true cisco-nso-base:6.3-bhagavan

docker run -itd --name nso --rm 
    -p 80:80
    -p 2024:2024
    -p 4443:443
    -p 222:22
    -e HTTP_ENABLE=true
    -e ADMIN_USERNAME=admin
    -e ADMIN_PASSWORD=admin
    -e ENABLE_ADMIN_USER=true cisco-nso-base:6.3-bhagavan

docker run -itd --name cisco-nso-dev 
    -p 2024:2024
    -p 8080:8080
    cisco-nso-dev:0.1

http://192.168.1.2
https://192.168.1.2

http://172.27.111.53
https://172.27.111.53

http://172.27.111.53:4443

docker exec -it nso63 bash

./etc/ncs/ncs.conf
./opt/ncs/ncs-6.3/etc/ncs/ncs.conf

https://download-ssc.cisco.com/files/swc/std/4_SDSP_17854794_1714724445635/1/nso-6.3-freetrial.container-image-dev.linux.arm64.signed.bin?ip=122.179.16.250&dtrTag=4_SDSP_17854794_1714724445635_bede75c9998ee565fa4228b19040e58f&userid=00uhefc18m9Qmjpeg5d7&ak-org=2w_ue&SEC=N&tenant-id=SDSP&client=NA&__gda__=1727337659_626bd873626cb64e00d10134e92c66c1f370859366856a4e01da7dbaa2f3f920&__gdb__=exp=1727334540~hmac=f5b0cb14ae874614aa9040fef5e40ae0b2b7217e6d3ead2111f3ca69bbd6293a&xac=4-O3qMM8ytIlgLS%2FpHAUUGyW7pCRDh%2Bm8RFOlcWFunnm0LGpzxLHs25TuGuPJJWvxd
