# RecipeHub

![RecipeHub homepage](/images/recipehub.jpg)

_Java · Spring Boot · React · MySQL · Docker_

A full-stack recipe discovery app. You can browse featured recipes, search by dish or by the ingredients you already have, follow step-by-step instructions, and build a printable shopping list from any recipe.

[View on GitHub](https://github.com/travisdotdev/recipehub)

## About the project

- **Backend architecture:** split the backend into a recipe service and a dedicated client for the Spoonacular recipe API, and reworked the endpoints and response models
- **Frontend structure:** rebuilt the homepage around custom React hooks for API calls, and refactored the recipe cards, carousel and detail page
- **Search:** added the search-type options (by dish or by ingredients) and connected search to the navbar
- **Docker and testing:** containerised the app with Docker Compose and wrote backend and frontend tests

## How it works

```
React frontend (port 3000)
   |  REST
   v
Spring Boot API (port 8080)
   |  cache + rate limiter
   v
Spoonacular API
```

The backend sits between the frontend and Spoonacular, so the API key never reaches the browser. Recipe responses are cached in memory for two minutes, recipe lists are also stored in MySQL through Spring Data JPA, and a per-minute and per-day limiter keeps usage within Spoonacular's free plan.

## Running it locally

Needs Docker and a free Spoonacular API key.

```
git clone https://github.com/travisdotdev/recipehub.git
cd recipehub
export SPOONACULAR_API_KEY=your-key
docker compose up --build
```

Then open localhost:3000 in your browser.

[← Projects](/projects)
