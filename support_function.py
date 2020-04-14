from os import path

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

    with locust.client.request(loadTestSetupInfo['methodType'], loadTestSetupInfo['url'], catch_response=True) as response:
      if len(expectStatusCode) > 0:
        if response.status_code == int(expectStatusCode):
          response.success()

  return _locust

def createLoadTestObject(url, methodType, expectStatusCode):
  loadTestObject = {
    "url": url,
    "methodType": methodType,
    "expectStatusCode": expectStatusCode
  }

  return loadTestObject