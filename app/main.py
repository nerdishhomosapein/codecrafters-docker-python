import subprocess
import sys
import os
import shutil
import tempfile
import ctypes



def main():

    command = sys.argv[3]
    args = sys.argv[4:]
    libc = ctypes.CDLL("libc.so.6", use_errno=True)

    CLONE_NEWPID = 0x20000000

    def unshare(flags):
        ret = libc.unshare(flags)
        if ret == -1:
            err = ctypes.get_errno()
            raise OSError(err, os.strerror(err))

    unshare(CLONE_NEWPID)
    with tempfile.TemporaryDirectory() as tempDir:
        os.makedirs(os.path.join(tempDir, os.path.dirname(command).strip("/")))
        shutil.copy(command, os.path.join(tempDir, command.strip("/")))
        os.chroot(tempDir)

        completed_process = subprocess.run([command, *args])
        exit(completed_process.returncode)


if __name__ == "__main__":
    main()
