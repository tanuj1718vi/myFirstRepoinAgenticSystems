import os


def read_numbers_from_file(file_name):
    numbers_list = []

    script_directory = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_directory, file_name)

    print("Opening file...")

    with open(full_path, "r") as file:
        print("File opened successfully")

        for line in file:
            cleaned_line = line.strip()
            if cleaned_line:
                number = int(cleaned_line)
                numbers_list.append(number)

    print("Data loaded successfully")
    return numbers_list


def compute_statistics(numbers_list):
    print("Starting computation...")

    total_count = len(numbers_list)
    total_sum = sum(numbers_list)

    if total_count > 0:
        average_value = total_sum / total_count
    else:
        average_value = 0

    print("Computation completed")
    return total_count, total_sum, average_value


def write_log(file_name, messages):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_directory, file_name)

    print("Writing results to log file...")

    with open(full_path, "a") as log_file:
        for message in messages:
            log_file.write(message + "\n")

    print("Log file updated successfully")


def main():
    input_file = "numbers.txt"
    log_file = "results.log"

    log_messages = []

    # Step 1: Read file
    numbers = read_numbers_from_file(input_file)
    log_messages.append("File opened successfully")
    log_messages.append(f"Read {len(numbers)} numbers")

    # Step 2: Compute
    count, total, average = compute_statistics(numbers)
    log_messages.append("Computation completed")
    log_messages.append(f"Total numbers: {count}")
    log_messages.append(f"Sum: {total}")
    log_messages.append(f"Average: {average}")

    # Step 3: Log results
    log_messages.append("Processing completed")
    write_log(log_file, log_messages)

    # Final terminal output
    print("\n----- FINAL RESULTS -----")
    print(f"Total numbers: {count}")
    print(f"Sum: {total}")
    print(f"Average: {average}")
    print("Processing completed successfully")


if __name__ == "__main__":
    main()