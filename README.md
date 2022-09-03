# Facebook-Find-and-Comment
## ABOUT
### Why did I create this project?
In order to advertsing purpose on Facebook posts, I decided to start this project.
### Features
- Auto login your Facebook account and save cookies for the next login.
- Comment string including texts and special icons.
- Will not comment already commented posts.
- Fast and easy to setup.
### How it works?
The program will read the page's html and find the content of each post if it contains matched texts from [textFiles/regex_find.txt](https://github.com/datdadev/Facebook-Find-and-Comment/blob/main/textFiles/regex_find.txt).
If it does, the program will comment [textFiles/comment.txt](https://github.com/datdadev/Facebook-Find-and-Comment/blob/main/textFiles/comment.txt) and post it automatically.
Then the process will be looped *REFRESH_TIME* times - set in [.env](https://github.com/datdadev/Facebook-Find-and-Comment/blob/main/sources.env).
## INSTALLATION
Install project's dependencies in [requirements.txt](https://github.com/datdadev/Auto-Find-and-Comment/blob/main/requirements.txt):

```bash
pip install -r requirements.txt
```
Create environment file for project by rename *resource.env* to *.env*:

```bash
cp resources.env .env
```
Setup environment variables:
- FACEBOOK_LOGIN = your Facebook login
- FACEBOOK_PASSWORD = your Facebook password
- REFRESH_TIME = time to refresh Facebook page for new posts

Edit text files:

- [textFiles/regex_find.txt](https://github.com/datdadev/Facebook-Find-and-Comment/blob/main/textFiles/regex_find.txt): string in regex format that you want to find
- [textFiles/comment.txt](https://github.com/datdadev/Facebook-Find-and-Comment/blob/main/textFiles/comment.txt): texts (including special icon) that you want to comment
It's all set! Run [*main.py*](https://github.com/datdadev/Facebook-Find-and-Comment/blob/main/main.py) to start the program. Enjoy!
## UPDATE
The project will be update occasionally when I'm free.
