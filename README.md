# HTML

# 목차
1. 태그 (tag)
    * 텍스트태그
    * 목록태그
    * 표 태그
    * 이미지, 링크 태그
    * 폼 태그
2. CSS
    * 주요 선택자 (class, id 선택자)
    * 텍스트
    * 문단
    * 배경
    * 박스 모델

# 태그 `<>`
## 텍스트태그
<b> [예시 1](10_01_text_tag.html) ⓒ 2021. emily all rights resereved) </b>
- `<hn>` : 제목표시 ex. `<h1> ~ <h6>`, 숫자가 커질수록 글씨가 작아짐
- `<p>` : paragraph 줄임말. 단락표시
- `<br>` : 줄 바꾸기
- `<hr>` : 수평 줄 넣기. 단락의 주제가 바뀌는 경우 사용
- `<blockquote>` : 인용문 표시
- `<pre>` : 입력 그대로 화면에 표시
- `<strong>, <b>` : 굵게 표시
- `<em>, <i>` : 이탤릭체 (기울이게 표시)
- `<mark>` : 형광펜으로 그어놓은 듯한 효과
- `<span>` : 텍스트만 묶어 스타일 적용하고자 할 때 사용

## 목록테그
- `<ul>,<li>` : 순서가 필요하지 않은 목록 만들기
- `<ol>,<li>` : 순서가 필요한 목록 만들기, type 속성을 수정해주면 다양한 순서를 지정할 수 있음.
- `<dl>, <dt>, <dd>` : 제목과 설명이 한 쌍인 설명 목록만들기 dl, dt, dd는 각각 목록, 제목, 설명이다.

## 표 테그
<b> [예시 2](10_02_table.html) ⓒ 2021. emily all rights resereved </b>
- `<tr>,<td>,<th>` : tr, td, th는 각각 행, 셀, 제목을 생성해 준다. 속성 중 colspan과 rowspan은 각각 가로와 세로 셀을 합쳐준다.
- `<caption>` : table 다음에 사용되는 태그. 표에 제목을 붙일 수 있다. 표 위쪽 중앙에 표시됨
- `<figcaption>` : 표 위에 제목이 표시되고, 아래에 쓰면 표 아래에 제목이 표시됨
- `<img>` : 웹 문서에 이미지를 삽입할 때 사용, src속성을 사용해 경로 지정을 해줘야 이미지가 표시
- `<a>` : 텍스트나 이미지 앞에 지정. 클릭 시 다른 페이지로 넘어갈 수 잇도록 하는 태그
<br>

|속성|설명|
|:---|:----|
|href|링크한 문서나 사이트 주소 입력|
|target|링크한 내용이 표시될 위치 지정|
|download|링크한 내용을 보여주는 것이 아니라 다운로드|
|rel|현재 문서와 링크한 문서의 관계|
|hreflang|링크한 문서의 언어 지정|
|type|링크한 문서의 파일 유형|</br>

## 폼 테그
### 속성
<b> [예시 3](10_03_form.html) ⓒ 2021. emily all rights resereved </b>

`<form>` 속성
<table>
  <tr>
    <th>속성</th>
    <th>설명</th>
  <tr>
    <td rowspan="2">method</td>
    <td>get : 주소 표시줄에 사용자가 입력한 내용이 드러남. 256 ~ 4096 byte까지 데이터를 넘김</td>
  </tr>
  <tr>
    <td>post : 입력 내용 길이 제한을 받지 않고 사용자가 입력한 내용이 드러나지 않음. 네트워크에 한 공간으로 이동하게 됨 </td>
  </tr>
  <tr> 
    <td>name</td>
    <td>폼 이름 지정. 여러 개의 폼을 사용하면 구분 짓기 위해 사용</td>
  </tr>
  <tr> 
    <td>action</td>
    <td>form 태그 안의 내용들을 처리해 줄 서버 상의 프로그램 지정</td>
  </tr>
  <tr> 
    <td>target</td>
    <td>action 속성에서 지정한 파일을 지정한 위치에 열도록 지정</td>
  </tr>
</table>

