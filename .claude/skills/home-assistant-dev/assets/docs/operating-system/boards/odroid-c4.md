# Source: https://developers.home-assistant.io/docs/operating-system/boards/odroid-c4

## Experimental

ODROID-C4 support is based heavily on the Odroid-C2 and N2 configurations. Given the similarity of the SoCs, as well as the comparable level of support in the Linux kernel, the C4 should hopefully present few surprises. However, Home Assistant support should be regarded as experimental.

Please also refer to the documentation pages for the [ODROID-C2](/docs/operating-system/boards/odroid-c2) and [Odroid-N2](/docs/operating-system/boards/odroid-n2), as some of that information may apply to the C4 as well.

Common C4 issues that have been specifically tested and appear to be working:

* boot from SD
* boot from eMMC
* MAC address obtained from eFuse

## GPIO

Refer to [the odroid wiki](https://wiki.odroid.com/odroid-c4/hardware/expansion_connectors).