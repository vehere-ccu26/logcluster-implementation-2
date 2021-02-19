import os

directory = 'user_data/'
parent_dir = "/home/pratik/Downloads/Projects/logcluster-0.10/logcluster_sec_pattern_discovery/User_behaviour/"
path = os.path.join(parent_dir, directory)

user_data = open("user_data.csv",'r').read().split('\n')

user_ip = []

for data_line in user_data:
    if len(data_line) < 2:
        continue
    data =data_line.split(',')
    ip = data[1]
    time = data[0]
    if ip in user_ip:
        pass
        # if os.path.exists(path + user_ip) == False:
        #     os.mkdir(path + user_ip)
        #     print(path + user_ip)
    else:
        user_ip.append(ip)
        try:
            os.mkdir(path + str(ip))
        except:
            pass
        print(path + str(ip) + '/' + time + '.csv')
    
    try : 
        user_file = open(path + str(ip) + '/' + time + '.csv','a')
    except:
        user_file = open(path + str(ip) + '/' + time + '.csv','w')
    user_file.write(data_line + '\n')

