import subprocess

version = '0.87'

command1 = 'sudo docker build -t ogruiz/ampdocs:' + version + ' .'
command2 = 'sudo docker push ogruiz/ampdocs:' + version


def subprocess_cmd(command, directory):
    output = subprocess.check_output(command, shell=True).decode("utf-8")
    print(output)
    
    
subprocess_cmd(command1, 'ampDocs')
subprocess_cmd(command2, 'ampDocs')

