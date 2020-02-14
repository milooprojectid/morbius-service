# Morbius

Miloo Sentiment Analysis Module

## Prerequisite

Before you can use the app, you have to set up the virtual env and install dependencies. Run the following command in the project root directory. 
```bash
bin/setup
```
It will generate a local virtual environment required to run the app.

## Usage
To run the app execute the following command without any parameter. 
```bash
bin/run
```
It will start the Rest-API server.

### Endpoint
There is only one endpoint served by the Rest-API server, which is root ("/"). It takes "text" field as a JSON input and will returns the sentiment class of given text. 

##### Input
```javascript
{
  "text": "Semalang-malangnya nasib lu, masih malang nasib underpass kemayoran."
}
```

#### Output
```javascript
{
  "message": "sentiment analysis finished",
  "data": {
     "class": 1,
     "description": "neutral"
  }
}
```