import os  # 1. F401 (unused-import)


def calculate_data(df):
    # 2. B006 (mutable-argument-default)
    def append_to_list(value, target_list=[]):
        target_list.append(value)
        return target_list

    # 3. F841 (unused-variable)
    unused_result = append_to_list(10)

    print("Calculations complete")

