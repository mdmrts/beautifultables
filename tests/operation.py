"""Returns a string with the operation based on filename as input"""

class Operation():
    def determine_operation(filename):
        first_split = filename.split("/")
        second_split = first_split[1].split(".")
        final_operation = second_split[0]
        return final_operation