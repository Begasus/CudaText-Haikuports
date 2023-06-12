# CudaText-Haiku
Haiku files for CudaText code/text editor

Files placed in 'files/icons':
- CudaText.iom:       Icon-O-Matic CudaText icon for Haiku
- CudaText.rdef:      RDEF file descriptor for CudaText
- CudaText.rsrc:      RSRC resource file (obtained throug 'rc CudaText.rdef')
- CudaTextIcon.rdef:  Icon only RDEF file

- Branch '32bit' holds the needed files to create a 32bit package CudaText on Haiku
- Branch 'hpkg' holds the package(s) needed to install CudaText on Haiku

## File/folder structure
CudaText already sets the 'config' folder in the right place on Haiku, that is, in /boot/home/config/settings/cudatext.

CudaText searches for it's data in /boot/system/data/cudatext


![CudaText Package](/CudaText_hpkg.png)

![CudaText Software](/CudaText.png)

Kudos to ![Roided](https://github.com/roired/CudaText-Haiku) for all the groundwork!

![CudaText Homepage](https://github.com/Alexey-T/CudaText)
