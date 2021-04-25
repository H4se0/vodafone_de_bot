Simply bot to connect vodafone 30 min hotspot in Germany.
1)For linux just copy folder to desired location and change pid location if you don't won't or need to run it as sudo, and chmod +x vodafone.py 
2)run /your_path/vodafone/vodafone.py start / stop
3)Enjoy / viele Spaß

Method: Since wifi it's connected to vodafone hotspot, other methods to check for connection has failed (sock, url.open).
Explanation: Times for loop are adjusted, to let system go to suspend or hibernation. You can change first value under 15 sec, to check for connection more often. 
TODO: Windows version if you wish (I don't use it anymore); using event class method instead of time.sleep, so script should avoid loop, and would use thread instead. Feel free to contrinute if you want to make it better.
If you enjoy leave a comment. 
