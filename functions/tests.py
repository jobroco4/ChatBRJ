import get_files_info

def test1():
    get_files_info = get_files_info()
    result = get_files_info.evaluate("calculator", ".")
    assert result ==  f'- main.py: file_size=719 bytes, is_dir=False' + '\n' + f'- tests.py: file_size=1331 bytes, is_dir=False' + '\n' + f'- pkg: file_size=44 bytes, is_dir=True'
    print("Test 1 passed")

def test2():
    get_files_info = get_files_info()
    result = get_files_info.evaluate("calculator", "pkg")
    assert result == f'- calculator.py: file_size=1721 bytes, is_dir=False' + '\n' + f'- render.py: file_size=376 bytes, is_dir=False'
    print("Test 2 passed")

def test3():
    get_files_info = get_files_info()
    result = get_files_info.evaluate("calculator", "/bin")
    assert result == 'Error: Cannot list "/bin" as it is outside the permitted working directory'
    print("Test 3 passed")

def test4():
    get_files_info = get_files_info()
    result = get_files_info.evaluate("calculator", "../")
    assert result == 'Error: Cannot list "../" as it is outside the permitted working directory'
    print("Test 4 passed")

