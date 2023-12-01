import os
import pprint


if __name__ == '__main__':
    # List all the files in the /output folder
    files = os.listdir('output')
        
    for file in files:
        # Open file
        with open(f'output/{file}', 'r') as f:
            # Read all lines
            lines = f.readlines()
        
        # Remove header
        lines = lines[1:]
        
        # Create a dictionary with the following structure:
        # name: str
        # dest_ip: str (the filename without extension)
        # src_ip: list[str]
        # dest_port: list[str]
        # dest_protocol: list[str]
        data = {}
        data['name'] = '.'.join(file.split('.')[:-1])
        data['dest_ip'] = data['name']
        data['src_ip'] = []
        data['dest_port'] = []
        data['dest_protocol'] = []
        
        # Loop over all lines
        for line in lines:
            # Split the line into a list of values
            line = line.strip().split(',')
            
            # Add the values to the dictionary
            data['src_ip'].append(line[2])
            data['dest_port'].append(line[3])
            data['dest_protocol'].append(line[4])
        
        # Remove duplicates
        data['src_ip'] = list(set(data['src_ip']))
        data['dest_port'] = list(set(data['dest_port']))
        data['dest_protocol'] = list(set(data['dest_protocol']))
        
        # Print the dictionary
        pprint.pprint(data, indent=4)
