Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # --- Numeric sub-pipeline: impute missing → standardize ---
... numeric_pipeline = Pipeline([
...     ('imp',    SimpleImputer(strategy='median')),   # robust to skewed Age/Fare
...     ('scaler', StandardScaler())                    # zero mean, unit variance
... ])
... 
... # --- Categorical sub-pipeline: impute missing → one-hot encode ---
... categorical_pipeline = Pipeline([
...     ('imp', SimpleImputer(strategy='most_frequent')),  # fill 2 missing Embarked rows
...     ('ohe', OneHotEncoder(handle_unknown='ignore',     # safe for unseen categories
...                           sparse_output=False))
... ])
... 
... # --- ColumnTransformer: route columns to their sub-pipelines ---
... preprocessor = ColumnTransformer([
...     ('num', numeric_pipeline,     num_cols),
...     ('cat', categorical_pipeline, cat_cols)
... ])
... 
... # --- Full Pipeline: preprocessing + classifier ---
... pipe = Pipeline([
...     ('prep', preprocessor),
...     ('clf',  LogisticRegression(max_iter=1000, random_state=42))
... ])
... 
... print('Pipeline structure:')