- `<label>` 속성  : 폼 요소에 레이블을 붙이기 위한 것 
- `<fieldset>, <legend>` 속성 : 태그 사이의 폼들을 하나의 영역으로 붂어주고 제목을 붙여주는 역할 
- `<input>` 속성 

|속성|설명|
|:---|:----|
|autofocus|페이지 호출 시 첫번째로 커서를 표시할 수 있음|
|placeholder|텍스트 입력 시 도움이 되도록 힌트를 보여줌. 사라지게 할 수 있음|
|required|form을 submit할 때 필수 값으로 지정해서 값이 등록되어있는지 확인|
|min,max,step|날짜, 숫자, 범위바에 적용필
|size, minlength, maxlength|몇 글자까지 나타나게 할지 지정|

- `<select>, <optgroup>, <option>` : 주어진 옵션 중에서 선택할 수 있또록 하는 드롭다운 목록
- `<textarea` : 여러 줄의 텍스트를 입력할 수 있도록 해준다.
  
# CSS
홈페이지를 이쁘게 꾸며주는 것?! 근데, 굉장히 문법이 어려우니 공부를 해야한다.

## 주요선택자
  1. 전체 선택자 : 스타일 모든 요소에 적용
  ```css
  * {
    margin: 0; padding: 0;
  }
  ```
  2. 태그 선택자 : 특정 태그가 쓰인 모든 요소에 스타일 적용
  ```css
  p { text-aligh : center; }
  h2 { color:darkblue; }
  ```
  3.<b>클래스 선택자</b> : 한꺼번에 둘 이상의 클래스 스타일도 적용 가능, `.`으로 시작
  ```css
  .reg {
    font-size:14px;
    color:darkblue;
  }
  ```
  4. <b>id 선택자</b> : 웹 문서 안의 특정 부분에 스타일을 적용
  ```css
  #container {
    width:600px  /* 너비 */
    padding:15px /* 테두리와 내용 사이의 여백 */
    border :1px /* 테두리 스타일 */
  }
  ```
## 글꼴
- `font-family` : 텍스트를 사용하는 요소들에 사용
- `font-size` : 글자 크기 조절

|단위|설명|
|:---|:----|
|em|해당 글꼴의 <b>대문자 M</b>의 너비를 기준으로 크기 조절 (1em = 16px)|
|ex|해당 글꼴의 <b>소문자 x</b>의 너비를 기준으로 크기 조절|
|px|모니터에 따라 상대적 크기|
|pt|일반 문서에서 사용하는 단위|
  - 일반적으로 px를 사용하지만, 모바일에서는 디바이스 기준으로 크기가 표시되어 em을 사용
- `font-weight` : 글자 굵기 지정
 
|속성 값|설명|
|:---|:----|
|normal|기본값(default)|
|bold, lighter, bolder |각각 굵게, 가늘게, 더 굵게|
|100 ~ 900 수치|400 = normla. 700 = bold|

- `font-style` : 글자 스타일 지정

```css
p{font-famil:"맑은 고딕";} /*모든 p 태그에 맑은 고딕 사이즈로 지정*/

body{ /*body는 font스타일, 굵기, 글꼴, 사이즈를 각각 아래와 같이 지정*/
  font-style : italic ;
  font-weight : 400;
  font-family : '선명조';
  font-size : 4em;
}
.content{ /* content class 태그에는 다음과 같은 조건을 적용*/
  font-style : 'Arial', 'Times New Roman';
  font-size : 14px;
  color : #2B6574 ;
  text-align : justify; /*글씨가 양쪽에 맞추어 문단을 정렬시키기*/
}
.content h1{ /*content class 태그에 쓰이는 h1은 다음과 같은 폰트를 적용*/
font-size : 60px;
font-family : '맑은 고딕';

#profile-img{ /*profile-img id 태그에는 다음과 같은 조건이 사용*/
  justify-content: center; /*이미지 위치를 가운데로 정렬*/
  width:150px;
  height:150px;
  border: 1px solid white; /*이미지 외곽에 1px 굵기를 가진 하얀색 선을 표현*/
  border-radius: 70%; /*이미지를 둥글게 만든다. 수가 커질수록 둥그러진다.*/
}
```