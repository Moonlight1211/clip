# CLIp
This project was inspired by the discontinued maintenance for [IP-Tracer](https://github.com/rajkumardusad/IP-Tracer). It aims to be a more feature-rich re-imagining of the original IP-Tracer in Python instead of PHP.

Example using the [Google Public DNS](https://dns.google) IP address:
```sh
$ clip 8.8.8.8
    IP Geolocation data for 8.8.8.8
        Continent: North America
        Country: United States
        Province: Virginia
        City: Ashburn
        Zip Code: 20149
        Latitude: 39.03
        Longitude: -77.5
        Timezone: America/New_York
        Interner Service Provider: Google LLC
        Organization Name: Google Public DNS    
```

### Usage
Clip follows GNU getopt syntax, meaning options will work in any order, even after an argument. You can give clip a comma-separated list of the data fields about the IP address to display, listed in full [here](https://ip-api.com/docs/api:json):
```sh
$ clip 8.8.8.8 --fields timezone,continent,isp
    IP Geolocation data for 8.8.8.8
        Continent: North America
        Timezone: America/New_York
        Interner Service Provider: Google LLC
```

Or read them straight from a CSV file:
```sh
$ clip 8.8.8.8 -F fields.csv
    IP Geolocation data for 8.8.8.8
        Continent: North America
        Country: United States
        Interner Service Provider: Google LLC
        Organization Name: Google Public DNS    
```

You can also output the API response directly to a JSON file like so:
```sh
$ clip 8.8.8.8 -f timezone,continent,isp -o response
$ cat response.json
{
    "continent": "North America",
    "timezone": "America/New_York",
    "isp": "Google LLC",
    "query": "8.8.8.8"
}
```

More usage information is available with the `--help` option:
```sh
clip --help
```

### Installation
> [!NOTE]
> For installing on Windows, please see [this document](./Windows-Installation.md)

The following installation instructions are for Linux specifically, but are most likely applicable to other POSIX-compatible systems like macOS or *BSD's.

Make sure `git`, `python3`, and `make` are installed on your system (`gmake` for BSD systems)

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

> [!NOTE]
> If you need the `clip` binary to be installed elsewhere, just change the `BIN_DIR` variable in the Makefile to your preferred bin location.
> ```sh
> BIN_DIR = /usr/bin
> ```

### Disclaimer
Do not use this program in any way for illicit purposes such as doxxing or harassment.
