# HBSMITH MO 서버리스 어플리케이션

## 실행
```
serverless deploy
```

위 명령만 실행하시면 됩니다.

```
Service Information
service: HBSmithMOAPI
stage: dev
region: ap-northeast-2
stack: HBSmithMOAPI-dev
resources: 30
api keys:
  None
endpoints:
  POST - https://ai3gp489ti.execute-api.ap-northeast-2.amazonaws.com/dev/messages
  GET - https://ai3gp489ti.execute-api.ap-northeast-2.amazonaws.com/dev/messages
  GET - https://ai3gp489ti.execute-api.ap-northeast-2.amazonaws.com/dev/messages/{id}
  DELETE - https://ai3gp489ti.execute-api.ap-northeast-2.amazonaws.com/dev/messages/{id}
functions:
  create: HBSmithMOAPI-dev-create
  list: HBSmithMOAPI-dev-list
  get: HBSmithMOAPI-dev-get
  delete: HBSmithMOAPI-dev-delete
layers:
  None
```


## 테스트

### 생성
```
 $ curl -X POST <URL> --data "sn_list=13568922&id_list=hbsmith00&mo_number_list=01333665511&callback_list=01039743916&msg_list=%A4%BE%A4%BF%C0%CC%C7%CF%C0%CC%C7%CF%C0%CC&rcv_date_list=2020-06-17+12%3A39%3A53"

 {"id": "b34573df-b91a-11ea-b9db-5d27aaad8b21", "received_at": "2020-06-17 12:39:53", "serial_number": "13568922", "account_id": "hbsmith00", "mo_number": "01333665511", "callback_number": "01039743916", "message": "ㅎㅏ이하이하이"}
```

### 리스트 보기 / 조회
```
$ curl <URL>
```
또는
```
$ curl <URL>/b34573df-b91a-11ea-b9db-5d27aaad8b21
```

