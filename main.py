import os
import pprint
from headers import FIELDS as headers

def parse_csv(path) -> list[dict]:
    """Load a CSV file into a list of dictionaries."""
    with open(path, 'r') as f:
        lines = f.readlines()
    header = lines[0].strip().split(',')
    header = [headers.get(h, h) for h in header]
    data = []
    for line in lines[1:]:
        data.append(dict(zip(header, line.strip().split(','))))
    return data

if __name__ == '__main__':
    data = parse_csv('input/data.csv')
    data = [line for line in data if line['searchSubject.orientation'] == 'client']
    
    # Create output folder if not exists
    if not os.path.exists('output'):
        os.makedirs('output')
    
    # Group by dest_ip
    grouped_data = {}
    for line in data:
        # Only add line if the exact combination of dest_ip, dest_port and dest_protocol does not already exist
        if not any(line['dest_ip'] == l['dest_ip'] and line['dest_port'] == l['dest_port'] and line['dest_protocol'] == l['dest_protocol'] for l in grouped_data.get(line['dest_ip'], [])):
            grouped_data.setdefault(line['dest_ip'], []).append(line)
    
    # Write output files, one per dest_ip
    for dest_ip, lines in grouped_data.items():
        with open(f'output/{dest_ip}.csv', 'w') as f:
            f.write('src_ip,dest_port,dest_protocol\n')
            for line in lines:
                f.write(f"{line['src_ip']},{line['dest_port']},{line['dest_protocol']}\n")