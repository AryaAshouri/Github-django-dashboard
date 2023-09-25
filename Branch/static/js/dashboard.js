AOS.init()

function load_info(){
  document.getElementById("other-info-section").style.display = "block"
  document.getElementById("followers-main-section").style.display = "none"
}
function load_followers(){
  document.getElementById("other-info-section").style.display = "none"
  document.getElementById("followers-main-section").style.display = "flex"
}
