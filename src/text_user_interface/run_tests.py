import subprocess
import threading


class RunTests:
    def __init__(self):
        pass

    def run_command(self, command):
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        output, error = process.communicate()
        print("Output:", output.decode())
        if error:
            print("Error:", error.decode())

    def run_tests(self):
        command = (
            "python -m pytest -v ./test/test_hash_table.py"
        )
        thread = threading.Thread(target=self.run_command, args=(command,))
        thread.start()
        thread.join()
