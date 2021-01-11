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


