class Ring:
    @staticmethod
    def display_array_list(pid):
        print("[", end=" ")
        for x in pid:
            print(x, end=" ")
        print("]")

    @staticmethod
    def init_election(process_id, max_processes, processes, pid, coordinator):
        if processes[process_id - 1]:
            pid.append(process_id)

            temp = process_id

            print(f"Process P{process_id} sending the following list:- ", end="")
            Ring.display_array_list(pid)

            while temp != process_id - 1:
                 # Update temp using modular arithmetic
                if processes[temp]:
                    pid.append(temp + 1)
                    print(f"Process P{temp + 1} sending the following list:- ", end="")

                    
                    Ring.display_array_list(pid)
                temp = (temp + 1) % max_processes 

            coordinator = max(pid)
            print(f"Process P{process_id} has declared P{coordinator} as the coordinator")
            pid.clear()
            return coordinator


    @staticmethod
    def display_processes(max_processes, processes, coordinator):
        for i in range(max_processes):
            if processes[i]:
                print(f"P{i + 1} is up.")
            else:
                print(f"P{i + 1} is down.")
        print(f"P{coordinator} is the coordinator")

    @staticmethod
    def up_process(process_id, processes):
        if not processes[process_id - 1]:
            processes[process_id - 1] = True
            print(f"Process P{process_id} is up.")
        else:
            print(f"Process P{process_id} is already up.")

    @staticmethod
    def down_process(process_id, processes):
        if not processes[process_id - 1]:
            print(f"Process P{process_id} is already down.")
        else:
            processes[process_id - 1] = False
            print(f"Process P{process_id} is down.")

def main():
    max_processes = int(input("Enter the total number of processes: "))
    processes = [True] * max_processes
    pid = []
    coordinator = 1

    while True:
        print("Ring Algorithm")
        print("1. Display processes")
        print("2. Up a process")
        print("3. Down a process")
        print("4. Run election algorithm")
        print("5. Exit Program")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            Ring.display_processes(max_processes, processes, coordinator)
        elif choice == 2:
            process_id = int(input("Enter the process to up: "))
            Ring.up_process(process_id, processes)
        elif choice == 3:
            process_id = int(input("Enter the process to down: "))
            Ring.down_process(process_id, processes)
        elif choice == 4:
            process_id = int(input("Enter the process which will initiate election: "))
            coordinator=Ring.init_election(process_id, max_processes, processes, pid, coordinator)
        elif choice == 5:
            exit(0)
        else:
            print("Error in choice. Please try again.")

if __name__ == "__main__":
    main()
