# Introduction
--------
This repository contains the codes of the Python scripting task required for security engineer intern position at Bugbase. The task is to create 2 python scripts in which script1 sends a user specified file encrypted using AES-256 to script2. Script2 decrypts the data and saves the file in a designated folder and runs the "File" command on it. The output is formatted as JSON and sent back to script1.


# Design
---------

![image](https://github.com/Swayampadhy/Bugbase_Interview_python/assets/37104162/7d9f7ae3-bdd9-4f78-8045-1a6db354ee79)


# Working
----------
This project consists of two scripts - script1.py and script2.py. It's working is as follows -

1. Script1 allows an user to give the filename ofthe file to be uploaded through command line arguments.
2. Then the contents of the specified file is stored in a variable.
3. Script1 creates a TCP socket and connects to script2 which is acting as a server.
4. While starting script2, the user is asked to specify a foldername in which the received file is going to be stored.
5. Script1 encrypts the data using AES-256 using the provided key and initialization vector.
6. Script1 then sends the encrypted data to script2 through the TCP connection.
7. Script2 receives the encrypted data and decrypts it using the same key and IV.
8. Both filename and file contents are separated using a delimiter - '\n' and they are split at script2 into an array.
9. Script2 checks if the specified foldername is created or not. If it is not created, then it uses the os.makedirs() module to create one.
10. A file path is created by joining the received filename and the foldername using os.path.join() function.
11. The file is written in the file path.
12. Script2 uses the python's subprocess module to create a new process to run unix's "File" command on the received file.
13. Output from the command is sent bak to script1 as JSON data using the JSON module.
14. Script1 receives the JSON data and prints it to stdout.
15. The received JSON data is also saved to a created JSON file.
16. The scripts can also handle runtime exceptions and show the underlying problem.

# Steps to run
-----------

1. Create a python virtual Environment using - `virtualenv <name>`.

  ![image](https://github.com/Swayampadhy/Bugbase_Interview_python/assets/37104162/4997a6df-6328-4c75-93fa-9e2abc761e3e)

2. Start the virtual environment

   ![image](https://github.com/Swayampadhy/Bugbase_Interview_python/assets/37104162/c94a9951-f8d4-46a2-8881-01fb832b3b14)

4. In one terminal, run - `python script2.py`. Then enter the desired foldername when prompted by the program.

   ![image](https://github.com/Swayampadhy/Bugbase_Interview_python/assets/37104162/379d7bbb-96fd-4612-8ce3-88a9f7939183)

5. In another terminal, run - `python script1.py <file name>` and specify the desired file to transfer as a command line argument and run.

  ![image](https://github.com/Swayampadhy/Bugbase_Interview_python/assets/37104162/a62c9494-051f-4a3d-b068-6147d02fdc16)

6. Now upon executing `ls` command, it can be seen that a JSON file has been created. This JSON file has the results of the FILE operation saved on disk.

   ![image](https://github.com/Swayampadhy/Bugbase_Interview_python/assets/37104162/4da30235-cf6b-4f33-a63f-a199f66256dd)

7. Going back to the previous terminal, it can be seen that script2 has also printed it's output and stopped executing.

   ![image](https://github.com/Swayampadhy/Bugbase_Interview_python/assets/37104162/fe8faef8-1e7d-41e4-b013-bd76a8322ad0)

# To-Do
------
Add SSL to the TCP connection
