def analyze_logs(file_name):
    try:
        with open(file_name, "r") as file:
            logs = file.readlines()

        error_count = 0
        warning_count = 0

        print("---- Error Logs ----")
        for line in logs:
            if "ERROR" in line:
                print(line.strip())
                error_count += 1

        print("\n---- Warning Logs ----")
        for line in logs:
            if "WARNING" in line:
                print(line.strip())
                warning_count += 1

        print("\nSummary:")
        print(f"Total Errors: {error_count}")
        print(f"Total Warnings: {warning_count}")

    except FileNotFoundError:
        print("Log file not found.")
    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    analyze_logs("server.log")
