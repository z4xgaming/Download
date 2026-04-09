#!/usr/bin/env python3 
#YOU CHANGE THIS FILE AND LEAK IN YOUR CHANNEL SO GIVE CREDIT @sulav_codex_01 , @agajayofficial
#OTHER WISE I F*CK YOU 
# -*- coding: utf-8 -*-

import requests
import time
import sys
from os import system

# ========== STYLING CONSTANTS ==========
R = '\033[91m'   # Red
G = '\033[92m'   # Green
Y = '\033[93m'   # Yellow
B = '\033[94m'   # Blue
P = '\033[95m'   # Purple
C = '\033[96m'   # Cyan
W = '\033[97m'   # White
BR = '\033[1m'   # Bold
RS = '\033[0m'   # Reset

def clear():
    system('clear' if sys.platform != 'win32' else 'cls')

def type_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_header():
    clear()
    banner = f"""
{BR}{C}╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                                  ║
║   ▄████  ▄▄▄       ██▀███   ██▓▓█████  ███▄    █  ▄▄▄       ██░ ██              ║
║  ██▒ ▀█▒▒████▄    ▓██ ▒ ██▒▓██▒▓█   ▀  ██ ▀█   █ ▒████▄    ▓██░ ██              ║
║ ▒██░▄▄▄░░▒▀▀██    ▓██ ░▄█ ▒▒██▒▒███   ▓██  ▀█ ██▒▒██  ▀█▄  ▒██▀▀██              ║
║ ░▓█  ██▓░  ▄██    ▒██▀▀█▄  ░██░▒▓█  ▄ ▓██▒  ▐▌██▒░██▄▄▄▄██ ░▓█ ░██              ║
║ ░▒▓███▀▒ ▒████▀▒  ░██▓ ▒██▒░██░░▒████▒▒██░   ▓██░ ▓█   ▓██▒░▓█▒░██▓             ║
║  ░▒   ▒   ░▒   ▒  ░ ▒▓ ░▒▓░░▓  ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒   ▓▒█░ ▒ ░░▒░▒             ║
║   ░   ░    ░   ░    ░▒ ░ ▒░ ▒ ░ ░ ░  ░░ ░░   ░ ▒░  ▒   ▒▒ ░ ▒ ░▒░ ░             ║
║ ░ ░   ░  ░ ░   ░    ░░   ░  ▒ ░   ░      ░   ░ ░   ░   ▒    ░  ░░ ░             ║
║       ░        ░     ░      ░     ░  ░         ░       ░  ░ ░  ░  ░             ║
║                                                                                  ║
║                      {Y}🔐 GARENA ACCOUNT SECURITY TOOL 🔐{C}                                ║
║                                                                                  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  {BR}{P}Developer    :{RS}{C} @sulav_codex_ff  , @agajayofficial                                       {C}║
║  {BR}{P}Made by      :{RS}{C} Sulavcodex , Agajayofficial                                               {C}║
║  {BR}{P}Version      :{RS}{C} 2.0 | Elite Edition                                      {C}║
║  {BR}{P}Type         :{RS}{C} Advanced Account Management                              {C}║
╚══════════════════════════════════════════════════════════════════════════════╝{RS}
"""
    print(banner)

def print_menu():
    print(f"""
{BR}{Y}┌─────────────────────────────────────────────────────────────────┐
│                         📋 MAIN MENU 📋                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│   {G}[{C}01{G}] {W}• Add Recovery Email        {G}[{C}05{G}] {W}• Unbind Email                    │
│   {G}[{C}02{G}] {W}• Check Recovery Email      {G}[{C}06{G}] {W}• Change Bind Email               │
│   {G}[{C}03{G}] {W}• Check Linked Platforms    {G}[{C}07{G}] {W}• Revoke Access Token             │
│   {G}[{C}04{G}] {W}• Cancel Recovery Email     {G}[{C}00{G}] {W}• Exit                            │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘{RS}
    """)

