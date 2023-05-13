TO RUN THE SCRIPT ON TARGET MACHINES:
Step 1:
Install Ansible on your local machine. You can download the latest version of Ansible from the official website: https://www.ansible.com/

Step 2: 
Update inventory.ini with the IP address of all your machines

Step 3: 
Run the ansible playbook using
  ansible-playbook -i inventory.ini deploy_agent.yml

This configuration sets up Squid to listen on port 3128, allows access from the local network, and denies access from all other sources. 
Change your configuration at the squid.conf file. 

TO RUN THE ADMIN GUI:
Step 1: 
Run the command python main.py and enter your target address and update the configuration as required. Verify the script if you have 
changed the location of the squid configuration file on your machine