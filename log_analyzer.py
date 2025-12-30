def read_log_lines(filename):
    with open(filename , "r") as file:
        for line in file:
            yield line
            
def filter_by_level(lines, level):
    for line in lines:
        if level in line:
            yield line

def parse_log_entry(line):
    splited_line = line.split(" ")
    parse_line = {'timestamp' : splited_line[0]+" "+splited_line[1] ,
                  'level' : splited_line[2],
                  'message' : " ".join(splited_line[3:]).strip()
                  }
    return parse_line

def analyze_logs(filename, level=None):
    gen_lines = read_log_lines(filename)
    if level is not None:
        gen_lines = filter_by_level(gen_lines , level)
    result = []    
    for i in gen_lines:
        result.append(parse_log_entry(i))
    return result
    
    
    
    
if __name__ == '__main__':
    # Test 1: Get all logs
    print("=== ALL LOGS ===")
    all_logs = analyze_logs("sample.log")
    for log in all_logs:
        print(log)
    
    print("\n=== ERROR LOGS ONLY ===")
    errors = analyze_logs("sample.log", level="ERROR")
    for log in errors:
        print(log)
    
