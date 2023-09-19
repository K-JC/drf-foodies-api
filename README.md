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
I aim to achieve a content sharing platform for all things baking, where users can post images of their creations, they can like and comment on other users posts. A user can also follow another user so they can keep up to date with that user. The post user will have the ability to edit or delete their posts.
When at the first stage of planning my project I put myself in the shoes of the user, I needed to understand what the users wants or needs for this platform. I noted down the following.
Why would the user come here in the first place? To post about their baking creations. To like and comment on other users' creations. To create awareness of their talent to others.
The first thing the user should see is that this is a content sharing platform. It should be very clear how to navigate it for great user experience.
What would make them come back after their first visit? To edit/delete their original post or to make a new post. To check if a user they followed has posted anything new or if there are any comments that they need to reply to.
If the experience of navigating is straightforward, easy to use and the platform looks good this should create a good user experience.
Goal for a user to post their creations to a global network of people
Core Values
A place for users to upload their own post(photos of their baking). A place for users to like or comment on another users post. A user can edit or delete their own posts/comments/images. A user can see all the posts that they have liked. A user can follow another user. A user will have their own profile page/about/profile image(can upload their own image). A user will have login and log out functionality. A new user will be able to sign up for their own account. Will need a react-bootstrap library to aid in the styling and responsiveness of the website. The application will be hosted on heroku. Will connect to a custom API to store our users/posts/likes/comments. User stories to guide me to build functionality . Simple automated tests to check the project works correctly. CRUD functionality for users.

## Scope
The features I want to implement are the ability for a user to create their own account, they can log in and log out with their own username and password which will make their account secure. 
They will be able to personalize their account with an about me section, so that other users can find out more about you. 
They will also be able to upload a profile picture. They can change this at any time. The about me section can also be edited/updated.
They will be able to create a post about their creations, this will include a title, an image and a description relating to the image uploaded. 
They will be able to edit/delete their own posts. Follow/ unfollow other users. Like and comment on other users posts and can comment on their own post in response to other users comments. 


## Structure
Logically grouping the main home page so that additional pages are easy to navigate through a collapsible navigation icon. When a user who isn't signed in/signed up accesses the platform they will only be able to see the “Home,Sign In or Sign Up” navigation links. Only once they are a logged user will they have access to the full navigation links such as “Home, Add Post, Feed, Liked, Sign Out and Profile”.
The user will be able to navigate easily through the platform which will add to a positive user experience. 

## Skeleton
Navigation links and posted content will be presented in a tidy way.
Collapsible navigation links on smaller screen sizes to avoid too much clutter.
Only a logged in user will be able to access the platform fully. There will only be “Home, Sign In and Sign Up navigation links visible to non-signed in users, so it will be clear to the user that to access the site they will need an account and will have to sign up . Once a user is logged in they can access the platform and will now be able to create a post etc. Once posted there will be a drop down to the side of the post with an edit or delete option.
The user will have the ability to log out of their account.
Information on the homepage will be relevant to this sharing content platform, from the description to the imagery used. The Sign In/Sign Up page will have imagery relevant to baking. The favicon/logo used will be related to baking as well, I would like a cake or a mixing bowl. 

## Surface
I want this to look visually pleasing and clean. Google fonts of Noto Serif and a backup of sans-serif. A combinations of different colors (purple) #B8A1BC, #F2C6D0 and #E2D9E3.
A user would visit the platform and see the logo to the left hand side “Foodies” to the right would be all the navigation links. On smaller screen sizes there would be a navigation drop down menu. 
Only the Home, Sign Up and Sign In navigations will be visible to non logged users. Once a user is either signed up/signed in they will see the other navigation links such as “Add Post, Liked, Feed, Sign Out and Profile”.

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
Code Institute - Code inspired and altered from Moments Walkthrough
Code Institute - Code inspired and altered from Django Rest Framework Walkthrough
Code Institute - Code inspired and altered from React Essentials Mini Walkthrough
Alert messages - Code from [](https://blog.logrocket.com/create-custom-react-alert-message/)
Landing page code inspired and altered from ...




