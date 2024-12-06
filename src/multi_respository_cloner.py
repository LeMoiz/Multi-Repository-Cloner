import os
import subprocess

def clone_repos(repos_file_path, target_directory):
    # Create the target directory if it does not exist
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    os.chdir(target_directory)

    with open(repos_file_path, 'r') as file:
        repos = file.readlines()

    # Clone each repository
    for repo in repos:
        repo = repo.strip()
        if repo:
            result = subprocess.run(['git', 'clone', repo])
            if result.returncode != 0:
                print(f"Failed to clone repository: {repo}")
            else:
                print(f"Successfully cloned: {repo}")

if __name__ == '__main__':
    # EXAMPLE USAGE
    repos_file_path = '../repos.txt'
    target_directory = './cloned_repos'
    
    clone_repos(repos_file_path, target_directory)