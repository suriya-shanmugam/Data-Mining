
# Mobile Price Prediction Using AutoML (Akkio)

This project demonstrates the use of AutoML via Akkio to predict mobile phone prices based on features like battery life, RAM, and processor speed. The model was trained using a dataset sourced from Kaggle, and the project has been hosted on a public URL.

[Video Demo](https://youtu.be/yp1ItbnqN-Y)

[Product site](https://youtu.be/yp1ItbnqN-Y)

## Project Overview 

In this project, I used the **Akkio AutoML platform** to build a regression model for predicting the price of mobile phones. The goal is to leverage machine learning to predict the price based on a variety of features. 



### Dataset

- **Source**: The dataset used in this project was sourced from [Kaggle Mobile Price Dataset](https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification).
- **Features**:
  - `battery_power`: Total energy stored in the battery (mAh)
  - `ram`: Random Access Memory (MB)
  - `px_height`: Pixel height of the mobile phone screen
  - `px_width`: Pixel width of the mobile phone screen
  - `clock_speed`: Speed of the mobile phone's processor (GHz)
  - `talk_time`: Maximum time the battery will last in a single call (hours)
  - ... (other features related to screen size, battery, processor, etc.)
  
### Problem Statement

The aim of this project is to predict the **price range** of a mobile phone based on several features. The prediction task is handled by Akkio’s AutoML platform, which allows for rapid model development without manual intervention in feature engineering and hyperparameter tuning.

### Tools Used

- **Akkio**: An AutoML platform that simplifies the process of building machine learning models.
- **Kaggle**: Used to source the dataset.
- **GitHub**: For version control and project hosting.

## Model Training

The model was trained using Akkio’s AutoML capabilities. Akkio automatically selected the most appropriate algorithm and tuned hyperparameters to provide the best possible performance.

### Steps:

1. **Data Upload**: Uploaded the Kaggle dataset into Akkio.
2. **Model Training**: Akkio AutoML handled the feature engineering and model training automatically.
3. **Evaluation**: The model's performance was evaluated using metrics like Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared.
4. **Deployment**: The trained model is deployed and hosted publicly.

## Deployment

The model is accessible via the following public URL:
- [Mobile Price Prediction Model](https://app.akkio.com/deployments/82824317-ab17-443c-b8d6-a26f0399ea5d)

This URL allows you to input mobile features and get a predicted price.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/suriya-shanmugam/Data-Mining

   ```

2. Navigate to the project directory:

   ```bash
   cd Tasks/Todo-1/Assignment-3
   ```

3. Explore the dataset and model.

4. Access the hosted model via the public URL provided above.

## Usage

The deployed model accepts several features of a mobile phone and predicts its price. To use it:
- Visit the [Mobile Price Prediction Model](https://app.akkio.com/deployments/82824317-ab17-443c-b8d6-a26f0399ea5d).
- Input the relevant mobile phone specifications.
- Get the predicted price in real-time.

## Project Structure

```bash
├── dataset/
│   └── mobile_price_dataset.csv   # The dataset used in this project
├── README.md                      # Project documentation

```


## Acknowledgements

- The dataset was sourced from [Kaggle](https://www.kaggle.com).
- Thanks to [Akkio](https://www.akkio.com) for providing the AutoML platform.
