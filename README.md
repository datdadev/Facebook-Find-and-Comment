# Facebook-Find-and-Comment
## ABOUT
### Why did I create this project?
In oder to advertsing purpose on Facebook posts, I decided to start this project.
### How it works?
The automation will read and find the content of each post if it contains matched texts from [textFiles/regex_find.txt](https://github.com/datdadev/Facebook-Find-and-Comment/blob/main/textFiles/regex_find.txt).
If it does, the bot will comment [textFiles/comment.txt](https://github.com/datdadev/Facebook-Find-and-Comment/blob/main/textFiles/comment.txt) and post it automatically.
Then the program looped *REFRESH_TIME* times - setted in [.env](https://github.com/datdadev/Facebook-Find-and-Comment/blob/main/sources.env).
## INSTALLATION
- Install project's dependencies in [requirements.txt](https://github.com/datdadev/Auto-Find-and-Comment/blob/main/requirements.txt) by running command below in your terminal:

```bash
pip install -r requirements.txt
```
- Setting environment file for project by rename *source.env* to *.env* by using command below:

```bash
cp sources.env .env
```
- Setup environment variables:
  - FACEBOOK_LOGIN = your Facebook login
  - FACEBOOK_PASSWORD = your Facebook password
  - REFRESH_TIME = time to refresh Facebook page for new posts
## UPDATE
The project will be update occasionally when I'm free.
