from mergexp import *

# Create a network topology object. This network will automatically
# add IP addresses to all node interfaces and configure static routes
# between all experiment nodes. 
net = Network('pae', addressing==ipv4, routing==static)

# Creating the node.
a,b,c,d = [net.node(name, memory.capacity>=gb(16), image == 'bullseye-edu') for name in ['a','b','c','d']]

# Create a link connecting the three nodes.
link = net.connect([a,b,c,d])

# Make this file a runnable experiment based on our three node topology.
experiment(net)