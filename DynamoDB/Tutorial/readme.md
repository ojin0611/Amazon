# DynamoDB Tutorial with Python

## Import Sample Data

- moviedata.json : 영화 데이터 json file

- MoviesCreateTable.py : Create Table(Movies) - partition key(year), sort key(title) 설정

- MoviesLoadData.py : Update - json file upload to Movies



## CRUD

- MoviesItemOps01.py : Create 항목
- MoviesItemOps02.py : Read 항목
- MoviesItemOps03.py : Update - 새로운 속성(json 형식) 추가
- MoviesItemOps04.py : Update - 속성 내의 값 변경
- MoviesItemOps05.py : Update - 조건에 해당하면 해당 속성 변경
- MoviesItemOps06.py : Delete -  조건에 해당하면 해당 항목 제거
- MoviesDeleteTable.py : Delete - Table 삭제

## Query

- MoviesQuery01.py : year==1985

- MoviesQuery02.py : year==1992 & title between A,L

## Scan

- MoviesScan.py : [Scan AWS Document](https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/GettingStarted.Python.04.html#GettingStarted.Python.04.Scan "Scan 개념과 예제 설명")

