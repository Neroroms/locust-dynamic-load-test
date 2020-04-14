# Getting start
1. Install python3 or use python3 docker image
2. Install locust
```
pip3 install locust
```
3. Clone this project
4. Start docker streamtank/sample-object:node-12-13-0 for example
```
docker run -idt --name sample-object --restart unless-stopped -p 3000:3000 streamtank/sample-object:node-12-13-0
```
5. Start locust load test
```
locust -f load_test.py
```
6. Open browser and goto locust page
  - localhost:8089 (install on local or docker bind port)
  - YOUR_SERVER:8089

7. Add max user, hatch user per second and sample-sample object http://SAMPLE_OBJECT_URL:3000