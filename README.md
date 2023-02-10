# footprint-py

<p align="center">
  <img src="https://github.com/Frikallo/footprint/blob/main/examples/banner.png" width="500" title="footprint-banner">
</p>

## What is footprint-py

A python OSINT tool to discover and analyze the digital footprint of a targets email or username across millions of sites. Perfect for gathering gneral information about a target email.

#### Features: :eyes:

* Email validation
* Check social accounts
* Scan Pastebin Dumps
* Check Breached Sites
* DNS/IP Lookup
* Username search (WIP)
* Check if email is active (WIP)
* Check related emails (WIP)

## Services (APIs):

| Service | Function | Status |
| :--- | :--- | :--- |
| [ipapi.co](https://ipapi.co/) - Public | More Information About Domain | :white\_check\_mark: |
| [psbdmp.ws](https://psbdmp.ws/) - Public | Pastebin Dumps | :white\_check\_mark: |
| [hunter.io](https://hunter.io/) - Public | Related Emails | :white\_check\_mark: :key: |
| [emailrep.io](https://emailrep.io/) - Public | Breached Sites Names | :white\_check\_mark: :key: |
| [BreachDirectory](https://breachdirectory.org/)| Password Leaks | :white\_check\_mark: :key: |

:key: API key required

#### If you want to use footprint with full features, set your API keys:

 ```
  footprint set hunter <hunter.io API key>
  footprint set emailrep <emailrep.io API key>
  footprint set breachdirectory <breachdirectory.org API key>
  ```

## Installation:
```
pip install footprint-py
-----------
OR
-----------
git clone https://github.com/Frikallo/footprint.git
cd footprint
python setup.py install
```

## Usage:
```
footprint example@email.com
-----------
OR
-----------
python -m footprint example@email.com
```

## Demo:
<p align="center">
  <img src="https://github.com/Frikallo/footprint/blob/main/examples/demo.gif" width="500" title="footprint">
</p>

This project is licensed under the APACHE License - see the [LICENSE](https://github.com/Frikallo/footprint/blob/main/LICENSE) file for details