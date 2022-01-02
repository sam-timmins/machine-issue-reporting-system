# Machienary Issue Reporting System

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
The landing page, login screens and edit information pages will be a very simple look with an image in the background and the form centred on all screen sizes.

![Homepage and Forms](readme/docs/wireframes/form-wireframe.png)


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


### Fonts


#### Content 


#### Headings



### Colours

| Colour | HEX | Usage |
|--|--| --|


# Structure

## Data Schema



## Models

| Name | Key | Type | Other Details |
| -- | -- | -- | -- |



## Forms

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;


# Features

## Existing Features


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


## Libraries and Frameworks
| Libraries / Frameworks | Description | Link |
|--|--|--|


## Tools
| Tools | Description | Link |
|--|--|--|


# Testing



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

<!-- ADD LIVE LINK HERE -->


### Set up your Workspace

### Deployment via Heroku



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