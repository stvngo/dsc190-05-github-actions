def calculate_data(df):
    def append_to_list(value, target_list=None):
        if target_list is None:
            target_list = []
        target_list.append(value)
        return target_list

    append_to_list(10)

    print("Calculations complete")
