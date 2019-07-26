function make_card(name, quantity, address, phone){
   
    let temp_html = '<tbody>\
                        <th scope="row">1</th>\
                        <td>'+name+'</td>\
                        <td>'+quantity+'</td>\
                        <td>'+address+'</td>\
                        <td>'+phone+'</td>\
                    </tbody>';
  
      $('#in_table').append(temp_html);
  }
  
  function posting() {
    var name = $("#name_give").val(); // url 이라는 변수에 #posting-url 이라는 아이디의 값을 저장 하겠다라는 의미
    var quantity = $("#quantity_give option:selected").val(); // comment 라는 변수에 #posting-comment 라는 아이디의 값을 저장한다는 의미
    var address = $("#address_give").val();
    var phone = $("#phone_give").val();
  // 아래의 코드는 위의 변수에서 받은 값을 POST방식으로 flask 서버에 저장하는 ajax 코드
  
  $.ajax({
    type: "POST", // POST 방식으로 요청하겠다.
    url: "/post", // /post라는 url에 요청하겠다.
    data: { name_give: name, quantity_give: quantity, address_give: address, phone_give: phone }, // 데이터를 주는 방법
    success: function(result){ // 성공하면
      if (result['result'] == 'success'){
        alert("포스팅 성공") 
        window.location.reload();
      } else {
        alert("포스팅 실패")
      }
    }
  })
  }

    
  function get_posting() {
    
    $.ajax({
      type: "GET",
      url: "/post",
      data: {},
      success: function(response){
        var cards = response["articles"];
  
  
        for (let i = 0; i < cards.length; i++){
          var name = cards[i]["name"]
          var quantity = cards[i]["quantity"]
          var address = cards[i]["address"]
          var phone = cards[i]["phone"]
  
          make_card(name, quantity, address, phone);
        }
      }
    })
  }
  
  window.onload=function(){
      get_posting();
  }