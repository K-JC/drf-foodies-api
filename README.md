## Foodies
For my fifth and final project with Code Institute I chose to create a baking community based content sharing platform to share baking creations to a global audience. Foodies is all about yummy food, sweet treats and all things good. The platform enables users to create posts, edit or delete posts,read posts,comment and like on posts. Users can also follow other users and keep up to date on their latest creations. Users can use the search bar at the top to browse through the platform's posts. Search results can be filtered on usernames, popularity, date created, title, content keywords and category. This is my advanced front-end project, I hope you enjoy it! - [Link To Foodies](https://drf-foodies-api-1b38deb7eb8c.herokuapp.com/)

Combined Repository - [Link](https://github.com/K-JC/drf-foodies-api)

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

## Scope

## Structure

## Skeleton

## Surface

# Wireframe
Once I had an idea of what the user would need, I could then begin to figure out what the platform would look like.
I created some wireframes using Figma, this is how I envisioned the homepage of the platform to look and the rest of the pages to keep the same visuals.
![]()
![]()
![]()

# User Stories
![]()
 Authentication
* Authentication - Sign up/Sign in - As a site user I can sign up and sign in to the site so that I can access the functionality of the website.
* Authentication - Log Out -As a site user I can log out of my account so that I have more security over it.
* Authentication - Logout Status - As a site user I can maintain my logged-in status until I choose to log out so that my user experience is not compromised.
* Posts -As a site user I cannot edit or delete any posts another user has created so that there is complete protection/control over a user's content.
* Comments- As a site user I cannot edit or delete any comments and likes made that another user has created so that there is complete protection/control over a user’s content.
* Likes -As a site user I can only like or unlike other users' posts/comments, not my own so that I can show my support for other posts/comments.
* Following- As a site user I can follow other users so that I can keep up to date with the user’s posts.
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
* Edit/delete posts- As a site user I can edit/delete my posts so that I can make changes to an existing post title/description or remove my post completely.
* View posts Feed- As a site user I can view all user posts made on the Feed page so that I can keep up to date with other users.
* Post Order View- As a site user I can view the most recent posts, ordered by the most recent first so that I am kept up to date with the latest content.
* Search Posts- As a site user I can search for posts/users in a search box so that I can find specific posts/users that I am searching for.
* Content Filters- As a site user I can view content filtered by users I follow so that I can keep up to date with their creations they post about.
Comment 
* View Comment- As a site user I can view comments on a post so that I can read what others are saying. 
* Post Comment- As a site user I can post a comment on a post so that I can share what I am thinking.
* Edit/Delete Comment- As a site user I can edit/delete my comments so that I have control over what I want to say and either fix or remove my comment. 
* Comment Creation Date- As a site user I can see how long ago a comment was made so that I know how old a comment is.
* Comment Likes - As a site user I can like another user's comment so that I can show I support their comment.
Likes  
* Likes- As a site user I can see the number of likes on a post so that I can see which are becoming popular.
* Like/Unlike- As a site user I can like/unlike comments so that I can show my support/remove support for a particular post.
Profile
* Following Users- As a site user I can follow/unfollow other users so that I have control over whether I want to see their content on my feed or not.
* Popular Profiles- As a site user I can see the most popular profiles so that I can gauge who’s creations are getting noticed more.
* Update Profile About- As a site user I can update my about me so that I can make changes when necessary and other users will keep updated on me.
* Update Profile Picture- As a site user I can update my profile picture so that I can keep my profile up to date.
* View Profiles- As a user I can view another user's profile picture so I can easily identify other users of the platform.
* Update Profile Info- As a site user I can update my username and password so that I can change my display name and keep my profile secure.
* View Other Profiles- As a site user I can view other users' profiles, about me, number of posts, follows and users followed so that I can learn more about them.



From the development plane and wireframe I got a good idea of what user stories I create.
I created a GitHub project called Foodies Stories and connected this to my project repository. The user stories are as follows.

# Features


# Bugs
While originolly trying to deploy my project my api wasnt talking to my front end and I had alot of CORS errors come up in my chrome dev tools console. After much headache over trying to fix this I had seen that we could combined our reposityrs into one work space which would mean that cors would no longer be an issue as the api was coming from the same workspace/shared base URL. I followed the steps set by code institute to enable my project to contain both front end and back end portions of the project and once all was set up and I deployed my project to heroku it was finally working! 

## Solved
## Unsolved Bugs


# Future Features
# Validator Testing
HTML - W3C HTML Validator
CSS - W3C CSS Validator
PEP8 - Python Validator
Eslint Play Validator

# Testing
## Manual Testing 


# Technologies Used
## Frameworks, Libraries, Programs & Applications Used
Django Rest
React.js
Bootstrap.js
Python
PostgreSQL
Cloudinary - I used Cloudinary to store images from this project.
Font Awesome - I used Icons from Font Awesome for my navigation links.
Figma - I used Figma in the planning stage to create my sitemap, from this I created my content sharing platform like I had designed.
GitHub - My project was stored on Github.
GitPod - Gitpod was used for writing my code and when I pushed commits from Gitpod they were uploaded to Github where my project was stored.
Heroku - Where the project was deployed to.
Google Development Tool - Where I checked the responsiveness of the website and edited any code without the risk of making it a permanent change.
Elephantsql - I used Elephantsql for my database.

## Languages
HTML
CSS
Python
Javascript


# Accessibility
Lighhouse Information 

# Deployment
DEPLOYMENT PROCESS HEROKU - FRONT END AND BACK END
Ended up being a combined deployment, explain proccess...

# Credits

## Media 
All images used are from Pexels, I used Tiny PNG to compress images down and then used Cloudinary as my storage for them.[Pexels](https://www.pexels.com/)
All icons used for my navigation links are from FontAwesome.-[FontAwesome](https://fontawesome.com/)
All icons used for default images are from Icons8.-[Image8](http://icons8.com)
My favicon and logo I created myself from using Canva.-[]()



## Content 
Code Institute - Some code inspired and altered from Moments Walkthrough
Code Institute - Some code inspired and altered from Django Rest Framework Walkthrough
Code Institute - Some code inspired and altered from React Essentials Mini Walkthrough
Alert messages - code from [](https://blog.logrocket.com/create-custom-react-alert-message/)
Landing page code inspired and altered from ...




