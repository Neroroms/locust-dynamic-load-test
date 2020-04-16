from os import path
from datetime import datetime
import json

def replaceVariable(urlPath, jsonData):
  newUrlPath = urlPath

  while True:
    startPos = newUrlPath.find("{{")
    endPos = newUrlPath.find("}}")

    if startPos == -1:
      break

    searchString = newUrlPath[startPos + 2:endPos]

    newUrlPath = newUrlPath.replace("{{" + searchString + "}}", jsonData[searchString])

  return newUrlPath

def locustFactory(loadTestSetupInfo):
  def _locust(locust):
    expectStatusCode = loadTestSetupInfo['expectStatusCode']

    headers = loadTestSetupInfo['headers']
    headers['Content-Type'] = loadTestSetupInfo['contentType']

    if loadTestSetupInfo['contentType'] == "application/json":
      requestBody = json.dumps(loadTestSetupInfo['bodyVariable'])
    else:
      requestBody = loadTestSetupInfo['bodyVariable']
    
    with locust.client.request(loadTestSetupInfo['methodType'], loadTestSetupInfo['url'], catch_response=True, data=requestBody, headers=headers) as response:
      if len(expectStatusCode) > 0:
        if response.status_code == int(expectStatusCode):
          response.success()

  return _locust

def createLoadTestObject(url, methodType, expectStatusCode, contentType, bodyVariable, headers):
  loadTestObject = {
    "url": url,
    "methodType": methodType,
    "expectStatusCode": expectStatusCode,
    "contentType": contentType,
    "bodyVariable": bodyVariable,
    "headers": headers
  }

  return loadTestObject