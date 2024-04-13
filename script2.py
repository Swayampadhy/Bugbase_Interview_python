import socket
import os
import subprocess
import json

# Function to Receive file and Generate JSON
def receive_file_and_execute(host, port, folder_name):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:                                # Creating a socket
            s.bind((host, port))
            s.listen()
            print(f"Waiting for connection on {host}:{port}")                                       

            conn, addr = s.accept()
            with conn:                                                                              # Confirmation for connection established
                print(f"Connected to {addr}")
            
                received_data = conn.recv(2048).decode()                                            # Receiving and splitting filename and file contents
                split_data = received_data.split('\n', 1)
                filename = split_data[0]                                                            # Split filename
                file_contents = split_data[1] if len(split_data) > 1 else ''                        # File contents

                if not os.path.exists(folder_name):                                                 # Create folder if it doesn't exist
                    os.makedirs(folder_name)
            
                file_path = os.path.join(folder_name, filename)                                     # Full path to file
            
                with open(file_path, "w") as file:                                                  # Receiving and saving the file
                    file.write(file_contents)

                print(f"File '{filename}' received.")                                               # Confirmation for receiving file

                output = subprocess.run(["file", file_path], capture_output=True, text=True)        # Executing "File" command on the file

                response = {"filename": filename, "output": output.stdout}                          # Send the output back to script1.py as JSON
                conn.sendall(json.dumps(response).encode())
                print("File command output sent back as a JSON file.")
                
    except socket.error as e:                                                                       # Handling Socket errors
        print(f'Socket error: {e}')
    except Exception as e:                                                                          # Handling Exceptions
        print(f'Unexpected error: {e}')
    finally:
        conn.close()
        s.close()                                                                                   # Close the connection
    

def main():
    host = "127.0.0.1"                                                                          # Server IP address
    port = 5000                                                                                 # Server port number

    folder_name = input("Enter a foldername to save the file in:")                              # User specifies the foldername to save the file in
    
    receive_file_and_execute(host, port, folder_name)                                           # Receive the file and execute the 'file' command

if __name__ == "__main__":
    main()
