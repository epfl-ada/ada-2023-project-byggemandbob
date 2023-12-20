# Datastory (website)
[Datastory REPO](https://github.com/Nuimo/ada-website-byggemandbob/tree/master)

[Datastory LINK](https://nuimo.github.io/ada-website-byggemandbob/)


# Maximizing Box-Office Revenue and Rankings: Crafting the Perfect Movie Formula

## Abstract

Movies constitute a vast global industry and a significant part of the international entertainment sector. Given the industry's scale, it is valuable to investigate features contributing to the success of movies. Identifying key factors linked to movie success aids industry stakeholders in making informed investment decisions and reveals whether top-grossing films share a common formula.

Using the CMU Movie Summary Corpus dataset and TMDB movie data, this project will uncover similarities in movie and character data among high-earning and high-ranking movies. This is done through two different models:

1. A linear regression model predicting movie ratings and revenue, based on traditional movie attributes such as gender distribution, original language, and genre.
2. A NLP model for analyzing the movie plot summaries, using unsupervised learning for clustering. The assessment will be made on whether the clusters differ significantly in terms of revenue and ratings.

## Research Questions

1. How are the main attributes within both movie metadata and movie character metadata distributed?
2. What is the distribution of the box-office revenue and the TMDB movie ratings?
3. How do the different relevant attributes from the meta-data impact the rating and revenue of movies? And what combination of features contribute to a high rating, and to a high revenue?
4. What patterns and relationships exist between word clusters in movie plot summaries and how do they correlate with the average revenue and ratings?
5. What insights can be drawn regarding the content and themes associated with highly rated and high revenue movies based on the top 10 words in the different clusters?

## Additional Datasets

We used [TMDB](https://www.themoviedb.org/) for enriching our data with both revenue and TMDB ratings for the movies.

## Methods
Data Preparation: This stage involves data cleaning, filtering, and transformation. We strive to refine the dataset to ensure accuracy and relevance for our analysis.

Data Collection: We use API calls to collect extensive data. This step is important for gathering rich and comprehensive datasets, mainly TMDB, which will enrich our understanding of movie revenues and ratings.

Natural Language Processing (NLP): An integral part of our analysis involves NLP techniques. We start with data preprocessing, where the raw text data is cleaned and prepared for analysis. This is followed by tokenization and TF/IDF vectorization, breaking down the text into meaningful segments and evaluating their significance. Our approach includes word clustering using unsupervised machine learning techniques like K-means++, which helps in identifying patterns and themes in movie plot summaries.

Statistical and Regression Analysis: To predict movie ratings and revenue, we are developing a multivariate linear regression model. This model will help us understand the relationship between various movie attributes and their impact on success. Furthermore, we perform a range of statistical analyses, including the generation of boxplots, histograms, and t-tests, to understand the distribution and correlation of different variables. Confidence intervals will also be used to understand the precision of our estimates.

Visualization Techniques: To effectively display our findings, we employ visualization tools. This includes creating box plots and histograms to illustrate data distributions, scatterplots for exploring relationships between variables, and word clouds to visually represent the most prominent themes in movie plot summaries.

Utilizing ChatGPT-4 for Movie Poster Creation: As part of our visualization strategy, we're using ChatGPT-4's capabilities to generate movie posters. This method involves feeding the AI a list of top prominent words in a cluster, allowing it to create posters that visually represent each movie's essence. This approach not only enhances our project's visual appeal but also demonstrates a new application of AI in trying to blend data analysis with creative design.

## Contributions of group members
- Mathias: Natural language processing
- Emma: Linear regression modelling, README
- Sofie: Data cleaning, Linear regression modelling
- Kavus: Linear regression modelling, README
- Gustav: Enrichment, datastory setup

All group members contributed equally to the writing aspect of the datastory.

## Notebook
A notebook containing initial analyses and data handling pipelines can be found in [pipeline.ipynb](pipeline.ipynb).

