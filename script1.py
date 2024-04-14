import socket
import os
import sys
import hashlib
from Crypto.Cipher import AES

KEY = hashlib.sha256(b"some random password").digest()		                # AES Key

IV = b"abcdefghijklmnop"								                 	#Initialization vector should always be 16 bit
obj_enc = AES.new(KEY, AES.MODE_CFB, IV)					            	#creating an object to encrypt our data with

# Function to Upload File
def upload_file(filename, host, port , file_contents):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:       # Creating a socket
            s.connect((host, port))
            print(f"Connected to {host}:{port}")

            message = f"{os.path.basename(filename)}\n{file_contents}"     # Creating data message
            message_enc = obj_enc.encrypt(message.encode('utf-8'))         # Encrypting data with AES
            print("Encrypting data with AES")
            print("Encrypted data:", message_enc)
            s.sendall(message_enc)                                         # Sending data to the script2 server
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
