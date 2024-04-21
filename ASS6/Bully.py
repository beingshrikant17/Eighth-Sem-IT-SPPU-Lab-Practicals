class Bully:

    @staticmethod
    def init_election(process_id, max_processes, processes, coordinator):
        coordinator = process_id
        keep_going = True
        for i in range(process_id, max_processes):
            print(f"Election message sent from process {process_id} to process {i + 1}")
            if processes[i]:
                keep_going = False
                coordinator = Bully.init_election(i + 1, max_processes, processes, coordinator)
                break  # Exit the loop since a higher ID process has been found
        Bully.display_processes(max_processes, processes, coordinator)
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

    coordinator = 1

    while True:
        print("Bully Algorithm")
        print("1. Display processes")
        print("2. Up a process")
        print("3. Down a process")
        print("4. Run election algorithm")
        print("5. Exit Program")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            Bully.display_processes(max_processes, processes, coordinator)
        elif choice == 2:
            process_id = int(input("Enter the process to up: "))
            Bully.up_process(process_id, processes)
        elif choice == 3:
            process_id = int(input("Enter the process to down: "))
            Bully.down_process(process_id, processes)
        elif choice == 4:
            process_id = int(input("Enter the process which will initiate election: "))
            coordinator = Bully.init_election(process_id, max_processes, processes, coordinator) 
        elif choice == 5:
            exit(0)
        else:
            print("Error in choice. Please try again.")

if __name__ == "__main__":
    main()
