CMD CHALLENGE is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

In addition to completing the project tasks and submitting the required screenshots to GitHub, you are also required to demonstrate the use of the SFTP (Secure File Transfer Protocol) command-line tool to move your local screenshots to the sandbox environment.

**Here are the steps to follow for windows users**
1. Take the screenshots
2. Download WinSCP
3. Once installed, launch WinSCP.
4. Configure the Connection:
**In the WinSCP login window:**
-Choose "SFTP" as the file protocol.
-Enter the hostname, username, and password provided to you for the sandbox environment.
-Click the "Login" button to connect.
5. Navigate to Target Directory:
After connecting to the sandbox environment, you should see two panels. The left panel represents your local machine, and the right panel represents the remote server (sandbox environment). Navigate to the directory where you want to upload the screenshots in the right panel. In this case, navigate to /root/alx-system_engineering-devops/command_line_for_the_win/.
6. Upload Screenshots:
In the left panel, navigate to the local directory where you have the screenshots. Then, in the left panel, select the screenshots you want to upload and drag them to the right panel's target directory (sandbox).
7. Confirm Transfer:
After the upload is completed, you can confirm that the screenshots have been successfully transferred by checking the right panel's content (sandbox directory).
8. Push Screenshots to GitHub:
Once the screenshots are transferred to the sandbox environment, you can proceed to push the screenshots to GitHub as mentioned in the initial requirements. Follow the regular steps you use to push files to your GitHub repository.
