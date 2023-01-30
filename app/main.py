import subprocess
import sys
import os
import shutil
import tempfile


def main():
        
    command = sys.argv[3]
    args = sys.argv[4:]

    with tempfile.TemporaryDirectory() as tempDir:
        os.makedirs(os.path.join(tempDir, os.path.dirname(command).strip("/")))
        shutil.copy(command, os.path.join(tempDir, command.strip("/")))
        os.chroot(tempDir)

        completed_process = subprocess.run([command, *args])
        exit(completed_process.returncode)

if __name__ == "__main__":
    main()
