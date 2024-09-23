# deblive-config

`deblive-config` is a wrapper tool designed to simplify the configuration process of Debian Live Build. This tool makes it easier to create custom Debian Live CD/USB images.

## Note

This tool is a wrapper for the `lb config` command. For detailed customization, please refer to the official `live-build` documentation.

https://wiki.debian.org/DebianLive

## Features

- Easy configuration of key `lb config` command options
- Specification and automatic addition of extra packages

## Requirements

- Python 3.6 or higher
- Debian or Ubuntu system
- `live-build` package installed

This tool has been tested with the following version of live-build:

```
$ dpkg -l live-build
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name           Version      Architecture Description
+++-==============-============-============-=================================
ii  live-build     1:20240810   all          Live System Build Components
```

## Usage

Basic usage:

```
$ ./deblive-config.py [options]
```

### Usage Examples

Basic configuration:

```
$ ./deblive-config.py --distribution bullseye --architecture i386
```

Including additional packages:

```
$ ./deblive-config.py --packages "vim,git,htop"
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) for details.
