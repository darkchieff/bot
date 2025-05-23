# Discord Radio Bot on Replit

## Setup Instructions

1. Go to the "Secrets" tab in Replit and add:
   - Key: YOUR_BOT_TOKEN
   - Value: (your actual Discord bot token)

2. Open the Shell and run these commands to install ffmpeg:
   wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.tar.xz
   tar -xf ffmpeg-release-i686-static.tar.xz
   mv ffmpeg-*/ffmpeg .
   chmod +x ffmpeg

3. Click "Run" and ensure you see:
   - Running on http://0.0.0.0:8080/
   - Logged in as [your bot]

4. Use https://uptimerobot.com to ping your Repl's URL every 5 minutes to keep it alive.

Commands:
- !join
- !play
- !stop
