
# Region-based pollution classification and strategy implementation through ensemble learning and ANN(Artificial Neural Networks)

The model aims to identify the necessary
parameters and the pollutants, their quantities to predict the
types of pollution in a region, particularly industrial pollution,
due to
Urbanization namely vehicular emissions and constructional
activities, pollution due to agricultural activities and pollution
of water bodies of the region and then suggest the most optimum and economic
strategies for pollution management in the region.

The multiclass classification problem under consideration
comprised 16 classes and employed an ensemble learning model
to address the challenge. The accuracy of the decision trees
classifier was observed to be 97%, while both the random forest
and XGBoost classifiers exhibited accuracies exceeding 99%.
However, there is a noticeable concern that Random Forest and
XGBoost may have overfitted the data.
It is indeed plausible that Random Forest and XGBoost overfitted
the data, despite achieving higher accuracy compared to decision
trees. Ensemble methods, such as Random Forest and XGBoost,
are inherently more susceptible to overfitting than individual
decision trees. Overfitting occurs when a model excessively learns
the nuances and noise within the training data, hindering its ability
to generalize effectively to unseen data.
The dataset in question consisted of 12000 entries with 16 classes
of equal significance. The observation that decision trees, which
are less prone to overfitting, achieved lower accuracy but
demonstrated better generalization might be attributed to the
dataset's size and complexity.

The ensemble learning model gave a high accuracy of 97%
on the testing dataset. Some of the notable predictions by
the model are listed below:

• The model accurately predicted that Delhi is currently
suffering from industrial pollution, marine pollution and
pollution due to construction and vehicular emissions,
since the land under agriculture use in Delhi is 5%, the
model was able to classify that pollution due to
agricultural activities and soil fertility is not an issue to
be held important for Delhi.
• The model was able to accurately predict that the main
category of pollution in Andaman and Nicobar Islands is
marine pollution, and the reason for that is since the D.O.
for the region comes out to be 7mg/L which comes under
the category of slightly polluted water according to WHO
guidelines.
• The model accurately predicted that Punjab is suffering
from pollution of all categories under observation,
namely industrial pollution, pollution due to vehicular
emissions and constructional activities, pollution due to
agricultural activities and pollution of water bodies.
Research Paper for Pollution classification, November 2023 8
Based on these predictions, our program was able to
suggest the best strategies to be implemented in these
regions for economic way of pollution control.

Project Walkthrough:

https://github.com/RaghavMangla/Region-based-Pollution-Classifier-ML/assets/97332401/0f9e42f0-24fe-4d8a-b25a-0df9ed581340

The predictions for the 3 places shown in the video are for Delhi, Andaman and Nicobar Islands and Punjab



## Author

- Raghav Mangla

