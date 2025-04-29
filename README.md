# World of Games post site

You want to buy video games and are from Austria? Give our site a chance!

![World of Games image](/docs/world-of-games.png)

World of Games is a fictional B2C e-commerce shop where a user can buy video games. Digital and physical games can be bought and users can leave reviews beneath each product.
The user can get signed up, subscribe to a newsletter or get in contact with the site owner if he wants to. 

The website has a user friendly interface and is responsive for different screen sizes.

Visit World of Games [here](https://world-of-games-edc70ca11f8f.herokuapp.com/)!!




## Content
- [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)
    - [User Stories](#user-stories)
        - [Developer/Site Owner/Superuser](#developersite-ownersuperuser-stories)
        - [First Time User](#first-time-user)
        - [Returning User](#returning-user)
        - [Frequent User](#frequent-user)
- [Design](#design)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Color Scheme](#color-scheme)
- [Wireframes](#wireframes)
- [Relationship Models](#relationship-models)
- [Agil Methology](#agil-methology)
- [Features](#features)
    - [Common Features](#common-features)
      - [Navbar](#navbar)
      - [Footer](#footer)
    - [Main Page](#main-page)
      - [Shop access button](#shop-access-button)
    - [Product Page](#product-page)
        - [All Product View](#all-product-view)
        - [Product Detail View](#product-detail-view)
        - [Sorting](#sorting)
        - [Superuser Product Managment](#superuser-product-managment)
    - [Shopping Bag Page](#shopping-bag-page)
    - [Checkout Page](#checkout-page)
    - [Profile Page](#profile-page)
    - [About us Page](#about-us-page)
    - [FAQ Page](#faq-page)
    - [Newsletter Page](#newsletter-page)
    - [Signup Page](#signup-page)
    - [Sign in Page](#login-page)
    - [Logout Page](#logout-page)
    - [404 Page](#404-page)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Programs Used - Frameworks - Libraries - Databases](#programs-used---frameworks---libraries---databases)
- [Web Marketing](#web-marketing)
    - [SEO Keywords](#seo-keywords)
    - [Facebook Buisness Page](#facebook-buisness-page)
    - [Robots.txt](#robotstxt)
    - [sitemap.xml](#sitemapxml)
    - [Newsletter](#newsletter)
    - [Marketing Plan](#marketing-plan)
- [Deployment](#deployment)
    - [PostgreSQL](#postgresql)
    - [Github](#github-setup)
    - [Heroku Deployment](#heroku-deployment)
    - [Amazon Web Services](#amazon-web-services)
    - [Heroku set up](#heroku-set-up)
    - [Running the project locally](#running-the-project-locally)
- [Credits](#credits)
    - [Code](#code)
    - [Similar students projects](#similar-students-projects)
    - [Resources Used](#resources-used)
    - [Media](#media)
- [Fixed Bugs](#fixed-bugs)
- [Future Content](#future-content)
- [Acknowledgments](#acknowledgments)


## Site Owner Goals
- to create a fully working e-commerce page
- to provide the user with a website where they can buy games
- to provide the user with the ability to sort and search games
- to provide the user with the ability to leave a review
- to provide the user with the ability to create a profile for an easier ordering process
- to provide the user with the ability to read through FAQs
- to provide the user with the ability to subscribe to a newsletter
- to provide the user with the ability to get in contact with owners 


## User Experience
### User Stories

#### Developer/Site Owner/Superuser Stories
- As a developer I can link VS code with my GitHub repository and install dependencies so that I can work on my project.
- As a Developer I can set up necessary base items so that I can run the server to check the page in preview. 
- As a superuser I can have the ability to update/add/delete products on the website, add extra security on CRUD pages so that only I can work on the products inventory and work on pages outside of the admin panel.
- As an admin/user I can have access to the admin panel so that I can control all the content and the user base.
- As a site owner I want the website to be public so that real users can use it.
- As a site owner I can document my project so that other developers and I can understand and further work on the project. 
- As a site owner I can document all different types of tests so that the passing criteria of the website are in one file.

#### First Time User
- As a site user I can find the site content's links instinctively so that I can easily navigate through to find contents.
- As a site user I can search for a product by name so that I can find a specific product.
- As a site user I can view a list of products and select products from this list so that I can see an overview of things I might buy and select them.
- As a site user I can see categories and special offers so that I can see special offers, save money or look through the categories.
- As a site user I can see product in great detail and put item in shoppingbag so that am informed about the product and can buy it.
- As a site user I can check my order before finally submitting payment so that I can see if everything is there that I want.
- As a site user I can checkout with my order so that I can finish my order and receive the products I want.
- As a site user I can add products to the shopping bag in various sizes or game types so that I can buy the amount and game types I want.
- As a site user I want to see common questions on a FAQ page so that I can get a better knowledge of common things.
- As a site user I can get an email after placing an order so that I see all the information about it.



#### Returning User
- As a site user I want to read about the store and get in contact with the store owner so that I ask things that might not have been answered in FAQs
- As a site user I can see my previous orders and delivery information so that I can use them for future orders and update delivery information.
- As a site user I can sort the products to my desire so that I can find the best-rated or best-priced products
- As a site user I can add my own review below a product so that I can give my opinion.

#### Frequent User
- As a site user I can see my previous orders and delivery information so that I can use them for future orders and update delivery information.
- As a user I can subscribe to a newsletter so that I am being updated about new products.


## Design
### Typography

[Google Fonts](https://fonts.google.com/) was used for the following font:
- ![Lato Font](/docs/readme-images/lato.png) Lato font was picked because I like the look of it, it is simple and easy to read.

### Imagery

All Images were taken from different websites. I give credit to them in the [credits](#credits) section.

### Color Scheme

* I have used `#FFFFFF` and `#000000` as the primary color for text used on the site.
* I have used `#AAB7CA` as the line underneath headings and as for the coloring of category and the star rating.
* I have used `#EA0000` as the eyecather on the Homepage for the Game Now button.
* I have used `#FFC107` as the color for my borders and as the color for the hover option.

![World of Games site color palette](/docs/readme-images/coolors-palette.png)

## Wireframes
<details>

<summary>Desktop Wireframe</summary>
Index Page:

![Wireframe Index Page](/docs/wireframes-images/index-page-desktop.png)

Products Page:

![Wireframe Products Page](/docs/wireframes-images/products-page-desktop.png)

Product Detail Page:

![Wireframe Product Detail Page](/docs/wireframes-images/product-detail-page-desktop.png)

Shoppingbag Page:

![Wireframe Shoppingbag Page](/docs/wireframes-images/shoppingbag-page-desktop.png)

Checkout Page:

![Wireframe Checkout Page](/docs/wireframes-images/checkout-page-desktop.png)

Profile Page:

![Wireframe Profile Page](/docs/wireframes-images/my-profile-page-desktop.png)

About us Page:

![Wireframe About us Page](/docs/wireframes-images/about_us-page-desktop.png)

FAQ Page:

![Wireframe FAQ Page](/docs/wireframes-images/faq-page-desktop.png)

Newsletter Page:

![Wireframe Newsletter Page](/docs/wireframes-images/newsletter-page-desktop.png)

Add Product Page:

![Wireframe Add Product Page](/docs/wireframes-images/add-product-page-desktop.png)

Edit Product Page:

![Wireframe Edit Product Page](/docs/wireframes-images/edit-product-page-desktop.png)

Sign in Page:

![Wireframe Sign in Page](/docs/wireframes-images/sign-in-page-desktop.png)

Sign up Page:

![Wireframe Register Page](/docs/wireframes-images/sign-up-page-desktop.png)

Sign out Page:

![Wireframe Sign out Page](/docs/wireframes-images/logout-page-desktop.png)

</details>

<details>

<summary>Mobile Wireframe</summary>
Index Page:

![Wireframe Index Page](/docs/wireframes-images/index-page-mobile.png)

Products Page:

![Wireframe Products Page](/docs/wireframes-images/products-page-mobile.png)

Product Detail Page:

![Wireframe Product Detail Page](/docs/wireframes-images/product-detail-page-mobile.png)

Shoppingbag Page:

![Wireframe Shoppingbag Page](/docs/wireframes-images/shoppingbag-page-mobile.png)

Checkout Page:

![Wireframe Checkout Page](/docs/wireframes-images/checkout-page-mobile.png)

Profile Page:

![Wireframe Profile Page](/docs/wireframes-images/my-profile-page-mobile.png)

About us Page:

![Wireframe About us Page](/docs/wireframes-images/about-us-page-mobile.png)

FAQ Page:

![Wireframe FAQ Page](/docs/wireframes-images/faq-page-mobile.png)

Newsletter Page:

![Wireframe Newsletter Page](/docs/wireframes-images/newsletter-page-mobile.png)

Add Product Page:

![Wireframe Add Product Page](/docs/wireframes-images/add-product-page-mobile.png)

Edit Product Page:

![Wireframe Edit Product Page](/docs/wireframes-images/edit-product-page-mobile.png)

Sign in Page:

![Wireframe Sign in Page](/docs/wireframes-images/sign-in-page-mobile.png)

Sign up Page:

![Wireframe Register Page](/docs/wireframes-images/sign-up-page-mobile.png)

Sign out Page:

![Wireframe Sign out Page](/docs/wireframes-images/logout-page-mobile.png)

</details>

## Relationship Models

I used [LucidChart](https://www.lucidchart.com/) to create a relationship diagram of my models.

<details>
<summary>Website Navigation Diagram</summary>

![Website Navigation Diagram](/docs/readme-images/website-navigation.png)

</details>

<details>
<summary>First ERD Diagram</summary>

![ERD draft](/docs/readme-images/erd-draft.png)

</details>

<details>
<summary>Final ERD Diagram</summary>

![ERD final](/docs/readme-images/erd-final.png)

</details>


- This diagram shows the relationships in my models and beetween one another.
- I used the [Django AllAuth](https://docs.allauth.org/en/latest/) library for user authentification, which created my user model for me.

## Agil Methology

This project was designed with the Agile methodology, using the Project Board and Issues sections in GitHub.

>[Project Board](https://github.com/users/FlorianS4/projects/10)

Because I forgot to update my project board with every sprint I finished taking a look at my commits is a better way of seeing how I implemented agile methology.
I created each app and functionality one after another. One can see from later commits, that through additional external testing (mentor and test users) and through my creating my TESTING.md commits outside of sprints occured.
I also created a Sprint to-do list on a notebook, but since it is in German and written on top of one another, I decided to not include an image after I tried if my test users could read something from it.

## Features
### Common Features

#### Favicon

![Favicon](/docs/readme-images/favicon-screenshot.png)

#### Navbar

![Navbar desktop view](/docs/readme-images/navbar-screenshot.png)

- The navbar gives the user menu options to be redirected to. Depending if they are already logged in or not the Account dropdown has different options.

![Navbar mobile view](/docs/readme-images/navbar-mobile1-screenshot.png)

- The navbar on mobile view has a drop down menu for all options.

![Navbar mobile view dropdown](/docs/readme-images/navbar-mobile2-screenshot.png)

#### Footer

![Footer view](/docs/readme-images/footer-screenshot.png)

- The footer has a link to my GitHub as well as links to popular social media sites in a different tab.

### Main Page
#### World of Games Home Page
 
![World of Games desktop view](/docs/readme-images/home-screenshot-desktop.png)

![World of Games mobile view](/docs/readme-images/home-screenshot-mobile.png)

#### Shop access button

![Game now button for quick shop access](/docs/readme-images/game-now-screenshot.png)

- A button to be redirected to the products in an eye catching colour.

### Product Page

#### All Product View

![Product Page View](/docs/readme-images/products-screenshot.png)

- The user can see all the games which are beeing sold on the products pages.

#### Product Detail View

![Product Detail Page View](/docs/readme-images/productdetail-zoomed-screenshot.png)

- If the user wants to buy the game he can decide if he wants a physical version with a CD, or a digital version with a code he can play on popular game launchers (steam, Epic, etc.). 
- The user can choose the quantity of products he wants to buy.

![Product detail select View](/docs/readme-images/product-details-screenshot.png)

#### Sorting

- The user can always sort the products in whichever product list according to a selected list of sorting abilities.

![Product Sorting View](/docs/readme-images/sorting-screenshot.png)

#### Superuser Product Managment

- The Superuser/Admin has more function then the normal user in line with CRUD functionality.
- He can edit and delete products from the products list, but also from the product detail page.

![Superuser products view](/docs/readme-images/products-superuser-screenshot.png)

![Superuser product detail view](/docs/readme-images/product-edit-delete-superuser-screenshot.png)

- The Superuser/Admin is the only one who can add products to the store from the account dropdown.

![Products Add view](/docs/readme-images/product-management-screenshot.png)

![Products Edit view](/docs/readme-images/edit-product-management-screenshot.png)

#### Review Section

- A logged in user can leave a review on the product detaul page.
- A user can edit and delete his own reviews.

![Review logged in view](/docs/readme-images/reviews-screenshot.png)

- If user is not logged in he gets a prompt to log in or register.

![Review logged out view](/docs/readme-images/reviews-signed-out-screenshot.png)

### Shopping Bag Page

- The user can see all the items in his shopping bag.
- The user can make adjustments of the quantity of producst or remove products from the shopping bag.

![Shopping Bag view](/docs/readme-images/shoppingbag-screenshot.png)

- And if he is happy with the selection he can procedd to checkout.

![Shopping Bag view](/docs/readme-images/shoppingbag-checkout-screenshot.png)

### Checkout Page

- The user has to enter delivery information. 
- If the user is logged in, he can store his form data.

![Checkout view](/docs/readme-images/checkout-screenshot.png)

- If the checkout was successful the user will see a checkout success with his order information.

![Checkout success view](/docs/readme-images/checkout-success-screenshot.png)

- The user will also get an confirmation email with his order information.

![Confirmation email](/docs/readme-images/order-confirmaton-mail-screenshot.png)

### Profile Page

- A logged in user can administer his stored data.
- A logged in user can see his old orders.

![Profile Page](/docs/readme-images/my-profile-screenshot.png)

### About us Page

- A page about World of Games with a contact form to get in contact with is displayed.
- Only users that are not the admin can see the form, as the admin should be in contact with himself.

![About us Page](/docs/readme-images/about-us-screenshot.png)

### FAQ Page

- A short, but informative FAQ section.

![FAQ view](/docs/readme-images/faq-screenshot.png)

- The Superuser/Admin can edit and delete FAQs and add new ones on the same page.

![Superuser FAQ view](/docs/readme-images/faq-superuser-screenshot.png)

### Newsletter Page

- A site where site users subscribe to a newsletter.

![Newsletter Page view](/docs/readme-images/newsletter-screenshot.png)

- The user will receive a confirmation mail.

![Newsletter confirmation mail](/docs/readme-images/newsletter-confirmaton-mail-screenshot.png)

### Signup Page

![Signup Page](/docs/readme-images/sign-up-screenshot.png)

- A standard sign up page with validation for the user.

### Sign in Page

![Sign in Page](/docs/readme-images/sign-in-screenshot.png)

- A standard sign in page with validation for the user.

### Logout Page

![Logout Page](/docs/readme-images/logout-screenshot.png)

- A standard logout page for the user.

### 404 Page
![404 Page](/docs/readme-images/404-screenshot.png)
- When an error occurs or a wrong input is given to the url the 404-page will show up with the information on how to be redirected to the landing page.

## Testing
See the testing results in the [TESTING.md](TESTING.md) file.

## Technologies Used
### Languages
HTML, CSS, JavaScript, Python

### Programs Used - Frameworks - Libraries - Databases
- [Google Fonts](https://fonts.google.com/) - to import  fonts used on website.
- [FontAwesome](https://fontawesome.com/) - for footer's and navbar's icon.
- [Google Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools)- for troubleshooting, debugging, inspecting page's elements, testing responsiveness and styling elements.
- [VScode](https://code.visualstudio.com/) - IDE to develop the website.
- [GitHub](https://GitHub.com/) - for version control and hosting.
- [Balsamiq](https://balsamiq.com/wireframes/)- to create wireframes.
- [Coolors](https://coolors.co/) - to create color palette.
- [Google Chrome's Lighthouse](https://developers.google.com/web/tools/lighthouse) - to test performance and accessibility.
- [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS code.
- [W3C HTML Markup Validator](https://validator.w3.org/) to validate HTML code.
- [JShint JavaScript Validator](https://jshint.com/) to validate JS code.
- [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/) to validate Python code.
- [LucidChart](https://www.lucidchart.com/) - was used to make the ERD Diagram.
- [Django](https://www.djangoproject.com/) - used for the project's web framework. Is a Python framework. Other libraries that build on Django (eg.: Django Allauth) were also used.
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - used as a CSS framework.
- [AWS](https://aws.amazon.com/) - online static file storage used for uploaded pictures.
- [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/) - used as Postgres database.
- [Heroku](https://www.heroku.com/) - used to deploy project.
- [Stripe](https://stripe.com/at) - used to provide secure payment.

## Web Marketing

### SEO Keywords

According to [Backlinko](https://backlinko.com/hub/seo/seo-keywords): 
“SEO keywords (also known as “keywords” or “keyphrases”) are terms added to online content in order to improve search engine rankings for those terms. Most keywords are discovered during the keyword research process and are chosen based on a combination of search volume, competition and commercial intent.”

We used the following meta tags with the keywords in them:

``<meta name="description" content="Online e-commerce shop for video games based in Vienna. Different Sales ongoing. Shipping digital and physical content all over Austria.">``

 ``<meta name="keywords" content="Games, Sale, DLC, Digital, Physical, Action, RPG, Rogue-like, Multiplayer, Two-for-one, Co-op, Game bundles, Publisher Sales, DLC for free">``

### Facebook Buisness Page

I created a mockup Facebook page with the Wireframe Code Institute provided. These SNS Pages are a good way to advertise a live site and is important to get the main website a good page ranking.
![Facebook Mockup Page](/docs/wireframes-images/facebook-wireframe.png)

### Robots.txt

A robots file tells search engines which URLs they should get access to while telling them which sections to avoid. Yet I did not write anything to avoid in my file. However, this is only a guide. Search engines can access your website differently from it..


### sitemap.xml 

A sitemap is intended to lead a search engine. It can be seen as a blueprint to guide search engines in finding one’s website's content. They should create better visibility in search engines which means a higher user base.

I used [XML-Sitemaps](https://www.xml-sitemaps.com/) to create my sitemap.xml file.

### Newsletter

The user can stay up-to-date with the website's content through subscribing to a newsletter. 

### Marketing Plan

*For the project's sake this section is written as it would be real with an employed world of game's team*

World of Games is a B2C e-commerce online store. As we are new to the industry our marketing budget is not as big, so we aim for simple social media marketing, search enginge optimization and establishing ourselves at Austrian Based games- and comic conventions. As gamers are on their PC anyways we opted out of the plan of a physical shop and for now solely focus on the online store. Therefore, on sight we have our office and storage room, which is, so far, pretty much the same.
We know that there are big competitors such as Amazon, Valve and many more, but since we want to establish ourself in Austria, we aim to held gaming days withing our 5 year plan, therefore we also want to create a community not just a money making machine.
- The functionality is kept as simple as possible, as most gamers want to get the job done as quick as possible, so do we!
- For our team the CRUD functionality is most important as not every one of us knows how to use the admin panel and you do not need to!
- Unlike many other areas in the world, facebook is still a thing in Austria ^^ We created our facebook site with this in mind and also intend to join regional gaming groups with this. Yet, this is not the end, Instagram, TikTok and Reddit are right around the corner. We can reuse content and maybe cut some videos of the gameplay of the games we are selling. This is all in our concept board for the next five year
- Our target market remain gamers in Austria: From age 16-75 with an Austrian median income and already know on how to buy games online.

**5 year plan**
1. Year:
   - In the first months mainly market on facebook, with family and friends
   - From the second quarter, after the office-/storage and our gaming database has been reached start documenting everything for other social media channels
   - Establish social media channels and look for more investors for eg.: local events
2. Year:
   - Hire Gen-Z's for social media marketing
   - Establish a rating system for the customer
   - Start going to conventions
3. Year:
   - Break Even
   - Create a Blog or community page
   - Try to get early access for new games to sell as well, or getting beta codes
4. Year:
   - Create an own meet-up that has to do solely with world-of-games and establish a brand name for that as well
5. Year:
   - Get out of our current space and get a local store where we can also have our local events


## Deployment

### PostgreSQL

How to setup your PostgreSQL database:
- got to [CI Database Maker](https://dbs.ci-dbs.net/)
- input your LMS email address
- create your PostgreSQL database
- press on Info and copy the Database URL to your env.py file.

### Github Setup

This site was deployed to GitHub pages.
Instructions:

- Login to Github.
- Go to the GitHub repository: https://github.com/FlorianS4/world_of_games, navigate to the Settings tab.
- Select the Pages tab on the menu on the left side.
- Under Source, choose main from the Branch dropdown menu. Save it.
- The page will refresh itself and the website is now deployed with a text indicating such.

### Heroku Deployment

- Log into your [Heroku](https://www.heroku.com/) account or create an account.
- Select the New button on the right at the top and select "Create New App".
- Enter a application name.
- Select a region.
- Click "Create App".
- Go to the deploy option.
- Select GitHub as your deployment option.
- Confirm the connection to Github and choose the correct repository.
- Select "Enable Automatic" and "Deploy branch" with the selection main.
- Select "view" to see the live website.

### Amazon Web Services

- ### Create an AWS Account
- Search for s3 and create a Bucket.
- Provide a unique name for your bucket (`name it after your project`)
- Select `ACLs enabled`.
- Deselect `Block all puplic access`.
- Leave the other options unchanged.
- Click `create bucket`.

- ### Next enable static website hosting.
- Click on the bucket name to view the bucket details.
- Click on `Properties`.
- Select `static website hosting` and click `edit`.
- Click `Enable`, Enter `index.html` into the index document input and enter `error.html` into the Error document input.
- Save changes.

- ### Change CORS configuration.
- Go to the newly created bucket and click on the `Permissions` tab.
- Scroll down to the CORS section.
- Add the following code for the CORS settings.
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
- Save changes.

- ### Add a bucket policy
- Click `Policy Generator`.
- For the policy select `S3 Bucket Policy`
- For the principal enter * .
- For the Action select `GetObject`.
- Go back to the bucket policy editor and copy the `ARN`
- Then go back to the Policy Generator and past the `ARN` into the `ARN input`
- Click `Add Statement`.
- Scroll down and click `Generate Policy`.
- Copy the text in the popup:
```
{
    "Version": "2012-10-17",
    "Id": "Policy1720032710777",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": "*"
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
            "YOUR_ARN/*"
            ]
        }
    ]
}
```
- Save changes.

- ### Install reuqired packages.
- `boto3` and `django-storages`.

- ### Update your Django settings.
```
 # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'world-of-games'  # AWS bucket name
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
- Update your INSTALLED_APPS to include `storages`.

- ### Run the `collect static files command`
```
python manage.py collectstatic
```
- Your Static and media files should now be in your S3 bucket.


### Heroku set up

- In your GitPod workspace create an env.py file and add it to .gitignore.
- Add your SECRET_KEY value and the DATABASE_URL and the to the env.py file.
- Add your `AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY and add USE_AWS', 'True` to the env.py file.
- In the settings.py file import the env.py file and add the SECRET_KEY and DATABASE_URL file paths.
- Add TEMPLATES_DIR in settings.py file and change the templates directory to TEMPLATES_DIR.
- Add these Config Vars in Heroku:
    - `AWS_ACCESS_KEY_ID` - AWS Access Key ID
    - `AWS_SECRET_ACCESS_KEY` - AWS Secret Key
    - `DATABASE_URL` - Postgre SQL Url
    - `EMAIL_HOST_PASS` - Email Password
    - `EMAIL_HOST_USER` - Email
    - `SECRET_KEY` - Secret Key
    - `STRIPE_PUBLIC_KEY` - Stripe Public Key
    - `STRIPE_SECRET_KEY` - Stripe Secret Key
    - `STRIPE_WH_SECRET` - Stripe WH Secret
    - `USE_AWS` - True
- Additional Heroku Files:
    - Requirements.txt file
    - Create Procfile via gunicorn

        ```python
        web: gunicorn codestar.wsgi
        ```

### Running the project locally
Additional files needed for installation of dependencies:
    Requirements.txt file

How to Fork:
- Login to Github
- Go to the GitHub repository: 
- Select the Fork button on the right at the top

How to clone:
- Login to Github
- Go to the GitHub repository: 
- Select the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
- Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
- Type 'git clone' into the terminal and then paste the link you copied in step 3. and enter.
- A clone will be created.

## Credits
### Code

This project was based on the Code Institute - Boutique Ado.
The walkthrough provided a base for an E-commerce store. I customised a lot of the layouts and styling of this base with Bootsrap and custom CSS.

### Similar students projects

- When I browsed through the peer review slack channel I found [this project](https://github.com/AtsukoCoffey/little_plant) by [AtsukoCoffey](https://github.com/AtsukoCoffey).
- When I browsed through the peer review slack channel I found [this project](https://github.com/Sarah-Bue/bake-me-happy) by [Sarah-Bue](https://github.com/Sarah-Bue).
- My mentor gave this project as an inspiration for a project 5 README [this project](https://github.com/pauline-rugwevera/ecommerce-pp5) by [pauline-rugwevera](https://github.com/pauline-rugwevera).

### Resources Used
- Code Institute's lessons (Boutique Ado)
- Code Institute Slack Community.
- [Stack Overflow](https://stackoverflow.com/)
- [W3Schools](https://www.w3schools.com/)
### Media
- [Link to Image](https://www.pexels.com/photo/mosaic-alien-on-wall-1670977/) - I used this image as my background image, created by [Francesco Ungaro](https://www.pexels.com/@francesco-ungaro/) .
- [Favicon](https://favicon.io/emoji-favicons/video-game).
- Images and Game Description comes directly from [Steam](https://store.steampowered.com/).

## Fixed Bugs
- If clauses in product view did not run correctly.

	* It was because they focused on the wrong clause. I wrote one if clause in another, but because the first one was wrong/condition not met, the clause with a condition that would have been met, was ignored. I took out the first if-clause and it worked.

- Jquery did not run.

	* It was because I used the wrong value for the ``integrity`` attribute.  After cross checking with the source material I replaced the value and it ran.

- Order total did not update in the admin, but was correctly calculated in stripe.

	* First, I adjusted the template with the correct model variables. Then I  adjusted the model with unique variable name and I adjusted ``physical_or_digital_type``’s value to save it correctly to the database. I migrated all the model updates. Then, I updated the variable name to the new variable name, everywhere it was written with new name ``physical_or_digital_type`` While doing this I noticed, that in my views I misspelled bag for shopping bag and corrected that as well. **Conclusion:** Order is saved to the database and is shown after the checkout as well in the admin panel.

- When submitting whitespace for forms it was accepted or I got an error on certain forms, as well as being able to double submit forms.

	* I added either the correct ``HttpResponse`` or ``reverse`` to redirect user after either a  successful or invalid attempt so the user cannot submit invalid data or double submit.

- Website threw an error due to wrong url.

	*  I had href-attributes in place, even though I did not write the according views yet and templates yet, so I removed the whole anchor element  during that project phase. 

- Product images were not displayed correctly.

	* I referred to the correct variable (``product.image.url``) for my ``src`` attribute

-  When there were items in the shoppingbag, on large screens, it showed a few items of the mobile view as well.

	* I tried various CSSand bootstrap related fixes. Even tutor support could not help me. So I randomly enclosed certain div elements with the following div element ``<div class="d-block d-md-none"></div>`` instead of just enclosing it once. I pretty much enclosed all element blocks separately and it worked.

## Known Bug
- No image file is not accessed when there is no upload without an image. I could not find out why it was not referring to it correctly, yet in a real life case we would never let website admins upload a product without an image.

## Future Content
- Adding a rating system for the user.
- More marketing, look at other social media channels.

## Acknowledgments
My mentor Jubril Akolade for his guidance, input and support.

The Slack community on Code Institute for reviewing my project and for support.

Code Institute for informational courses.

Special thanks to my wife, who let me complain about everything wrong my project.
