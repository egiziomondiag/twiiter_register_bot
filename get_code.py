def get_code(data_str):
    data_arr = data_str.split(":")
    email = data_arr[0]
    password = data_arr[1]
    return email,password
