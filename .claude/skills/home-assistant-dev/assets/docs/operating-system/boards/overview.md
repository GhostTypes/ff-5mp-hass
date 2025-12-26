# Source: https://developers.home-assistant.io/docs/operating-system/boards/overview

## Overview

The following boards/devices are supported:

* Nabu Casa
  + [Home Assistant Green](https://www.home-assistant.io/green/)
  + [Home Assistant Yellow](https://www.home-assistant.io/yellow/) (based custom carrier board and powered by a Raspberry Pi 4 Compute Module)
  + [Home Assistant Blue](https://www.home-assistant.io/blue/) (based on ODROID-N2+)
* Raspberry Pi
  + Pi 5 ([4 GB](https://www.raspberrypi.com/products/raspberry-pi-5/?variant=raspberry-pi-5-4gb) and [8 GB](https://www.raspberrypi.com/products/raspberry-pi-5/?variant=raspberry-pi-5-8gb) model) 64-bit
  + Pi 4 Model B ([1 GB](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/?variant=raspberry-pi-4-model-b-1gb), [2 GB](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/?variant=raspberry-pi-4-model-b-2gb), [4 GB](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/?variant=raspberry-pi-4-model-b-4gb) and [8 GB](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/?variant=raspberry-pi-4-model-b-8gb) model) 32-bit or 64-bit (recommended)
  + [Pi 3 Model B](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/) and [B+](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/) 32-bit or 64-bit (recommended)
  + [Pi 2](https://www.raspberrypi.com/products/raspberry-pi-2-model-b/) (not recommended)
* Hardkernel
  + [ODROID-C2](https://www.hardkernel.com/shop/odroid-c2/) (discontinued)
  + [ODROID-C4](https://www.hardkernel.com/shop/odroid-c4/)
  + [ODROID-M1](https://www.hardkernel.com/shop/odroid-m1/)
  + ODROID-M1S [4 GB](https://www.hardkernel.com/shop/odroid-m1s-with-4gbyte-ram/) or [8 GB](https://www.hardkernel.com/shop/odroid-m1s-with-8gbyte-ram/)
  + [ODROID-N2](https://www.hardkernel.com/shop/odroid-n2/) (discontinued)
  + ODROID-N2+ [2 GB](https://www.hardkernel.com/shop/odroid-n2-with-2gbyte-ram-2/) or [4 GB](https://www.hardkernel.com/shop/odroid-n2-with-4gbyte-ram-2/)
  + [ODROID-XU4](https://www.hardkernel.com/shop/odroid-xu4-special-price/)
* Asus
  + [Tinker Board](https://tinker-board.asus.com/product/tinker-board.html)
* Generic x86-64 (UEFI, not suited for virtualization)
  + [Intel NUC5CPYH](https://www.intel.com/content/www/us/en/products/sku/85254/intel-nuc-kit-nuc5cpyh/specifications.html)
  + [Intel NUC6CAYH](https://www.intel.com/content/www/us/en/products/sku/95062/intel-nuc-kit-nuc6cayh/specifications.html)
  + [Intel NUC10I3FNK2](https://www.intel.com/content/www/us/en/products/sku/195503/intel-nuc-10-performance-kit-nuc10i3fnk/specifications.html)
  + [Gigabyte GB-BPCE-3455](https://www.gigabyte.com/Mini-PcBarebone/GB-BPCE-3455-rev-10/sp#sp)
  + Computers supporting x86-64 architecture and UEFI boot should generally work
* Virtual appliance (x86\_64/UEFI):
  + VMDK
  + OVA ?
  + VHDX ?
  + VDI ?
  + QCOW2 ?

Notes:

* see ? above: are these currently supported? see ova documentation which explains issues with previous OVA distribution)

## Board specifics

| Board | Build | Config | Docs |
| --- | --- | --- | --- |
| Green | `make green` | [green](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/configs/green_defconfig) | - |
| Yellow | `make yellow` | [yellow](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/configs/yellow_defconfig) | - |
| Pi5 64-bit | `make rpi5_64` | [rpi5\_64](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/configs/rpi5_64_defconfig) | [raspberrypi](/docs/operating-system/boards/raspberrypi) |
| Pi4B 64-bit | `make rpi4_64` | [rpi4\_64](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/configs/rpi4_64_defconfig) | [raspberrypi](/docs/operating-system/boards/raspberrypi) |
| Pi4B 32-bit | `make rpi4` | [rpi4](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/configs/rpi4_defconfig) | [raspberrypi](/docs/operating-system/boards/raspberrypi) |
| Pi3B 64-bit | `make rpi3_64` | [rpi3\_64](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/configs/rpi3_64_defconfig) | [raspberrypi](/docs/operating-system/boards/raspberrypi) |
| Pi3B 32-bit | `make rpi3` | [rpi3](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/configs/rpi3_defconfig) | [raspberrypi](/docs/operating-system/boards/raspberrypi) |
| Pi2 | `make rpi2` | [rpi2](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/configs/rpi2_defconfig) | [raspberrypi](/docs/operating-system/boards/raspberrypi) |
| ODROID-C2 | `make odroid_c2` | [odroid\_c2](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/configs/odroid_c2_defconfig) | [hardkernel](/docs/operating-system/boards/hardkernel) |
| ODROID-C4 | `make odroid_c4` | [odroid\_c4](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/configs/odroid_c4_defconfig) | [hardkernel](/docs/operating-system/boards/hardkernel) |
| ODROID-M1 | `make odroid_m1` | [odroid\_m1](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/configs/odroid_m1_defconfig) | [hardkernel](/docs/operating-system/boards/hardkernel) |
| ODROID-M1S | `make odroid_m1s` | [odroid\_m1s](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/configs/odroid_m1s_defconfig) | [hardkernel](/docs/operating-system/boards/hardkernel) |
| ODROID-N2/N2+ | `make odroid_n2` | [odroid\_n2](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/configs/odroid_n2_defconfig) | [hardkernel](/docs/operating-system/boards/hardkernel) |
| ODROID-XU4 | `make odroid_xu4` | [odroid\_xu4](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/configs/odroid_xu4_defconfig) | [hardkernel](/docs/operating-system/boards/hardkernel) |
| Tinker Board | `make tinker` | [tinker](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/configs/tinker_defconfig) | [asus](/docs/operating-system/boards/asus) |
| Generic x86-64 | `make generic_x86_64` | [generic\_x86\_64](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/configs/generic_x86_64_defconfig) | [generic-x86-64](/docs/operating-system/boards/generic-x86-64) |
| OVA | `make ova` | [ova](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/configs/ova_defconfig) | [ova](/docs/operating-system/boards/ova) |