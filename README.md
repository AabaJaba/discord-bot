# Discord Bot - Stalin

## Description
Stalin is a Discord bot with various utility, moderation, and entertainment commands. It includes features such as message management, arithmetic operations, banning/kicking users, sending direct messages, and fetching memes from Reddit.

## Features
- **Moderation Commands:** Kick, ban, unban, and message clearing.
- **Math Operations:** Addition, subtraction, multiplication, division, and remainder.
- **Fun Commands:** Meme fetching from Reddit, coin flip, and a game chooser.
- **Message Events:** Automatic response to deleted messages and 'f' in chat.
- **Direct Messaging:** Send images and predefined messages to users.

## Installation & Setup
### Prerequisites
- Python 3.8+
- `discord.py`
- `asyncpraw`
- `aiohttp`
- `requests`

### Installation
1. Clone this repository or download `disbot.py`.
2. Install dependencies:
   ```sh
   pip install discord.py asyncpraw aiohttp requests
   ```
3. Set up your Discord bot token in `client.run('#enter token')`.
4. Replace `client_id` and `client_secret` with your Reddit API credentials.
5. Run the bot:
   ```sh
   python disbot.py
   ```

## Usage
### Prefixes
- The bot responds to commands prefixed with `gu `, `Gu `, `GU `, or `gU `.

### Available Commands
| Command        | Description |
|---------------|-------------|
| `gu add a b`  | Adds two numbers. |
| `gu sub a b`  | Subtracts two numbers. |
| `gu mul a b`  | Multiplies two numbers. |
| `gu div a b`  | Divides two numbers. |
| `gu rem a b`  | Finds the remainder. |
| `gu clear n`  | Clears `n` messages (Admin only). |
| `gu kick @user` | Kicks a user (Admin only). |
| `gu ban @user` | Bans a user (Admin only). |
| `gu unban username#1234` | Unbans a user. |
| `gu khale @user` | Sends a poop emoji via DM. |
| `gu dm @user` | Sends an image via DM. |
| `gu choose opt1 opt2` | Randomly selects one of the options. |
| `gu coinflip` | Flips a coin. |
| `gu memes` | Fetches a meme from Reddit. |

## Notes
- The bot logs deleted messages to a specific channel.
- `on_message` event ensures that 'f' responses work while processing commands.
- Ensure the bot has the necessary permissions for moderation commands.

## Disclaimer
Use at your own risk. The developer is not responsible for any issues caused by the bot.

## Author
Developed Navnoor Singh

