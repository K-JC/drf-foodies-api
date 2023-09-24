## Foodies
For my fifth and final project with Code Institute I chose to create a baking community based content sharing platform to share baking creations to a global audience. Foodies is all about yummy food, sweet treats and all things good. The platform enables users to create posts, edit or delete posts,read posts,comment and like on posts. Users can also follow other users and keep up to date on their latest creations. Users can use the search bar at the top to browse through the platform's posts. Search results can be filtered on usernames, popularity, date created, title, content keywords and category. This is my advanced front-end project, I hope you enjoy it! - [Link To Foodies](https://drf-foodies-api-1b38deb7eb8c.herokuapp.com/)

Combined Repository - [Repository](https://github.com/K-JC/drf-foodies-api)

![Responsive](frontend/src/assets/responsive.png)

## Table of Contents  
* [Development Planes](#development-planes)
* [WireFrame](#wireframe)
* [User Stories](#user-stories)
* [Features](#features)  
* [Testing](#testing)
* [Bugs](#bugs)
* [Validator Testing](#validator-testing)
* [Deployment](#deployment)
* [Credits](#credits)


# Development Planes
## Strategy
I aim to achieve a content sharing platform for all things baking, where users can post images of their creations, they can like and comment on other users posts. A user can also follow another user so they can keep up to date with that user. The post user will have the ability to edit or delete their posts.
When at the first stage of planning my project I put myself in the shoes of the user, I needed to understand what the users wants or needs for this platform. I noted down the following. Why would the user come here in the first place? To post about their baking creations. To like and comment on other users' creations. To create awareness of their talent to others. The first thing the user should see is that this is a content sharing platform. It should be very clear how to navigate it for great user experience. What would make them come back after their first visit? To edit/delete their original post or to make a new post. To check if a user they followed has posted anything new or if there are any comments that they need to reply to.
If the experience of navigating is straightforward, easy to use and the platform looks good this should create a good user experience.
Goal for a user to post their creations to a global network of people.

* Core Values
A place for users to upload their own post(photos of their baking). A place for users to like or comment on another user's post. A user can edit or delete their own posts/comments/images. A user can see all the posts that they have liked. A user can follow another user. A user will have their own profile page/about/profile image(can upload their own image). A user will have login and log out functionality. A new user will be able to sign up for their own account. Will need a react-bootstrap library to aid in the styling and responsiveness of the website. The application will be hosted on heroku. Will connect to a custom API to store our users/posts/likes/comments. User stories to guide me to build functionality . Simple automated tests to check the project works correctly. CRUD functionality for users.

## Scope
The features I want to implement are the ability for a user to create their own account, they can log in and log out with their own username and password which will make their account secure. They will be able to personalize their account with an about me section, so that other users can find out more about them. 
They will also be able to upload a profile picture. They can change this at any time. The about me section can also be edited/updated.
They will be able to create a post about their creations, this will include a title, an image and a description relating to the image uploaded. 
They will be able to edit/delete their own posts. Follow/ unfollow other users. Like and comment on other users posts and can comment on their own post in response to other users comments. 

## Structure
Logically grouping the main home page so that additional pages are easy to navigate through a collapsible navigation icon. When a user who isn't signed in/signed up accesses the platform they will only be able to see the “Home,Sign In or Sign Up” navigation links. Only once they are a logged user will they have access to the full navigation links such as “Home, Add Post, Feed, Liked, Sign Out and Profile”. The user will be able to navigate easily through the platform which will add to a positive user experience. 

## Skeleton
Navigation links and posted content will be presented in a tidy way. Collapsible navigation links on smaller screen sizes to avoid too much clutter.
Only a logged in user will be able to access the platform fully. There will only be “Home, Sign In and Sign Up navigation links visible to non-signed in users, so it will be clear to the user that to access the site they will need an account and will have to sign up . Once a user is logged in they can access the platform and will now be able to create a post etc. Once posted there will be a drop down to the side of the post with an edit or delete option.
The user will have the ability to log out of their account. Information on the homepage will be relevant to this sharing content platform, from the description to the imagery used. The Sign In/Sign Up page will have imagery relevant to baking. The favicon/logo used will be related to baking as well, I would like a cake or a mixing bowl. 

## Surface
I want this to look visually pleasing and clean. Google fonts of Noto Serif and a backup of sans-serif. A combinations of different colors (purple) #B8A1BC, #F2C6D0 and #E2D9E3. A user would visit the platform and see the logo to the left hand side to the right would be all the navigation links. On smaller screen sizes there would be a navigation drop down menu. Only the Home, Sign Up and Sign In navigations will be visible to non logged users. Once a user is either signed up/signed in they will see the other navigation links such as “Add Post, Liked, Feed, Sign Out and Profile”.

![ER-Diagram](frontend/src/assets/er-diagram.png)

# Wireframe
Once I had an idea of what the user would need, I could then begin to figure out what the platform would look like.
I created some wireframes using Figma, this is how I envisioned the homepage of the platform to look and the rest of the pages to keep the same visuals.

![Homepage](frontend/src/assets/figma-homepage.png)
![Homepage-mobile](frontend/src/assets/figma-homepage-mobile.png)
![Profile](frontend/src/assets/figma-profile.png)
![Profile-mobile](frontend/src/assets/figma-profile-mobile.png)
![Sign-in](frontend/src/assets/figma-sign-in.png)
![Sign-up](frontend/src/assets/figma-sign-up.png)

From the development plane and wireframe I got a good idea of what user stories I will create.
I created a GitHub project called Foodies Stories and connected this to my project repository. The user stories are as follows.

# User Stories
![Stories-Start](frontend/src/assets/projectboard.png)
![In-Development-Stories](frontend/src/assets/stories.png)

 Authentication
* Authentication - Sign up/Sign in - As a site user I can sign up and sign in to the site so that I can access the functionality of the website.
  By using all auth a user can easily sign up or sign into their account.
* Authentication - Log Out -As a site user I can log out of my account so that I have more security over it.
  By using all auth a user can log out of their account which gives them security over their account. 
* Authentication - Logout Status - As a site user I can maintain my logged-in status until I choose to log out so that my user experience is not compromised.
  A logged in user can see their status in the nav bar by their logged in profile achieved by using Django's all auth. 
* Posts -As a site user I cannot edit or delete any posts another user has created so that there is complete protection/control over a user's content.
   By making custom permission so that a user is stopped from making changes to others posts/comments etc.
* Comments- As a site user I cannot edit or delete any comments and likes made that another user has created so that there is complete protection/control over a user’s content.
*  By making custom permission so that a user is stopped from making changes to others posts/comments etc.
* Likes -As a site user I can only like or unlike other users' posts/comments, not my own so that I can show my support for other posts/comments.
  Using the Likes and LikeComments model a user can like a post or like a user's comment, by having custom permissions a user can not like their own post or their own comment.
* Following- As a site user I can follow other users so that I can keep up to date with the user’s posts.
  Using the follower model with custom permissions this allows a user to follow another user but stops them from following themself.
* Unfollow - As a site user I can unfollow other users so that I have control over if I want to continue to follow those users anymore.
  
 Navigation
* Navigation- As a site user I can see a navigation bar on every page so that I can easily navigate to other pages I wish to visit.
* Navigation Scrolling- As a user I can keep scrolling through the posts on the site that are loaded for me automatically so that my user experience is not compromised.
* Navigation Bar- As a site user I can see the navigation bar is customized to my logged-in or out status so that I can either view all the functionalities available or have limited options. 
* Navigation 404 -As a site user I can see the 404 page so that I am aware I have reached an invalid web page.
* Routing- As a site user I can navigate through pages quickly so that I can view content seamlessly without page refresh.
* Navigation - As a site user I can be notified when my actions are successful so that I know if my actions were successful or not.
  
Post
* View Homepage posts- As a site user I can view all the posts on the Homepage so that I can choose to view/like and comment on any post I'm interested in. 
* View posts details - As a site user I can view details on a post made so that I can see comments made by all the different users of the platform.
* Create posts- As a site user I can create a post so I can share my creations with my community.
  By using the Post model a user can add an image, content, category and a title to their post. A user can see how long ago a post was made. 
* Edit/delete posts- As a site user I can edit/delete my posts so that I can make changes to an existing post title/description or remove my post completely.
 By using generics (RetrieveUpdateDestroyAPIView) in the Post views a user can edit/delete their post.
* View posts Feed- As a site user I can view all user posts made on the Feed page so that I can keep up to date with other users.

* Post Order View- As a site user I can view the most recent posts, ordered by the most recent first so that I am kept up to date with the latest content.
* Search Posts- As a site user I can search for posts/users in a search box so that I can find specific posts/users that I am searching for.
  By using custom filter set fields and search fields in the post view a user can search for relevant posts based on title, name and content.
* Content Filters- As a site user I can view content filtered by users I follow so that I can keep up to date with their creations they post about.
* By using custom filter set fields in the views of post/comment/profile a user can filter information based on what they search.
  
Comment 
* View Comment- As a site user I can view comments on a post so that I can read what others are saying. 
* Post Comment- As a site user I can post a comment on a post so that I can share what I am thinking.
* Edit/Delete Comment- As a site user I can edit/delete my comments so that I have control over what I want to say and either fix or remove my comment.
  By using generics (RetrieveUpdateDestroyAPIView) in the Comment views a user can edit/delete their comment.
* Comment Creation Date- As a site user I can see how long ago a comment was made so that I know how old a comment is.
 By using generics (ListCreateAPIView) in Comment views a user can see a list of comments on a post and by the django import naturaltime A user can see how long ago a comment was made. 

* Comment Likes - As a site user I can like another user's comment so that I can show I support their comment.
  The Comment Likes model enables a user to like another user's comment.

Likes  
* Likes- As a site user I can see the number of likes on a post so that I can see which are becoming popular.
  The likes model enables a users to like another user posts.

* Like/Unlike- As a site user I can like/unlike comments so that I can show my support/remove support for a particular post.
  By using generics (RetrieveDestroyAPIView) in the Like views. Users can remove their likes on a post.
  
Profile
* Following Users- As a site user I can follow/unfollow other users so that I have control over whether I want to see their content on my feed or not.
  By using the Follow model users can choose to follow or unfollow other users. 
* Popular Profiles- As a site user I can see the most popular profiles so that I can gauge who’s creations are getting noticed more.
* Update Profile About- As a site user I can update my about me so that I can make changes when necessary and other users will keep updated on me.
* Update Profile Picture- As a site user I can update my profile picture so that I can keep my profile up to date.
* View Profiles- As a user I can view another user's profile picture so I can easily identify other users of the platform.
  By using the profile model, a user can view users profile pictures. 
* Update Profile Info- As a site user I can update my username and password so that I can change my display name and keep my profile secure.
* View Other Profiles- As a site user I can view other users' profiles, about me, number of posts, follows and users followed so that I can learn more about them.
  By using the profile views any posts by a user, followers and followed count will show on their profile page.

# Features
For users with no account.
* Home Page (leads to the Feed Page but this can't be interact with if not signed up/logged in)
* About Us/Landing Page
* Sign In Page
* Sign Up Page
![No-Account](frontend/src/assets/logged-out.png)
For Users with an account.
* Add Post Page
* Feed Page
* Liked Page
* Sign Out Page
* Profile Page
![With-Account](frontend/src/assets/logged-in.png)
* Logo and Favicon
![Logo-Create](frontend/src/assets/canva-create.png)
![Foodies-Logo](frontend/src/assets/foodies.png)
  
  
# Bugs
* During the start of the project when using npm start an error occurred in the terminal which was “ code: 'ERR_OSSL_EVP_UNSUPPORTED” so I went to search slack for an answer and it looked like that everytime I wanted to start my app I would need to use “nvm install 16 && nvm use 16”  this would now allow me to start my app, but it was something I need to do every time.
* Foodies-drf-api profile page error 500, changes were migrated to the database, wasn't connected correctly. 
* The edit profile wasn’t loading correctly, my route needed a "/" to the end of the file path. 
* The drop down menu for editing posts was not working as expected, after going through my code I had used a capital in PostsPage it should have been lowercase to begin with postsPage. Once corrected the drop down menu worked as expected. 
* Comment count was not showing, after going through my code it turned out to be a spelling error in my post.js once corrected the number of comments was now showing as expected. 
* While trying to implement emoji picker so that a user could add an emoji to their comment I was unable to make this work, after looking through slack and stackoverflow I realised that emojis are universal and will already be in the keyboard for smaller screens like phones and tablets. For desktops you need to press the windows key + and . to open an emoji window and then these can be added into a comment. 
* When originally trying to deploy the back end to heroku the only page I had trouble with was the “profiles” page and an error of 500 was showing. I went back to my code and I did fix an error with my ProfilesList views. I had put the wrong generics in there and should have been generics.ListAPIView. I deployed once more and I then checked the profiles page and the 500 error was no longer showing and the information on the profile was showing.
* While originally trying to deploy my project my api wasn't talking to my front end and I had a lot of CORS errors come up in my chrome dev tools console(Cors No Header Origin). After much headache over trying to fix this I had seen that we could combine our repositories into one work space which would mean that cors would no longer be an issue as the api was coming from the same workspace/shared base URL. I followed the steps set by code institute to enable my project to contain both front end and back end portions of the project and once all was set up and I deployed my project to heroku it was finally working! 

# Future Features
I would like to implement more messages to the users when they interact with the site such as You have logged in/logged out successfully. I would also like the user to have the ability to add videos as well as images to their posts. 

# Validator Testing
* HTML - Using W3C HTML Validator, as there was some Django in my HTML the validator didn't like those very much. So my only issues were from this, percentages in href  attribute and trailing slash.
* CSS - Using W3C CSS Validator, all passed with no issues.
* PEP8 - Using Python Validator, all passed with no issues.
* I used Eslint Play Validator online, only came up with import and export that may appear only with sourceType: module.
* I used JSHint Online Validator also.

# Testing
## Manual Testing 
* Manual Testing of the platform was consistent through the development of the project in GitPod. All navigation links take me to the correct pages.
* Sign in and sign up forms work correctly and that information is shown on the database.
* The navigation link for adding a post takes the user to the add a post page where the user can then upload an image, create a title, choose a category and write a bit about their creation then they can create a post, this will then take the user to the post list page where all posts submitted will be. Only the posts owner can edit or delete their post which they can do by clicking a drop down menu to the right hand side of their post, there is an option to edit a post which works as expected and an option to delete that post, which again works as expected and the post is no longer available. 
* A user can click on the feed navigation link which will take them to the list of all posts made.
* The liked navigation link will show the user all the posts they have liked.
* The profile navigation link will take the logged user to their own profile in which they can edit their username, password, about me and profile image. These all worked as expected.
* The sign out navigation link signs the user out of their account and leads them back to a landing page. The foodies logo takes the user back to the feed page. All navigation works as expected though manual testing.
* Commenting on a post and the comment count work as expected and the like a comment function again works as expected and the number will increase the more likes a comment has. If a comment or a comment like is removed the number also goes down to highlight this.
* Collapsible navigation works on smaller screen sizes and all buttons work  as expected. 

# Testing A Profile
* Logging in as Winter's profile.
![Test-Login](frontend/src/assets/winter-signin.png)
* Show Winter's profile page with how many followers, following and posts made so far. On the right hand side can see who she is following in the popular profiles section.
![Test-Profile](frontend/src/assets/winter-profile-page.png)
* Show post page for Winter to create a post. Has title, category, description and also an upload section for images to upload.
![Test-Add-Post](frontend/src/assets/winter-post.png)
* Once the post has been submitted Winter is sent to the feed page where her newly created post is.
![Test-Posts-List](frontend/src/assets/winter-feed.png)
* Clicking on Winter's post, she has a comment and a like from profile user teresa.
![Test-Commenting-and-Liking](frontend/src/assets/teresa-comment-like.png)
* Now Winter can see comments and can react to these comments by liking them.
![Test-Like-Comment](frontend/src/assets/winter-like-comment.png)

# Testing Admin Panel
![Admin](frontend/src/assets/admin-panel.png)
* Login to admin panel to make sure all new accounts were showing on the admin panel.

# Testing Back End
![Back-End](frontend/src/assets/sign-up-data-form.png)
* Check to see if an account was showing on the back end which it was.
  
# Testing in React 
![P8P-Test](frontend/src/assets/pass-test.png)
* Tests pass for react in terminal and in P8P
![P8P-Test](frontend/src/assets/p8p-test.png)


# Technologies Used
## Frameworks, Libraries, Programs & Applications Used
* Django Rest
* React.js
* Bootstrap.js
* Python
* PostgreSQL
* Cloudinary - I used Cloudinary to store images from this project.
* Font Awesome - I used Icons from Font Awesome for my navigation links.
* Figma - I used Figma in the planning stage to create my sitemap, from this I created my content sharing platform like I had designed.
* Lucid - I used Lucid to create the ER Diagram for my platform.
* GitHub - My project was stored on Github.
* GitPod - Gitpod was used for writing my code and when I pushed commits from Gitpod they were uploaded to Github where my project was stored.
* Heroku - Where the project was deployed to.
* Google Development Tool - Where I checked the responsiveness of the website and edited any code without the risk of making it a permanent change.
* Elephantsql - I used Elephantsql for my database.
* Canva - For creating my logo/favicon.

## Languages
* HTML
* CSS
* Python
* Javascript

# Accessibility
Using Google Development tools, I tested the accessibility of the site via the lighthouse option. My platform scored 
![Lighthouse](frontend/src/assets/lighthouse.png)

# Setting up 
* For the back end I started by using the template provided by code institute to create my repository. I called this drf_foodies_api. I then began to install the libraries I would need, first “pip3 install ‘django<4’". Once installed I then created my project name by inputting “django-admin startproject drf-foodies-api. '' to the terminal. I then proceed to Install Cloudinary Storage by inputting “pip install django-cloudinary-storage==0.3.0”, this will be storage for any images used. And finally I Installed the image processing library known as  Pillow by inputting “pip install Pillow==8.2.0” to the terminal. Now that I had installed some libraries I needed to put these into my settings.py file under the INSTALLED APPS portion. I created an env file and made sure that this was also present in my gitignore file. This would keep all the sensitive stuff hidden so it wouldn't be visible on the repository. 
Next I added my profiles app, I needed to add this to settings.py under installed apps. Python3 manage.py startapp profiles. Every new app I need to install I use this same code but change the app name at the end. 
Time to add the super user so only this user can access the admin panel. Enter “python3 manage.py createsuperuser” to the terminal and create a superuser.
Install Django rest framework, enter “pip3 install djangorestframework”to the terminal and then add this library to installed apps “rest_framework”.
Making sure to migrate any changes to the models and to add libraries to the requirements.txt file.
Later I began on the JSON web tokens I entered “pip install dj-rest-auth==2.1.9 to the terminal.
Then input this to the terminal “pip install 'dj-rest-auth[with_social]” and “pip install djangorestframework-simplejwt”.

* For the front end I set up a new repository on Github called “foodies”. I then opened the workspace on Gitpod using the green Gitpod button. In the terminal I entered the following command: “npx create-react-app . --template git+https://github.com/Code-Institute-Org/cra-template-moments.git --use-npm”.Enter “y” to confirm installing the create-react-app package, then start the app with: “npm start”.
This set up my workspace with the correct template for working in github. Loading all the dependencies/versions needed for my project. As soon as I was ready to start my app I was met with my first error, “ code: 'ERR_OSSL_EVP_UNSUPPORTED”, I went straight to the slack community to see if I could find an answer and it looked like that everytime I wanted to start my app I would need to use “nvm install 16 && nvm use 16”  this would now allow me to start my app, but it was something I need to do every time.
Once I created some test text to see if everything was working fine I then saved and pushed my changes to github. Next on the list was to install bootstrap with react. Install with “npm install react-bootstrap@1.6.3 bootstrap@4.6.0” add link to html header. Import bootstrap buttons from react bootstrap in the apps.js file and then replace the test text with a button. This worked in the preview. 

# Deployment
I started out with early deployment to make sure things were working as expected.
* For the Back End portion of my project I made sure I had migrated all changes and saved my git pod workspace. 
I then logged in to my elephantsql account and created a new instance. Give the plan a name “drf-foodies-api", select a free plan, select the region I am in "europe-west2 (london)". Then review and create the instance. The instance is now on the dashboard. I copied the url for my instance.
Next I logged into heroku, I went to my dashboard, created a new app by clicking on new, new app. Create my unique name for my app, then select my region as europe and click create app. 
I then went to the settings tab and opened the config vars tab, created a config var key of DATABASE_URL and for the value my database url from elephantsql that I had just created. Add CLOUDINARY_URL key with a value of my own cloudinary url. Next DISABLE COLLECTSTATIC with a value of 1. And lastly a key of SECRET_KEY with a value of my chosen secret key that I have made. 
After this I then went to the deploy tab, I selected the deployment method to github, scroll down till I reached the deploy branch section and click the deploy branch button. I watched the main branch being deployed, this will show any errors with the deployment and will help to identify any issue. I had an issue where my branch was not deploying correctly and this is because I had an error with my allowed_hosts section of my code once I had changed the code and continued to debug it finally was working and the deployment was successful. Once the branch is finished with its building, you can then click on the open app and it should load successfully.

* For the front end portion of my project I made sure I had saved all changes and pushed them to GitHub.
I then went to Heroku to create my new app. I clicked on a new app, gave it a unique name of “foodies-project”, and selected my region as europe. Then I clicked create app. I then wanted to connect this to my github repository, so I went to the deployment section and searched for my repository. I selected this and then clicked on connect. Now my repository is wired up. I clicked on deploy branch, once it was finished building my app I then clicked on open app to view if it was working, which it was. Early deployment is ideal because I wanted to make sure everything was connected correctly from the get go.

* Combining the projects (after a big headache with CORS) Code institute had created a way in which the projects could be combined which would solve the pesky CORS issue.
I went to my GitHub repository for my React project (foodies) . I then clicked on the "Code" button, selected the HTTPS tab, and copied the URL provided. I then opened my workspace for my DRF project (drf-foodies-api). I went to the terminal window and typed "git clone <my_foodies_url> frontend" This created a new folder in my drf workspace called front end which contained all the files from my react foodies project. In the terminal window I change directory to my frontend folder with the following command
"cd frontend". I then entered this command to remove the .git folder, .gitignore file and README.md from the front end folder. "rm -rf .git .gitignore README.md".
I then installed the npm packages required for developing with React using the following command "npm install". 
I moved back to the root directory of my project with the following command "cd ..". I then opened the package.json file in the frontend directory, and at the bottom of the file I added a new key to the JSON object. This will allow the preview to run within my development environment proxy localhost 8000, I then opened the axiosDefaults.js file and commented out the baseURL setting.
To ensure that the API’s routes do not clash with the React application’s routes when the project is deployed I needed to set a new path for the API routes in the server and the baseURL. In my env.py file, I made the following changes:
Commented out the DEV environment variable.
Add a new key DEBUG with a value of ‘1’
Add a new key ALLOWED_HOST with the value of my development environment URL
Add a new key CLIENT_ORIGIN with the value of my development environment URL
A key for DATABASE_URL set to the value of my ElephantSQL database URL
A key for CLOUDINARY_URL set to the value of my Cloudinary URL
In settings.py:
I set the DEBUG to the value of the DEBUG environment variable and update ALLOWED_HOSTS to include the ALLOWED_HOST environment variable added to my env.py file.
Now that I have the two parts of my application within the same workspace, the CORS issues with the original separate projects are no longer a problem. This is because both parts of the project will come from the same base URL.
So I could remove most of the code in the Django project relating to CORS.
In settings.py I removed the line containing the import re
I removed all the CORS code, leaving only the CORS_ALLOWED_ORIGINS list
Now The Django API will run on Port 8000, and the React application will run on Port 8080.
I then went back to the terminal making sure I was in the root directory and I then installed whitenoise with the following command, "pip3 install whitenoise==6.4.0".
Once installed I added this dependency to my requirements.txt file. I created a new folder called staticfiles in the root directory with the following command "mkdir staticfiles".
In settings.py:
In the INSTALLED_APPS list, I made sure that the ‘cloudinary_storage’ app name was below ‘django.contrib.staticfiles’. 
This ensures that Cloudinary will not attempt to intervene with staticfiles, and allows white noise to become the primary package responsible for static files
In the MIDDLEWARE list, add WhiteNoise below the SecurityMiddleware and above the SessionMiddleware with "whitenoise.middleware.WhiteNoiseMiddleware".
In the TEMPLATES list in the DIRS key, I added "os.path.join(BASE_DIR, 'staticfiles', 'build')"  this tells Django and WhiteNoise where to look for Reacts index.html file in deployment.
In the static files section, I added the STATIC_ROOT and WHITENOISE_ROOT variables and values to tell Django and WhiteNoise where to look for the admin static files and Reacts static files during deployment with "STATIC_ROOT = BASE_DIR / 'staticfiles'" and "WHITENOISE_ROOT = BASE_DIR / 'staticfiles' / 'build'".
In the urls.py file of my drf-foodies-api:
I removed the root_route view from the .views imports, I then imported the TemplateView from the generic Django views with "from django.views.generic import TemplateView".
In the url_patterns list, I removed the root_route code and replaced it with the TemplateView pointing to the index.html file. At the bottom of the file, I added the 404 handler to allow React to handle 404 errors with "handler404 = TemplateView.as_view(template_name='index.html')".
I then went and added api/ to the beginning of all the API URLs, excluding the path for the home page and admin panelIn axiosDefault.js.
In the axiosDefault.js I then set the axios.defaults.baseURL to "/api".
I then went to compile all of the static files from both the Django admin panel and the React files into the staticfiles folder for deployment. By entering "python3 manage.py collectstatic" to the terminal this will collect the admin and DRF staticfiles to the empty staticfiles directory that was created earlier.
After this I compiled the react app and moved its files to the staticfile folderNext, we will compile the React application and move its files to the staticfiles folder. 
by running "npm run build && mv build ../staticfiles/."
In the root directory of my project I created a new file called runtime.txt and inside it I added "python-3.9.16".
Project is now working with both front end and back end in the workspace. Deployed to Heroku.

# Credits

## Media 
* All images used are from Pexels, I used Tiny PNG to compress images down and then used Cloudinary as my storage for them.[Pexels](https://www.pexels.com/)
* All icons used for my navigation links are from FontAwesome.-[FontAwesome](https://fontawesome.com/)
* All icons used for default images are from Icons8.-[Image8](http://icons8.com)
* My favicon and logo I created myself from using Canva.-[Canva](https://www.canva.com/)

## Content 
* Code Institute - Code inspired and altered from Moments Walkthrough
* Code Institute - Code inspired and altered from Django Rest Framework Walkthrough
* Code Institute - Code inspired and altered from React Essentials Mini Walkthrough
* Alert messages - Code from - [Alert Messages](https://blog.logrocket.com/create-custom-react-alert-message/)
* Landing page code inspired and altered from - [Landing Page](https://github.com/jyotiyadav2508/childhood-memories-react-pp5/blob/main/src/pages/landingPage/LandingPage.js)
