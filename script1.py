import socket
import os
import sys

# Function to Upload File
def upload_file(filename, host, port , file_contents):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:       # Creating a socket
            s.connect((host, port))
            print(f"Connected to {host}:{port}")

            s.sendall((os.path.basename(filename)+'\n').encode())          # Sending the filename to the script2 server
            s.sendall(file_contents.encode())                              # Sending the file contents to the script2 server
            print(f"File '{filename}' uploaded successfully.")             # Confirm the upload
            
            json_data = s.recv(1024).decode()                              # Receiving and printing the JSON data
            print("Received JSON data:\n")
            print(json_data)
            
            json_filename = filename + ".json"                             # saving the JSON data
            with open(json_filename, "w") as json_file:
                json_file.write(json_data)
                print(f"JSON data saved to '{json_filename}'")
                
    except Exception as e:
        print(f"Error uploading file: {e}")                                # Handling Exceptions
        
    finally:
        s.close()                                                          # Closing the socket

# Main function
def main():
    host = "127.0.0.1"                                                     # Server IP address
    port = 5000                                                            # Server port number

    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")                        # Handle command line arguments
        sys.exit(1)

    filename = sys.argv[1]
    
    if not os.path.isfile(filename):                                       # Check if file exists
        print("File not found.")
        return
    
    with open(filename, "r") as file:
        file_contents = file.read()                                        # Save file contents
    
    upload_file(filename, host, port, file_contents)                       # Sending file and receiving JSON response

if __name__ == "__main__":
    main()
