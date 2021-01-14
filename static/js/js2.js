// Sidebar
var sidebarOpen = false;
var sidebar = document.getElementById("sidebar");
var sidebarCloseIcon = document.getElementById("sidebarIcon");

function toggleSidebar() {
  if (!sidebarOpen) {
    sidebar.classList.add("sidebar_responsive");
    sidebarOpen = true;
  }
}

function closeSidebar() {
  if (sidebarOpen) {
    sidebar.classList.remove("sidebar_responsive");
    sidebarOpen = false;
  }
}


// Tabs

const tabContents = document.querySelectorAll(".tabContent");
const tabLinks = document.querySelectorAll(".tabs a");


function openTap(event, tabName) {
  tabContents.forEach((tabContent) => (tabContent.style.display = "none"));

  tabLinks.forEach((tabLink) => tabLink.classList.remove("active"));

  event.currentTarget.classList.add("active");
  document.getElementById(tabName).style.display = "block";

}



// pagination


// Upload Image
const realFileBtn = document.getElementById("real-file");
const customBtn = document.getElementById("custom-button");
const customTxt = document.getElementById("custom-text");

customBtn.addEventListener("click", function() {
  realFileBtn.click();
});

realFileBtn.addEventListener("change", function() {
  if (realFileBtn.value) {
    customTxt.innerHTML = realFileBtn.value.match(
      /[\/\\]([\w\d\s\.\-\(\)]+)$/
    )[1];
  } else {
    customTxt.innerHTML = "No file chosen, yet.";
  }
});




// Progress
$(document).ready(function() {
  
  var count = 0;
  var checked = 0;
  function countBoxes() { 
    count = $("input[type='checkbox']").length;
    console.log(count);
  }
  
  countBoxes();
  $(":checkbox").click(countBoxes);
  
  function countChecked() {
    checked = $("input:checked").length;
    
    var percentage = parseInt(((checked / count) * 100),10);
    $(".progressbar-bar").progressbar({
            value: percentage
        });
    $(".progress_inner").text(percentage + "%");
  }
  
  countChecked();
  $(":checkbox").click(countChecked);
});