import json
import os
import subprocess
import time

# Test 1: Check if package.json is created
def test1():
    assert os.path.exists("package.json"), "package.json is not present in your folder"

# Test 2: Check if Axios and Express.js is installed
def test2():
    if os.path.exists("package.json"):
        with open("package.json", "r") as file:
            json_data = file.read()
            data_dict = json.loads(json_data)
            assert "axios" in data_dict["dependencies"] and "express" in data_dict["dependencies"], "Axios and Express.js is not installed"

# Test 3: Check if a suitable project name is given
def test3():
    if os.path.exists("package.json"):
        with open("package.json", "r") as file:
            json_data = file.read()
            data_dict = json.loads(json_data)
            project_name = data_dict["name"]
            assert len(project_name)>0, "Project name not available"

# Test 4: Check if a suitable project description is given
def test4():
    if os.path.exists("package.json"):
        with open("package.json", "r") as file:
            json_data = file.read()
            data_dict = json.loads(json_data)
            project_description = data_dict["description"]
            assert len(project_description)>0, "Project description not available"

# Test 5: Check if server.js and client.js are created
def test5():
    assert os.path.exists("server.js") and os.path.exists("client.js"), "server.js and client.js are not present in your folder"

# Test 6: Check if first post gets created
def test6():
    server_process = subprocess.Popen(['node', 'server.js'], stdout=subprocess.PIPE, text=True)
    time.sleep(5)
    client_process = subprocess.run(['node', 'client.js'], stdout=subprocess.PIPE, text=True)
    assert "Post created successfully" in client_process.stdout, "Error in creating first post"
    server_process.terminate()

# Test 7: Check if second post gets created
def test7():
    server_process = subprocess.Popen(['node', 'server.js'], stdout=subprocess.PIPE, text=True)
    time.sleep(5)
    client_process = subprocess.run(['node', 'client.js'], stdout=subprocess.PIPE, text=True)
    time.sleep(5)
    new_process = subprocess.run(['node', 'client.js'], stdout=subprocess.PIPE, text=True)
    assert "Post created successfully" in new_process.stdout, "Error in creating second post"
    server_process.terminate()

# Test 8: Check server error
def test8():
    client_process = subprocess.run(['node', 'client.js'], stderr=subprocess.PIPE, text=True)
    assert "Error creating post" in client_process.stderr, "Error message not displayed"