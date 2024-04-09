import json

class jsongenerator:
    #Taking nos of equipment and sensor from user
    Enum=int(input("Enter the number of eqipment : "))
    Snum=int(input("Enter the number of sensor : "))
    l=[]
    path=r"F:\new_formatGenerator.json"

    def __init__(self):
        try:
            if self.Snum%self.Enum ==0:
                self.n1=self.Snum//self.Enum
                print("For {} equipment(s) system is assigning {} nos of vSens to each equipment".format(self.Enum,self.n1))
            else:
                self.n1=self.Snum//self.Enum
                print("For {} equipment(s) system is assigning {} nos of vSens".format(self.Enum,self.n1))
                print("Extra Sensor = {}, keep it with you".format(self.Snum%self.Enum))

        except ZeroDivisionError:
            print("Enum can't be zero")
        except Exception:
            print("Invalid Input")

    def equipmentSens(self):
        eqpindex=1
        sensorindex=1

        for i in range(self.Enum):

            a={
                "AttachedSensors":[],
                "Brokers":[
                    {
                        "BrokerName": "192.168.1.129",
                        "IpAddress": "192.168.1.129",
                        "Password": "4X4vF5J0ncI=",
                        "PortNumber": 1883,
                        "UserName": "vegam129"
                    }
                ],
                "EquipmentClass": "",
                "EquipmentID": "MotorTypeEquipment_2021_03_motor"+str(eqpindex),
                "EquipmentName": "Motor"+str(eqpindex),
                "EquipmentNumber": "E0734_"+str(eqpindex)
               }
            eqpindex+=1
            self.l.append(a)
            for j in range(self.n1):
                b={
                    "AxisX": "X",
                    "AxisY": "Y",
                    "AxisZ": "Z",
                    "ConnectionMode": "B",
                    "SensorIdentifier": str(sensorindex),
                    "SensorIdentifierOld": "",
                    "SensorMacID": "Sensor"+str(sensorindex),
                    "Tags":[
                        {
                            "Topic": "Sensor"+str(sensorindex),
                            "TopicRepresents": "NONE",
                            "TopicType": "P"
                        },
                        {
                            "Topic": "Sensor"+str(sensorindex)+"/RMSX",
                            "TopicRepresents": "RMSX",
                            "TopicType": "S"
                        },
                        {
                            "Topic": "Sensor"+str(sensorindex)+"/VelocityX",
                            "TopicRepresents": "VELOCITYX",
                            "TopicType": "S"
                        },
                        {
                            "Topic": "Sensor"+str(sensorindex)+"/DisplacementX",
                            "TopicRepresents": "DISPLACEMENTX",
                            "TopicType": "S"
                        },
                        {
                            "Topic": "Sensor"+str(sensorindex)+"/FFTX",
                            "TopicRepresents": "FFTX",
                            "TopicType": "S"
                        },
                        {
                            "Topic": "Sensor"+str(sensorindex)+"/AccelerometerX",
                            "TopicRepresents": "ACCX",
                            "TopicType": "S"
                        },
                        {
                            "Topic": "Sensor"+str(sensorindex)+"/RMSY",
                            "TopicRepresents": "RMSY",
                            "TopicType": "S"
                        },
                        {
                            "Topic": "Sensor"+str(sensorindex)+"/VelocityY",
                            "TopicRepresents": "VELOCITYY",
                            "TopicType": "S"
                        },
                        {
                            "Topic": "Sensor"+str(sensorindex)+"/DisplacementY",
                            "TopicRepresents": "DISPLACEMENTY",
                            "TopicType": "S"
                        },
                        {
                            "Topic": "Sensor"+str(sensorindex)+"/FFTY",
                            "TopicRepresents": "FFTY",
                            "TopicType": "S"
                        },
                        {
                            "Topic": "Sensor"+str(sensorindex)+"/AccelerometerY",
                            "TopicRepresents": "ACCY",
                            "TopicType": "S"
                        },
                        {
                            "Topic": "Sensor"+str(sensorindex)+"/RMSZ",
                            "TopicRepresents": "RMSZ",
                            "TopicType": "S"
                        },
                        {
                            "Topic": "Sensor"+str(sensorindex)+"/VelocityZ",
                            "TopicRepresents": "VELOCITYZ",
                            "TopicType": "S"
                        },
                        {
                            "Topic": "Sensor"+str(sensorindex)+"/DisplacementZ",
                            "TopicRepresents": "DISPLACEMENTZ",
                            "TopicType": "S"
                        },
                        {
                            "Topic": "Sensor"+str(sensorindex)+"/FFTZ",
                            "TopicRepresents": "FFTZ",
                            "TopicType": "S"
                        },
                        {
                            "Topic": "Sensor"+str(sensorindex)+"/AccelerometerZ",
                            "TopicRepresents": "ACCZ",
                            "TopicType": "S"
                        },
                        {
                            "Topic": "Sensor"+str(sensorindex)+"/OnOffStatus",
                            "TopicRepresents": "ONOFF",
                            "TopicType": "P"
                        },
                        {
                            "Topic": "Sensor"+str(sensorindex)+"/HealthStatus",
                            "TopicRepresents": "HEALTH",
                            "TopicType": "P"
                        },
                        {
                            "Topic": "Sensor"+str(sensorindex)+"/FaultStatus",
                            "TopicRepresents": "FAULT",
                            "TopicType": "P"
                        }
                    ]
                }
                sensorindex+=1
                a['AttachedSensors'].append(b)
        print(self.l)

        json_obj=json.dumps(self.l,indent=4)
        with open(self.path,'w') as file1:
            file1.write(json_obj)
o1=jsongenerator()
o1.equipmentSens()