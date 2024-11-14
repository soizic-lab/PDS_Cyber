from mergexp import *

# Create a network topology object. This network will automatically
# add IP addresses to all node interfaces and configure static routes
# between all experiment nodes. 
net = Network('dpra', addressing==ipv4, routing==static)

# Creating the node.
nodes = [net.node(name, memory.capacity>=gb(16), image == 'bullseye-edu') for name in ['nodex']]

# Making the experiment runnable.
experiment(net)