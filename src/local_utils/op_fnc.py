

import time, datetime

print("Output functions loaded")

def write_txt(file_suffix,append_text):
    with open("data/output/cap_oppr_" + file_suffix + ".txt", "w+") as f:
        f.write(str(datetime.datetime.now().isoformat()) + " - " + append_text + "\n")
        
        
def write_log(log_text):
    with open("data/logs/cap_oppr.log", "a+") as f:
        f.write(str(datetime.datetime.now().isoformat()) + " - " + log_text + "\n")