import re
import itertools
import os
import math

def main():
    with open("DorkTypes.txt", 'r') as f:
        dork_types = f.readlines()
        dork_types = [dork_type.strip() for dork_type in dork_types]

    place_holder_list = []
    
    pattern1 = re.compile(r'\((.*?)\)')

    for line in dork_types:
        matches = pattern1.findall(line)
        for match in matches:
            place_holder_list.append(match)
    combinations = itertools.product(*[open(f"{place_holder}.txt", 'r').read().splitlines() for place_holder in place_holder_list])

    lengths = [len(open(f"{place_holder}.txt", 'r').read().splitlines()) for place_holder in place_holder_list]
    # Calculate the product of the lengths
    num_dorks = math.prod(lengths)
    num_dorks_str = "{:,}".format(num_dorks)
    print(f"Number of dorks: {num_dorks_str}")

    for combination in combinations:
        modified_dork_types = dork_types.copy()
        for i, line in enumerate(modified_dork_types):
            for j, place_holder in enumerate(place_holder_list):
                # modified_dork_types[i] = re.sub(f'\({place_holder}\)', combination[j], modified_dork_types[i]) # regex
                pattern = re.compile(f'\({place_holder}\)')
                modified_dork_types[i] = pattern.sub(combination[j], modified_dork_types[i])
        modified_dork_types_str = " ".join(modified_dork_types)
        with open("combination.txt", "a") as f:
            f.write(f"{modified_dork_types_str}\n")

if __name__ == "__main__":
    if "combination.txt" in os.listdir():
        os.remove("combination.txt")
    main()
