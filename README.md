# API

## Requests
```
POST:
curl http://localhost:5000/data -d "camera_id=<camera_id>&full_place=<full_place>&total_place=<total_place>" -X POST
```

Retrieve all informations:
```
GET:
curl http://localhost:5000/data -X GET
```

Retrieve specific camera id:
```
GET:
curl http://localhost:5000/data?camera_id=<camera_id> -X GET
```