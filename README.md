# multi-card-combiner
Python script to combine data from multiple dotcodes.

# Usage
* Download [nedcenc](https://www.caitsith2.com/ereader/tools/nedcenc.rar) from [caitsith2.com E-Reader Development Tools](https://www.caitsith2.com/ereader/devtools.htm)
* Obtain the `.bin` files from the dotcodes you would like to combine
```
nedcenc.exe -i <input>.raw -o <output>.bin -d
```
* Name the `.bin` files as follows:

`<name>.bin`, `<name>1.bin`, `<name>2.bin`, etc.

* Run the script
```
combine.py <name>.bin
```
The script will then combine data for all files that follow the naming scheme and output it as `vpk.bin`
