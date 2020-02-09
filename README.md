# Student Life

## Purpose
The purpose of this site is to allow for all students who visit a universtity library the ability to access Student Life. We are here to show students how they can make 
delicious meals at a low cost which won't eat into their student loan. 

## High Level Requirements
The creation of this website allows for users to ... 
1. Access up to 3 categories of foods ie. Breakfast, Dinner and Protein Meals.
2. Allow each recipe to be displayed seperately to have a full screen view, showing the ingredience and instructions.
3. Allow users to edit, delete and submit new recipes. 
4. Scroll to the top button to ensure ease of use of the site.

## Future Features
Future features which I will implement when I have more time will be ...

1. Allowing users to log in to the site and log out. Meaning that only they can edit, delete and submit their recipes.
2. Create a rating system that allows for users to rate recipes from 0 to 10.
3. Create a feedback request form so that the author of a recipe can see how well they are doing. 
4. Create a comment section allowing for users to suggest improvements/feedback on recipes. 
5. Have a dropdown which allowed you to filter through if you wanted 'Breakfast', 'Lunch' or 'Dinner'.
6. Allow for each user to add their own images to their recipes.


## User Stories
The invention of this website come straight from a university student who never knew what to cook. I spent the majority of my student 
loan eating out and buying the most expensive things in the supermarkets. From fresh fruit and veg which i'd never eat to Ben and Jerry's,(even when it wasn't on sale!)
Whenever I was in the library, and needed a break i'd go to the shops to get some food ... so why not help other students make healthy student meals on a 
student budget. All students can access this site at the university library, meaning that only students can delete and edit the sites database.

## Features
 The site contains multiple pages 
- Home page - This contain's the home page image with information on what the site containts. Below this contain's all the recipes within the database. 
- Add A Recipe - This page contain's all the neccessary information for a user to add a new recipe to the site. From Name to price to protein intake.
- View Recipe - This page allows you to view the entirety of a recipe. At the bottom there are 2 buttons, one for editing and one for deleting. 
- Edit Recipe -  Edit your own or someone else's recipe. The submit button (when clicked) shows a pop up asking if they would like to submit 
or cancel their edit to make sure they know that they have edited the recipe.
- Delete Recipe - Completely remove a recipe with this button. However a confirmation pop up will appear to make sure the user knows that they are deleting 
a recipe.


## Overview Of MongoDB Database
- Name - The name of the recipe.
- Category_name - Select which category the recipe goes into ie. Breakfast, Lunch/Dinner or Protein Meal.
- Price - What the recipes costs?
- Protein - How much protein is in the recipe?
- Serves - How many people can this recipe serve?
- Ingredients -  What ingredients do you need to make the recipe?
- Instructions - How do you make the recipe? (in a step by step guide.)
- Description - How would you describe the recipe?

## Technologies Used
- Heroku - I used Heroku to deploy my site as it allows for me to use python within my project.
- MongoDB - Using this document based database, it allowed for me to add in large amounts of data (recipes) which can be easily stored within the cloud.
- Python - The use of Python within this project allowed for back end programming language for this app.
- HTML - With the use of HTML it allowed for the initial content to be creates and viewed on this app.
- CSS - Allows for custom styles to be created and added to my HTML.
- Google Fonts - Selected Quicksand font to add a sence of style to the writing. 
- Materialize - Creates a creative and responsive grid system, added pre-made styles and allows for jQuery scripts to be added.
- Font Awesome - Used to add icons within the app.
- Flask - Added a python micro web framework, which provides libraries, tools and technologies to create a web application.
- JavaScript - Used to enable bootstrap code for mobile devices.


## Wireframes
These can be seen in their own folder located in Static/wireframe.   

## Version control
- Git - Throughout the entire project, I have commited to using git as version controll in order to save and edit changes within my files and site.
- Git Hub - Allowed me to push my git commits to a remote repository.

## Hosting
- This project has been hosting on Heroku. This is due to Heroku allowing for python to be uesd within the project.

## Testing
1. When connecting my site to Heroku, there was an unknown error which meant that the site couldnt be previewed. After a few hours of testing and 
trying to figure out the problem I repushed my work to github, made Heroku the master branch again after disconnecting it. After reloading all my data 
and pushed all my code to github I found that the error occured due to my Procfile containing no information. After recreating my Procfile and pushing it 
to github and Heroku, this fixed the error and allowed me to preview my file on Heroku.

2. While importing my code within jinja, I came across multiple issues with {{_______}}. My issues came from not opening and closing my jinja correctly 
and due to not understanding that when redirecting to a view to display information a certain singular database item needs to pass in some way of itentifying 
that item. This was through giving an ID to the database item. However I went over this multiple times within the course and got extra help to understand where 
I was going wrong.

3. Due to an error with mongodb, I originally started writing my code within JsFiddle. An online code editor which allows you to preview your work immedietly.
This ensured me that I was creating the correct code even though I couldn't see it on my preview when using GitPod. When I had correctly made my database 
within MongoDB again, I reconnected my site to mongo ensuring that the names and collection names matched up due to mongoDB being case sensitive. This 
initially created some errors with my site as I was using capital letters instead of lower case.

4. When creating an environment.py fle I mistakenly wrote in error within my code which meant that there wasnt a connection to the rest of the files due 
to this incorrect syntax. From this I changed the syntax to
```python 
os.environ.setdefault
```
which effectively connected mt env.py file to the rest of the code.

5. When editing my work and going onto preview there was an issue which meant that my recent edits hadn't been updating within the preview. To fix this, I had to 
open the Chrome developer tool, long click on the reload button, and click on 'Empty cashe and hard reload'. This deleted all the recent cashe and forced a roload 
allowing for the new edits to be seen within the previews. This happened when using Safari, Chrome and Firefox. 

6. Near the end of testing, there was a large error caused by Pymongo. Stating that 'Cannot set option after executing query'. This was due to an error within my Index.html page 
where I had `{{ url_for('view_recipe', recipes_id=recipes._id)}}` meaning that I was trying to select multiple recipes when trying to locate one specific recipe.
Due to this error, extra care was taken to ensure that my spelling and use of 's' were added only when neccessary.

7. This site works on Safari, Chrome and Firefox broswers. However, there is no need for this application to be used on a mobile device due to the site being
 designed for library computers at a campus/university. This was taken into consideration while editing the site, and I chose to adapt the site to fit 
within smaller screens such as tablets. These are commonly used at universities and are handed out during classes occationally. 

8. There is an error occuring which I was unable to correct due to time restrictions. This error occures when adding a new recipe to 
the site. All information is correctly added apart from the Category section. 

## Code Validation
- Throughout this project I ensured that I was making use of W3C validator for both CSS and HTML. This allowed for me to check my code writing and 
to check there were no errors.
- To check my python code I used pep8 an online tool to validate my python syntax.

## Deployment

1. Type in 'heroku ps:scale web=1' into your terminal.
2. Create a requirements.txt file by entering 'sudo pip3 freeze --local > requirements.txt'.
3. Go to Heroku.com
4. Sign in and create a new app
5. Select your region.
6. Enter your new app name ie. Student-Life.
7. Click 'Create App'
8. Enter 'sudo snap install --clasic heroku' into the CLI.
9. Enter 'Heroku login --interactive'
10. Within Heroku, click 'Deploy'.
11. Within 'create new repositor', copy 'heroku git:remote -a global-Student-Life'.
12. Paste this into your bash terminal.
13. Go to the heroku dashboard for your app and click settings.
14. Copy the heroku git url.
15. In the bash terminal type 'git remoter add https://studentlife01.herokuapp.com/'.
16. Enter 'git push -u heroku master'.
17. On the heroku site, click settings.
18. Within reveal config vars enter 'IP' in the first box and in the next box enter '0.0.0.0' click add.
19. Enter 'PORT' in the first box and in the next box enter '5000' click add.
20. Enter your 'secret key'in the first box and in the next box enter 'default secret key' click add.


## When commiting to Github, follow theres steps...
1. Ensure you are on the /environment/ in your ternimal.
2. If not, use `cd ..` to got back one file at a time till you reach 'environment'.
3. Enter `git add .` to add all content to github.
4. `git commit -m "Initial commit` This code will commit your code and add a a small description.
5. `git push` will upload this file to a remote repository.

## Credits
- All images were sourced from Pixabay.com and Pexels.com
- Thanks to all my university friends who told me about all their weird and cheap student meals, even if some were not included in the website.
- Added Scroll to top butten thanks to the help of W3C.

## Acknowledgements
- Thanks to everyone on the Slack community for helping me with issues that I encountered.
- Thank you to the Tutors at the Code Institute for their help when I was really struggling.
- Thanks to my Mentor Brian Macharia, for the help and support with this project. 

## Disclaimer
 This project is for educational use only.