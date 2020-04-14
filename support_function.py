from os import path

def checkStringOk(checkData, dataType):
  if isinstance(checkData, str) == False:
    print("{} is not string".format(dataType))
    exit()

  if checkData.strip().len() == 0:
    print("{} not define".format(dataType))
    exit()

# Full path only
def checkFileExist(checkData):
  if path.exists(checkData) == False:
    print("File {} does not exists".format(checkData))

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