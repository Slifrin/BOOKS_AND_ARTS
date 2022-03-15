import first_definition.weather_pb2 as pb



def main():
    print('Hello main')
    message = pb.Temperature(station='s42', value=17.2)
    print(dir(message.time))
    print(message.time)
    print("Current_time: ", message.time.GetCurrentTime())

    data = message.SerializeToString()
    print(data)
    print(len(data))

    message2 = pb.Temperature.FromString(data)
    print(message2)

if __name__ == '__main__':
    main()