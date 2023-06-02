# Currency Converter - *Real time currency conversion*

[View code here](https://github.com/belovedpearl/Currency_Converter)

![Responsiveness](assets/images/siteRepresentation/screen_responsive.webp)

[View site responsiveness here](https://ui.dev/amiresponsive?url=https://belovedpearl.github.io/Historic_Center_Quiz_PP2/)


---

**Table of Contents:**
---

 * [Project Description](#project-description)
    * [Site Owners Goal](#site-owners-goal)
    * [Users Goal](#users-goal)
   
* [WireFrames](#wireframes)
     
* [Features](#features)
    * [Existing Features](#existing-features)
        *[Opening Section](#opening-section)
        *[Username Section](#username-section)
        *[Registration Section](#registration-section)
        *[Sign-up Section](#sign-up-section)
        *[Choice Section](#choice-section)
    
* [Future features](#future-features)
* [Design Choices](#design-choices)
* [Accessibility](#accessibility)

* [Technology, Frameworks and Programs](#technology-frameworks-and-programs)
     * [languages](#languages)
     * [Frameworks and Programs](#frameworks-and-programs)

* [Bugs](#bugs)
     * [Fixed Bugs](#fixed-bugs)
     * [Unfixed Bugs](#unfixed-bugs)

* [Deployment](#deployment)
* [Tools](#tools)
* [Testing](#testing)
     * [Validator Testing](#validator-testing)
         * [Pep8](#pep8)
         * [Local Terminal](#local-terminal)
         * [Heroku Terminal](#heroku-terminal)
     * [Functional Testing](#functional-testing)
* [Credit](#credits)
* [Acknowledgement](#acknowledgement)
 















---

 ## Project Description

---

MyCurrency as named is designed to provide real time currency conversion rate to its users.
It is designed to be an handy tool for users to convert the value of one currency to another . It also provides a convenient and efficient way to perform currency conversions for various needs, it can also be used in financial plannings especially when it involves other currencies.
It also seek to educate its users by providing a list of countries and their currencies. Through it, users are able to build up understanding about different currencies that exists and thier symbols. 

 ![View Live Site Here](https://git.heroku.com/mycurrency.git)
 
---

## Site Owners Goal

---

   * To educate its users on currencies and countries around the world.
   * Provide real time currency exchange rate.
   * Provide access to currency conversion with ease.
   * Register its users.
   * First time users needs to sign up to use.

   
---

## Users Goal

---

   * To easily navigate and understand the application.
   * Be able to view the list and perform desired conversion.
   * To be able to view the exchange rate.


---


## Wireframes

---

Lucid Chart was used in planning the project. Below is a representation of my thought on the project. 
![Project Plan](assets/images/project_draw.webp)


---

## Features

---

### Existing Features

Features on the application include:
#### Opening Section:
This consist of the title and a caption introducung the user to what the program does.


#### Username Section:
It takes in the username and opens up the program if the user is registered

#### Registration Check:
Users need to register to use this program.This section checks if the username is present on the worksheet attached.

#### Sign-up Section:
This section allows new user to register their name to access the program.

#### Choice Section:
Users are prompted to choose their desired path of operation to achieve a desired result.


---

## Future Features

---

 * I will add audio to improve user experience of the game.

 * Add an autosave feature.

 * Features that allow users to choose some custom settings to personalize the game.

 * Randomize the position of each option.

 * Add a reward section where users can choose a gift based on the scores they get.

 * Connect with social media account of users to provide a means to share the game scores online.

---

## Design Choices

---


* I have added red color to fonts to make some sections stand out to user.

* Blue color was also added to some statements to improve its appearance.


### Font

Standard terminal font is used to present the project.


--- 

## Accessibility

---

This project is a terminal based program, users are prompted for input to move through the application.



---

## Technology, Frameworks and Programs

---

### Language

* PYTHON

---

### Frameworks and Programs


* LucidChart
    * Used to sketch my thought in planing the project


* Github
    * To store written code


* Gitpod
    * This is the IDE used to write the code from where i can push to github.

* Heroku
    * This was used to deploy the web-application.

---

## Bugs

---

### Fixed Bugs

* Rows not appendeing in the worksheet

    *Converting my data to list before appending helped fixed this


* Heroku not recognising file containing my key.

    * 

### Unfixed Bugs
 * To my current understanding, there is no unfixed bug

---

## Deployment

---

### GitHub Pages

* The project was deployed using heroku.

The following illustrate the steps I took to deploy my website;
Fork or clone this repository in the following steps:

### How to Fork

  * Login to GitHub and locate the [GitHub Repository](https://github.com/belovedpearl/Currency_Converter).

  * At the top of the repository just above the **"Settings"** button on the menu, locate the **"Fork"** button.

  * Once **clicked**, you should have a copy of the original repository in your own account.

### To deploy
  * Sign up to create an account with heroku.
  * Click on create a new Heroku app.
  * Add Config Var by clicking on reveal config vars 
  * Set the build packs to Python and NodeJs in exact order.
  * Link the Heroku app to the repository.
  * Click on **Deploy**
  * A few minutes later, after refreshing the page, there will automatically be an update containing the **"live site link"**.

The live link can be found [here](https://git.heroku.com/mycurrency.git/).



---

## Tools

---
  
  *  [Free Currency Converter API](https://free.currencyconverterapi.com/)
  *  [Free Currency Converter API documentation](https://www.currencyconverterapi.com/docs)
  *  [Title Art](https://patorjk.com/)
  *  [Google Sheets API](https://console.cloud.google.com/)
  *  [Google Sheet](https://docs.google.com/spreadsheets/)
  *  [Black Vercel](https://black.vercel.app)
  *  [Python Checker](https://pythonchecker.com/)
  
  *  [Font Awesome](https://fontawesome.com/)

  *  [Fonts](https://fonts.google.com/) 

  *  [CSS Transition](https:youtu.be/EVze4Cq-dZ8)

  *  [Prettier](https://prettier.io/playground/)

  * [Favicon Generator](https://favicon.io/favicon-generator/)


---

## Testing

---

### Validator Testing

#### PEP8
* No errors  were found when passed through the official [W3C Validator check](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbelovedpearl.github.io%2FHistoric_Center_Quiz_PP2%2F)


![Pep8 Validation](assets/images/siteTest/htmlVal.webp)



#### Local Terminal

 * I have written the program and ran it several times on my terminal and it all work fine as desired.


 ![Local Terminal](assets/images/siteTest/cssVal.webp)

### Heroku Terminal
 * I have passed the code through [JSHint](https://jshint.com/)


 ![Heroku Terminal](assets/images/siteTest/jshint.webp)

 I have also tested the code using python checker.

 ![Python Checker](assets/images/python-checker.webp)
 


### Functional Testing

 Functional testing performed for every action within the website. If the behavior is the same as the expected behavior, it will be marked with P for pass, if not F for fail. 

  
| Action (CLICK) | Expected Behavior   | Actual Behavior |
| :---: | :---: | :---: |
| Username |  Takes in the username  | If user is registered, opens up the program   |
|  Press 1 | List the available currncies and symbols  | P   |
| Press 2 | Opens up the conversion section   | P   |
| Press 3 | Gets the exchange rate  of specified currencies printed  | P   |
|Press q | Exist the program   | P   |
|Sign-up section  | Adds the new user username to the worksheet  | P |


---

## Credits

* [Importing your own module properly](https://youtu.be/GxCXiSk6no)

* [Python style guide](https://google.github.io/styleguide/pyguide.html)

* [ReadMe Table Inspiration](https://github.com/belovedpearl/Green_Space-PP1/blob/main/README.md)

* [Code institute's template](https://github.com/Code-Institute-Org/gitpod-full-template)

* [Typewriter effect](https://youtu.be/2h8e0tXHfk0)

* [Clear screen function](https://www.101computing.net/python-typing-text-effect/).

* [Import your own modules](https://youtu.be/GxCXiSkm6no)

* [Add color to art](https://youtu.be/u4QMAloo4i0)

* [W3Schools](https://www.w3schools.com/), [Stack overflow](https://www.slackoverflow.com/) & [Mdn wed docs](https://developer.mozilla.org/en-US/) - Visited several times to learn different syntax used in the code.


---

## Acknowledgement

* I will like to thank **My Husband** for his support and understanding during the project, for all encouragement and even getting me on this programme.

* Much love to my **Children** for understanding and encouraging me through this project buildup.

* Special thanks to [Adam Boley](https://github.com/AdamBoley/) for his support during the build up of the project.

* A big thank you to my Mentor, **Sandeep Aggarwal**  for the support and through enlightment he provided during the buildup of this project.

* ReadMe layout inspiration from other Code Institute students from #peer-code-review forum and https://github.com/kera-cudmore/readme-examples/blob/main/milestone1-readme.md#development

* Thank you to everyone at **Code Institute** for helping us learn.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
