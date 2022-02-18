# Machinery Issue Reporting System

# Table of Contents
* [Background](#background "Background")
* [Mission Statement](#mission-statement "Mission Statement")
* [Target Audience](#target-audience "Target Audience")
* [Stakeholder Interviews](#stakeholder-interviews "Stakeholder Interviews")
    * [User Persona](#user-persona "User Persona")
    * [User Goals](#user-goals "User Goals")
    * [User Stories](#user-stories "User Stories")
    * [User Requirements and Expectations](#user-requirements-and-expectations)
        * Requirements
        * Expectations
    * [Site Owners Persona](#site-owner's-persona "Site Owner's Persona")
    * [Site Owners Goals](#site-owners-goals "Site Owner's Goals")
    * [Site Owners Stories](#site-owners-stories "Site Owner's Stories")
    * [Site Owners Requirements and Expectations](#site-owners-requirements-and-expectations "Site Owners Requirements and Expectations")
        * Requirements
        * Expectations
    * [Strategy](#strategy "Strategy")
        * Strategy Outline
        * Strategy Description
            * User
            * Site Owner
    * [Wireframes](#wireframes "Wireframes")
    * [Design Choices](#design-choices "Design Choices")
        * Fonts
            * Content
            * Headings
        * Colours
        * Images
    * [Structure](#structure "Structure")
        * Site Structure
        * Data Schema
        * Models
        * Forms
    * [Features](#features "Features")
        * Existing Features
        * Features to be implemented
    * [Technologies used](#technologies-used "Technologies used")
        * Languages
        * Libraries and Frameworks
        * Tools
    * [Testing](#testing "Testing")
        * UX Testing
        * Code Validation
        * Bugs
        * Unfixed Bugs
    * [Deployment](#deployment "Deployment")
    * [Credits](#credits "Credits")

# Background
With the restrictions in place within teaching in the Irish Universities due to the Coronavirus pandemic, the improved organisation of working methods to reduce contact with staff and students over more trivial tasks have to be looked at. With this in mind, TU Dublin's engineering department has been looking to implement a machinery issue reporting system for the many machines to which the students have access. Currently, the engineering department is using a manual process where students write into a diary, where unnecessary physical touchpoints are created, or send an email where there is potential for loss of information to happen. They are looking to create an automated system to improve the procedure for all stakeholders.

# Mission Statement
Provide a fully automated, easily used and aesthetically pleasing machinery issue reporting system for TU Dublin.

# Target Audience
The target audience consists of approximately 150 students, both full time and part-time. The students are of a similar educational standard due to the course entry requirements but there is a selection that has extra educational needs so this needs to be addressed with accessibility built into the application.

There are three members of staff, one technician and two lecturers.

# Stakeholder Interviews
I carried out short interviews with both a selection of staff and students that this project will affect. All people interviewed will be *Users*, however for an easier view of the breakdown of requirements, I have split the results into *students* and *staff*.

## Student Persona
These are the details of the students interviewed. Two criteria were taken into consideration when selecting appropriate candidates for interviews. Firstly that they are either a part-time or full-time student of TU Dublin, and also that the course they are enrolled on is within the engineering department.

| Name | Age | Course | Education |
| -- | -- | -- | -- |
| Don Heslip| 22 | Automation Engineering | Leaving Cert |
| Aodhgon Smith | 19 | Aviation Technology | Leaving Cert |
| Niall McCarthy | 34 | Design Technology and Innovation | Leaving Cert |
| Elaine Cross | 22 | Structural Engineering | Leaving Cert |

## Student Goals
From the resulting interviews, the user goals have been defined:
* See what defects or issues have been reported
* See what defects or issues I have reported
* Clear display in a landing page
* Clear navigation process
* Ability to use the system on a mobile phone

## Student Stories
* As a student, I want to have a clear and defined landing page
* As a student, I want to be able to report aa issue on a machine
* As a student, I want to see any issues that I have reported
* As a student, I want to see the machine's name and description
* As a student, I want to see if there are any issues already reported on a machine
* As a student, I want to know this is a TU Dublin application

## Student Requirements and Expectations
### Requirements
* Simple and well laid out
* Visually appealing
* TU Dublin colour pallet
* Clean and modern looking
* Easy to report an issue in just a few clicks
* Responsive design is required (Mobile first) as users may be viewing the site on Mobile, Tablet or Desktop

### Expectations
* I expect to use the application on any size device without the experience effected
* I expect that when I report an issue I can see that it has been logged
* I expect to be able to report issues on multiple machines

## Staff Persona
These are the details of the staff interviewed. The staff members will all be teaching in TU Dublin, within the engineering department. There are three staff that fit this category, two lecturers and one technician. Unfortunately, I was only able to interview one lecturer.

| Title | Description 
| -- | --
| Name | Keith Colton
| Age | 40
| Position | Assistant Lecturer in Product Design
| Education | Postgraduate Diploma Third Level Learning and Teaching, MSc Sports Engineering


## Staff Goals
From the resulting interview, the site owner's goals have been defined:
* Create a machine with a short description
* Delete a machine when required
* Edit a machine's details when required 
* See any issues that have been reported
* Change the status of a machine with an issue
* Delete an issue when it has been rectified
* Clear navigation process
* Visually clear that it is a TU Dublin application


## Staff Stories
* As a site owner, I want to see any issues with machines that have been reported
* As a site owner, I want to delete an issue when it is rectified
* As a site owner, I want to provide a description of the machine for the user
* As a site owner, I want to provide an image of the machine for the user
* As a site owner, I want to manage the users

## Staff Requirements and Expectations
### Requirements
* A higher level account than a student
* Different sections in the login to manage the different tasks
* Create, Read, Update and Delete functionality
* Simple and well laid out
* Visually appealing
* TU Dublin colour pallet
* Clean and modern looking

### Expectations
* I expect to quickly manage users
* I expect to quickly manage machines
* I expect to quickly delete issues on machines when required
* I expect to know this application is associated with TU Dublin



## Strategy
### Strategy Outline
The items are graded in a 0 - 5 system in both importance and feasibility as per the grading system below.

&nbsp;

| | Score - 0 | Score - 3 | Score - 5 |
|--|--|--| -- |
| Importance | Unwise use of time to address | Efforts should be made to accommodate these | Efforts MUST be made to address these
| Feasibility | Unwise use of time to address| Efforts should be made to accommodate these | Efforts MUST be made to address these

&nbsp;

The outcome is calculated by combining the scores from the *Importance* and *Feasibility* ratings. This then gives a final strategy rating of what items and where to focus on.

| | Score - 0 | Score - 5 | Score - 10 |
|--|--|--| -- |
| Item Description | Not viable | Efforts should be made | Efforts MUST be made

&nbsp;

### Strategy Description

#### Student 

|Item Description | Importance Score | Feasibility Score | Outcome |
| --------------- | ----------| -----------| ----------|
| See what defects or issues have been reported | 5 | 5 | 10 |
| See what defects or issues I have reported | 5 | 5 | 10 |
| Clear display in a landing page | 5 | 5 | 10 |
| Clear navigation process | 5 | 5 | 10 |
| Ability to use the system on a mobile phone | 5 | 5 | 10 |


#### Site Owner

|Item Description | Importance Score | Feasibility Score | Outcome |
| --------------- | ----------| -----------| ----------|
| A higher level account than a standard user | 5 | 5 | 10 |
| See any problems with machines that have been reported | 5 | 5 | 10 |
| Manage the users | 5 | 5 | 10 |
| Delete an issue when it is rectified | 5 | 5 | 10 |
| Delete a machine| 5 | 5 | 10 |
| Edit a machine's details| 5 | 5 | 10 |
| Create a new machine with a description| 5 | 5 | 10 |
| Create a new machine with an image| 5 | 5 | 10 |
| TU Dublin colour pallet | 5 | 5 | 10 |


\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;


# Wireframes
Originally, the design was that the user immediately was bought to the login page, however, following the agile process, I received feedback from the client that this was no longer the case and they requested a landing page. This is the wireframe for this page.

![Landing Page](readme/docs/wireframes/landing-page-wireframe.png)


Login screens and edit information pages will be a very simple look with an image in the background and the form centred on all screen sizes.

![Forms](readme/docs/wireframes/form-wireframe.png)


The other screens, dashboard and current issues screens will display the items in a simple grid display to keep the pages uniform.

![Dashboard](readme/docs/wireframes/dashboard-wireframe.png)

The individual machine page will be simple and will hold the title, description, image and the report an issue form.

![Machine Page](readme/docs/wireframes/machine-page-wireframe.png)

The manage users page will be displayed as a simple table 

<!-- ADD WIREFRAME WHEN BALSAMIC LICENCE FOR 2022 IS RELEASED -->

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;


## Design Choices
Because this project is being created for TU Dublin, and all the user's requirements include the need for it to be within keeping of the existing designs, the following design choices will be based on this.

### Fonts
The font that TU Dublin currently uses is [Visuelt-Regular](https://www.colophon-foundry.org/typefaces/visuelt/ "Visuelt-Regular"), this, however, is a font that would have to be bought and not something that is going to happen with this project. Because of this, I have picked a font from [Google Fonts](https://fonts.google.com/ "Fonts") that is as close as I can get to keep the user experience as close as possible.

#### Content 
Using a font weight of 300, [Roboto](https://fonts.google.com/specimen/Roboto "Roboto")

#### Headings
Using a font-weight of 900 and styled to be uppercase, [Lato](https://fonts.google.com/specimen/Lato "Lato")


### Colours
The colours will be set variables within the CSS file using the names in the table below.

| Colour | HEX | Usage |
|--|--| --|
| Blue | #004C6C | Navigation bar, Footer, Cards, Tables |
| White | #FFFFFF | Site background, Text |
| Orange | #BF510D | Buttons, Links,  |
| Red | #A90F26 | Buttons, Links |
| Green | #005C48 | Buttons, Links |

To keep the user experience consistent, the colour red will be used for deletion, orange for editing and green for the creation or to cancel an action.

![Colour Pallet](readme/docs/designs/colour-pallet.png)

The colours all pass the [WebAIM](https://webaim.org/resources/contrastchecker/ "WebAIM") tests and the results can be seen below.

* [Blue](readme/docs/designs/contrast-checker-blue.png)
* [Orange](readme/docs/designs/contrast-checker-orange.png)
* [Red](readme/docs/designs/contrast-checker-red.png)
* [Green](readme/docs/designs/contrast-checker-green.png)



# Structure
## App Flow
The basic template views displays have been planned out using [Lucid](https://lucid.co/ "Lucid").

| Colour | Details|
|---|---|
| Blue | The user authentication process |
| Green | Visible to all users  |
| Yellow | Visible to only staff |

![App Flow](readme/docs/designs/site-structure.png)


## Data Schema
The data schema was created using [dbdiagram](https://dbdiagram.io/home "dbdiagram").

![Data Schema](readme/docs/designs/data-structure.png)


## Models

### Machine

| Name | Key | Type | Other Details |
| -- | -- | -- | -- |
| name | | CharField | Max length 50 and unique |
| slug | | SlugField | Max length 200 and unique|
| description | | TextField | |
| status || IntegerField | From STATUS and default of 1 (Working)|
| image ||CloudinaryField| Set default as 'placeholder' |

### Issues

| Name | Key | Type | Other Details |
| -- | -- | -- | -- |
| description | | TextField | |
| created_at || DateTimeField | Auto, now|
| rectified ||BooleanField| From ISSUE_RECTIFIEDand default of 0 (Not Rectified) |
| machine | FK from Machine || On delete cascade, set related_name |
| user | FK from User || On delete set to deleted_user, set null, set related_name |

### User

This will be initally built at the start of the app as an empty model, giving me the oportunity to adapt the Django User fields if required.

## Forms

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;


# Features

## Existing Features

### Navbar
The navbar is fully responsive and has been created to have different links available, depending on if the user is signed in or not.

While the user has not been authenticated or signed in to the application, on display are the Login and Signup links only. The university logo at this point acts as a link back to the landing page.
\
&nbsp;

![Desktop Unauthenticated Navbar](readme/docs/features/navbar/desktop-unauth-nav.png)

The same applies to the links for the mobile view, however, the styling is adjusted to be responsive. A hamburger menu is used to slide from the right side of the screen. The location of the hamburger in the top right corner of the screen is to suit the 90% majority of right-handed people.
\
&nbsp;

![Mobile Unauthenticated Navbar](readme/docs/features/navbar/mobile-unauth-nav.gif)

\
&nbsp;

For a basic user, once signed in the options on the navbar change to show:

* University name - *links to the dashboard*
* Dashboard - *links to the dashboard*
* Issues - *links to the issues page*
* Profile - *links to the edit profile page*
* Logout - *links to the logout page*
* Machine search - *opens machine name search bar*

The orange underline of the link shows the active page to the user, also a hover effect of changing colour on the text adds to the user experience. The search feature on the mobile layout moves in and leaves the hamburger on the edge, to improve user experience as the hamburger is more likely to be used more often.
\
&nbsp;
![Desktop Authenticated Basic Navbar](readme/docs/features/navbar/desktop-auth-nav-basic.png)

\
&nbsp;
![Mobile Authenticated Basic Navbar](readme/docs/features/navbar/mobile-auth-nav.png)

\
&nbsp;
![Mobile Authenticated Basic Navbar](readme/docs/features/navbar/mobile-auth-nav-links-basic.png)

For a staff member, once signed in the options on the navbar change to add extra dropdowns:

* University name - *links to the dashboard*
* Dashboard
    * View Machines - *links to the dashboard*
    * Create Machine - *links to the create a machine page*
* Issues - *links to the issues page*
* Profile
    * Edit Profile - *links to the edit profile page*
    * All Users - *links to the all users page*
* Logout - *links to the logout page*
* Machine search - *opens machine name search bar*

\
&nbsp;
![Desktop Authenticated Staff Navbar](readme/docs/features/navbar/desktop-auth-nav.png)

\
&nbsp;
![Mobile Authenticated Staff Navbar](readme/docs/features/navbar/mobile-auth-nav-links.png)

The search feature in the navbar is available to both staff and basic users. It searches the machine database based on the machine name and this is prompted through the placeholder text. There is also a fade in and out on this element to improve the experience.

\
&nbsp;
![Desktop Machine Search Navbar](readme/docs/features/navbar/desktop-auth-nav-search.png)

\
&nbsp;
![Mobile Machine Search Navbar](readme/docs/features/navbar/mobile-auth-nav-search.png)
\
&nbsp;

### Footer
The footer comprises two elements, the university name with auto increment copyright year and links to their social accounts. The layout changes slightly depending on screen size, the social links are moved to a fade in and out container on the smaller screen sizes. This container can fade out when either the user scrolls back up the screen, or if they click elsewhere in the body of the application.

\
&nbsp;
![Desktop Footer](readme/docs/features/footer/desktop-footer.png)

\
&nbsp;
![Mobile Footer](readme/docs/features/footer/mobile-footer.png)

\
&nbsp;
![Mobile Footer Social Links](readme/docs/features/footer/mobile-social-links.gif)
\
&nbsp;

### Messages
Messages are displayed for continual feedback to the user on their interactions and follow the same layout for both mobile and desktop designs. These interactions include:

* Sign in
* Logout
* Create a machine
* Update a machine
* Delete a machine
* Create an issue
* Delete an issue
* Edit profile
* Edit staff status of a user

\
&nbsp;
![Desktop Authentication Messages](readme/docs/features/messages/desktop-auth-messages-signin.png)

\
&nbsp;
![Mobile Authentication Messages](readme/docs/features/messages/mobile-auth-messages-signout.png)


\
&nbsp;
![Desktop Messages](readme/docs/features/messages/desktop-messages-create-machine.png)
\
&nbsp;

### Homepage
The home page is a simple set-up with two elements, the hero image and the information cards.

The hero image of a machine is fitting with the context of the project and the colour scheme also suits perfectly with the universities pallet. The text container is consistent with TU Dublin's site so it helps with the staff user story of needing to know that it is associated with the university.

![Hero Image](readme/docs/features/homepage/desktop-home-hero-image.png)

The information cards give a brief outline of the reasoning behind the development of the application. The information is helped by the use of icons and is also responsive by stacking on top of each other for smaller devices.

* Desktop

![Desktop Information Cards](readme/docs/features/homepage/desktop-home-info-cards.png)

* Mobile

![Mobile Information Cards](readme/docs/features/homepage/mobile-home-info-cards.png)

### Dashboard

The dashboard includes a personal welcome to the user and introduces them to the dashboard. The machines that are created by the staff members are displayed here with the view changing depending on authentication level. 

If the user is logged in as a staff member, the delete and edit buttons will be displayed if the user is a basic user, the card with the image and title are displayed. The image and the title also act as a link that navigates to the detailed view of the machine. 

If an issue has been raised on one of the machines, then a warning note also shows on the card. The cards are ordered firstly by if there are any issues reported, then in alphabetical order.

* Staff view

![Desktop Dashboard Staff](readme/docs/features/dashboard/desktop-dashboard.png)

* Basic User view

![Desktop Dashboard Basic](readme/docs/features/dashboard/desktop-dashboard-basic.png)

To keep the display of the machine cards compact, there is pagination built into the application. Only six items will be displayed on the screen at one time, if there is more the next and previous buttons will navigate to these items.

![Desktop Dashboard Pagination](readme/docs/features/dashboard/desktop-dashboard-pagination-next.png)

![Desktop Dashboard Pagination](readme/docs/features/dashboard/desktop-dashboard-pagination-prev.png)

There is also notification to the users if there are no machines currently created. This provides a short explination and a shortcut link to create a new machine.

![Desktop Dashboard No Machines](readme/docs/features/dashboard/desktop-dashboard-no-machines.png)

\
&nbsp;
### Machine Details

The machine details page shows the detailed description of the provided by a staff member when the machine was created. This is also where a user can create an issue using the *Report an Issue* button. This opens the form in the way of a modal with the machine name populated. The Cancel button closes the modal, and the submit button add the issue to the database and gives the user a message of confirmation.

\
&nbsp;
![Desktop Machine Detailed View](readme/docs/features/machine-details/desktop-detailed-view.png)

\
&nbsp;
![Desktop Machine Create issue](readme/docs/features/machine-details/desktop-create-issue.png)
\
&nbsp;

### Issues

At the very top of the issues page, there is a search bar, that works in the very same way as the machines name search, only it searches through the descriptions in the issues.

![Desktop Issues Search](readme/docs/features/issues/desktop-issues-search.png)

The issues page, like the dashboard, is made up of a series of issue cards order by the date that they were created on. These contain:

* The machine name
* The username of the user that created it
* Timestamp of when it was created
* Description left by the user
* For staff members only, the Delete button.
\
&nbsp;
* Staff view

![Desktop Issues Card](readme/docs/features/issues/desktop-issues-card-staff.png)

* Basic view

![Desktop Issues Card](readme/docs/features/issues/desktop-issues-card-basic.png)

Only visible to staff members is the delete button when it is clicked, a defensive model pops up to ensure that the user is sure that they would like to delete the issue, on the confirmation, the issue is deleted from the database and a message is relayed to the user.

![Desktop Issues Delete Model](readme/docs/features/issues/desktop-issues-delete-model.png)

On deletion of the last issue or, if there have been none created yet, there is a prompt to the user so they are aware of this.

![Desktop No Issues](readme/docs/features/issues/desktop-issues-no-issues.png)

### All Users
This page is only available to the staff users of the application. At the top of the page, there is a search bar that can be used to search for the user's usernames, working in the same way as the previously detailed searches in the application. The main content consists of a table populated with a full list of all registered users and displays some of their details:

* Username
* First name
* Last name
* Staff status

![Desktop All Users](readme/docs/features/profile/desktop-all-users.png)


Each user also has an edit button associated with it and a delete button. The edit button allows a staff member to give another user full accessibility to the application. On clicking update, a message is displayed showing that the staff status has been changed for that particular user.

![Desktop Edit Staff Status](readme/docs/features/profile/desktop-all-users-edit-staff-status.png)

The delete button opens up a model for a defensive confirmation that this is the action wanted to be carried out. On deletion, the user is removed from the database.

![Desktop Edit Staff Status](readme/docs/features/profile/desktop-all-users-delete-model.png)

### Edit Profile
The edit profile page is available to all user levels. This page gives the user the ability to adjust their details:

* Username
* Email
* First name
* Last name

The update button updates the database and gives the user a message to confirm the profile was updated, and the cancel button returns to the dashboard.

![Desktop Edit Profile](readme/docs/features/profile/desktop-edit-profile.png)

### Authentication

The authentication process for the application has three parts.

* Sign Up
* Sign In
* Log out

#### Sign Up
The signup process requests three required fields from the user:

* Username
* Password
* Password confirmation

![Desktop Sign Up Form](readme/docs/features/authentication/desktop-sign-up.png)

If the user enters a username that already exists, or the two password fields do not match, then error messages are prompted to the user.

![Desktop Sign Up Messages](readme/docs/features/authentication/desktop-sign-up-messages.png)

If all the fields are correctly populated and the Sign-Up button is clicked the user is navigated to the dashboard and a message is displayed to tell the user that they are successfully signed in. If the user has already registered and is looking to sign in then there is a handy link to the correct page in the text above the form.

### Sign In
The sign-in form requires only two fields to be entered. 

* Username
* Password

![Desktop Sign In Form](readme/docs/features/authentication/desktop-sign-in.png)


Like the signup form, there are messages displayed if incorrect or non-matching data is entered. And a link to the signup page if the user has not already done so. The sign-in button, with correct credentials, directs the user to the dashboard with a successfully logged in message.

![Desktop Sign In Messages](readme/docs/features/authentication/desktop-sign-in-messages.png)

### Log out

This is the simplest of the three authentication form in the application. a simple choice of yes or no if the user would like to sign out. The yes button directs the user to the homepage with a message letting them know they have successfully logged out, and the no button directs the user back to the dashboard page.

![Desktop Sign Out](readme/docs/features/authentication/desktop-sign-out.png)

## Buttons
The buttons on the application, for consistency, have the same design, with the only difference being the colours.

* Green is for confirming an update or creating

![Green Button](readme/docs/features/buttons/button-green.png)

* Red is for deletion

![Red Button](readme/docs/features/buttons/button-red.png)

* Orange is for editing or cancelling an action

![Orange Button](readme/docs/features/buttons/button-orange.png)

All buttons also have the same hover effect to keep the user experience consistant.

![Button Hover](readme/docs/features/buttons/button-hover.gif)

## Features to be Implemented


\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# Technologies used

## Languages
| Languages | Description | Link |
|--|--|--|
|HTML|[HTML](https://en.wikipedia.org/wiki/HTML5 "HTML") | for the structure of the site
|CSS|[CSS](https://en.wikipedia.org/wiki/CSS "CSS") | for the design of the site
|JavaScript|[JavaScript](https://en.wikipedia.org/wiki/JavaScript "JS") | for the design of the site
|jQuery|[jQuery](https://jquery.com/ "jQuery") | for animations in the site
|Python|[Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python") | for the backend interactions
|Markdown|[Markdown](https://en.wikipedia.org/wiki/Markdown) | for the content in my README file

## Libraries and Frameworks
| Libraries / Frameworks | Description | Link |
|--|--|--|
|Django|Database Driven Framework| [django](https://en.wikipedia.org/wiki/Django_(web_framework) "django")|
|gunicorn|HTTP Interface Server|[gunicorn](https://en.wikipedia.org/wiki/Gunicorn "gunicorn")|
|psycopg2| Database adaptor | [psycopg2](https://wiki.postgresql.org/wiki/Psycopg "psycogg2")
|cloudinary |Image management|[cloudinary](https://cloudinary.com/ "cloudinary")|
|django auth|User authentication|[auth](https://docs.djangoproject.com/en/3.2/topics/auth/ "auth")|
|django widgit tweaks|Formats forms||


## Tools
| Tools | Description | Link |
|--|--|--|
| Google Fonts| Fonts |[Google Fonts](https://fonts.google.com/ "Fonts")|
| WebAIM| Colour contrast checks |[WebAIM](https://webaim.org/resources/contrastchecker/ "WebAIM")|
| Lucid | Site structure design | [Lucid](https://lucid.co/ "Lucid")
| dbdiagram | Data schema design | [dbdiagram](https://dbdiagram.io/home "dbdiagram")
| coolors|Colour pallet| [coolors](https://coolors.co/ "coolors")|
| GitPod | Development environment |[Gitpod](https://www.gitpod.io/ "Gitpod")
| Balsamic | Wireframes |[Balsamic](https://balsamiq.com/wireframes/ "Balsamic")
| Bootstrap | Responsive design |[Bootstrap](https://getbootstrap.com "Bootstrap")
| Font Awesome | Icons |[Font Awesome library](https://fontawesome.com/ "Font Awesome")
| Unsplash | Images |[Unsplash](https://unsplash.com/ "Unsplash")
| coverage | Testing | [Coverage](https://coverage.readthedocs.io/en/6.3.1/ "Coverage")
| WAVE | Accessibility Testing | [WAVE](https://wave.webaim.org/ "Wave")
| W3C | Markup Validation | [W3C Markup Validation Service](https://validator.w3.org/ "W3C")
| W3C | CSS Validation | [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/ "W3C")
| PEP8 | Python Validation | [PEP8](http://pep8online.com/ "PEP8")
| JSHint | JavaScript and JQuery Validation | [JSHint](https://jshint.com/ "JSHint")


# Testing

## Accessibility

With accessibility included as a user goal, I have tested the pages of the application using [WAVE](https://wave.webaim.org/ "Wave") to ensure there are no errors. The results can be seen by following the links below. Each test shows that there are 2 contrast errors, these errors are where WAVE is picking up screen reader only spans and suggesting that they have a poor ratio between the back and foreground colours. These two elements are not visible to the user as they hold the bootstrap class of *sr-only*, so the errors here can be ignored.

* [Homepage accessibility results](readme/docs/accessibility/homepage-accessibility-check.png "Homepage")

* [Dashboard accessibility results](readme/docs/accessibility/dashboard-accessibility-check.png "Dashboard")

* [Individual Machine accessibility results](readme/docs/accessibility/individual-machine-accessibility-check.png "Individual Machine")

* [Create Machine accessibility results](readme/docs/accessibility/create-machine-accessibility-check.png "Create Machine")

* [Edit Machine accessibility results](readme/docs/accessibility/edit-machine-accessibility-check.png "Edit Machine")

* [All Users accessibility results](readme/docs/accessibility/all-users-accessibility-check.png "All Users")

* [Issues accessibility results](readme/docs/accessibility/issues-accessibility-check.png "Issues Machine")



&nbsp;

| Age | Tech Experience | Task Completed | Comments/ Improvements
| --- | ----------      | -------------  | --------


&nbsp;



### UX Testing

| Requirements & Expectations | Implemented | Tested | Comments
| ------------ | ----------- | ------ | --------


&nbsp;

&nbsp;

| User Goals | Implemented | Tested | Comments
| ------------ | ----------- | ------ | --------


&nbsp;

&nbsp;

| Site Owners Goals | Implemented | Tested | Comments
| ------------ | ----------- | ------ | --------


\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Code Validation

### HTML
The HTML code within the application has been validated by [W3C Markup Validation Service](https://validator.w3.org/ "W3C"). Pages were put through the validator seperatly and the results can be seen below.

* [Homepage HTML validation results](readme/docs/validation/html/homepage-markup-validation.png "Homepage")

* [Dashboard HTML validation results](readme/docs/validation/html/dashboard-markup-validation.png "Dashboard")

* [Individual Machine HTML validation results](readme/docs/validation/html/individual-machine-validation/html-check.png "Individual Machine")

* [Create Machine HTML validation results](readme/docs/validation/html/create-machine-markup-validation.png "Create Machine")

* [Edit Machine HTML validation results](readme/docs/validation/html/edit-machine-markup-validation.png "Edit Machine")

* [All Users HTML validation results](readme/docs/validation/html/all-users-markup-validation.png "All Users")

* [Issues HTML validation results](readme/docs/validation/html/issues-markup-validation.png "Issues Machine")

* [Signup HTML validation results](readme/docs/validation/html/signup-markup-validation.png "Sign up")

* [Sign in HTML validation results](readme/docs/validation/html/signin-markup-validation.png "Sign in Machine")

* [Log out HTML validation results](readme/docs/validation/html/logout-markup-validation.png "Log out Machine")


\
&nbsp; 


## Bugs



## Unfixed Bugs



\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# Deployment

The live link to the application can be found [here](https://issue-reporting-system.herokuapp.com/ "Link")

### Cloudinary
* Visit Cloudinary by following this [link](https://cloudinary.com/ "Link")
* Click on the *Sign Up For Free* button
* When the account is created, you should see the *API Environment variable*, we will need this for a later process.

### Github
* Visit Github by following this [link](https://github.com/ "Link")
* Create an account or log in

#### Forking
* Navigate to the repository by following this [link](https://github.com/sam-timmins/machine-issue-reporting-system "Link")
* Click on the *Fork* button in the top right of the screen


#### Github Desktop
* Navigate to the repository by following this [link](https://github.com/sam-timmins/machine-issue-reporting-system "Link")
* Click on the *Code* button above the file list
* Select *Open with GitHub Desktop*


### Set up your Workspace
When you have your version of the original repository, 
* In the terminal run
```
pip3 install -r requirements.txt
```
* In the root directory create a file called **env.py** and add the following content, the content of these, must match the Config Vars in the Heroku deployment section

```py
import os

os.environ['DATABASE_URL'] = "FROM HEROKU DEPLOYMENT SECTION, DATABASE_URL CONFIG VAR"
os.environ['SECRET_KEY'] = "FROM HEROKU DEPLOYMENT SECTION SECRET_KEY CONFIG VAR"
os.environ['CLOUDINARY_URL'] = "API ENVIRONMENT VARIABLE REMOVE 'CLOUDINARY_URL=' FROM BEGINING"
os.environ['DEVELOP'] = '1'


os.environ['UNIVERSITY_NAME'] = "ADD CONTENT HERE"
os.environ['FACEBOOK_LINK'] = "ADD CONTENT HERE"
os.environ['INSTAGRAM_LINK'] = "ADD CONTENT HERE"
os.environ['TWITTER_LINK'] = "ADD CONTENT HERE"
os.environ['MACHINE_CARDS_CURRENT_ISSUE_TEXT'] = "ADD CONTENT HERE"
os.environ['NO_ISSUES_MODAL_TITLE'] = "ADD CONTENT HERE"
os.environ['NO_ISSUES_TEXT'] = "ADD CONTENT HERE"
```

### Deployment via Heroku
* Visit [heroku.com](https://www.heroku.com/home "Heroku")
* Create a new account or sign in
* From the dashboard, select **New** and then **Create new app**
* Enter an individual app name into the text box, select a region from the dropdown and then press **Create app**
* A Heroku app has now been created and the **Deploy** tab is opened. 
* Open the *Resources* tab and in the search bar for *Add-ons* type *Postgres*
* Select *Heroku Postgres*, on the popup, ensure the dropdown is set to *Hobby Dev - Free* and then *Submit Order Form*
* Open the *Settings* tab and then click on the *Reveal Config Vars* button and the database_url should be populated.
* Fill out the rest of the config vars with the content of the table below by filling out the *Key* and *Value* and clicking on *Add* for each entry 

| Key | Value |
| --- | --- |
| CLOUDINARY_URL | URL from Cloudinary
| SECRET_KEY | Secret Key generated from [here](https://miniwebtool.com/django-secret-key-generator/ "Shhh...")
| UNIVERSITY_NAME | Your university name
| FACEBOOK_LINK | URL for facebook page
| INSTAGRAM_LINK | URL for instagram page
| TWITTER_LINK | URL for twitter page
| MACHINE_CARDS_CURRENT_ISSUE_TEXT | 'Current Issues'
| NO_ISSUES_MODAL_TITLE | 'No Issues'
| NO_ISSUES_TEXT | 'There are currently no issues outstanding'


* In the buildpacks section of the settings tab, click on **Add Buildpack**, select **python** and then save changes
* Open the **Deploy** tab
* In the deployment method section, select **GitHub** and confirm the connection.
* Enter the repo-name into the text box and click **Search**. When the correct repo appears below, click **Connect**
* In the Automatic deploys section, click **Enable Automatic Deploys**. This updates every time GitHub code is pushed
* To complete the process click on the **Deploy Brach** button in the Manual deploy section, this will take a few seconds to complete while Heroku builds the app
* A message will appear informing you that the app was successfully deployed and a **View** button will bring you to the live site


\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# Credits



\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;