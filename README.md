# Student Life
add picture here                =========================EDIT========================

## Purpose
The purpose of this site is to allow for all students who visit a universtity library the ability to access Student Life. We are here to show students how they can make 
delicious meals at a low cost which wont eat into their student loan. 

## High Level Requirements
The creation of this website allows for users to ... 
1. Access up to 3 categories of foods ie. Dinner, Breakfast and Protein Meals.
2. Display the recipes within time order eg. Breakfast, Lunch/Dinner then Protein Meals for those how want extra help getting in shape.
3. Allow each recipe to be displayed seperately to have a full screen view, showing the ingredience and instructions.
4. Allow users to edit, delete and submit new recipes. 

## Future Features
Future features which I will implement when I have more time will be ...

1. Allowing users to log in to the site and log out. Meaning that only they can edit, delete and submit their recipes.
2. Create a rating system that allows for users to rate recipes from 0 to 10.
3. Create a feedback request form so that the author of a recipe can see how well they are doing. 
4. Create a commenting section allowing for users to suggest improvements/feedback on recipes. 

## User Stories

The invention of this website come straight from a university student who never knew what to cook. I spent the majority of my student 
loan eating out and buy the most expensive things in the supermarkets. From fresh fruit and veg which i'd never eat to Ben and Jerry's,(even when not on sale!)
Whenever I was in the library, and needed a break i'd go to the shops to get some food ... so why not help other students make healthy student meals on a 
student budget. All students can access this site at the university library, meaning thatonly students can access and delete the database.

## Features

- The site contains multiple pages 
⋅⋅⋅ Home page - This contains the home page image with information on what the site containts. Below this contains all the recipes on the screen. 
⋅⋅⋅ Add A Recipe - This page contains all the neccessary information for a user to add a new recipe to the site. From Name to price to protein intake.
⋅⋅⋅ View Recipe - This page allows you to view the entirety of a recipe. At the bottom there are 2 buttons, one for editing and one for deleting. 


## Overview Of MongoDB Database

Name - The name of the recipe.
Category - Select which category the recipe goes into ie. Breakfast, Lunch/Dinner or Protein Meal.
Price - What the recipe costs?
Protein - How much protein is in the recipe?
Serves - How many people can this recipe serve?
Ingredience -  What ingredience do you need to make the recipe?
Instructions - How do you make the recipe? (in a step by step guide.)
Description - How would you describe the recipe?

## Technologies Used

- Heroku - I used Heroku to deploy my site as it allows for me to use python within my project.
- mongoDB - Using this document based database, it allowed for me to add in large amounts of data (recipes) which can be easily stored within the cloud.
- Python - The use of Python within this project allowed for back end programming language for this app.
- HTML - With the use of HTML it allowed for the initial content to be creates and viewed on this app.
- CSS - Allows for custom styles to be created and added to my HTML.
- Google Fonts - Selected Quicksand font to add a sence of style to the writing. 
- Bootstrap - Creates a creative and responsive grid system, added pre-made styles and allows for jQuery scripts to be added.
- Font Awesome - Used to add icons within the app.
- Flask - Added a python micro web framework, which provides libraries, tools and technologies to create a web application.


## Wireframes

these can be seen in their own folder located in......... here is a link ()                 =========================EDIT========================

## Version control

- Git - Throughout the entire project, I have commited to using git as version controll in order to save and edit changes within my files and site.
- Git Hub - Allowed me to push my git commits to a remote repository.

## Hosting

- This project has been hosting on Heroku. This is due to Heroku allowing for python to be uesd within the project.

## Testing

what web applications did you test them on
what mobile sizes did you test ? any issues?
test your files online - w3c html validator
vocab and spell check!
use 'am i responsive' web tool
did anything fail? why did it fail?

1. When connecting my site to Heroku, there was an unknown error which meant that the site couldnt be previewed. After a few hours of testing and 
trying to figure out the problem I repushed my work to github, made Heroku the master branch again after disconnecting it. After reloading all my data 
and pushed all my code to github I found that the error occured due to my Procfile containing no information. After recreating my Procfile and pushing it 
to github and Heroku, this fixed the error and allowed me to preview my file on Heroku.

2. While importing my code within jinja, I canme across multiple issues with {{_______}}. My issues came from not opening and closing my jinja correctly 
and due to not understanding that when redirecting to a view to display information a certain singular database iten needs to pass in some way of itentifying 
that item. This was through giving an ID to the database item. However I went over this multiple times within the course and got extra help to understand where 
I was going wrong.

3. Due to an error with mongodb, I originally started writing my code within JsFiddle. An online code editor which allows you to preview your work immedietly.
This ensured me that I was creating the correct code even though I couldnt see it on my preview when using GitPod. When I had Correctly made my database 
within mongoDB again I reconnected my site to mongo ensuring that the names and collection names matched up due to mongoDB being case sensitive. This 
initially created some errors with my site as I was using capital letters instead of lower case.

4. When creating an environment.py fle I mistakenly wrote in error within my code which meant that there wasnt a connection to the rest of the files due 
to this incorrect syntax. From this I changed the syntax to
```python 
os.environ.setdefault
```
which effectively connected mt env.py file to the rest of the code.

5. MOBILE APPLICATION DOES IT WORK DOES IT NOT 
DOES IT WORK ON SAFARI/FIREFOX/CHROME                              =========================EDIT========================
DID YOU USE THE INSPECT TOOL 



## Code Validation
- Throughout this project I ensured that I was making use of W3C validator for both CSS and HTML. This allowed for me to check my code writing and 
to check there were no errors.
- To check my python code I used pep8 an online tool to validate my python syntax.

## Deployment
where is the live site hosted(heroku)
                                                 =========================EDIT========================

## When commiting to Github, follow theres steps...
1. Ensure you are on the /environment/ in your ternimal.
2. If not, use `cd ..` to got back one file at a time till you reach 'environment'.
3. Enter `git add .` to add all content to github.
4. `git commit -m "Initial commit` This code will commit your code and add a a small description.
5. `git push` will upload this file to a remote repository.

## Credits
- All images were sourced from Pixabay.com and Pexels.com
- Thanks to all my university friends who told me about all their weird and cheap student meals, even if some were not included in the website.

## Acknowledgements
⋅⋅⋅Thanks to everyone on the Slack community for helping me with issues that I encountered.
⋅⋅⋅Thank you to the Tutors at the Code Institute for their help when i was really struggling.
⋅⋅⋅Thanks to Brian Macharia, for the help and support with this project. 

## Disclaimer
⋅⋅⋅This project is for educational use only.