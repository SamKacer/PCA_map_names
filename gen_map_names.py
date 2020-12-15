import re
import sys

def extract_map_name(line: str):
    match = re.search("mapgroup (.+),.+,", line)
    if not match: return None
    else: return match.group(1)

def format_name(raw_name: str) -> str:
    return raw_name.replace('_', ' ').lower().replace(' rb', '').title()

#assume is formatted
def output_map_name(map_id, map_name):
    print(f"[{map_id}] = \"{map_name}\",")

if __name__ == "__main__":
    filename = sys.argv[1]
    group_number = int(sys.argv[2])
    map_number = 1
    with open(filename) as f:
        print('maps = {')
        for line in f:
            if 'newgroup' in line:
                group_number += 1
                map_number = 1
            else:
                maybe_map_name = extract_map_name(line)
                if not maybe_map_name: continue
                map_id = group_number * 256 + map_number
                map_number += 1
                output_map_name(map_id, format_name(maybe_map_name))
        print('}')