def loading_animation(text="Processing", duration=1):
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    for i in range(int(duration * 10)):
        sys.stdout.write(f"\r{BR}{Y}{text} {chars[i % len(chars)]}{RS}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write(f"\r{BR}{G}{text} ✓{' ' * 20}{RS}\n")

def log_success(msg):
    print(f"{BR}{G}[✓] {RS}{G}{msg}{RS}")

def log_error(msg):
    print(f"{BR}{R}[✗] {RS}{R}{msg}{RS}")

def log_info(msg):
    print(f"{BR}{C}[i] {RS}{W}{msg}{RS}")

def log_warning(msg):
    print(f"{BR}{Y}[!] {RS}{Y}{msg}{RS}")

def separator():
    print(f"{C}─" * 65 + f"{RS}")

# ========== CORE FUNCTIONS ==========

def send_otp(email, access_token):
    url = "https://100067.connect.garena.com/game/account_security/bind:send_otp"
    headers = {
        "User-Agent": "GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }
    data = {
        "email": email,
        "locale": "en_MA",
        "region": "IND",
        "app_id": "100067",
        "access_token": access_token
    }
    try:
        resp = requests.post(url, headers=headers, data=data)
        return resp
    except Exception as e:
        log_error(f"Connection failed: {str(e)}")
        return None

def verify_otp(otp, email, access_token):
    url = "https://100067.connect.garena.com/game/account_security/bind:verify_otp"
    headers = {
        "User-Agent": "GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    data = {
        "app_id": "100067",
        "access_token": access_token,
        "otp": otp,
        "email": email
    }
    resp = requests.post(url, data=data, headers=headers)
    return resp

def create_bind_request(verifier_token, access_token, email):
    cancel_request(access_token)
    url = "https://100067.connect.garena.com/game/account_security/bind:create_bind_request"
    headers = {
        "User-Agent": "GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    data = {
        "app_id": "100067",
        "access_token": access_token,
        "verifier_token": verifier_token,
        "secondary_password": "91B4D142823F7D20C5F08DF69122DE43F35F057A988D9619F6D3138485C9A203",
        "email": email
    }
    resp = requests.post(url, data=data, headers=headers)
    return resp

def add_recovery_email():
    print_header()
    print(f"\n{BR}{P}┌────────────── ADD RECOVERY EMAIL ──────────────┐{RS}\n")
    
    email = input(f"{C}┌─[{G}INPUT{C}]─[{W}Email{C}] ──> {RS}")
    access_token = input(f"{C}┌─[{G}INPUT{C}]─[{W}Access Token{C}] ──> {RS}")
    
    loading_animation("Sending OTP")
    resp = send_otp(email, access_token)
    
    if not resp or resp.status_code != 200:
        log_error("Failed to send OTP")
        return
    
    log_success("OTP sent successfully")
    otp = input(f"{C}┌─[{G}INPUT{C}]─[{W}Enter OTP{C}] ──> {RS}")
    
    loading_animation("Verifying OTP")
    verify_resp = verify_otp(otp, email, access_token)
    
    if verify_resp.status_code != 200:
        log_error("OTP verification failed")
        return
    
    verifier_token = verify_resp.json().get("verifier_token")
    if not verifier_token:
        log_error("No verifier token received")
        return
    
    log_success("OTP verified! Getting authorization...")
    loading_animation("Creating bind request")
    
    bind_resp = create_bind_request(verifier_token, access_token, email)
    
    if bind_resp.status_code == 200:
        log_success(f"Email {email} added successfully!")
    else:
        log_error(f"Failed: {bind_resp.text}")

def check_recovery_email():
    print_header()
    print(f"\n{BR}{P}┌────────────── CHECK RECOVERY EMAIL ──────────────┐{RS}\n")
    
    access_token = input(f"{C}┌─[{G}INPUT{C}]─[{W}Access Token{C}] ──> {RS}")
    
    loading_animation("Fetching account info")
    
    url = "https://100067.connect.garena.com/game/account_security/bind:get_bind_info"
    payload = {'app_id': "100067", 'access_token': access_token}
    headers = {
        'User-Agent': "GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip"
    }
    
    try:
        resp = requests.get(url, params=payload, headers=headers)
        if resp.status_code == 200:
            data = resp.json()
            email = data.get("email", "")
            email_to_be = data.get("email_to_be", "")
            countdown = data.get("request_exec_countdown", 0)
            
            separator()
            print(f"\n{BR}{G}📧 ACCOUNT INFORMATION:{RS}\n")
            if email == "" and email_to_be != "":
                print(f"  {Y}📨 Pending Email    :{RS} {C}{email_to_be}{RS}")
                print(f"  {Y}⏰ Confirmation in  :{RS} {C}{convert_time(countdown)}{RS}")
            elif email != "" and email_to_be == "":
                print(f"  {G}✅ Current Email    :{RS} {C}{email}{RS}")
                print(f"  {G}🔒 Status           :{RS} {C}Verified & Active{RS}")
            elif email == "" and email_to_be == "":
                print(f"  {R}⚠️  No recovery email configured{RS}")
            separator()
        else:
            log_error(f"API Error: {resp.status_code}")
    except Exception as e:
        log_error(f"Connection error: {str(e)}")

def check_platforms():
    print_header()
    print(f"\n{BR}{P}┌────────────── LINKED PLATFORMS ──────────────┐{RS}\n")
    
    access_token = input(f"{C}┌─[{G}INPUT{C}]─[{W}Access Token{C}] ──> {RS}")
    
    loading_animation("Scanning linked accounts")
    
    url = "https://100067.connect.garena.com/bind/app/platform/info/get"
    headers = {
        'User-Agent': "GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip"
    }
    
    try:
        resp = requests.get(url, params={'access_token': access_token}, headers=headers)
        if resp.status_code not in [200, 201]:
            log_error("Failed to fetch platform data")
            return
        
        platform_names = {3: "Facebook", 8: "Gmail", 10: "iCloud", 5: "VK", 11: "Twitter", 7: "Huawei"}
        data = resp.json()
        bounded = data.get("bounded_accounts", [])
        available = data.get("available_platforms", [])
        
        separator()
        print(f"\n{BR}{C}🔗 SECONDARY LINKED ACCOUNTS:{RS}\n")
        
        found = False
        for account in bounded:
            try:
                platform = account.get('platform')
                uid = account.get('uid')
                user_info = account.get('user_info', {})
                email = user_info.get('email', '')
                nickname = user_info.get('nickname', '')
                
                if platform in platform_names:
                    print(f"  {G}▶ {platform_names[platform]}{RS}")
                    if email:
                        print(f"    {C}📧 Email: {email}{RS}")
                    if nickname:
                        print(f"    {W}📝 Name : {nickname}{RS}")
                    print()
                    found = True
            except:
                continue
        
        if not found:
            print(f"  {Y}⚠️  No secondary links found{RS}\n")
        
        separator()
        print(f"\n{BR}{C}🎮 MAIN PLATFORM:{RS}\n")
        for pid, name in platform_names.items():
            if pid not in available:
                print(f"  {G}▶ {name}{RS}")
                break
        separator()
        
    except Exception as e:
        log_error(f"Connection error: {str(e)}")

def cancel_recovery_email():
    print_header()
    print(f"\n{BR}{P}┌────────────── CANCEL RECOVERY EMAIL ──────────────┐{RS}\n")
    
    access_token = input(f"{C}┌─[{G}INPUT{C}]─[{W}Access Token{C}] ──> {RS}")
    
    loading_animation("Cancelling request")
    
    url = "https://100067.connect.garena.com/game/account_security/bind:cancel_request"
    payload = {'app_id': "100067", 'access_token': access_token}
    headers = {
        'User-Agent': "GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip"
    }
    
    try:
        resp = requests.post(url, data=payload, headers=headers)
        if resp.status_code == 200:
            log_success("Recovery email request cancelled")
            print(f"  {C}Response: {resp.json()}{RS}")
        else:
            log_error("No active request found")
    except Exception as e:
        log_error(f"Error: {str(e)}")

def revoke_token():
    print_header()
    print(f"\n{BR}{P}┌────────────── REVOKE ACCESS TOKEN ──────────────┐{RS}\n")
    
    access_token = input(f"{C}┌─[{G}INPUT{C}]─[{W}Access Token{C}] ──> {RS}")
    
    loading_animation("Revoking token")
    
    url = f"https://100067.connect.garena.com/oauth/logout?access_token={access_token}"
    
    try:
        resp = requests.get(url)
        if resp.text.strip() == '{"result":0}':
            log_success("Token revoked successfully!")
        else:
            log_error(f"Revoke failed: {resp.text}")
    except Exception as e:
        log_error(f"Error: {str(e)}")

def unbind_email():
    print_header()
    print(f"\n{BR}{P}┌────────────── UNBIND EMAIL ──────────────┐{RS}\n")
    
    print(f"  {G}[1]{RS} {W}By Email OTP{RS}")
    print(f"  {G}[2]{RS} {W}By Secondary Password{RS}")
    
    choice = input(f"\n{C}┌─[{G}OPTION{C}] ──> {RS}")
    
    headers = {
        "User-Agent": "GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }
    
    email = input(f"{C}┌─[{G}INPUT{C}]─[{W}Linked Email{C}] ──> {RS}")
    access_token = input(f"{C}┌─[{G}INPUT{C}]─[{W}Access Token{C}] ──> {RS}")
    
    identity_token = None
    
    if choice == '1':
        loading_animation("Sending OTP")
        send_otp_url = "https://100067.connect.garena.com/game/account_security/bind:send_otp"
        send_otp_data = {
            "email": email, "locale": "en_MA", "region": "IND",
            "app_id": "100067", "access_token": access_token
        }
        resp = requests.post(send_otp_url, headers=headers, data=send_otp_data)
        
        if '"result":0' not in resp.text.replace(" ", ""):
            log_error("OTP send failed")
            return
        log_success("OTP sent")
        
        otp = input(f"{C}┌─[{G}INPUT{C}]─[{W}Enter OTP{C}] ──> {RS}")
        loading_animation("Verifying OTP")
        
        verify_url = "https://100067.connect.garena.com/game/account_security/bind:verify_identity"
        verify_data = {"email": email, "otp": otp, "app_id": "100067", "access_token": access_token}
        resp = requests.post(verify_url, headers=headers, data=verify_data)
        identity_token = resp.json().get("identity_token")
        
    elif choice == '2':
        secondary_password = input(f"{C}┌─[{G}INPUT{C}]─[{W}Secondary Password{C}] ──> {RS}")
        loading_animation("Verifying password")
        
        verify_url = "https://100067.connect.garena.com/game/account_security/bind:verify_identity"
        verify_data = {"email": email, "secondary_password": secondary_password, "app_id": "100067", "access_token": access_token}
        resp = requests.post(verify_url, headers=headers, data=verify_data)
        identity_token = resp.json().get("identity_token")
    else:
        log_error("Invalid option")
        return
    
    if not identity_token:
        log_error("Failed to get identity token")
        return
    
    loading_animation("Creating unbind request")
    unbind_url = "https://100067.connect.garena.com/game/account_security/bind:create_unbind_request"
    unbind_data = {"app_id": "100067", "access_token": access_token, "identity_token": identity_token}
    resp = requests.post(unbind_url, headers=headers, data=unbind_data)
    
    if '"result":0' in resp.text.replace(" ", ""):
        log_success("Email unbind request created!")
    else:
        log_error(f"Failed: {resp.text}")

def change_bind_email():
    print_header()
    print(f"\n{BR}{P}┌────────────── CHANGE BIND EMAIL ──────────────┐{RS}\n")
    
    print(f"  {G}[1]{RS} {W}Verify Old Email by OTP{RS}")
    print(f"  {G}[2]{RS} {W}Verify by Secondary Password{RS}")
    
    method = input(f"\n{C}┌─[{G}OPTION{C}] ──> {RS}")
    access_token = input(f"{C}┌─[{G}INPUT{C}]─[{W}Access Token{C}] ──> {RS}")
    old_email = input(f"{C}┌─[{G}INPUT{C}]─[{W}Old Email{C}] ──> {RS}")
    new_email = input(f"{C}┌─[{G}INPUT{C}]─[{W}New Email{C}] ──> {RS}")
    
    headers = {
        "User-Agent": "GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }
    
    identity_token = None
    
    if method == '1':
        loading_animation(f"Sending OTP to {old_email}")
        send_url = "https://100067.connect.garena.com/game/account_security/bind:send_otp"
        data = {'email': old_email, 'locale': 'en_MA', 'region': 'IND', 'app_id': '100067', 'access_token': access_token}
        r = requests.post(send_url, headers=headers, data=data)
        
        otp_old = input(f"{C}┌─[{G}INPUT{C}]─[{W}OTP for {old_email}{C}] ──> {RS}")
        loading_animation("Verifying identity")
        
        verify_url = "https://100067.connect.garena.com/game/account_security/bind:verify_identity"
        verify_data = {'email': old_email, 'app_id': '100067', 'access_token': access_token, 'otp': otp_old}
        r = requests.post(verify_url, headers=headers, data=verify_data)
        identity_token = r.json().get("identity_token")
        
    elif method == '2':
        secondary_password = input(f"{C}┌─[{G}INPUT{C}]─[{W}Secondary Password{C}] ──> {RS}")
        loading_animation("Verifying secondary password")
        
        verify_url = "https://100067.connect.garena.com/game/account_security/bind:verify_identity"
        verify_data = {'email': old_email, 'secondary_password': secondary_password, 'app_id': '100067', 'access_token': access_token}
        r = requests.post(verify_url, headers=headers, data=verify_data)
        identity_token = r.json().get("identity_token")
    else:
        log_error("Invalid option")
        return
    
    if not identity_token:
        log_error("Failed to get identity token")
        return
    
    loading_animation(f"Sending OTP to {new_email}")
    send_url = "https://100067.connect.garena.com/game/account_security/bind:send_otp"
    data_new = {'email': new_email, 'locale': 'en_MA', 'region': 'IND', 'app_id': '100067', 'access_token': access_token}
    r = requests.post(send_url, headers=headers, data=data_new)
    
    otp_new = input(f"{C}┌─[{G}INPUT{C}]─[{W}OTP for {new_email}{C}] ──> {RS}")
    loading_animation("Verifying new OTP")
    
    verify_otp_url = "https://100067.connect.garena.com/game/account_security/bind:verify_otp"
    verify_new_data = {'email': new_email, 'app_id': '100067', 'access_token': access_token, 'otp': otp_new}
    r = requests.post(verify_otp_url, headers=headers, data=verify_new_data)
    verifier_token = r.json().get("verifier_token")
    
    if not verifier_token:
        log_error("Failed to get verifier token")
        return
    
    loading_animation("Finalizing rebind request")
    rebind_url = "https://100067.connect.garena.com/game/account_security/bind:create_rebind_request"
    final_data = {'identity_token': identity_token, 'email': new_email, 'app_id': '100067', 'verifier_token': verifier_token, 'access_token': access_token}
    r = requests.post(rebind_url, headers=headers, data=final_data)
    
    if '"result":0' in r.text.replace(" ", ""):
        log_success("Email rebind created successfully!")
    else:
        log_error(f"Failed: {r.text}")

def convert_time(seconds):
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f"{days}d {hours}h {minutes}m {seconds}s"

# ========== MAIN MENU ==========

def main():
    while True:
        print_header()
        print_menu()
        
        choice = input(f"{BR}{C}┌─[{G}SELECT{C}]─> {RS}")
        
        if choice == '1':
            add_recovery_email()
        elif choice == '2':
            check_recovery_email()
        elif choice == '3':
            check_platforms()
        elif choice == '4':
            cancel_recovery_email()
        elif choice == '5':
            unbind_email()
        elif choice == '6':
            change_bind_email()
        elif choice == '7':
            revoke_token()
        elif choice == '00' or choice == '0':
            print(f"\n{BR}{G}╔════════════════════════════════════════╗")
            print(f"║  {C}Exiting Garena Account Tool...{G}        ║")
            print(f"║  {Y}Credits: @sulav_codex_ff{G}              ║")
            print(f"╚════════════════════════════════════════╝{RS}\n")
            sys.exit(0)
        else:
            log_warning("Invalid option selected")
        
        input(f"\n{BR}{C}Press Enter to continue...{RS}")
        clear()

if __name__ == "__main__":
    main()
    
    
#MADE BY SULAV AND AJAY
