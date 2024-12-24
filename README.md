## CLIp
This project was inspired by the discontinued maintenance for (IP-Tracer)[https://github.com/rajkumardusad/IP-Tracer]. It aims to be a more feature-rich re-imagining of the original IP-Tracer in Python instead of PHP.

# Installation
**Only Linux is officially supported,** but macOS and *BSD's *might* work as well. If Windows support is highly requested, it might be implemented at a later date. The focus right now is on finalizing the basic features.

Make sure `git` and `python3` are installed on your system. A Bourne-compliant shell is also required to run the scripts.

Navigate to where you want to keep the files for clip and run the following command:
```bash
git clone https://github.com/Moonlight1211/clip && cd ./clip
```

Using `su`, `sudo`, or `doas`, run the `./install` script. Feel free to examine the script before running it if you are weary of handing out elevated system privileges; there are comments explaining what each part of the script does.
```bash
sudo ./install
```

The script should print this message if the installation was successful:
```
Installation finished!
Consider reloading your terminal for all changes to take effect.
```

That's it! As long as `/usr/local/bin` is in your `$PATH` variable, (which you can check by running `echo $PATH`) you should be able to run `clip` from anywhere in your system like so:
```bash
clip -F ./lib/fields.csv example.ip.address
```

### Disclaimer
Do not use this program in any way for illicit purposes such as doxxing or harassment.
