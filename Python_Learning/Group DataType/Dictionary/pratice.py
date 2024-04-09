
api_input1= [{"Broker":
                  {"ip":"127.0.0.1", "port" : "1883", "username" : "xyz1", "password" : "pass123", "qos":"2",
                   "calledable_name":"test_name1"},
              "Topic":
                  {'s':['s1','s2'],'p':['p1','p2']}},

                  {"Broker":
                       {"ip": "127.0.0.2", "port": "1883", "username": "xyz2", "password": "pass123", "qos": "0",
                        "calledable_name": "test_name2"},
              "Topic":
                  {'s':['s4','s5'],'p':['p4','p5']}}
             ]
for i in range(len(api_input1)):
    broker = api_input1[i]["Broker"]["ip"]
    port = api_input1[i]["Broker"]["port"]
    username = api_input1[i]["Broker"]["username"]
    password = api_input1[i]["Broker"]["password"]
    qos = api_input1[i]["Broker"]["qos"]
    calledable_name = api_input1[i]["Broker"]["calledable_name"]
    print(broker, port, username, password, qos, calledable_name)

    v2 = (api_input1[i]['Topic'])
    # print(v2['s'])
    # print(v2['p'])
    a1 = v2['s']
    a2 = v2['p']

    for j in range(len(a1)):
        print("Subscribed Topics=",a1[j])

    for k in range(len(a2)):
        print("Published Topics=",a2[k])




'''
api_input1= [
    {"Broker":{'ip':'123','port':'456'},
     "Topic":{'s':['s1','s2'],'p':['p1','p2']}
     },

]

for i in range(len(api_input1)):

    v2=(api_input1[i]['Topic'])
    #for j in range(len(v2)):
    print(v2['s'])
    print(v2['p'])
    a1=v2['s']
    a2=v2['p']
    for j in range(len(a1)):
        print(a1[j])

    for k in range(len(a2)):
        print(a2[k])
'''
