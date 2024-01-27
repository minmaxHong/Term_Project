## 사무실 관리 : 물품이 보관될 공간 결정

* 사무실 코드(자동 할당), 건물 명칭, 사무실 호실, 사무실 담당자
* 조회, 입력, 수정, 삭제 구현
---

## 영역 관리 : 사무실 내 물품이 보관될 영역 관리
* 사무실 코드, 영역 코드, 영역 명칭, 영역 담당자
* 영역은 책장, 책상 등 물품을 보관하는 영역
* 조회, 입력, 수정, 삭제 구현

---

## 물품 관리 : 관리할 물품
* 물품코드, 사무실코드, 영역 코드, 물품 종류, 물품 명칭, 가격, 대여자, 대여일자, 반납일자
* 대여 정보는 최종 사용자 정보만 유지
* 별도의 대여, 장소 이관 메뉴 제공 필수
* 조회, 입력, 수정, 삭제 구현

---

## 검색 : 물품 전체 조회 혹은 물품코드로 특정 물품 조회
* 사무실별로 테이블을 만들어서 조회
* 테이블은 영역 단위로 행을 만들어서 물품코드 및 물품 명칭 출력

---
## 준수 사항
* 한글은 입력받지 않고, 영문 기호 및 숫자만 입력받는다.
* output은 반드시 사무실 관리, 영역 관리, 물품 관리, 검색 순으로 실행 결과 제출한다.
* 사무실 관리, 영역 관리, 물품 관리는 최대한 나누어서 개발한다.
* 모든 데이터는 저장하기/읽어오기 제공, 구현은 반드시 Pickling을 사용한다.
* 수업시간에 다루지 않은 외부 모듈 사용을 허가하지 않는다.
* 절차적인 언어를 사용해서 개발하고 객체지향언어(OOP)는 허용하지 않는다.
