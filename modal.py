def add_user(username, password, days, user_info, chat_id):
    # Check if the user is verified
    if not user_verified(chat_id):
        return "You need to verify yourself first by providing the secret key using /verify command."

    current_date = datetime.now()
    expiration_date = current_date + timedelta(days=int(days))
    expiration_date_str = expiration_date.strftime('%Y-%m-%d')

    # Check if the user already exists
    existing_users = subprocess.check_output(['cat', '/etc/passwd']).decode('utf-8')
    if f'{username}:' in existing_users and user_info.lower() not in existing_users.lower():
        return f"User {username} already exists with a different info."

    # Generate hashed password
    osl_version = subprocess.check_output(['openssl', 'version']).decode('utf-8')
    osl_version = osl_version.split()[1][:5]
    password_option = '-6' if osl_version == '1.1.1' else '-1'
    passs = subprocess.check_output(['openssl', 'passwd', password_option, password]).decode('utf-8').strip()

    # Create user
    try:
        subprocess.run(['sudo', 'useradd', '-M', '-s', '/bin/false', '-e', expiration_date_str, '-K', f'PASS_MAX_DAYS={days}', '-p', passs, '-c', f'{user_info},{password}', username], check=True)

        # Get server IP address
        server_ip = subprocess.check_output(['hostname', '-I']).decode('utf-8').strip()

        # Send success message with details
        success_message = f"User {username} added successfully!\n\nServer Details:\n{server_ip}:1-65535@{username}:{password}"
        return success_message
    except subprocess.CalledProcessError as e:
        return f"Failed to add user {username}. Error: {e}"
