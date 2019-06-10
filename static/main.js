// Initialize Firebase
var config = {
    apiKey: "AIzaSyCcQ1aGessQpZIplJfzUcbVgI6gD36ob0w",
    authDomain: "bookkeeper-f75d2.firebaseapp.com",
    databaseURL: "https://bookkeeper-f75d2.firebaseio.com",
    projectId: "bookkeeper-f75d2",
    storageBucket: "bookkeeper-f75d2.appspot.com",
    messagingSenderId: "163815018826"
};
firebase.initializeApp(config);
console.log(firebase)

var database = firebase.database();

var ref = database.ref('one')

ref.on('value',gotData,errData)

var twoRef = database.ref('two')

twoRef.on('value',gotData,errData)

function gotData(data){
    console.log(data.val())
    console.log(data.val().initials)
    console.log(data.val().score)
}

function errData(err){
    console.log('Error')
    console.log(err)
}

$(function() {
    //single book
    $('#mybook').booklet();

    //multiple books with ID's
    $('#mybook1, #mybook2').booklet();

    //multiple books with a class
    $('.mycustombooks').booklet();
});


$(document).ready(function(){
  
    /* 1. Visualizing things on Hover - See next part for action on click */
    $('#stars li').on('mouseover', function(){
      var onStar = parseInt($(this).data('value'), 10); // The star currently mouse on
     
      // Now highlight all the stars that's not after the current hovered star
      $(this).parent().children('li.star').each(function(e){
        if (e < onStar) {
          $(this).addClass('hover');
        }
        else {
          $(this).removeClass('hover');
        }
      });
      
    }).on('mouseout', function(){
      $(this).parent().children('li.star').each(function(e){
        $(this).removeClass('hover');
      });
    });
    
    
    /* 2. Action to perform on click */
    $('#stars li').on('click', function(){
      var onStar = parseInt($(this).data('value'), 10); // The star currently selected
      var stars = $(this).parent().children('li.star');
      
      for (i = 0; i < stars.length; i++) {
        $(stars[i]).removeClass('selected');
      }
      
      for (i = 0; i < onStar; i++) {
        $(stars[i]).addClass('selected');
      }
      
      // JUST RESPONSE (Not needed)
      var ratingValue = parseInt($('#stars li.selected').last().data('value'), 10);
      var msg = "";
      if (ratingValue > 1) {
          msg = "Thanks! You rated this " + ratingValue + " stars.";
      }
      else {
          msg = "We will improve ourselves. You rated this " + ratingValue + " stars.";
      }
      responseMessage(msg);
      
    });
    
    
  });
  
  
  function responseMessage(msg) {
    $('.success-box').fadeIn(200);  
    $('.success-box div.text-message').html("<span>" + msg + "</span>");
  }