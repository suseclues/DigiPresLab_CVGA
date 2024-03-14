import os
from bagit import Bag

def validate_bags_in_directory(directory):

    validation_fails = []

    # count the bags
    total_bags = 0
    failed_bags = 0

    # loops over bags in the directory
    for bag_name in os.listdir(directory):
        bag_path = os.path.join(directory, bag_name)
        if os.path.isdir(bag_path):
            total_bags += 1
            try:
                bag = Bag(bag_path)
                bag.validate()
            except Exception as e:
                failed_bags += 1
                validation_fails.append(bag_name)

    # Loop through folders in the directory
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        if os.path.isdir(folder_path):
            # Loop through bags in the folder
            for bag_name in os.listdir(folder_path):
                bag_path = os.path.join(folder_path, bag_name)
                if os.path.isdir(bag_path):
                    total_bags += 1
                    try:
                        bag = Bag(bag_path)
                        bag.validate()
                    except Exception as e:
                        failed_bags += 1
                        validation_fails.append(bag_name)

    # write the failed bag names to file
    with open('validation_fails.txt', 'w') as f:
        for name in validation_fails:
            f.write(name + '\n')

    return total_bags, failed_bags

bag_directory = "Path to directory"
validated, failed = validate_bags_in_directory(bag_directory)
print(f"Total bags validated: {validated}")
print(f"Total bags failed: {failed}")
