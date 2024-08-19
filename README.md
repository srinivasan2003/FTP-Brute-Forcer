
# FTP-Brute-Forcer

This Python script is designed to perform a brute-force attack on an FTP server to discover valid login credentials. The script uses asynchronous operations to maximize the efficiency of the attack by trying multiple passwords concurrently.

## Features

- **Asynchronous Execution**: The script uses `asyncio` and `aioftp` for handling multiple connections simultaneously.
- **Concurrency Control**: Allows limiting the number of concurrent password attempts to prevent overwhelming the server.
- **Customizable Parameters**: Users can specify the target FTP server, port, username, and wordlist of passwords.

## Requirements

- Python 3.7+
- Required Python packages:
  - `aioftp`
  - `termcolor`

You can install the required packages using pip:

```bash
pip install aioftp termcolor
```

## Usage

```bash
python ftp-brute-forcer.py <target> -u <username> -w <wordlist> [-p <port>]
```

### Positional Arguments

- `target`: The IP address or hostname of the target FTP server.

### Optional Arguments

- `-u`, `--username`: The username to use for the brute-force attack.
- `-w`, `--wordlist`: Path to the wordlist file containing possible passwords.
- `-p`, `--port`: The port to connect to on the target FTP server (default is 21).

### Example

```bash
python ftp-brute-forcer.py 192.168.1.10 -u admin -w passwords.txt -p 21
```

## How It Works

1. **Input Parsing**: The script first parses the command-line arguments to get the target IP, port, username, and wordlist file.
  
2. **Wordlist Reading**: It then reads the wordlist file to get the list of possible passwords.

3. **Asynchronous Bruteforcing**: The script attempts to log in to the FTP server using each password in the wordlist. It uses asynchronous tasks to attempt multiple passwords concurrently, which speeds up the process.

4. **Concurrency Control**: The script limits the number of concurrent attempts to avoid overloading the server.

5. **Output**: If a correct password is found, it is displayed on the terminal in green. If the brute-force attack fails to find a valid password, a failure message is displayed in red.

## Output

- **Success**: If the correct password is found, it will be displayed in green as follows:

  ```
  [21] [ftp] host: 192.168.1.10 login: admin password: password123
  ```

- **Failure**: If no correct password is found, a failure message will be displayed in red:

  ```
  [-] Failed to find the correct password.
  ```

## Important Notes

- **Ethical Use**: This tool is intended for educational purposes only. Do not use it for illegal activities.
- **Permission**: Ensure you have explicit permission from the owner of the target server before using this tool.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```

This `README.md` provides a complete guide to the project, including installation, usage, and ethical considerations.
