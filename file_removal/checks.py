def is_target_file(file_name, ext_list) -> bool:
    return any(file_name.endswith(ext) for ext in ext_list)
