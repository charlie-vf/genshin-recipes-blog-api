# Genshin Food Blog API

Further documentation, including user stories, agile methodology, design reasoning & implementation, main site testing etc. can be found in the ReadMe for the Client Site, [here](https://github.com/charlie-vf/genshin-recipes-blog)

This ReadMe will document API-specific content.

## *Testing*

Following intial manual testing pre-development of the client site, the majority of testing was completed via the main client site.

Initial testing inside this project can be found in the test.py file inside the recipes folder.


### Client-BackEnd cross-testing

1. Profiles

A profile was created using the Sign Up option on the client site and cross-checked in the API's [profile URL](https://genshin-food-blog-api.herokuapp.com/profiles/).

Through this, I ensured new profiles were successfully created and stored in the back-end, as well as relevant features such as whether the user logged in is the owner(is_owner), biography (listed back-end as 'content'), number of recipes, number of followers, number of followed users, and profile image.

Editing profile data was tested by performing the action in the client site and cross-checking it against the stored data in the back-end.

2. Recipes

A recipe was created using the Create Recipe option on the client site and checked with the [recipes list](https://genshin-food-blog-api.herokuapp.com/recipes/) displayed in the back-end.

Through this, I ensured new recipes were successfully created and stored in the back-end, with all relevant fields present & storing the correct data, e.g. title, ingredients. image, number of likes, creation data, is_owner etc and that they are associated with the correct profiles.

Editing and deleting recipe data was, again, tested by performing these actions client-side and checking they have occurred correctly in the API site.

3. Liking, marking as made & commenting on recipes.

Again, this was tested by performing the above actions on a recipe the logged in user of the client site does not own and checking the relevant changes occured back-end.

## **Deployment**

This API project was created using a GitPod workspace, commited to Git, pushed to GitHub and deployed on Heroku.

Before deployment, ensure:

- Development is set to False in settings.py
- You have created a Procfile with the relevant information, e.g. web
- Your requirements.txt file is up to date

### Heroku Deployment

- Select New App
- Choose App name and region
- Select Deploy & link to GitHub repository
- Manually deploy site (can choose automatic deployment after this, if desired)

Environment Set-Up:

- Select Settings -> Reveal Config Vars
- Add the following:
    - ALLOWED_HOST: URL for deployed API site
    - CLIENT_ORIGIN: URL for deployed client site
    - CLIENT_ORIGIN_DEV: URL for client site active workspace
    - CLOUDINARY_URL: your cloudinary URL
    - DATABASE_URL: your postgreSQL URL
    - SECRET_KEY: the secret key you created in your workspace env.py file
