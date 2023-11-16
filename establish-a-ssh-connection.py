
# Import required modules/packages/Library
from difflib import unified_diff
import difflib
import pexpect

# Define variables
ip_address = '192.168.56.101'
username = 'prne'
password = 'cisco123!'
password_enable = 'class123!'

# Create the SSH session
session = pexpect.spawn('ssh ' + username + '@' + ip_address, encoding='utf-8', timeout=20)
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if exists then display error and exit
if result != 0:
    print('----FAILURE! creating session for: ', ip_address)
    exit()

# Enter enable mode
session.sendline('enable')
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if exists then display error and exit
if result != 0:
    print('----FAILURE! entering enable mode')
    exit()
# Session expecting password, enter details
session.sendline(password)
result = session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])

# Chek for error, if exists the display error and exit
if result != 0:
    print('----Failure! entering password: ', password)
    exit()

# Enter enable mode 
session.sendline('enable')
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if exists then display error and exit
if result != 0:
    print('---- Failure! entering enable mode')
    exit()

# Send enable password details
session.sendline(password_enable)
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if exists then display error and exit
if result != 0:
    print('-----FAILURE! entering enable mode after sending password')
    exit()

# Enter configuration mode
session.sendline('configure terminal')
result = session.expect([r'.\(config\)#', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if exists then display error and exit
if result != 0:
    print('----Failure! entering config mode')
    exit()

# Change the hostname to R1
session.sendline('hostname R1')
result = session.expect([r'R1\(config\)#', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if exists then display error and exit
if result != 0:
    print('----Failure! setting hostname')

# Exit config mode
session.sendline('exit')

# Exit enable mode
session.sendline('exit')

from difflib import Differ

# Create a Differ object
#startup_config = session.sendline("show startup_config")
#running_config = session.sendline("show running_config")
#differ = Differ()
session.sendline('show running-config')
running_config = session.read()

session.sendline('show startup_config')
startup_config = session.read()
compare_configs = running_config, startup_config
# Compare consequence
diff = compare_configs
print('\n---- Differences between running and startup configurations----')
print(diff)


# Display a success message if works
print('------------------------------------')
print('')
print('----Success! connecting to: ', ip_address)
print('----           Username: ', username)
print('')
print('-----------------------------------------')
print('-----------------------------------------')

# Saving the file locally
with open("example_file.txt", "w") as open_file:
    # Write the text to the file
    open_file.write('establish-a-ssh-connection.py')

# Terminate SSH session
session.close()
    