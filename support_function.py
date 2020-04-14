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
    locust.client.request(loadTestSetupInfo['methodType'], loadTestSetupInfo['url'])
  return _locust