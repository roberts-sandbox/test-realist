$(function() {
  $("body .main .big-list-holder .clickable").click(function(e) {
    e.preventDefault();
    location.href = $('article h2 a', e.currentTarget).attr('href');
  });
});
