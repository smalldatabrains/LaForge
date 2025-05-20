//Change picture when category is changed
$('select').on('change', function() {
  var selected=$(this).val();
  selected= selected.replace(/\s/g, '');
  console.log(selected);
  var item=$(":focus").parent().parent().find('img').attr('id');
  console.log(item);
  document.getElementById(item).src = "../media/"+selected+".jpg"
})