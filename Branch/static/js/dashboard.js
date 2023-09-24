AOS.init()
function show_followers(){
  document.getElementById("user-text-data").style.display = "none"
  document.getElementById("user-followers-data-scroll").style.display = "flex"
}
function show_info(){
  document.getElementById("user-text-data").style.display = "flex"
  document.getElementById("user-followers-data-scroll").style.display = "none"
}
