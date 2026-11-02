

def running_total():
    total = 0
    count = 0
    while True:
        entry = input("Please enter numbers to your running total, or type 'done': ").strip().lower()

        if entry == "done":
            break
        else:
            try: 
                number = int(entry)
            except ValueError:
                print("Invalid entry!")
                continue

        total += number
        count += 1

    print(f"Total: {total}")
    if count > 0:
        print(f"Mean: {total/count}")
    else:
        print("No numbers entered; no mean.")

running_total()