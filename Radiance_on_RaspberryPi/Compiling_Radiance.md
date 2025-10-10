# Radiance on Raspberry Pi

1. **Installation from the source codes:**

Download the latest source codes:
```bash
sudo apt-get install libx11-dev
wget --no-check-certificate https://github.com/LBNL-ETA/Radiance/archive/refs/heads/master.tar.gz
wget --no-check-certificate https://www.radiance-online.org/download-install/radiance-source-code/latest-release/rad6R0supp.tar.gz
```
Unzip files:
```bash
tar -xf master.tar.gz
tar -xf rad6R0supp.tar.gz
```
2. **Replace the config.guess file:**
	- Go to the folder where the `config.guess` file is located, it should be `ray/src/px/tiff`
	- Download a new [config.guess](http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.guess;hb=HEAD) file and replace the existing one:
	 ```bash
	 cd ray/src/px/tiff
	 wget 'http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.guess;hb=HEAD' -O config.guess
	 ```
3. **Try to install (more problematic)**
   -  find proper makefile, in ```bash ray/src/px/tiff``` are only some functions for tiff processing
   -  rather go to downloaded ```bash Radiance-master``` and there is the make file, that need to be executed
   -  but the command ```bash sudo ./makeall install``` is only supported by C shell
   -  first, you need to do ```bash sudo apt install csh tcsh```
   -  then ```bash sudo csh ./makeall install```
   -  and go through the questions during the installation
   -  after the instalation is done, will be the source code files copied to ```bash /usr/local/bin```
   -  then e.g. evalglare can be executed from anywhere
   -   
