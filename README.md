# PicoGit (Embedded VCS)

A bare-metal, content-addressable version control system engineered specifically for the Raspberry Pi Pico W (RP2040). 

**Disclaimer:** The core Content-Addressable Storage (CAS) math and hardware logic were manually architected. The asynchronous API routing and the CORS-busting frontend dashboard were entirely vibecoded to bridge the gap between strict web browser security policies and bare-metal silicon.

## System Architecture

PicoGit is a lightweight, snapshot-based version control system built in MicroPython. It is designed to survive the strict hardware bottlenecks of a microcontroller (264KB RAM, 2MB Flash).

*   **Content-Addressable Storage (CAS):** Files are not saved by their filenames, but by their mathematical contents. The hardware hashes incoming text payloads using SHA-1 and shards the hash to securely store the data in the `.picogit` database.
*   **Asynchronous Bare-Metal API:** The Pico W runs a custom `microdot` web server asynchronously over the 2.4GHz Wi-Fi band, handling HTTP POST requests directly on the chip without a traditional operating system.
*   **Browser Security Bypass:** Includes an explicit CORS bypass engine to allow modern web browsers to communicate directly with local IP addresses on a private network.

## Hardware & Stack

*   **Microcontroller:** Raspberry Pi Pico W
*   **Language:** MicroPython / Python 3
*   **Frontend:** HTML5, Vanilla JavaScript, CSS (Vibecoded UI)
*   **Development OS:** Fedora 43 (Linux)

## Quick Start

1. **Flash the Hardware:** Ensure your Pico W is flashed with the latest MicroPython UF2 firmware.
2. **Deploy Backend:** Using the MicroPico extension in VS Code, upload the following files to the Pico's flash memory:
   * `userver.py` (API Server)
   * `ucommit.py` (CAS Engine)
   * `uhash.py` (SHA-1 Generator)
   * `microdot.py` (Async Router)
3. **Boot the Server:** Run `userver.py` on the Pico to establish a Wi-Fi connection and retrieve the hardware's local IP address.
4. **Launch the Dashboard:** 
   * Open `index.html` via VS Code Live Server (or run an isolated browser instance).
   * Enter the Pico's IP address, specify the target file, and push the commit over the air.

## Author

**Ayushman**
