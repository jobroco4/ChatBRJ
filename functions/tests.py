import write_file_content

def test1():
    get_files_info = write_file_content()
    result = get_files_info.evaluate("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    assert result 
    print("Test 1 passed")

def test2():
    get_files_info = write_file_content()
    result = get_files_info.evaluate("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    assert result 
    print("Test 2 passed")

def test3():
    get_files_info = write_file_content()
    result = get_files_info.evaluate("calculator", "/tmp/temp.txt", "this should not be allowed")
    assert result
    print("Test 3 passed")



