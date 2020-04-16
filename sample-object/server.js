const express = require('express')

const app = express()

app.use(express.json())
app.use(express.text())

app.get("/textRes/:var1", (req,res) => {
  var resString

  switch(req.params['var1']) {
    case "hello":
      resString = "world"
      break

    case "Greeting":
      resString = "Stranger"
      break

    default:
      resString = "No greeing message"
      break
  }

  res.send(resString)

})

app.get("/jsonRes/:var1", (req,res) => {
  var resJson

  switch(req.params['var1']) {
    case "hello":
      resJson = { message: "world" }
      break

    case "Greeting":
      resJson = { message: "Stranger" }
      break

    default:
      resJson = { message: "No greeting message" }
      break 
  }
  
  res.send(resJson)
})

app.get("/:number1/add/:number2", (req, res) => {
  var firstVar = parseInt(req.params['number1'])
  var secondVar = parseInt(req.params['number2'])

  var result = firstVar + secondVar

  res.send(result.toString())
})

app.post("/testPostText", (req, res) => {
  var resMessage = ""

  switch (req.body) {
    case "hello":
      resMessage = "world"
      break;

    case "Greeting":
      resMessage = "stranger"
      break;
  
    default:
      break;
  }

  res.send(resMessage)
})

app.post("/testPostJson", (req, res) => {
  var resMessage

  switch (req.body['message']) {
    case "hello":
      resMessage = {
        message: "world"
      }
      break;
  
    case "Greeting":
      resMessage = {
        message: "Greeting"
      }
      break

    default:
      break;
  }

  res.send(resMessage)
})

function DoYouKnowMe(answer) {
  var response

  if (answer == "no") {
    response = "stranger"
  }
  else {
    response = "But I don't know you."
  }

  return response
}

app.post("/readHeaderTest", (req, res) => {
  var greetingHeader = req.headers['greeting-header']
  var greetingAnswer = req.body['greetingAnswer']
  var responseMessage = ""

  switch (greetingHeader) {
    case "hello":
      responseMessage = DoYouKnowMe(greetingAnswer)
      break;
  
    case "Greeting":
      responseMessage = DoYouKnowMe(greetingAnswer)
      break

    default:
      responseMessage = "I don't know how to response"
      break;
  }

  res.send(responseMessage)
})

app.listen(3000, () => {
  console.log("App listen 3000")
})
