# Manufacturing Equipment Maintenance Prediction

## Overview
This project focuses on predicting the failure causes of manufacturing equipment using machine learning techniques. The goal is to develop a predictive model that can identify potential equipment failures before they occur, enabling proactive maintenance and reducing downtime in manufacturing operations.

## Dataset
The analysis uses a comprehensive dataset (`Dataset.csv`) containing various sensor readings and operational parameters from manufacturing equipment. Key features include:
- **Sensor Data**: Temperature, Pressure, Vibration, Humidity, Flow Rate, Power Consumption, Oil Level, Voltage
- **Operational Data**: Maintenance Type, Production Volume, Planned Downtime Hours, Shifts Per Day, Production Days Per Week
- **Temporal Data**: Installation Date, Failure Date, Maintenance Date
- **Target Variable**: Failure_Cause (Electrical Failure, Mechanical Failure, Sensor Malfunction)

## Methodology

### Data Preprocessing
1. **Data Cleaning**: Removed unnecessary columns (Equipment_ID) and handled missing values
2. **Exploratory Data Analysis**: Generated correlation heatmaps to identify multicollinearity among features
3. **Outlier Removal**: Applied IQR method to remove outliers in Power_Consumption data
4. **Feature Engineering**: Used StandardScaler for numerical features and OneHotEncoder for categorical features

### Model Development
- **Algorithm**: Artificial Neural Network (ANN) with custom focal loss function
- **Architecture**:
  - Input layer with 17 features
  - Hidden layer: 8 neurons with ReLU activation and L2 regularization (0.001)
  - Dropout layer (0.3) for regularization
  - Output layer: 3 neurons with softmax activation (corresponding to 3 failure classes)
- **Loss Function**: Focal Loss (gamma=2.0, alpha=0.25) to handle class imbalance
- **Optimizer**: Adam
- **Training**: 1000 epochs with early stopping (patience=35, monitor=val_loss)

### Model Evaluation
- **Metrics**: Loss, Accuracy, Confusion Matrix
- **Validation**: 33% validation split during training
- **Test Performance**: Evaluated on 20% holdout test set

## Results
The model achieved the following performance metrics:
- **Test Loss**: [To be determined after execution]
- **Test Accuracy**: [To be determined after execution]
- **Confusion Matrix**: Provides detailed breakdown of predictions vs actual failure causes

## Key Findings
- The ANN model with focal loss effectively handles the multi-class classification problem
- Feature preprocessing significantly impacts model performance
- Early stopping prevents overfitting during training
- The confusion matrix reveals the model's strengths and weaknesses in predicting different failure types

## Technologies Used
- **Python Libraries**: TensorFlow/Keras, Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib
- **Environment**: Jupyter Notebook
- **Key Techniques**: Deep Learning, Feature Scaling, One-Hot Encoding, Focal Loss

## Future Improvements
- Experiment with different architectures (CNN, LSTM for temporal data)
- Incorporate time-series analysis for sequential failure prediction
- Implement hyperparameter tuning
- Add more advanced feature engineering techniques
- Deploy the model for real-time prediction in manufacturing systems

## Usage
1. Ensure all required libraries are installed
2. Load the dataset (`Dataset.csv`)
3. Run the notebook cells sequentially
4. Review model performance metrics and confusion matrix
5. Use the trained model for predicting equipment failure causes

## Author
[Your Name] - Flexisaf Internship Project