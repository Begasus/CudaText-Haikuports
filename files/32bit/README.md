# Cudatext files

This is the CudaText executable for Haiku 32bit and the data files that need to be installed to 
/boot/system/data folder when making the package

This new version 1.195.0.6 has already included Python support added by Alextey-T.
Thanks to Begasus, now it's not needed to package libQt5Pas with the HPKG as it's already 
provided by Haikuports, thus when installing the CudaText HPKG it pulls the needed requirements.
