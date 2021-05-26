from pathlib import Path
from enum import Enum

import json
import os
import sys

allowedOperations = ["IS_COMPATIBLE", "PERSIST_INFO", "MARKDOWN"]

operation = os.environ['OPERATION']
compatibilityFile = os.environ['ROOT_FOLDER'] + "/" + os.environ['COMPATIBILITY_FILE']
componentOne = os.environ['COMPONENT_ONE']
versionOne = os.environ['VERSION_ONE']
componentTwo = os.environ['COMPONENT_TWO']
versionTwo = os.environ['VERSION_TWO'] 
compatibility = os.environ['COMPATIBLE']

class Compatibility(Enum):
    TRUE = 1
    FALSE = 2
    UNKNOWN = 3 

def check_compatibility(compatFilePath, c1, c2, v1, v2):
    compatFile = Path(compatFilePath)
    if not compatFile.is_file():
        return Compatibility.UNKNOWN

    with open(compatFilePath) as json_file:
        compatibilityInformation = json.load(json_file)
        for compatInfo in compatibilityInformation:
            if not c1 in compatInfo or not c2 in compatInfo:
                continue
            if compatInfo[c1] == v1 and compatInfo[c2] == v2:
                if to_bool(compatInfo["compatible"]):
                    return Compatibility.TRUE
                else:
                    return Compatibility.FALSE
    
    return Compatibility.UNKNOWN

def persist_compatibility_info(compatFilePath, c1, c2, v1, v2, compatible):
    compatFile = Path(compatFilePath)
    compatInfo = []
    if compatFile.is_file():
        compatInfo = json.load(open(compatFilePath))
    new_info = {c1: v1, c2: v2, "compatible": compatible}
    old_element = {}
    for info in compatInfo:
        if not c1 in info or not c2 in info:
            continue
        if info[c1] == v1 and info[c2] == v2:
            old_element = info
    if old_element:
        compatInfo.remove(old_element)
    compatInfo.append(new_info)
    print(compatInfo)
    with open(compatFilePath, 'w') as outfile:
        json.dump(compatInfo, outfile)

def parse_to_markdown(compatFilePath, c1, c2):
    markdown_output = f"| {c1} | {c2} | Compatible | \n |-------|------|-----| \n"
    compatFile = Path(compatFilePath)
    if not compatFile.is_file():
        print("No compatibility info provided.")
        sys.exit(1)
    with open(compatFilePath) as json_file:
        compatibilityInformation = json.load(json_file)
        for info in compatibilityInformation:
            v1 = info[c1]
            v2 = info[c2]
            compat = info["compatible"]
            new_line = f"| ```{v1}``` | ```{v2}``` | ```{compat}``` | \n"
            markdown_output += new_line
    print(markdown_output)
    return markdown_output

def to_bool(stringValue):
    if stringValue == "True":
        return True
    else:
        return False

if operation == "IS_COMPATIBLE": 
    print("Check")
    checkResult = check_compatibility(compatibilityFile, componentOne, componentTwo, versionOne, versionTwo)
    print(checkResult)
    if checkResult != Compatibility.TRUE:
        print(f"{componentOne}:{versionOne} and {componentTwo}:{versionTwo} are not compatible or compatibility is unknown.")
        sys.exit(1)
elif operation == "PERSIST_INFO":
    persist_compatibility_info(compatibilityFile, componentOne, componentTwo, versionOne, versionTwo, to_bool(compatibility))
elif operation == "MARKDOWN":
    parse_to_markdown(compatibilityFile, componentOne, componentTwo)