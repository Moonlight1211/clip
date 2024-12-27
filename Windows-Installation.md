# CLIp Windows Installation

Open a command prompt window (Windows Key + R then type `cmd`) and use `cd` to navigate to the directory where you want to keep the files for CLIp.
```sh
cd Documents
```

Before prcoeeding, make sure you have `git`, and `python` installed. If not, install them using the `winget` utility (You may need to install `winget` from the Microsoft Store):
```sh
winget install git.git
```
```sh
winget install python3
```

Clone the repository and `cd` into it:
```sh
git clone https://github.com/Moonlight1211/clip && cd clip
```

Type `win-build` to run the build script:
```sh
win-build
```
Once the script says `Done!`, the program has been built and is ready to be used immediately!

Unfortunately, there are no further installation steps to take; Windows comes with another utility called `clip` pre-installed that will override calls to our `CLIp`. Unless you want to delete that program/remove it from your `PATH` variable, your best bet for using `CLIp` is to either move the binary (`clip.exe`) to where you need it and then calling it directly:
```sh
.\clip.exe -f country,timezone 8.8.8.8
```
Or to rename the file to something more distinct and call it normally:
```sh
winclip -o response.json -f country,lon,lat
```
