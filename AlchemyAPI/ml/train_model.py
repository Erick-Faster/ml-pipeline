from flask_restful import Resource, reqparse
from processors.data_management import extract_data
from sklearn.model_selection import train_test_split
from pipeline import model


class Train(Resource):

    def get(self):

        df = extract_data()

        X_train, X_test, y_train, y_test = train_test_split(df.drop(['risk'], axis=1), 
                                                    df['risk'], 
                                                    test_size=0.2, 
                                                    random_state=42)

        
        model.fit(X_train, y_train)

        train_score = model.score(X_train, y_train)

        return {'train_score': train_score}
