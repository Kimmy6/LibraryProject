도서관 대출 서비스
============================

## 프로젝트에 사용된 프로그램 및 패키지

### 개발 환경: Visual Studio Code

### Python (Back-end)
> · Flask       
> · SQLAlchemy       

### HTML (Front-end)
> · Vanilla HTML          
> · Jinja2           
> · JavaScript          
> · CSS           

## 프로젝트에 구현된 기능들

### 1. 로그인

#### 필수

> · 유저로부터 아이디(이메일)와 비밀번호 정보를 입력받아 로그인 합니다.      
> · 아이디와 비밀번호는 필수 입력 사항 입니다.         
> · 로그인한 유저에 대해 session으로 관리해야 합니다.           

#### 선택

> · 비밀번호는 조건에 맞추어 최소 8자리 이상의 길이로 입력 받아야 합니다.          
> · 아이디는 이메일 형식으로만 입력 받아야 합니다.        

### 2. 회원가입

#### 필수

> · 유저로부터 아이디(이메일), 비밀번호, 이름 정보를 입력받아 회원가입합니다.              
> · 비밀번호와 비밀번호 확인의 값이 일치해야 합니다.

#### 선택 

> · 아이디는 이메일 형식으로만 정보를 입력 받아야 합니다.     
> · 이름은 한글, 영문으로만 입력 받아야 합니다.            
> · 비밀번호는 조건에 맞추어 영문, 숫자, 특수문자 중 2종류 이상을 조합하여 최소 10자리 이상 또는 3종류 이상을 조합하여 최소 8자리 이상의 길이로 구성합니다.     

### 3. 로그아웃

#### 필수

> · 현재 로그인한 유저에 대해 로그아웃 합니다.          
> · 로그아웃한 유저를 현재 session에서 제거해야 합니다.        

### 4. 메인페이지

#### 필수

> · 현재 DB 상에 존재하는 모든 책 정보를 가져옵니다.                
> · 현재 DB 상에 존재하는 남은 책의 수를 표기합니다.           
> · 책 이름을 클릭 시 책 소개 페이지로 이동합니다.          
> · 책의 평점은 현재 DB 상에 담겨있는 모든 평점의 평균입니다. 숫자 한자리수로 반올림하여 표기합니다.

#### 선택

> · 페이지네이션 기능을 추가합니다. 한 페이지 당 8권의 책만을 표기합니다.

### 5. 대여하기

#### 필수

> · 메인 페이지의 대여하기 버튼을 클릭하여 실행합니다.           
> · 현재 DB 상에 책이 존재 하지 않는 경우, 대여되지 않습니다.         
> · 현재 DB 상에 책에 존재하는 경우, 책을 대여하고 책의 권수를 -1 합니다.

#### 선택

> · 현재 DB 상에 책이 존재하지 않는 경우, 유저에게 대여가 불가능하다는 메세지를 반환합니다.            
> · 유저가 이미 이 책을 대여했을 경우, 이에 대한 안내 메세지를 반환합니다.

### 6. 반납하기

#### 필수

> · 로그인한 유저가 대여한 책을 모두 보여줍니다.    
> · 반납하기 버튼을 통해 책을 반납합니다. 책을 반납한 후 DB 상에 책의 권수를 +1 합니다.

### 7. 책 소개

#### 필수

> · 메인 페이지의 책 이름을 클릭하여 접근합니다.              
> · 책에 대한 소개를 출력합니다.

#### 선택 

> · 가장 최신의 댓글이 보이도록 정렬하여 보여줍니다.          
> · 댓글을 작성함으로써 책에 대한 평가 점수를 기입합니다.           
> · 댓글 내용과 평가 점수는 모두 필수 입력 사항입니다.           

### 8. 대여기록

#### 선택

> · 로그인한 유저가 대여 후 반납했던 책에 대한 모든 사항을 출력합니다.

### 사용할 데이터베이스 구조

![MyERD](/uploads/856a8c34aa2b72cb7ad9b4c5457637e3/MyERD.jpg)

#### 테이블 설명
> · myMember : 회원 정보를 보관하는 테이블   
> · myBooks : 도서관에 비치된 책 정보를 보관하는 테이블   
> · bookReviews : 모든 책에 대한 모든 리뷰를 보관하는 테이블   
> · rentHistory : 모든 회원에 대한 모든 대여 기록을 보관하는 테이블    
> · nowRenting : 현재 도서관에 없는 책(고객이 대여한 책) 정보를 보관하는 테이블
