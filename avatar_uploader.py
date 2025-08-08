import asyncio
import time
from telethon import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, GetUserPhotosRequest
import os

api_id = int(input("Enter api_id: "))
api_hash = input("Enter api_hash: ")
phone = input("Enter your phone number: ")

avatar_filename = "avatar.jpg"

while True:
    try:
        avatar_count = int(input("How many avatars do you want to set? "))
        if avatar_count <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

async def main():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        await client.start(phone=phone)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        avatar_path = os.path.join(script_dir, avatar_filename)
        if not os.path.isfile(avatar_path):
            print(f"Avatar file '{avatar_filename}' not found next to the script.")
            return
        print(f"{avatar_count} identical avatars will be set: {avatar_filename}")
        try:
            for i in range(avatar_count):
                file_obj = await client.upload_file(avatar_path)
                await client(UploadProfilePhotoRequest(file=file_obj))
                print(f"Avatar {i+1}/{avatar_count} set successfully!")
            photos = await client(GetUserPhotosRequest(
                user_id='me',
                offset=0,
                max_id=0,
                limit=100
            ))
            print(f"Total avatars set: {len(photos.photos)}")
            if len(photos.photos) >= avatar_count:
                print(f"All {avatar_count} avatars have been set successfully!")
            else:
                print(f"Warning: only {len(photos.photos)} avatars were set.")
        except Exception as e:
            print(f"Error while setting avatar: {e}")

if __name__ == "__main__":
    asyncio.run(main())
