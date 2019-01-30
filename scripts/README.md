# One-click setup

Script to completely setup a vanilla RasPI to run the codebase.

**Note :** Written for **Raspbian Stretch Lite (version November 2018)**.

#### Before using

* Make sure there is active internet connection in the RasPI
* Connect the Eyes (LED Matrix) to the proper pins in the RasPI since the I2C address is fetched by the script.
If eye is not connected, update the I2C address later by doing the following :
  * `i2cdetect -y 1`
  * Get the address displayed in the Matrix. If address is 0x70 nothing more needs to be done.
  * If address is something else, modify EYE_I2C_ADDRESS in [globals.py](../alien/lib/globals.py)
* If you wish to use backdoor, the set it up when asked by the script. Know more about backdoor [here](../backdoor/)
