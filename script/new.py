from telethon import TelegramClient
import os
from dotenv import load_dotenv
import logging

# Ensure the scrapped_data directory exists
media_dir = '../assets/scrap/photos'
os.makedirs(media_dir, exist_ok=True)

# Set up logging configuration
logging.basicConfig(
    filename='../assets/scrap/scrapped_data/scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

# Load environment variables
load_dotenv('.env')
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone = os.getenv('PHONE_NO')

# Function to scrape photos from specific channels
async def scrape_photos(client, channel_username, media_dir):
    try:
        entity = await client.get_entity(channel_username)
        channel_title = entity.title 
        logging.info(f"Scraping photos from channel: {channel_title}")
        
        async for message in client.iter_messages(entity):
            if message.media and hasattr(message.media, 'photo'):
                # Create a unique filename for the photo
                photo_filename = f"{channel_username}_{message.id}.jpg"
                media_path = os.path.join(media_dir, photo_filename)

                # Download the media to the specified directory if it's a photo
                await client.download_media(message.media, media_path)
                logging.info(f"Downloaded media: {photo_filename}")

        logging.info(f"Photo scraping complete for channel: {channel_title}")

    except Exception as e:
        logging.error(f"Error scraping photos from channel {channel_username}: {str(e)}")

# Initialize the client
client = TelegramClient('scraping_session', api_id, api_hash)

async def main():
    try:
        await client.start()
        logging.info("Telegram client started")

        # Channels to scrape photos from
        photo_channels = [
            '@CheMed123',
            '@lobelia4cosmetics'
        ]

        # Scrape photos from the specified channels
        for channel in photo_channels:
            await scrape_photos(client, channel, media_dir)
            print(f"Scraped photos from {channel}")

    except Exception as e:
        logging.error(f"Error in the main function: {str(e)}")

with client:
    client.loop.run_until_complete(main())