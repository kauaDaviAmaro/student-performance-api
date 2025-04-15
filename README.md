```
# FastAPI Application

To start the application, run the following command:

```bash
uvicorn main:app --reload
```

Once the server is running, you can access the API documentation at:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Example Request Payload

Below is an example of the JSON payload that can be sent to the API:

```json
{
  "data": [
    {
      "gender": "female",
      "race_ethnicity": "group A",
      "parental_level_of_education": "some college",
      "lunch": "free/reduced",
      "test_preparation_course": "none",
      "math_score": 20,
      "reading_score": 20,
      "writing_score": 12
    },
    {
      "gender": "male",
      "race_ethnicity": "group C",
      "parental_level_of_education": "high school",
      "lunch": "standard",
      "test_preparation_course": "completed",
      "math_score": 90,
      "reading_score": 82,
      "writing_score": 75
    },
    {
      "gender": "female",
      "race_ethnicity": "group D",
      "parental_level_of_education": "master's degree",
      "lunch": "free/reduced",
      "test_preparation_course": "completed",
      "math_score": 95,
      "reading_score": 92,
      "writing_score": 94
    },
    {
      "gender": "male",
      "race_ethnicity": "group B",
      "parental_level_of_education": "associate's degree",
      "lunch": "standard",
      "test_preparation_course": "none",
      "math_score": 76,
      "reading_score": 70,
      "writing_score": 80
    },
    {
      "gender": "female",
      "race_ethnicity": "group A",
      "parental_level_of_education": "high school",
      "lunch": "free/reduced",
      "test_preparation_course": "completed",
      "math_score": 65,
      "reading_score": 22,
      "writing_score": 18
    }
  ]
}
```