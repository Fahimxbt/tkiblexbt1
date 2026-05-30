from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("=" * 60)
print("Telegram String Session Generator")
print("=" * 60)
print()

api_id = input("Enter your API ID: ").strip()
api_hash = input("Enter your API Hash: ").strip()

print()
print("Generating session...")
print("You will receive a code on Telegram. Enter it below.")
print()

try:
    with TelegramClient(StringSession(), int(api_id), api_hash) as client:
        session_string = client.session.save()
        print()
        print("=" * 60)
        print("YOUR STRING SESSION:")
        print("=" * 60)
        print()
        print(session_string)
        print()
        print("=" * 60)
        print("Copy the above string and paste it in Railway as STRING_SESSION")
        print("=" * 60)
except Exception as e:
    print(f"Error: {e}")

input("\nPress Enter to exit...")
