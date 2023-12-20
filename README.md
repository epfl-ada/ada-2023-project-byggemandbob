# Datastory (website)
[Datastory REPO](https://github.com/Nuimo/ada-website-byggemandbob/tree/master)

[Datastory LINK](https://nuimo.github.io/ada-website-byggemandbob/)


# Maximizing Box-Office Revenue and Rankings: Crafting the Perfect Movie Formula

## Abstract

Movies constitute a vast global industry and a significant part of the international entertainment sector. Given the industry's scale, it is valuable to investigate features contributing to the success of movies. Identifying key factors linked to movie success aids industry stakeholders in making informed investment decisions and reveals whether top-grossing films share a common formula.

Using the CMU Movie Summary Corpus dataset and TMDB movie data, this project will uncover similarities in movie and character data among high-earning and high-ranking movies. This is done through two different models:

1. A linear regression model predicting movie ratings and revenue, based on traditional movie attributes such as gender distribution, original language, and genre.
2. A NLP model for analyzing the movie plot summaries, using unsupervised learning for clustering. The assessment will be made on whether the clusters differ significantly in terms of revenue and ratings.

Lastly, the attributes found to contribute to high revenue and rating from the two models will be compared.

## Research Questions

1. How are the main attributes within both movie metadata and movie character metadata distributed?
2. What is the distribution of the box-office revenue and the TMDB movie ratings?
3. How do the different relevant attributes from the meta-data impact the rating and revenue of movies? And what combination of features contribute to a high rating, and to a high revenue?
4. What patterns and relationships exist between word clusters in movie plot summaries and how do they correlate with the average revenue and ratings?
5. What insights can be drawn regarding the content and themes associated with highly rated and high revenue movies based on the top 10 words in the different clusters?

## Proposed Additional Datasets

We would like to use [TMDB](https://www.themoviedb.org/) for enriching our data with both revenue and TMDB ratings for the movies. The core of this project is to investigate factors contributing to the success of a movie, measured by revenue and TMDB ratings. It is therefore essential to have sufficient amounts of such data to ensure robustness and representativeness of our findings.

## Methods

- Data cleaning, filtering, and transformation
- Data collection by making API calls
- Natural language processing: data preprocessing, tokenization, TF/IDF vectorization, word clustering using unsupervised machine learning such as K-means++
- Multivariate linear regression (in process)
- Statistical analysis: Boxplots, histograms, linear regression, confidence intervals, t-tests
- Visualization: Box Plots, histograms, scatterplot, word clouds

## Proposed Timeline

### Week 1: 13/11-19/11/2023 (5 weeks until the final deadline week)

- Submit Project Milestone 2
- Finish project pipeline and research questions
- Finish preliminary data analysis
- Finish data enrichment
- Finish filtering and preprocessing
- Start on linear regression model
- Continue working on natural language processing model

### Week 2: 20/11-26/11/2023 (4 weeks until the final deadline week)

- Work on Homework 2

### Week 3: 27/11-03/12/2023 (3 weeks until the final deadline week)

- Set up website
- Continue working on model constructions
- Start writing data story
- Start analyzing initial results

### Week 4: 04/12-10/12/2023 (2 weeks until the final deadline week)

- Finalize model constructions
- Continue working on the analysis of results
- Continue writing the data story

### Week 5: 11/12-17/12/2023 (1 week until the final deadline week)

- Finalize the analysis of results
- Almost finalize writing the data story
- Almost finalize writing the project repository

### Week 6: 18/12-24/12/2023 (0 weeks until the final deadline week)

- Finalize writing the data story
- Finalize writing the project repository
- Proofread the data story, Readme.me, and final project repository
- Submit the project repository

## Organization Within the Team

### Internal Milestones

- Fri 17/11/2023: Submit Project Milestone 2
- Sun 26/11/2023: Submit Homework 2
- Sun 10/12/2023: Finalize models
- Wed 13/12/2023: Finalize the analysis of results
- Fri 15/12/2023: Finalize 80% of writing
- Wed 20/12/2023: Finalize writing
- Fri 22/12/2023: Submit Project Milestone 3

## Questions for the TA

- Model comparison: How can we compare the NLP model clustering movies based on plot summaries with the linear regression model investigating the coefficient of traditional attributes for predicting rating and revenue? Is comparing the dominant attributes of clusters to the coefficients of the regression model reasonable?
- Handling missing data for revenue: Should we only include data points with both revenue and rating?
- Transform predicting attributes: When making a linear fit, if the predicting attributes are heavy-tailed, should we log-transform the data before fitting the model?
- Is it incorrect to use SEM instead of STD when plotting error bars?

## Notebook

A notebook containing initial analyses and data handling pipelines can be found in [pipeline.ipynb](pipeline.ipynb).



