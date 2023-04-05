# World News
World News is a site for users who are interested in reading news of different categories. World News will keep them aware about the happenings around the world. The goal of the site is provide a platform to the users for discussion while commenting and liking or unliknig the news. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/different-screen-sizes.jpg" alt="Website on different screen sizes">
</div>

## [View live website](https://ci-fsf-django-news.herokuapp.com/)

___
# Table of contents
- [UX](#ux)
    - [Website owner goals](#website-owner-goals)
    - [User goals](#user-goals)
    - [User stories](#user-stories)
    - [Structure of the website](#structure-of-the-website)
    - [Surface](#surface)
- [Features](#features)
    - [Navigation bar](#navigation-bar)
    - [Footer](#footer)
    - [Home](#home)
    - [News categories](#news-categories)
        - [Sports](#sports)
        - [Worklife](#worklife)
        - [Climate](#climate)
        - [Science](#science)
        - [Environment](#environment)
        - [Business](#sports)
    - [News detail](#news-detail)
    - [Register](#register)
    - [Sign In](#sign-in)
    - [Sign Out](#sign-out)
    - [Like/Unlike a news post](#like-unlike-a-news-post) 
    - [Submission of comment](#submission-of-comment)
    - [Approval of comment](#approval-of-comment)
- [Technologies used](#technologies-used)
- [Testing](#testing)
    - [Automated testing](#automated-testing)
        - [Code validation](#code-validation)
        - [Performance testing](#performance-testing)
    - [Manual testing](#manual-testing)
      - [Testing User Stories](#testing-user-stories)
      - [Full Testing](#full-testing)
    - [Compatibility testing](#compatibility-testing)
    - [Functionality testing](#functionality-testing)
    - [Issues found during site development](#issues-found-during-site-development)
- [Deployment](#deployment)
- [Credits](#credits)

___
# UX

## Website owner goals
The main goals of the website owner are:
* To create a discussion community for the users.
* To provide a website for different categories of news. 
* To provide the possibilty for the users to leave their comments.
* To provide the possibilty for the users to like or unlike the news.

## User goals
The main goals of the website user are 
* To post the news.
* To read the news.
* To leave comment on the news.
* To like or unlike the news.

## User stories

### As a site user/site owner
* As a site owner I can create, read, update, and delete posts so that I can manage my news content.
* As a site owner I can categorize a post so that I and site user can view the list of posts based on their category.
* As a site owner I can create draft posts so that I can finish writing the content later on.
* As a site owner/site user I can view the number of likes on each post so that I can see which is the most popular or viral news these days.
* As a site owner/site user I can view comments on an individual post so that I can read the conversation among the community.
* As a site owner I can approve or disapprove comments on each post so that I can filter out the objectionable comments.

### As a site user
* As a site user I can view a navigation bar so that I can easily navigate around the different pages of the website.
* As a site user I can view a paginated list of posts so that I can easily select the post to view. 
* As a site user I can view the list of posts so that I can select the one to read.
* As a site user I can click on the title of the post so that I can read the full text about that news.
* As a site user I can register an account so that I can comment and like the news.
* As a site user I can leave comments on the posts so that I can be involved in the conversation with the community.
* As a site user I can like or unlike a post so that I can interact with the content and share my feelings about that news.

## Structure of the website
* The design of the website is user-friendy as this is responsive on all type of devices: desktop, laptops, tablets, ipads and mobiles.
* On all the above mentioned devices users can have a fantastic experience. 
* All parts of the website are designed to achieve maximum user satisfaction.

## Surface

### Colors
Main colours used in the development of World News:
* background color: #F9FAFC; #fff; #75dcdc; #f8f9fb; #23BBBB; 
* font color: #171719; #d14111; #171719; white; lightgray; #171719; #fff; #d6e2e2;
* link color: #052241; #13355b; #0a9292;
* link hover color: #481404; #97250e; rgb(109, 10, 10)
* button color: #138197; #585655; 
* button hover color: #094c59; #363534;
* social networks: rgb(109, 10, 10)

### Fonts 
* As a main font lato and as a backup font sans-serif are used for the contents of the website.

### Images
* Images are taken from [Google Images](https://images.google.nl/), which is credited in the [credits](#credits) section.

[Back to Table of contents](#table-of-contents)

___
# Features

## Navigation bar
The full responsive navigation bar is featured on all the pages to allow for easy navigation from page to page across all devices.
* On the left side is logo and title of the website, which can be used as navigation link to Home page.
* On the left side are also links to the Home, News categories, Register, Sign In, Sign Out.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/nav-bar.jpg" alt="navigation bar">
</div>

## Footer
The footer section is consistent on all pages and includes links to the relevant social media sites for World News.
* The links will open in a separate tab in a browser to allow easy navigation for the users.
* The footer is useful for users to get connected with the community for socialization through social networks.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/footer.jpg" alt="Footer">
</div>

## Home
* The home page includes all categories of news published on World News.
* The inclusion of an eye-catching animation draws the attention of users for different caegories of news.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/home-page.jpg" alt="Home page">
</div>

## News Categories
* Different categories of news such as sports, science, worklife, and business will appear on their respective pages. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="assets/images/home-page.jpg" alt="Home page">
</div>

### Sports
* The news related to sports are on sports page. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/sports-page.jpg" alt="Sports page">
</div>

### Worklife
* The news related to worklife are on worklife page. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/worklife-page.jpg" alt="Worklife page">
</div>

### Climate
* The news related to climate are on climate page. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/climate-page.jpg" alt="climate page">
</div>

### Science
* The news related to science are on science page. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/science-page.jpg" alt="Science page">
</div>

### Environment
* The news related to environment are on environment page. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/environment-page.jpg" alt="Environment page">
</div>

### Business
* The news related to business are on business page. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/business-page.jpg" alt="Business page">
</div>

## News detail
The users can read the detail about the news by clicking on the title of the news post. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/news_detail.jpg" alt="News detail">
</div>

## Register
Users can register an account so that they can comment and like different categories of news posts on World News.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/register.jpg" alt="Register">
</div>

## Sign In
After registration users can sign in so that they can comment and like different categories of news on World News.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/sign-in.jpg" alt="Sign In">
</div>

## Sign Out
Users can sign out if they would like to be signed out due to security reasons.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/sign-out.jpg" alt="Sign Out">
</div>

## Like/Unlike a news post 
After creating an account the user can like or unlike the news post by click/unclick the icon of thumb-up on the post detail page.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/like-unlike-news-post.jpg" alt="Like/Unlike news post">
</div>

## Submission of comment 
The message of successful submission will appear on the post details page after leaving the comment on a news post.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/submission-comment.jpg" alt="Submission comment">
</div>

## Approval of comment 
On the post details page after leaving the comment on a news, the message will appear to indicate that your comments needs approval.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/approval-comment.jpg" alt="Approval comment">
</div>

[Back to Table of contents](#table-of-contents)

___
# Technologies used

Different technologies were used to complete the contents of World news website.

### GitHub
* As a software hosting platform to keep project in a remote location.

### Git
* As a version-control system tracking.

### Gitpod  
* As a development hosting platform.

### Codeanywhere
* As a development hosting platform.

### Heroku
* Platform as a service offering to carry out application deployment, scaling, and management.

### HTML5
* As a structure language.

### CSS
* As a style language.

### Python
*  As an interpreted, interactive, and object oriented scripting language.

### JavaScript
* As an interactivity langauage.

### Django
* As a high-level Python web framework that encourages rapid development and clean, pragmatic design.

### Postgres
* As a relational database.

### Font Awesome
* As an icon library for icons used in the World News comments and likes section, and social links.

[Back to Table of contents](#table-of-contents)

___
# Testing

## Automated testing 
The automated testing includes all the testing that is carried out by a program. World News is validated for a code using four websites ([W3C HTML Validator](https://validator.w3.org/); [W3C CSS Validator (Jigsaw)](https://jigsaw.w3.org/css-validator/); [JSHint JavaScript Validator](https://jshint.com/); [PEP8 online validator](http://pep8ci.herokuapp.com/#)), and performance was tested using [Lighthouse](https://developers.google.com/web/tools/lighthouse/) tool.

### Code validation

#### HTML
* No errors were found when passing through the official [W3C HTML Validator](https://validator.w3.org/)

#### CSS
* No errors were found when passing through the official [W3C CSS Validator (Jigsaw)](https://jigsaw.w3.org/css-validator/)

#### JavaScript
* No errors were found when passing through the official [JSHint JavaScript Validator](https://jshint.com/)

#### Python
* No errors were found when passing through the official [PEP8 online validator](http://pep8ci.herokuapp.com/#)

### Performance testing
[Lighthouse](https://developers.google.com/web/tools/lighthouse/) tool was used to check the performance of the website.
* Couple of changes were made to improve the performance.

### Final results
* The colors and fonts chosen are easy to read and accessible on desktop. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/accessibility-desktop.jpg" alt="Accessibility on desktop">
</div>

* The colors and fonts chosen are easy to read and accessible on mobile.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/accessibility-mobile.jpg" alt="Accessibility on mobile">
</div>

### Running python testing
Django testing was done for forms.py, models.py, and views.py. Test were run OK.

* forms.py

<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/test-forms.jpg" alt="Test forms">
</div>

* models.py

<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/test-models.jpg" alt="Test models">
</div>

* views.py

<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/test-views.jpg" alt="Test views">
</div>

### Coverage of python testing

<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/coverage.jpg" alt="Coverage">
</div>

## Manual testing

### Testing User Stories
World News website is meeting the needs of the [User stories](#user-stories) as described in the UX section of this README document.

#### As a site user/site owner
| Goals | Steps to achieve them |
| :--- | :--- |
| Manage posts | The site owner can create, read, update, and delete posts after login to admin account to manage the news content. The post model is created with the functions to create, read, update, and delete posts. |
| Categorize a post | In the navigation bar is a link to news categories. After clicking on that link, a list of categories will be opened for the site user/site ownner to select the list of the news posts according to their category of interest. The category model is created with the functions to select the post category. |
| Create draft posts | The site owner can create draft posts after login to admin account. The post model is created with the functions to create draft news and leave the contents to publish them later on. |
| View likes | Under each post, the total number of likes are shown on the home page, and on the pages for individaul categories of news posts so that site user/site owner can see which is the most popular or viral news these days. |
| View comments | Under each post, the total number of comments are shown on th home page. However, to see the list of the approved comments, the site user should open the detail of the news post by clicking on the tilte of the post; so that site user can read the conversation among the community. Under the details of the news post, on left side is the list of the comments and on the right side is the comment box to leave the comment. |
| Approve comments | The site owner can approve or disapprove comments on each post to filter out the objectionable comments after login to admin account. The comment model is created with the functions to approve or disapprove comments. The approved comments will be shown on the post detail page. |

#### As a site user
| Goals | Steps to achieve them |
| :--- | :--- |
| Easy navigation | A navigation bar is provided for site user on each page to easily navigate around the different pages of the website. |
| Site pagination | Site user can view a paginated list of posts on the home page and on the pages for individaul categories of news posts to easily select a post to view. |
| View post list | Site user can view the list of posts on the home page and on the pages for individaul categories of news posts to select the one to read. |
| Open a post | Site user can click on the title of the news post to read the detail about that news post. |
| Account registration | In the navigation bar is a link to register an account so that site user can leave a comment and like or unlike the news post. |
| Comment on a post | After creating an account the site user can leave a comment on the news post in the comments section on the post detail page to be involved in the conversation with the community. |
| Like/Unlike a post | After creating an account the site user can like or unlike the news post by clicking on the icon of thumb-up on the post detail page to interact with the content and to share his/her feelings about that news. |

- - -

### Full Testing
 
#### Compatibility testing
The website was tested across multiple devices such as desktop, laptops, tablets, ipads and mobiles, and browsers manually. people were asked to visit the website on a variety of devices, to setup accounts within the World News and to leave their comments and like the news. This feedback was very useful to determine any bugs that may have been present. 

Below is the list of Internet Browsers that were used to test the display of the website:
* Google Chrome
* Microsoft Edge
* Internet Explorer

</br>Manual testing was carried out using the above browsers. No bugs or display issues could be identified.

#### Functionality testing
Chrome developer tools were used throughout the project for testing and solving problems with responsiveness and style issues.

#### Navigation bar
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Navigation bar | Links direct the user to different pages of the website | Clicked the links | Different pages load | Pass |
| Website title | Link directs the user back to the home page | Clicked the title | Home page reloads | Pass |
| Home | Link directs the user back to the home page | Clicked the link | Home page reloads | Pass |
| News categories | Link directs the user to the individual categories of news | Clicked the link | List of all categories of news opened | Pass |
| Registration | Link directs the user to the registration page | Clicked the link | Registration page loads | Pass |
| Sign In | Link directs the user to the sign in page | Clicked the link | Sign In page loads | Pass |
| Sign Out | Link directs the user to the sign Out page | Clicked the link | Sign Out page loads | Pass |

#### Footer
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Footer | The footer section is consistent on all pages | Checked footer on all pages | Footer available on different pages | Pass |
| Links to social media | Links direct the user to different/relevant social media sites (Facebook, Twitter, Instagram, and Youtube) | Clicked the links | Social media sites load | Pass |
| Link to Facebook | Link directs the user to Facebook | Clicked the link | Facebook loads | Pass |
| Link to Twitter | Link directs the user to Twitter | Clicked the link | Twitter loads | Pass |
| Link to Instagram | Link directs the user to Instagram  | Clicked the link | Instagram loads | Pass |
| Link to Youtube | Link directs the user to Youtube | Clicked the link | Youtube loads | Pass |

#### Home Page
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Website title | Link directs the user back to the home page | Clicked the title | Home page reloads | Pass |
| Home | Link directs the user back to the home page | Clicked the link | Home page reloads | Pass |
| News posts | User can see six news posts on one page and new pages are added in case of more than six news posts | Pages checked for number of news posts | Six news posts were on one page and then new pages are added in case of more than six news posts | Pass |
| Order of news posts | User should be able see the recent news posts first | News posts were checked based on their created date | The news posts were in descending order according to their created date | Pass |

#### News categories
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| News categories | Link directs the user to the individual categories of news | Clicked the link | List of all categories of news opened | Pass |
| Sports | Link directs the user to the news related to sports | Clicked the link | List of news related to sports opened | Pass |
| Worklife | Link directs the user to the news related to worklife | Clicked the link | List of news related to worklife opened | Pass |
| Climate | Link directs the user to the news related to climate | Clicked the link | List of news related to climate opened | Pass |
| Science | Link directs the user to the news related to science | Clicked the link | List of news related to science opened | Pass |
| Environment | Link directs the user to the news related to environment| Clicked the link | List of news related to environment opened | Pass |
| Business | Link directs the user to the news related to business| Clicked the link | List of news related to business opened | Pass |

#### News Detail
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| News detail | Title of the news posts directs the user to read the details about that news | Clicked the title | Detail of the news opened | Pass |

#### Comment on a news post
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Comment on a news post | User should be able to leave a comment on the news post | Added comment in the comment box | Comment was added | Pass |

#### Submission of comment
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Submit a comment | User should be able to submit a comment | Clicked the submit button | Comment was submitted | Pass |
| Submission message | User should be confirmed about their submission of a comment | Clicked the submit button | Submission successful message | Pass |

#### Approval of comment 
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Approval of comment | User should be able to see that their submission needs approval | Comment approved after login to the admin | Message that comment is awaiting approval | Pass |

#### Comment list 
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Order of comment list | User should be able see the recent comments first | Comments were checked based on their created date | The comments were in ascending order according to their created date | Pass |

#### Like/Unlike a news post
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Like/Unlike a news post | User should be able to like or unlike a news post | Clicked/unclicked the icon of thumb-up on the news detail page | Like or unlike recorded | Pass |

#### Registration
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Registration | Link directs the user to the registration page | Clicked the link | Registration page loads | Pass |
| User details | User will be able to input username and password with optional email | Input of username, password and email | Username, password and email added | Pass |
| Send button | The username, password and email will be sent | Clicked on send button | Username, password and email sent | Pass |
| Send button - hover effect | Send button background should change when hovered over to it as suggested | Hover over the send button | Send button displayed the correct styling when hovered over | Pass |

#### Sign In
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Sign In | Link directs the user to the sign in page | Clicked the link | Sign In page loads | Pass |
| User details | User will be able to input username and password | Input of username and password | Username and password added | Pass |
| Sign In button | The user will be able to sign in | Clicked on sign in button | User could sign in | Pass |
| Sign In button - hover effect | Sign In button background should change when hovered over to it as suggested | Hover over the sign in button | Sign In button displayed the correct styling when hovered over | Pass |

#### Sign Out
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Sign Out | Link directs the user to the sign out page | Clicked the link | Sign Out page loads | Pass |
| Sign Out button | The user will be able to sign out | Clicked on sign out button | User could sign out | Pass |
| Sign Out button - hover effect | Sign Out button background should change when hovered over to it as suggested | Hover over the sign out button | Sign Out button displayed the correct styling when hovered over | Pass |

---

## Issues found during site development

### Navigation link for news categories
* The list of different categories of news was opened on the side of the page instead of below the news categories navigation link.<br>
I adjusted this issue:
   * 

## Unfixed bugs
* No unfixed bugs

[Back to Table of contents](#table-of-contents)

___
# Deployment

## GitHub
Gitpod and Codeanywhere were used as a development environment where all the changes were committed to git version control system. The push command was used in Gitpod and Codeanywhere to save changes into GitHub.

## Heroku
World News was deployed using Code Institute's mock terminal for Heroku.
The steps for deployment were as follows:
* Fork or clone this repository
* Create a new Heroku app
* Set the buildpacks to Python and NodeJS in that order
* Link the Heroku app to the Github repository
* Click on Deploy

## [View live website](https://ci-fsf-django-news.herokuapp.com/)

[Back to Table of contents](#table-of-contents)

___
# Credits

To complete the contents of World News website, I learned coding and collected the information from different sources.
* Learned HTML, CSS, JavaScript, and Python coding from [Code Institute](https://learn.codeinstitute.net/)
* Used Code Institute student template [gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template)
* Collected information on good and bad coding practices from:
  * [Write Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  * [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
* The description on the DjangoBlog provided by the tutor of the Code Institute with [DjangoBlog](https://codestar2021.herokuapp.com/) was useful as well as an inspiration to design World News.
* I acknowledge [Adegbenga Adeye](https://www.linkedin.com/in/adegbenga-adeye-psm-i-14003635/) for mentor support and finishing touches.

## Content
* The details about the news were found at [BBC](https://www.bbc.com/news) and [CNN](https://edition.cnn.com/).
* The icons used in the World News comments and likes section, and social links were taken from [Font Awesome](https://fontawesome.com/)
* The code to make the social networks links was taken from [Project](https://github.com/HumaIlyas/Project-1)

## Media
* The images used on the Home and News Categories pages were taken from [Google Images](https://images.google.nl/)
# World News
World News is a site for users who are interested in reading news of different categories. World News will keep them aware about the happenings around the world. The goal of the site is provide a platform to the users for discussion while commenting and liking or unliknig the news. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/different-screen-sizes.jpg" alt="Website on different screen sizes">
</div>

## [View live website](https://ci-fsf-django-news.herokuapp.com/)

___
# Table of contents
- [UX](#ux)
    - [Website owner goals](#website-owner-goals)
    - [User goals](#user-goals)
    - [User stories](#user-stories)
    - [Structure of the website](#structure-of-the-website)
    - [Surface](#surface)
- [Features](#features)
    - [Navigation bar](#navigation-bar)
    - [Footer](#footer)
    - [Home](#home)
    - [News categories](#news-categories)
        - [Sports](#sports)
        - [Worklife](#worklife)
        - [Climate](#climate)
        - [Science](#science)
        - [Environment](#environment)
        - [Business](#sports)
    - [News detail](#news-detail)
    - [Register](#register)
    - [Sign In](#sign-in)
    - [Sign Out](#sign-out)
    - [Like/Unlike a news post](#like-unlike-a-news-post) 
    - [Submission of comment](#submission-of-comment)
    - [Approval of comment](#approval-of-comment)
- [Technologies used](#technologies-used)
- [Testing](#testing)
    - [Automated testing](#automated-testing)
        - [Code validation](#code-validation)
        - [Performance testing](#performance-testing)
    - [Manual testing](#manual-testing)
      - [Testing User Stories](#testing-user-stories)
      - [Full Testing](#full-testing)
    - [Compatibility testing](#compatibility-testing)
    - [Functionality testing](#functionality-testing)
    - [Issues found during site development](#issues-found-during-site-development)
- [Deployment](#deployment)
- [Credits](#credits)

___
# UX

## Website owner goals
The main goals of the website owner are:
* To create a discussion community for the users.
* To provide a website for different categories of news. 
* To provide the possibilty for the users to leave their comments.
* To provide the possibilty for the users to like or unlike the news.

## User goals
The main goals of the website user are 
* To post the news.
* To read the news.
* To leave comment on the news.
* To like or unlike the news.

## User stories

### As a site user/site owner
* As a site owner I can create, read, update, and delete posts so that I can manage my news content.
* As a site owner I can categorize a post so that I and site user can view the list of posts based on their category.
* As a site owner I can create draft posts so that I can finish writing the content later on.
* As a site owner/site user I can view the number of likes on each post so that I can see which is the most popular or viral news these days.
* As a site owner/site user I can view comments on an individual post so that I can read the conversation among the community.
* As a site owner I can approve or disapprove comments on each post so that I can filter out the objectionable comments.

### As a site user
* As a site user I can view a navigation bar so that I can easily navigate around the different pages of the website.
* As a site user I can view a paginated list of posts so that I can easily select the post to view. 
* As a site user I can view the list of posts so that I can select the one to read.
* As a site user I can click on the title of the post so that I can read the full text about that news.
* As a site user I can register an account so that I can comment and like the news.
* As a site user I can leave comments on the posts so that I can be involved in the conversation with the community.
* As a site user I can like or unlike a post so that I can interact with the content and share my feelings about that news.

## Structure of the website
* The design of the website is user-friendy as this is responsive on all type of devices: desktop, laptops, tablets, ipads and mobiles.
* On all the above mentioned devices users can have a fantastic experience. 
* All parts of the website are designed to achieve maximum user satisfaction.

## Surface

### Colors
Main colours used in the development of World News:
* background color: #F9FAFC; #fff; #75dcdc; #f8f9fb; #23BBBB; 
* font color: #171719; #d14111; #171719; white; lightgray; #171719; #fff; #d6e2e2;
* link color: #052241; #13355b; #0a9292;
* link hover color: #481404; #97250e; rgb(109, 10, 10)
* button color: #138197; #585655; 
* button hover color: #094c59; #363534;
* social networks: rgb(109, 10, 10) 

### Fonts 
* As a main font lato and as a backup font sans-serif are used for the contents of the website.

### Images
* Images are taken from [Google Images](https://images.google.nl/), which is credited in the [credits](#credits) section.

[Back to Table of contents](#table-of-contents)

___
# Features

## Navigation bar
The full responsive navigation bar is featured on all the pages to allow for easy navigation from page to page across all devices.
* On the left side is logo and title of the website, which can be used as navigation link to Home page.
* On the left side are also links to the Home, News categories, Register, Sign In, Sign Out.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/nav-bar.jpg" alt="navigation bar">
</div>

## Footer
The footer section is consistent on all pages and includes links to the relevant social media sites for World News.
* The links will open in a separate tab in a browser to allow easy navigation for the users.
* The footer is useful for users to get connected with the community for socialization through social networks.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/footer.jpg" alt="Footer">
</div>

## Home
* The home page includes all categories of news published on World News.
* The inclusion of an eye-catching animation draws the attention of users for different caegories of news.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/home-page.jpg" alt="Home page">
</div>

## News Categories
* Different categories of news such as sports, science, worklife, and business will appear on their respective pages. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="assets/images/home-page.jpg" alt="Home page">
</div>

### Sports
* The news related to sports are on sports page. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/sports-page.jpg" alt="Sports page">
</div>

### Worklife
* The news related to worklife are on worklife page. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/worklife-page.jpg" alt="Worklife page">
</div>

### Climate
* The news related to climate are on climate page. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/climate-page.jpg" alt="climate page">
</div>

### Science
* The news related to science are on science page. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/science-page.jpg" alt="Science page">
</div>

### Environment
* The news related to environment are on environment page. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/environment-page.jpg" alt="Environment page">
</div>

### Business
* The news related to business are on business page. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/business-page.jpg" alt="Business page">
</div>

## News detail
The users can read the detail about the news by clicking on the title of the news post. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/news_detail.jpg" alt="News detail">
</div>

## Register
Users can register an account so that they can comment and like different categories of news posts on World News.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/register.jpg" alt="Register">
</div>

## Sign In
After registration users can sign in so that they can comment and like different categories of news on World News.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/sign-in.jpg" alt="Sign In">
</div>

## Sign Out
Users can sign out if they would like to be signed out due to security reasons.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/sign-out.jpg" alt="Sign Out">
</div>

## Like/Unlike a news post 
After creating an account the user can like or unlike the news post by click/unclick the icon of thumb-up on the post detail page.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/like-unlike-news-post.jpg" alt="Like/Unlike news post">
</div>

## Submission of comment 
The message of successful submission will appear on the post details page after leaving the comment on a news post.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/submission-comment.jpg" alt="Submission comment">
</div>

## Approval of comment 
On the post details page after leaving the comment on a news, the message will appear to indicate that your comments needs approval.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/approval-comment.jpg" alt="Approval comment">
</div>

[Back to Table of contents](#table-of-contents)

___
# Technologies used

Different technologies were used to complete the contents of World news website.

### GitHub
* As a software hosting platform to keep project in a remote location.

### Git
* As a version-control system tracking.

### Gitpod  
* As a development hosting platform.

### Codeanywhere
* As a development hosting platform.

### Heroku
* Platform as a service offering to carry out application deployment, scaling, and management.

### HTML5
* As a structure language.

### CSS
* As a style language.

### Python
*  As an interpreted, interactive, and object oriented scripting language.

### JavaScript
* As an interactivity langauage.

### Django
* As a high-level Python web framework that encourages rapid development and clean, pragmatic design.

### Postgres
* As a relational database.

### Font Awesome
* As an icon library for icons used in the World News comments and likes section, and social links.

[Back to Table of contents](#table-of-contents)

___
# Testing

## Automated testing 
The automated testing includes all the testing that is carried out by a program. World News is validated for a code using four websites ([W3C HTML Validator](https://validator.w3.org/); [W3C CSS Validator (Jigsaw)](https://jigsaw.w3.org/css-validator/); [JSHint JavaScript Validator](https://jshint.com/); [PEP8 online validator](http://pep8ci.herokuapp.com/#)), and performance was tested using [Lighthouse](https://developers.google.com/web/tools/lighthouse/) tool.

### Code validation

#### HTML
* No errors were found when passing through the official [W3C HTML Validator](https://validator.w3.org/)

#### CSS
* No errors were found when passing through the official [W3C CSS Validator (Jigsaw)](https://jigsaw.w3.org/css-validator/)

#### JavaScript
* No errors were found when passing through the official [JSHint JavaScript Validator](https://jshint.com/)

#### Python
* No errors were found when passing through the official [PEP8 online validator](http://pep8ci.herokuapp.com/#)

### Performance testing
[Lighthouse](https://developers.google.com/web/tools/lighthouse/) tool was used to check the performance of the website.
* Couple of changes were made to improve the performance.

### Final results
* The colors and fonts chosen are easy to read and accessible on desktop. 
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/accessibility-desktop.jpg" alt="Accessibility on desktop">
</div>

* The colors and fonts chosen are easy to read and accessible on mobile.
<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/accessibility-mobile.jpg" alt="Accessibility on mobile">
</div>

### Running python testing
Django testing was done for forms.py, models.py, and views.py. Test were run OK.

* forms.py

<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/test-forms.jpg" alt="Test forms">
</div>

* models.py

<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/test-models.jpg" alt="Test models">
</div>

* views.py

<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/test-views.jpg" alt="Test views">
</div>

### Coverage of python testing

<div style="margin-top: 20px; margin-bottom: 20px;">
    <img src="static/images/coverage.jpg" alt="Coverage">
</div>

## Manual testing

### Testing User Stories
World News website is meeting the needs of the [User stories](#user-stories) as described in the UX section of this README document.

#### As a site user/site owner
| Goals | Steps to achieve them |
| :--- | :--- |
| Manage posts | The site owner can create, read, update, and delete posts after login to admin account to manage the news content. The post model is created with the functions to create, read, update, and delete posts. |
| Categorize a post | In the navigation bar is a link to news categories. After clicking on that link, a list of categories will be opened for the site user/site ownner to select the list of the news posts according to their category of interest. The category model is created with the functions to select the post category. |
| Create draft posts | The site owner can create draft posts after login to admin account. The post model is created with the functions to create draft news and leave the contents to publish them later on. |
| View likes | Under each post, the total number of likes are shown on the home page, and on the pages for individaul categories of news posts so that site user/site owner can see which is the most popular or viral news these days. |
| View comments | Under each post, the total number of comments are shown on th home page. However, to see the list of the approved comments, the site user should open the detail of the news post by clicking on the tilte of the post; so that site user can read the conversation among the community. Under the details of the news post, on left side is the list of the comments and on the right side is the comment box to leave the comment. |
| Approve comments | The site owner can approve or disapprove comments on each post to filter out the objectionable comments after login to admin account. The comment model is created with the functions to approve or disapprove comments. The approved comments will be shown on the post detail page. |

#### As a site user
| Goals | Steps to achieve them |
| :--- | :--- |
| Easy navigation | A navigation bar is provided for site user on each page to easily navigate around the different pages of the website. |
| Site pagination | Site user can view a paginated list of posts on the home page and on the pages for individaul categories of news posts to easily select a post to view. |
| View post list | Site user can view the list of posts on the home page and on the pages for individaul categories of news posts to select the one to read. |
| Open a post | Site user can click on the title of the news post to read the detail about that news post. |
| Account registration | In the navigation bar is a link to register an account so that site user can leave a comment and like or unlike the news post. |
| Comment on a post | After creating an account the site user can leave a comment on the news post in the comments section on the post detail page to be involved in the conversation with the community. |
| Like/Unlike a post | After creating an account the site user can like or unlike the news post by clicking on the icon of thumb-up on the post detail page to interact with the content and to share his/her feelings about that news. |

- - -

### Full Testing
 
#### Compatibility testing
The website was tested across multiple devices such as desktop, laptops, tablets, ipads and mobiles, and browsers manually. people were asked to visit the website on a variety of devices, to setup accounts within the World News and to leave their comments and like the news. This feedback was very useful to determine any bugs that may have been present. 

Below is the list of Internet Browsers that were used to test the display of the website:
* Google Chrome
* Microsoft Edge
* Internet Explorer

</br>Manual testing was carried out using the above browsers. No bugs or display issues could be identified.

#### Functionality testing
Chrome developer tools were used throughout the project for testing and solving problems with responsiveness and style issues.

#### Navigation bar
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Navigation bar | Links direct the user to different pages of the website | Clicked the links | Different pages load | Pass |
| Website title | Link directs the user back to the home page | Clicked the title | Home page reloads | Pass |
| Home | Link directs the user back to the home page | Clicked the link | Home page reloads | Pass |
| News categories | Link directs the user to the individual categories of news | Clicked the link | List of all categories of news opened | Pass |
| Registration | Link directs the user to the registration page | Clicked the link | Registration page loads | Pass |
| Sign In | Link directs the user to the sign in page | Clicked the link | Sign In page loads | Pass |
| Sign Out | Link directs the user to the sign Out page | Clicked the link | Sign Out page loads | Pass |

#### Footer
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Footer | The footer section is consistent on all pages | Checked footer on all pages | Footer available on different pages | Pass |
| Links to social media | Links direct the user to different/relevant social media sites (Facebook, Twitter, Instagram, and Youtube) | Clicked the links | Social media sites load | Pass |
| Link to Facebook | Link directs the user to Facebook | Clicked the link | Facebook loads | Pass |
| Link to Twitter | Link directs the user to Twitter | Clicked the link | Twitter loads | Pass |
| Link to Instagram | Link directs the user to Instagram  | Clicked the link | Instagram loads | Pass |
| Link to Youtube | Link directs the user to Youtube | Clicked the link | Youtube loads | Pass |

#### Home Page
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Website title | Link directs the user back to the home page | Clicked the title | Home page reloads | Pass |
| Home | Link directs the user back to the home page | Clicked the link | Home page reloads | Pass |
| News posts | User can see six news posts on one page and new pages are added in case of more than six news posts | Pages checked for number of news posts | Six news posts were on one page and then new pages are added in case of more than six news posts | Pass |
| Order of news posts | User should be able see the recent news posts first | News posts were checked based on their created date | The news posts were in descending order according to their created date | Pass |

#### News categories
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| News categories | Link directs the user to the individual categories of news | Clicked the link | List of all categories of news opened | Pass |
| Sports | Link directs the user to the news related to sports | Clicked the link | List of news related to sports opened | Pass |
| Worklife | Link directs the user to the news related to worklife | Clicked the link | List of news related to worklife opened | Pass |
| Climate | Link directs the user to the news related to climate | Clicked the link | List of news related to climate opened | Pass |
| Science | Link directs the user to the news related to science | Clicked the link | List of news related to science opened | Pass |
| Environment | Link directs the user to the news related to environment| Clicked the link | List of news related to environment opened | Pass |
| Business | Link directs the user to the news related to business| Clicked the link | List of news related to business opened | Pass |

#### News Detail
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| News detail | Title of the news posts directs the user to read the details about that news | Clicked the title | Detail of the news opened | Pass |

#### Comment on a news post
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Comment on a news post | User should be able to leave a comment on the news post | Added comment in the comment box | Comment was added | Pass |

#### Submission of comment
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Submit a comment | User should be able to submit a comment | Clicked the submit button | Comment was submitted | Pass |
| Submission message | User should be confirmed about their submission of a comment | Clicked the submit button | Submission successful message | Pass |

#### Approval of comment 
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Approval of comment | User should be able to see that their submission needs approval | Comment approved after login to the admin | Message that comment is awaiting approval | Pass |

#### Comment list 
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Order of comment list | User should be able see the recent comments first | Comments were checked based on their created date | The comments were in ascending order according to their created date | Pass |

#### Like/Unlike a news post
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Like/Unlike a news post | User should be able to like or unlike a news post | Clicked/unclicked the icon of thumb-up on the news detail page | Like or unlike recorded | Pass |

#### Registration
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Registration | Link directs the user to the registration page | Clicked the link | Registration page loads | Pass |
| User details | User will be able to input username and password with optional email | Input of username, password and email | Username, password and email added | Pass |
| Send button | The username, password and email will be sent | Clicked on send button | Username, password and email sent | Pass |
| Send button - hover effect | Send button background should change when hovered over to it as suggested | Hover over the send button | Send button displayed the correct styling when hovered over | Pass |

#### Sign In
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Sign In | Link directs the user to the sign in page | Clicked the link | Sign In page loads | Pass |
| User details | User will be able to input username and password | Input of username and password | Username and password added | Pass |
| Sign In button | The user will be able to sign in | Clicked on sign in button | User could sign in | Pass |
| Sign In button - hover effect | Sign In button background should change when hovered over to it as suggested | Hover over the sign in button | Sign In button displayed the correct styling when hovered over | Pass |

#### Sign Out
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Sign Out | Link directs the user to the sign out page | Clicked the link | Sign Out page loads | Pass |
| Sign Out button | The user will be able to sign out | Clicked on sign out button | User could sign out | Pass |
| Sign Out button - hover effect | Sign Out button background should change when hovered over to it as suggested | Hover over the sign out button | Sign Out button displayed the correct styling when hovered over | Pass |

---

## Issues found during site development

### Navigation link for news categories
* The list of different categories of news was opened on the side of the page instead of below the news categories navigation link.<br>
I adjusted this issue:
   * 

## Unfixed bugs
* No unfixed bugs

[Back to Table of contents](#table-of-contents)

___
# Deployment

## GitHub
Gitpod and Codeanywhere were used as a development environment where all the changes were committed to git version control system. The push command was used in Gitpod and Codeanywhere to save changes into GitHub.

## Heroku
World News was deployed using Code Institute's mock terminal for Heroku.
The steps for deployment were as follows:
* Fork or clone this repository
* Create a new Heroku app
* Set the buildpacks to Python and NodeJS in that order
* Link the Heroku app to the Github repository
* Click on Deploy

## [View live website](https://ci-fsf-django-news.herokuapp.com/)

[Back to Table of contents](#table-of-contents)

___
# Credits

To complete the contents of World News website, I learned coding and collected the information from different sources.
* Learned HTML, CSS, JavaScript, and Python coding from [Code Institute](https://learn.codeinstitute.net/)
* Used Code Institute student template [gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template)
* Collected information on good and bad coding practices from:
  * [Write Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  * [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
* The description on the DjangoBlog provided by the tutor of the Code Institute with [DjangoBlog](https://codestar2021.herokuapp.com/) was useful as well as an inspiration to design World News.
* I acknowledge [Adegbenga Adeye](https://www.linkedin.com/in/adegbenga-adeye-psm-i-14003635/) for mentor support and finishing touches.

## Content
* The details about the news were found at [BBC](https://www.bbc.com/news) and [CNN](https://edition.cnn.com/).
* The icons used in the World News comments and likes section, and social links were taken from [Font Awesome](https://fontawesome.com/)
* The code to make the social networks links was taken from [Project](https://github.com/HumaIlyas/Project-1)

## Media
* The images used on the Home and News Categories pages were taken from [Google Images](https://images.google.nl/)
