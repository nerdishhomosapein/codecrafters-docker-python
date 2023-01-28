import subprocess
import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    #
    command = sys.argv[3]
    args = sys.argv[4:]

    completed_process = subprocess.run([command, *args], capture_output=True)
    returnCode = completed_process.returncode
    output = completed_process.stdout.decode("utf-8")
    error = completed_process.stderr.decode("utf-8")
    if output:
        output = output.strip("\n")
        print(f"{output}")

    if error:
        error = error.strip("\n")
        print(f"{error}", file=sys.stderr)
    return sys.exit(returnCode)

if __name__ == "__main__":
    main()
