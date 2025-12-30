line = "2025-12-30 10:15:23 INFO User logged in: user123\n"

splited_line = line.split(" ")
parse_line = {'timestamp' : splited_line[0]+" "+splited_line[1] ,
                  'level' : splited_line[2],
                  'message' : " ".join(splited_line[3:]).strip()
                  }

print(parse_line)