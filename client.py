from ftplib import FTP


def main():
    ftp = FTP()

    try:
        # Connect to FTP server
        ftp.connect("127.0.0.1", 2121)
        print("Connected to FTP server")

        # Login
        ftp.login("user", "12345")
        print("Login successful")

        while True:
            print("\n------- FTP CLIENT -------")
            print("1. List files")
            print("2. Upload files")
            print("3. Download files")
            print("4. Delete files")
            print("5. Quit")

            choice = input("Enter your choice: ")

            # List files
            if choice == "1":
                print("\nFiles on server:")
                ftp.retrlines("LIST")

            # Upload file
            elif choice == "2":
                filename = input("Enter the filename to upload: ")

                try:
                    with open(filename, "rb") as file:
                        ftp.storbinary("STOR " + filename, file)

                    print("File uploaded successfully.")

                except FileNotFoundError:
                    print("File not found.")

            # Download file
            elif choice == "3":
                filename = input("Enter the file to download: ")

                try:
                    with open("download_" + filename, "wb") as file:
                        ftp.retrbinary(
                            "RETR " + filename,
                            file.write
                        )

                    print("File downloaded successfully.")

                except Exception as e:
                    print("Download failed:", e)

            # Delete file
            elif choice == "4":
                filename = input("Enter the filename to delete: ")

                try:
                    ftp.delete(filename)
                    print("File deleted successfully.")

                except Exception as e:
                    print("Delete failed:", e)

            # Quit
            elif choice == "5":
                ftp.quit()
                print("Disconnected from server.")
                break

            else:
                print("Invalid choice.")

    except Exception as e:
        print("Connection failed:", e)


if __name__ == "__main__":
    main()

