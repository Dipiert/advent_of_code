from pathlib import Path

def get_file_as_str(path='input.txt'):
    p = Path(__file__).with_name(path)

    with p.open("r") as f:
        file = f.read()
        
    return file
    
    