AOS.init()
let first_time = 0
let dark_bg_color = "#0e101c"
let main_bg_color = "#A6E1FA"
let darker_darker_bg_color = "#1b1f33"
let darker_bg_color = "#57cdff"
var current = document.querySelector(':root')

let current_theme = localStorage.getItem("theme")
if (current_theme == "dark"){
  document.getElementById("light_mode").style.display = "none"
  document.getElementById("dark_mode").style.display = "block"
  current.style.setProperty('--main-bg-color', dark_bg_color)
  current.style.setProperty('--darker-bg-color', darker_darker_bg_color)
}
else if (current_theme == "light"){
  document.getElementById("light_mode").style.display = "block"
  document.getElementById("dark_mode").style.display = "none"
  current.style.setProperty('--main-bg-color', main_bg_color)
  current.style.setProperty('--darker-bg-color', darker_bg_color)
}
function change_mode(){
  if (first_time == 0){
    if (document.getElementById("light_mode").style.display == "block"){
      document.getElementById("light_mode").style.display = "none"
      document.getElementById("dark_mode").style.display = "block"
      first_time = 1
      current.style.setProperty('--main-bg-color', dark_bg_color)
      current.style.setProperty('--darker-bg-color', darker_darker_bg_color)
      localStorage.setItem("theme", "dark")
    }
    else if (document.getElementById("dark_mode").style.display == "block"){
      document.getElementById("light_mode").style.display = "block"
      document.getElementById("dark_mode").style.display = "none"
      first_time = 1
      current.style.setProperty('--main-bg-color', main_bg_color)
      current.style.setProperty('--darker-bg-color', darker_bg_color)
      localStorage.setItem("theme", "light")
    }
  }
  else {
    if (document.getElementById("dark_mode").style.display == "block"){
      document.getElementById("light_mode").style.display = "block"
      document.getElementById("dark_mode").style.display = "none"
      current.style.setProperty('--main-bg-color', main_bg_color)
      current.style.setProperty('--darker-bg-color', darker_bg_color)
      localStorage.setItem("theme", "light")
    }
    else if (document.getElementById("light_mode").style.display == "block"){
      document.getElementById("light_mode").style.display = "none"
      document.getElementById("dark_mode").style.display = "block"
      current.style.setProperty('--main-bg-color', dark_bg_color)
      current.style.setProperty('--darker-bg-color', darker_darker_bg_color)
      localStorage.setItem("theme", "dark")
    }
  }
}
function send_theme_to_home(){

}
