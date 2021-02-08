import platform

# Method 1 - using individual methods

print('=========using individual methods========')

print('Operating System : ', platform.system())
print('Hostname : ', platform.node())
print("Machine : ", platform.machine())
print("Processor : ", platform.processor())
print("Release : ", platform.release())
print("Version : ", platform.version())

# Method 2 - using uname method

system_data = platform.uname()

print('=========using uname method========')
print('Operating System : ', system_data.system)
print('Hostname : ', system_data.node)
print("Machine : ", system_data.machine)
print("Processor : ", system_data.processor)
print("Release : ", system_data.release)
print("Version : ", system_data.version)

