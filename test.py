import subprocess

# start a new process with pipes for input and output
process = subprocess.Popen(['bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)

# communicate with the process via the pipes
while True:
    try:
        command = input("$ ")
        if command.strip() == 'exit':
            break
        output, error = process.communicate(command + '\n')
        print(output, end='')
    except KeyboardInterrupt:
        break

# close the pipes and wait for the process to exit
process.stdin.close()
process.stdout.close()
process.stderr.close()
process.wait()