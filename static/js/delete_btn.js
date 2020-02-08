function confirm_delete(recipe_delete_url){
  var delete_confirmed = confirm("Delete this recipe?")
  if (delete_confirmed){
      window.location.href = recipe_delete_url;
  }
}
