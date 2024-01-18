```

   _____   ____ ___.____  ___________.___             _____      ________________________  
  /     \ |    |   \    | \__    ___/|   |           /     \    /  _  \__    ___/\_____  \ 
 /  \ /  \|    |   /    |   |    |   |   |  ______  /  \ /  \  /  /_\  \|    |    /  ____/    
/    Y    \    |  /|    |___|    |   |   | /_____/ /    Y    \/    |    \    |   /       \ 
\____|__  /______/ |_______ \____|   |___|         \____|__  /\____|__  /____|   \_______ \
        \/                 \/                              \/         \/                 \/
```
[MAT2](https://github.com/tpet/mat2) is currently in **beta**, please don't use it for anything critical.

## Purpose
Multi-MAT2 automates MAT2, a CLI tool for Unix terminals, making metadata cleaning more efficient. Instead of manually typing filenames, multi-mat2 utilizes Python subprocesses to apply MAT2 to each file in a directory. It then moves only the cleaned files to a designated folder, leaving the originals untouched.

### Using only MAT2:
```
> mat2 filename1 filename2 filename3 filename4 ...
```
### Using Multi-MAT2:
```
> python3 main.py <file_extension>
```

Multi-MAT2 has automated the tidious task of typing every file you wish you clean.

## Usage
Make sure MAT2 and Python are installed on your system. Move all files you wish to clean inside a new directory. Make sub-directory within the new directory called "cleaned":
```
> mkdir images
> mv file1 images // move all files inside this directory
> cd images
> mkdir cleaned
```
Clone this repository and copy `main.py` into the directory (e.g images) but outside of `/cleaned`:
```
> cd images
> git clone https://github.com/ibnaleem/multi-mat2.git
> mv main.py /images
> rm -rf multi-mat2
```
Your new directory should contain all your files you wish to clean, a `main.py` file, and a `/cleaned` sub-directory. You can run the script in a terminal by providing a file extension argument:
```
python3 main.py <file_extension>
```
## Disclaimer
Even though MAT2 works on *most* file extensions, it does not cover all, therefore, Multi-MAT2 may not work for your file extension. [You can read MAT2's supported file extensions here.](https://0xacab.org/jvoisin/mat2#supported-formats)

## Acknowledgements
[0xacab.org](https://about.0xacab.org)
[tpet/mat2](https://github.com/tpet/mat2)
[jvoisin/mat2](https://0xacab.org/jvoisin/mat2)

## LICENSES
MultiMAT2 is under the [MIT License](https://github.com/ibnaleem/multi-mat2/blob/main/docs/LICENSE)
MAT2 is under the [GNU Lesser General Public License](https://0xacab.org/jvoisin/mat2/-/blob/master/LICENSE?ref_type=heads)
