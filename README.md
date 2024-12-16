# Git Repository Cloner

This Python script automates the process of cloning multiple Git repositories from a list of URLs. It reads repository URLs from a file and clones them into a specified directory.

## Features
- Reads repository URLs from a text file.
- Clones repositories into a specified target directory.
- Automatically creates the target directory if it doesn’t exist.
- Provides feedback on the success or failure of each repository clone operation.

## Usage

### Prerequisites
- Python 3.x installed on your system.
- Git installed and available in your system’s PATH.

### Script Parameters
1. **`repos_file_path`**: The path to the file containing the list of repository URLs (one per line).
2. **`target_directory`**: The directory where repositories will be cloned.

### Example Usage

#### `repos.txt` File Example
```txt
https://github.com/example/repo1.git
https://github.com/example/repo2.git
https://github.com/example/repo3.git
```

#### Script Example
```python
repos_file_path = '../repos.txt'  # Path to your repos.txt file
target_directory = './cloned_repos'  # Directory to clone repositories

clone_repos(repos_file_path, target_directory)
```

### How It Works
1. The script reads the `repos.txt` file to get a list of repository URLs.
2. It checks if the target directory exists; if not, it creates the directory.
3. Changes the working directory to the target directory.
4. Iterates over each repository URL:
   - Executes `git clone <repo_url>` using the `subprocess.run` command.
   - Prints a success message if cloning is successful, or an error message if it fails.

### Output
- Cloned repositories will be stored in the specified target directory.
- Feedback on each repository clone operation will be printed to the console.

### Error Handling
- If a repository URL is invalid or unreachable, the script will print an error message and continue with the next repository.
- Checks if directories exist before proceeding.

### Example Directory Structure After Cloning
```
cloned_repos/
├── repo1/
├── repo2/
└── repo3/
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## Author
Me
