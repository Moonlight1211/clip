# CLIp
This project was inspired by the discontinued maintenance for [IP-Tracer](https://github.com/rajkumardusad/IP-Tracer). It aims to be a more feature-rich re-imagining of the original IP-Tracer in Python instead of PHP.

### Installation
Make sure `git`, `python3`, and `make` are installed on your system. Currently, this means Windows is not supported, but there are plans to support it eventually!

Navigate to where you want to keep the files for clip and run the following command:
```bash
git clone https://github.com/Moonlight1211/clip && cd ./clip
```

First run `make` by itself **without root privileges**. Running `make` here as root runs `PyInstaller` as root, which will no longer be supported in future versions, and currently prints a warning discouraging it. It also makes all build files owned by the root user, and not you, which may be inconvenient.
```bash
make
```

Then use root privileges to run `make install`. If you are weary of handing out elevated permissions, feel free to examine the Makefile; it contains comments explaining what it does.
```bash
sudo make install
```

That's it! As long as `/usr/local/bin` is in your `$PATH` variable, (which you can check by running `echo $PATH`) you should be able to run `clip` from anywhere in your system like so:
```bash
clip -F ./lib/fields.csv example.ip.address
```

#### Installation quirks
If you need the `clip` binary to be installed elsewhere, just change the `BIN_DIR` variable in the Makefile to your preferred bin location.
```sh
BIN_DIR = /usr/bin
```


### Disclaimer
Do not use this program in any way for illicit purposes such as doxxing or harassment.
