# meal.py

def main():

    time_input = input("What time is it? ")

    hour = convert(time_input)

    if 7.0 <= hour <= 8.0:
        print("breakfast time")
    elif 12.0 <= hour <= 13.0:
        print("lunch time")
    elif 18.0 <= hour <= 19.0:
        print("dinner time")



def convert(time):
    
    hours, minutes = time.split(":")

    hours = int(hours)
    minutes = int(minutes)

    return hours + minutes / 60

if __name__ == "__main__":   
    main()
