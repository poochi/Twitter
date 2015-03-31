
<snippet>
  <content><![CDATA[
# TwitterInformer

This is a simple project to explore twitter's api using tweepy.
The aim of this project is to provide important news tweets from reliable handles to your Ubuntu PC in a convinient manner.

![alt tag](https://raw.github.com/poochi/TwitterNews/master/pics/example.png)

Currently, the app uses information from app.cfg (like authentication key, full-permision folder and reliable news source handles) to fetch and display push notification in ubuntu.

## Installation
Set the config parameters correctly
Just run this python file from command line. Ensure to set the DISPLAY environment variable to  0.0 

## Usage

TODO: Write usage instructions

simply cron it even hr :) 
* */1 * * * DISPLAY=:0.0 /home/poochi/App_TwitterNews/TwitterNews.py 1>/home/poochi/App_TwitterNews/log1 2>/home/poochi/App_TwitterNews/log2

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Plans

TODO: Clean up tweets (ReTweet, removing http)
Resize to icon without aliasing
Database based maintanence of tweets
Display time stamp
Display recent tweets only 
Periodic cleaning of content
Make it work everywhere :)


## Credits

TODO: Write credits

## License

TODO: Write license
]]></content>
  <tabTrigger>readme</tabTrigger>
</snippet>

