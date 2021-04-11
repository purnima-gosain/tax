// nav ko scroll ko lago js start
$(window).scroll(function() {
  if ($(this).scrollTop() > 50) {
    $("header").addClass("scrolltop");
  } else {
    $("header").removeClass("scrolltop");
  }
});
// nav ko scroll ko lago js end

// responsive navigation js start
function openSlideMenu() {
  {
    if (screen.width <= 550) {
      document.getElementById("side-menu").style.width = "100%";
    } else {
      document.getElementById("side-menu").style.width = "50%";
    }
  }
  document.getElementById("side-menu").style.display = "block";
  document.getElementById("logo").style.display = "none";
}

function closeSlideMenu() {
  document.getElementById("side-menu").style.display = "none";
  document.getElementById("logo").style.display = "block";
}
// responsive navigation js end

// login ko lagi js start
// $("login-background").show();
$(".login-icon").click(function() {
  $("#login-background").toggle();
});

// responsive nav login start
// $("side_nav-login-background ").show();
$(".side_nav-login").click(function() {
  $("#side_nav-login-background ").toggle();
});
// responsive nav login end

// login ko lago js end

// search ko lagi js start
function openSlideSearch() {
  if (screen.width <= 750) {
    document.getElementById("form-a").style.width = "100%";
  } else {
    document.getElementById("form-a").style.width = "50%";
  }
}
function closeSlideSearch() {
  document.getElementById("form-a").style.width = "0";
}
// search ko lagi js end

// owl carousel js start
$(document).ready(function() {
  $(".owl-carousel").owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    autoplay: true,
    autoplayTimeout: 5000,
    autoplayHoverPause: true,
    animateIn: "fadeIn",
    animateOut: "fadeOut",
    responsive: {
      0: {
        items: 1
      }
    }
  });
});
// owl carousel js end
